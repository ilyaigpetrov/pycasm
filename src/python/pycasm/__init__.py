# Copyright (c) 2011, Petrov Ilya
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * The name of the author may not be used to endorse or promote products
#       derived from this software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL PETROV ILYA BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

__all__ = ['parser','assemble']
import pycasm.syntax

def parse(asmcode):
	import antlr3
	lexer = pycasm.syntax.pycasmLexer(antlr3.ANTLRStringStream(asmcode))
	tokens = antlr3.CommonTokenStream(lexer)
	parser = pycasm.syntax.pycasmParser(tokens)
	return parser.root().tree

def assemble(fstream):
	import antlr3
	bytecode = ''
	#try:
	lexer = pycasm.syntax.pycasmLexer(fstream)
	tokens = antlr3.CommonTokenStream(lexer)
	parser = pycasm.syntax.pycasmParser(tokens)
	root_return = parser.root()
	ast = root_return.tree

	nodes = antlr3.tree.CommonTreeNodeStream(ast)
	nodes.setTokenStream(tokens)
	dwalker = pycasm.syntax.pycasmDirectiveWalker(nodes)
	dwalker_root = dwalker.root()
	ast = dwalker_root.tree

	nodes = antlr3.tree.CommonTreeNodeStream(ast)
	nodes.setTokenStream(tokens)
	snwalker = pycasm.syntax.pycasmSymnameWalker(nodes)
	ast = snwalker.root().tree

	nodes = antlr3.tree.CommonTreeNodeStream(ast)
	nodes.setTokenStream(tokens)
	genwalker = pycasm.syntax.pycasmGenerativeWalker(nodes)
	ast = genwalker.root().tree

	nodes = antlr3.tree.CommonTreeNodeStream(ast)
	nodes.setTokenStream(tokens)
	generator = pycasm.syntax.pycasmBytecodeGenerator(nodes)
	bytecode = generator.root()
	#except Exception,e:
	#	if isinstance(e, antlr3.RecognitionException):
	#		return
	#	raise e

	return bytecode







