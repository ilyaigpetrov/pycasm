import sys
if len(sys.argv) < 2:
	print(sys.argv[0]+' file')
	sys.exit(1)

import os
filePath = sys.argv[1]
fileName = os.path.basename(filePath)
f = open(filePath, 'r+')
fileContent = f.read()
import re
f.truncate(0)
f.seek(0)
f.write( re.sub(fileName[:-3]+'Lexer', fileName[:-3] , fileContent) )
