
#coding:utf8

import os, sys
import re #, codecs

reload(sys)
sys.setdefaultencoding('utf8') 


RE_PATTERN_CODECOG= re.compile( r"(!\s*\[\s*\]\s*\(\s*http://latex\.codecogs\.com/gif\.latex\?)(.*?)(\))" )

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

				content = re.sub( RE_PATTERN_CODECOG ,  "![](http://www.sciweavers.org/tex2img.php?eq="  + r"\2" + \
						"&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=" + r"\3" , content )

				#content = content.replace( "&plus;" , "+" )

				fp = open( path  , "w" )
				fp.write(content )
				fp.close()

			except:
				import traceback
				traceback.print_exc() 

if __name__=='__main__':

	os.path.walk( ".", visit, None )

	print 'done'

