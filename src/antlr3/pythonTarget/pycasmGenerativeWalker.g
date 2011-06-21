/*
	Copyright (c) 2011, Petrov Ilya
	All rights reserved.

	Redistribution and use in source and binary forms, with or without
	modification, are permitted provided that the following conditions are met:
		* Redistributions of source code must retain the above copyright
		  notice, this list of conditions and the following disclaimer.
		* Redistributions in binary form must reproduce the above copyright
		  notice, this list of conditions and the following disclaimer in the
		  documentation and/or other materials provided with the distribution.
		* The name of the author may not be used to endorse or promote products
		  derived from this software without specific prior written permission.

	THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
	ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
	WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
	DISCLAIMED. IN NO EVENT SHALL PETROV ILYA BE LIABLE FOR ANY
	DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
	(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
	LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
	ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
	(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
	SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/

tree grammar pycasmGenerativeWalker;

options
{
backtrack=true;
output=AST;
tokenVocab=pycasmParser;
ASTLabelType=CommonTree;
rewrite=true;
language=Python;
}

@members
{
def expandGenerative(self, gentree):
	# Currently the only generatives pycasm has are types
	# and untyped string wich can be considered as an empty
	# typed string.
	s = gentree.getText()
	type_prefix  = re.search(r'\w*', s).group(0)
	type_suffix = re.search(r'\w*$', s).group(0)
	m = re.search(r'["\'](.+)["\']', s)
	if type_prefix and type_suffix or not s or not m or not m.group(1):
		raise RuntimeError() # todo

	res_ast

	if not type_prefix and not type_suffix:
		res_ast = self.adaptor.create(HEX, ''.join([hex(ord(c))[2:] for c in s[1:-1]]))
	else:
		res_ast = rootScope.getType(type_prefix or string_content).getHexAst(type_suffix or string_content)

	return res_ast

def getErrorHeader(self, e):
	h = super(self.__class__, self).getErrorHeader(e)
	return "\nGENERATIVE WALKER ERROR: " + h

def patchInErrorReporter(self, reporterObject):
	'''Applies monkey patch to overload error reporting methods, all reporterObject\'s methods overload methods of this recognizer.
	Not too pythonic, but handy.
	'''
	import functools
	[setattr(self,method, functools.partial(getattr(reporterObject,method).im_func,self) ) for method in dir(reporterObject)\
                                if callable(getattr(reporterObject, method))]

}

@init {
from pycasm.syntax.errors import StandardErrorReporter
self.patchInErrorReporter(StandardErrorReporter())
}

root
	:
		^(ROOT block?)
	;

block
	:
		^(BLOCK block_child+)
	;

block_child
	:
		HEX
	|	GEN -> ^({self.expandGenerative($GEN)})
	|	block
	;
