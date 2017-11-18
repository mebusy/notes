
#coding:utf8

import os, sys
import re, hashlib ,urllib
import time

RE_PATTERN_CODECOG= re.compile( r"(!\s*\[\s*\]\s*\(\s*http://latex\.codecogs\.com/gif\.latex\?)(.*)" )
RE_PATTERN_CODECOG2= re.compile( r"(http://latex\.codecogs\.com/gif\.latex\?)(.*)" )


def getSha1( path ):
sha1obj = hashlib.sha1()
sha1obj.update( path )
return sha1obj.hexdigest()

def visit(arg, dirname, names):
global list_hash_url

for name in names:
if name[-3:] == '.md':
#print name
try:
path = os.path.join( dirname , name )
fp = open(path)
lines = fp.read().split('\n')
fp.close()


for line in lines:
if line.find( "http://latex.codecogs.com/gif.latex?" ) != -1:


results = re.findall( RE_PATTERN_CODECOG , line  )

if len( results ) > 0 and len( results[0] ) > 1:
latex = results[0][1][:-1].strip()
else:
results = re.findall( RE_PATTERN_CODECOG2 , line  )

latex = results[0][1].strip()

if len( results ) > 0 and len( results[0] ) > 1:
pass
else:
print path,line , 'is not a inline image'
sys.exit(1)


# 统一处理
link = "http://www.sciweavers.org/tex2img.php?eq=" + latex + "&fs=12&ff=arev&edit=0"

link = link.replace( "&plus;" , "%2B")

#print link

sha1= getSha1( link )
#os.system( 'curl "%s" > ../imgs/%s.png' % ( link + str(int(time.time())) , sha1 ) )

print sha1 , link
print urllib.unquote(link)

list_hash_url.append( "sha1:\t" + sha1 + "\n"  )

list_hash_url.append( "link:\t" +  link + "\n"   )

list_hash_url.append( "unquote:\t" + urllib.unquote(link) + "\n"   )
list_hash_url.append( "\n"  )
list_hash_url.append( "\n"  )


"""


for result in results:
#print result[1]
#print re.findall( RE_PATTERN_ESCAPE ,  result[1] )
link = "http://www.sciweavers.org/tex2img.php?eq=" + result[1] + "&fs=12&ff=arev&edit=0"
print link

sha1= getSha1( link )
os.system( 'curl "%s" > ../imgs/%s.png' % ( link, sha1 ) )
#"""

"""
content = re.gsub( RE_PATTERN_CODECOG ,  "http://www.forkosh.com/cgi-bin/mimetex.cgi?"  + r'\2\3'   , content )
content = re.gsub( RE_PATTERN_ESCAPE ,   '+'  , content )

fp = codecs.open( path  , "w", "utf-8")
            fp.write(content )
            fp.close()
            """

except:
import traceback
traceback.print_exc() 

if __name__=='__main__':
list_hash_url = []
os.path.walk( ".", visit, None )

output = "".join(list_hash_url )
fp =  open( "latex_hash_url.txt"   , "w" )
fp.write( output )
fp.close()

print 'done'

