
#coding:utf8

import re
import md5
import os

RE_PATTERN_MENU_BODY= re.compile( r"\.\.\.menustart[\s\S]*\.\.\.menuend\n\n\n" )
RE_PATTERN_MENU_SYNTAX= re.compile( r"^(\#+)(.*?)$" )
RE_PATTERN_MENU_JUMP_ID = re.compile( r"^<h\d*\s+id=" )

def createMenu4MD( path ):
	print 'parsing' , path

	fp = open(path)
	content = fp.read()
	fp.close()

	content = re.sub(RE_PATTERN_MENU_BODY,'',content)

	menu = "...menustart\n\n"
	body = ''

	lines = content.split("\n")
	
	bCodeStart = False

	all_title_level = set([])
	for i, line in enumerate( lines ):
		if line[:3]=="```":
			bCodeStart = not bCodeStart

		if bCodeStart:
			if not re.search( RE_PATTERN_MENU_JUMP_ID , line  ):
				body += line+'\n'
			continue

		result = re.search( RE_PATTERN_MENU_SYNTAX , line )
		if result:
			sharps = result.group(1)
			title = result.group(2).strip()
			
			m = md5.new()
			m.update( title )
			id = m.hexdigest()

			curTitleActualLevel = len(sharps) 
			all_title_level.add( curTitleActualLevel )

			menu +=   ( '%s - [%s](#%s)' % ( '\t' * (  sorted(all_title_level).index( curTitleActualLevel )  )  , title ,  id  ) )  +  '\n'

			body += '<h2 id="%s"></h2>\n' % id 
			#print sharps, title

		if not re.search( RE_PATTERN_MENU_JUMP_ID , line  ):
			body += line+'\n'

	menu += '\n...menuend\n\n\n'  
	
	if bCodeStart :
		raise Exception( "code pair error" )

	#print menu

	fp = open(path , 'w')
	fp.write( menu + body[:-1]   )  # remoev last \n
	fp.close()


	return

def visit( arg, dirname, fnames):
	#print arg
	#print dirname
	#print fnames

	for f in fnames:
		if f[-3:] == '.md':
			path = os.path.join( dirname , f  )
			createMenu4MD( path )


	pass


if '__main__' == __name__ :

	#createMenu4MD( '../dev_notes/ML-傻子机器学习入门.md' )
	os.path.walk( "../dev_notes" , visit , None )



