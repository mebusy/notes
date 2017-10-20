
# Apple Script

# Lexical Conventions

## Identifiers

 - Identifiers are **NOT** case sensitive
    - AppleScript记住并强制执行标识符的第一个大写。 
    - 所以如果它首先遇到一个标识符作为myAccount，那么以后在编译时，将MyAccount和myaccount这样的版本更改为myAccount。
 - AppleScript provides a loophole to the preceding rules: identifiers whose first and last characters are vertical bars (|) can contain any characters
    - The leading and trailing vertical bars are not considered part of the identifier.
    - The following are legal identifiers: `|back&forth|`, `|Right*Now!|`

## Comments

 - `--end-of-line comments extend to the end of the line`
 - `#!/usr/bin/osascript  end-of-line comment `
 - nest comments

```
(*  Here are some
    --nested comments
    (* another comment within a comment *)
*)
```

## The Continuation Character ¬  (alt+l)

 - A simple AppleScript statement must normally be entered on a single line
 - You can extend a statement to the next line by ending it with the continuation character, ¬

```
display dialog "This is just a test." buttons {"Great", "OK"} ¬
default button "OK" giving up after 3
```

 - A continuation character within a quoted text string is treated like any other character

## Boolean

 - true, false 

## List
 
 - collection of values, known as items, of any class
 - `{1, 7, "Beethoven", 4.5}`

## Record

 - `{product:"pen", price:2.34}`

## Operators

 - (\*) multiplies two numeric operands
 - (&) joins two objects (such as text strings).
 - The `is equal` operator performs a test on two Boolean values.

## Variables

 - declare and initialize a variable at the same time with a `copy` or `set` command.

```
set myName to "John"
copy 33 to myAge
```

## Expressions

 - `3 * 7`
 - 对象说明符 指定查找另一个对象所需的一些或全部信息。
    - 例如，以下对象说明符指定一个命名文档：
    - document named "FavoritesList"

## Statements

 - A simple statement is one that can be written on a single line:
    - `set averageTemp to 63 as degrees Fahrenheit`
 - A compound statement is written on more than one line, can contain other statements, and has the word `end` (followed, optionally, by the first word of the statement) in its last line.

```
tell application "Finder"
    set savedName to name of front window
    close window savedName
end tell
```

## Commands

 - used in an AppleScript statement to request an action
 - Every command is directed at a `target`
    - which is the object that responds to the command
    - The target is usually an application object or an object in macOS, but it can also be a `script` object or a value in the current script.

```
get name of front window of application "Finder"
```

## Results

 - The result of a statement is the value generated
 - AppleScript stores the result in the globally available property `result`

## Raw Codes

 - When you open, compile, edit, or run scripts with a script editor, you may occasionally see terms enclosed in double angle brackets, or chevrons `(«»)` , in a script window or in another window. 
 - These terms are called  `raw format or raw codes` , because they represent the underlying Apple event codes that AppleScript uses to represent scripting terms.
 - For compatibility with Asian national encodings, “《” and “》” are allowed as synonyms for “«” and “»” ( (Option- \ and Option-Shift- \, respectively, on a U.S. keyboard), since the latter do not exist in some Asian encodings.

---

# AppleScript Fundamentals

## AppleScript and Objects

 - AppleScript is an object-oriented language
 - When you write, compile, and execute scripts, everything you work with is an object. An *object* is an instantiation of a class definition, which can include properties and actions.
 - AppleScript defines classes for the objects you most commonly work with, starting with the top-level **script** object
 - Within in a script **object**, you work with other objects, including:
    - AppleScript objects
        - boolean values, scripts, text, numbers, and other kinds of objects for working in scripts , etc
    - macOS objects:
        - such as Finder, System Events, and Database Events (located in /System/Library/CoreServices), define many useful classes.
    - Application objects:
        - Third-party scriptable applications define classes that support a wide variety of features.

## What Is in a Script Object


