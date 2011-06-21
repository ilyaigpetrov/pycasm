# first step
# sift all grammars through antlr
import os
import sys
project_root = os.path.abspath('..')+'\\'
pycasm_sources = project_root+'\\src\\'
grammars_dir = pycasm_sources+'antlr3\\javaTarget\\'
output_dir = pycasm_sources+'java\\pycasm\\parser' # relative to grammars_dir
libs_dir = project_root+'libs\\'

def trace(msg):
	print "\n!"+msg+"\n"

def fail():
	trace("test_them_all failed")
	sys.exit(1)

trace("test_them_all is processing grammars")

ext = '.g'
#gs = [file[0:-len(ext)] for file in os.listdir(grammars_dir) if file.lower().endswith(ext)]
# Grammars must be processed in this fixed order.
gs = ['pycasmLexer','pycasmParser','pycasmDirectiveWalker','pycasmSymnameWalker','pycasmGenerativeWalker','pycasmBytecodeGenerator']
for g in gs:
	#print 'antlr3 -lib '+output_dir+' -o '+output_dir+' '+grammars_dir+g+'.g'
	os.system('pyantlr -o '+output_dir+' '+grammars_dir+g+ext) and fail()

classpath = pycasm_sources+'java\\;'
libs = [file for file in os.listdir(libs_dir) if file.lower().endswith('.jar')]
for l in libs:
	classpath += libs_dir + l + ';'

classpath += ';.\\'

trace("test_them_all is compiling generated classes")

for g in gs:
	command = 'javac -nowarn -Xlint:unchecked -cp '+classpath+' '+output_dir+'\\'+g+'*.java'
	trace(command)
	os.system(command) and fail()

trace("test_them_all is compiling and running tests")

os.system('javac -nowarn -Xlint:unchecked -cp '+classpath+' '+'*Test*.java') and fail()
os.system('java -cp '+classpath+' org.junit.runner.JUnitCore TestPycasm') and fail()
