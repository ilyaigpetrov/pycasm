import os
import sys
target = 'python'
s = os.path.sep
project_root = os.path.abspath('..')+s
pycasm_sources = project_root+s+'src'+s
grammars_dir = pycasm_sources+'antlr3'+s+target+'Target'+s
output_dir = pycasm_sources+target+s+'pycasm'+s+'syntax'+s # relative to grammars_dir
libs_dir = project_root+'libs'+s

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
	print('generating recognizer from grammar:'+g)
	os.system('./pyantlr -o '+output_dir+' '+grammars_dir+g+ext) and fail()
# patch 'No module named <...>Lexer' error
for g in gs[1:]:
	filePath = output_dir + g + '.py'
	os.system('python .'+s+'tools'+s+'pypatch.py '+filePath) and fail('patching')
# run tests
os.system('python TestPycasm.py') and fail()
