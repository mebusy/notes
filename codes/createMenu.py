#!python3

import hashlib
import os
import re
import sys
from urllib import parse

RE_PATTERN_MENU_BODY = re.compile(
    r"""
    (\[\]\()?       # match new/old menu start
    \.\.\.menustart
    .*?
    \.\.\.menuend
    \)?           # match new/old menu end
    \s*""",
    re.DOTALL | re.VERBOSE,
)
RE_PATTERN_MENU_SYNTAX = re.compile(r"^(\#+)(.*?)$")
RE_PATTERN_MENU_JUMP_ID = re.compile(r"^<h\d*\s+id=")
RE_PATTERN_TABLE = re.compile(r"^\s*---(\s*\|\s*---)+")
RE_PATTERN_ITALIC_BOLD_HEAD_NON_SPACE = re.compile(r"(.?)(\*\*\*[^*]+\*\*\*)(.?)")

RE_PATTERN_CODE_BLOCK = re.compile(r"^\s*```")
RE_PATTERN_SINGLE_QUOTE_PAIR = re.compile(r"`[^`]+?`")
RE_TAG_CONTENT = re.compile(r"<([a-zA-Z0-9-_]+?)>")

PARAGRAPH_SEP = "-----"


def createMenu4MD(path):
    # print( 'parsing' , path)

    bShowPath4debug = False
    _path, _name = os.path.split(path)
    global all_md_filenames
    all_md_filenames[_name] = path

    fp = open(path)
    content = fp.read()
    fp.close()

    content = content.replace("\r", "")

    content = re.sub(RE_PATTERN_MENU_BODY, "", content)

    menu = "[](...menustart)\n\n"
    body = ""

    lines = content.split("\n")

    bCodeStart = False
    bFollowLinkID = True

    all_title_level = set([])
    for i, line in enumerate(lines):
        if RE_PATTERN_CODE_BLOCK.search(line) is not None:
            bCodeStart = not bCodeStart
            DEBUG = False
            if DEBUG:
                if bCodeStart:
                    print("codeline start: ", i + 1, lines[i + 1])
                else:
                    print("codeline end: ", i - 1, lines[i - 1])

        if bCodeStart:
            if not re.search(RE_PATTERN_MENU_JUMP_ID, line):
                body += line + "\n"
            continue

        result = re.search(RE_PATTERN_MENU_SYNTAX, line)
        if result:
            sharps = result.group(1)
            title = result.group(2).strip()

            m = hashlib.md5()
            m.update(title.encode("utf8"))
            m5id = m.hexdigest()

            curTitleActualLevel = len(sharps)

            sort_l = sorted(all_title_level)
            if curTitleActualLevel in sort_l:
                idx = sort_l.index(curTitleActualLevel)
                if idx >= 0:
                    all_title_level = set(sort_l[:idx])

            all_title_level.add(curTitleActualLevel)

            escaped_title = title.replace("[", "\\[")
            escaped_title = escaped_title.replace("]", "\\]")

            nIndent = sorted(all_title_level).index(curTitleActualLevel)
            menu += ("%s- [%s](#%s)" % ("    " * nIndent, escaped_title, m5id)) + "\n"

            body += '<h2 id="{}"></h2>\n\n'.format(m5id)
            # print( sharps, title)

        isJumpIDLine = re.search(RE_PATTERN_MENU_JUMP_ID, line) is not None
        if not isJumpIDLine:
            if bFollowLinkID and (line.strip() == "" or line.strip() == PARAGRAPH_SEP):
                pass
            else:
                bFollowLinkID = False
                body += line + "\n"
        else:
            bFollowLinkID = True

        # error checking
        if re.search(RE_PATTERN_TABLE, line):
            # print( 'table' , line )
            table_sep_count = line.count(r"|")
            table_1stline_sep_count = lines[i - 1].replace(r"\|", "").count(r"|")
            if table_sep_count != table_1stline_sep_count:
                print("table error:", i - 1, lines[i - 1])
                bShowPath4debug = True

        # italic bold headed non space
        result = re.search(RE_PATTERN_ITALIC_BOLD_HEAD_NON_SPACE, line)
        if result:
            if (
                result.group(1) != " " and result.group(1) != ""
            ):  # or (result.group(3) != " " and result.group(3) != "")  :
                print("italic bold headed non space:", result.group(1), result.group(2))
                bShowPath4debug = True

        # html tag should be in ``
        if not isJumpIDLine:
            results = RE_TAG_CONTENT.findall(RE_PATTERN_SINGLE_QUOTE_PAIR.sub("", line))
            for result in results:
                if result not in [
                    "I",
                    "center",
                    "sup",
                    "sub",
                    "summary",
                    "details",
                    "b",
                    "br",
                ]:
                    print(result, "in a html tag may can not display")
                    print(" -> ", path, i, line)
                    raise Exception("html tag issue")

    global bForceCreateMenu
    menu += "\n[](...menuend)\n\n\n"
    if path.lower().endswith("readme.md") and not bForceCreateMenu:
        menu = ""

    if bCodeStart:
        print(_name)
        raise Exception("code pair error")

    # print( menu)

    fp = open(path, "w")
    fp.write(menu + body[:-1])  # remoev last \n
    fp.close()

    if bShowPath4debug:
        print("\n\t", "in", path)

    return


def visit(dirname, _, fnames):
    for f in fnames:
        if f[-3:] == ".md":
            path = os.path.join(dirname, f)
            createMenu4MD(path)


if "__main__" == __name__:

    all_md_filenames = {}

    bSpecifiedDirectory = len(sys.argv) >= 2
    bForceCreateMenu = bSpecifiedDirectory and "forcemenu" in sys.argv[2:]

    if bSpecifiedDirectory:
        specifiedDir = sys.argv[1]
        # for files outside this repo
        if os.path.isfile(specifiedDir):
            # single file
            createMenu4MD(specifiedDir)
        else:
            # parse other directory
            # os.path.walk(specifiedDir, visit, None)
            for root, dirs, files in os.walk(specifiedDir):
                visit(root, dirs, files)

        sys.exit(1)

    # for this repository only
    for root, dirs, files in os.walk("../"):
        visit(root, dirs, files)

    print("-----")

    RE_PATTERN_LINK_FILE = re.compile(r"\[.*?\]\s*\(.*?(?=[^/]+\.md)([^/()]+\.md)\s*\)")
    linkFiles = []
    for key in all_md_filenames:
        if key.lower().endswith("readme.md"):
            # print( key)
            fp = open(all_md_filenames[key])
            data = fp.read()
            fp.close()

            urls = re.findall(RE_PATTERN_LINK_FILE, data)
            for url in urls:

                unescape_url = parse.unquote(url)
                if unescape_url in all_md_filenames:
                    linkFiles.append(unescape_url)
                else:
                    print("no such key: ", unescape_url)

    for linkFile in linkFiles:
        del all_md_filenames[linkFile]
        pass

    for key in all_md_filenames:
        print(key)
