import os
# grammars processing
import sys
target = 'python'
project_root = os.path.abspath('..')+'\\'
pycasm_sources = project_root+'\\src\\'
grammars_dir = pycasm_sources+'antlr3\\'+target+'Target\\'
output_dir = pycasm_sources+target+'\\pycasm\\syntax\\' # relative to grammars_dir
libs_dir = project_root+'libs\\'

def trace(msg):
	print "\n!"+msg+"\n"

def fail(msg=''):
	trace("test_them_all failed on: "+msg)
	sys.exit(1)

trace("test_them_all is processing grammars")

ext = '.g'
# Grammars must be processed in this fixed order.
gs = ['pycasmLexer','pycasmParser','pycasmDirectiveWalker','pycasmSymnameWalker','pycasmGenerativeWalker','pycasmBytecodeGenerator']
for g in gs:
	os.system('pyantlr -o '+output_dir+' '+grammars_dir+g+ext) and fail()
# patch 'No module named <...>Lexer' error
for g in gs[1:]:
	filePath = output_dir + g + '.py'
	os.system('.\\tools\\pypatch.py '+filePath) and fail('patching')
# run tests
os.system('python TestPycasm.py') and fail()
