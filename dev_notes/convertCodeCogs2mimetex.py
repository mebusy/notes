
#coding:utf8

import os, sys
import re #, codecs

reload(sys)
sys.setdefaultencoding('utf8') 


RE_PATTERN_CODECOG= re.compile( r"(!\s*\[\s*\]\s*\(\s*http://latex\.codecogs\.com/gif\.latex\?)(.*?)(\))" )
RE_PATTERN_ESCAPE = re.compile( r"&[a-z][A-Z]+;" )

def visit(arg, dirname, names):
	for name in names:
		if name[-3:] == '.md':
			#print name
			try:
				path = os.path.join( dirname , name )
				fp = open(path)
				content = fp.read()
				fp.close()

				
				#results = re.findall( RE_PATTERN_CODECOG , content  )
				"""
				for result in results:
					#print result[1]
					print re.findall( RE_PATTERN_ESCAPE ,  result[1] )
				#"""

				content = re.sub( RE_PATTERN_CODECOG ,  "![](http://www.forkosh.com/cgi-bin/mimetex.cgi?"  + r'\2\3'   , content )
				content = re.sub( RE_PATTERN_ESCAPE ,   '+'  , content )

				fp = open( path  , "w" )
				fp.write(content )
				fp.close()

			except:
				import traceback
				traceback.print_exc() 

if __name__=='__main__':

	os.path.walk( ".", visit, None )

	print 'done'

