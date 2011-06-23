import unittest
import antlr3
import sys
import os
s = os.path.sep
sys.path.append('..'+s+'src'+s+'python')
from pycasm.syntax import pycasmLexer, pycasmParser, pycasmDirectiveWalker, pycasmSymnameWalker, pycasmGenerativeWalker, pycasmBytecodeGenerator

def runLexer(input):
	lexer = pycasmLexer(antlr3.ANTLRStringStream(input))
	return antlr3.CommonTokenStream(lexer)

def getTokenType(input):
	lexer = pycasmLexer(antlr3.ANTLRStringStream(input))
	return lexer.nextToken().getType()

def testLexer(input):
	lexer = pycasmLexer(antlr3.ANTLRStringStream(input))
	try:
		t = []
		t.append(lexer.nextToken())
		while t[-1] != antlr3.EOF_TOKEN:
			t.append(lexer.nextToken())
	except antlr3.RecognitionException, re:
		print('textLexer failed but constructed tokens:\n'+'\n'.join([lexer.getTokenErrorDisplay(tt) for tt in t]))
		raise re

def runParser(tokens):
	try:
		parser = pycasmParser(tokens)
		r = parser.root()
		return r
	except Exception,e:
		print("Parser failed on input: "+tokens.toString())
		raise e

def testParser(input):
	tokens = runLexer(input)
	runParser(tokens)

def chainDirectiveWalker(parser_result, tokens):
	root = parser_result.tree
	nodes = antlr3.tree.CommonTreeNodeStream(root)
	nodes.setTokenStream(tokens)
	dwalker = pycasmDirectiveWalker(nodes)
	#try:
	r = dwalker.root()
	return r
	#except Exception,e:
	#	print("Walker failed on input: "+tokens.toString())#.toString())
	#	raise e

def runPycasm(input):
	tokens = runLexer(input)
	chainDirectiveWalker( runParser(tokens), tokens )

# LEXER TESTS
# todo: split lexer, parser, walker tests out to different files.

class TestLexer(unittest.TestCase):

	def testIndent(self):
		testLexer(
'''
.dirname argument another
	body
	more body
.end dirname
''')

	def testIndentStaircase(self):
		testLexer(
'''
.dirname argument another
  body
    more body
	  last step of the staircase 
.end dirname
''')

	def testNoDedentButEof(self):
		testLexer('''.dirname argument another
  body
    more body
	 one more
	  last step of the staircase''')

	def testWS(self):
		from pycasm.syntax.pycasmLexer import WS
		from pycasm.syntax.pycasmParser import tokenNames
		tt = getTokenType(' ')
		self.assertEqual(tt, WS, tokenNames[tt]+" != "+tokenNames[WS])

	def testCommentNoNL(self):
		testLexer('# comment me out')

	def testCommentWithNL(self):
		testLexer('# comment me out\n\n\n')

	def testOnelinerDotDotDirective(self):
		testLexer('''..def nameMe (args, args)''')

	def testDotDotDirectiveWithBody(self):
		testLexer('''
..def nameMe (args, args)
	print(2222)
	print 2 
	   
	   ppp
	print 12 

	print 23	 
''')

	def testThisOne(self):
		testLexer('''
.codeobject
	.consts
		.codeobject
			.firstlineno
				04000000
			.lnotab
				0f01
		.int(28)
''')

# PARSER TESTS

class TestParser(unittest.TestCase):

	def testUnrestrictedDirective(self):
		testParser('''..OneLiner''')

	def testUnrestrictedDirectiveWithArgs(self):
		testParser('''..OneLiner name(1,2, 33) gg''')

	def testUnrestrictedDirectiveWithBody(self):
		testParser('''..OneLiner name(1, 2)
	print(dsklfj)
		print(333)
''')

	# Basic common tests.
	def testEmpty(self):
		testParser("")

	def testNewlines(self):
		testParser("\r\n\n\n\r\n")

	# Bytecode generation tests.
	def testHex(self):
		testParser("5f 67")
		testParser("2a6f aabb cc")
		testParser("01abcdef a0")

	# todo: this code raises exception to unittest, fix the test
	#def testHexFailure(self):
	#	self.assertRaises(antlr3.RecognitionException, testParser("01abcdefa0"))

	def testQuotedString(self):
		testParser("'generate_me'")

	def testTypedValue(self):
		testParser("s'generate_me' t'another type'")

	# Symnames' tests.
	def testSymnames(self):
		testParser("this_is_A_SymName")

	# Directives' tests.
	def testOneLinerDirectiveWithArgs(self):
		testParser(".oneLinerDirective 012 hh")

	def testNoArgsOneLinerDirective(self):
		testParser(".oneLinerDirective")

	def testFollowedDirective(self):
		testParser(".stamp now\n'string'")

	#def testPythonDirective(self):
	#	testParser(".python")

	def testDirectiveWithBody(self):
		testParser('''
.codeobject
	.argscount 0
	.another 92 11
''')
	
	# codeobject
	def ttestCoParse(self):
		testParser(
'''
.python
	dfef
.stamp
.codeobject
	.argcount
	.nlocals
	.stacksize
	.flags
	.code
	.consts
	.names
	.varnames
	.freevars
	.cellvars
	.filename
	.name
	.firstlineno
	.lnotab

''')

# TEST OF THE WHOLE THING

class TestPycasm(unittest.TestCase):

	def testEmpty(self):
		runPycasm('')

	def testUnrestrictedDirectiveDeclaration(self):
		runPycasm('''..def name(a,b):
	print(12)
	print(55)
''')

	#@unittest.expectedFailure
	#def testUndefinedPythonDirective(self):
	#		runPycasm(".undefinedDirective 2.5")

if __name__ == '__main__':
	unittest.main()
