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

/*
 * This grammar describes the second pycasm transformation step.
 * 
 * Tree transformation steps:
 *
 * 0) on input we have a pycasm tree: directives, symnames, bcgen, hex code
 * 1) expand directives,
 *        bcgen on demand (for symnames defs, mutable), symnames on demand (for symnames defs, symnames are kept)
 *    result: symnames, partialy sub-d bcgen, hex code
 * 2) expand symnames
 *    result: hex code with bcgen
 * 3) expand bcgen
 *    result: indented `xxd -ps`-like hex
 * 4) expand hex codes
 *    result: compiled bytecode
 *
**/
tree grammar pycasmSymnameWalker;

options
{
output=AST;
tokenVocab=pycasmParser;
ASTLabelType=CommonTree;
language=Python;
}

@header {
import opcode
from pycasm.semantics import SemanticException
import re
}

@members
{

def as_long(self, x):
	# todo: if x is too long, 'L' is appended, fix
	# todo: delete this method, sub-te on smth like marshal.dumps(3)[1:].encode('hex')
	return  ''.join([
			('0'+(hex( x      & 0xff))[2:])[-2:],
			('0'+(hex((x>> 8) & 0xff))[2:])[-2:],
			('0'+(hex((x>>16) & 0xff))[2:])[-2:],
			('0'+(hex((x>>24) & 0xff))[2:])[-2:]
		])

def expandSymname(self, symname):
	if symname.upper() not in opcode.opmap:
		raise SemanticException("opname "+symname+" is not defined for this scope.")
	return self.adaptor.create( HEX, ('0'+hex(opcode.opmap[symname.upper()])[2:])[-2:] )

def expandGenerative(self, generative_ast):
	text = generative_ast.getText()
	if text.startswith('"') or text.startswith("'"):
		prefix = ''
		the_string = text
	else:
		m = re.match(r'(\w+)(.+)', text)
		prefix = m.group(1)
		the_string = m.group(2)

	result_hex_string = ''

	if prefix:
		if prefix not in 'st':
			raise SemanticException("Currently the only supported types for strings are 's' and 't'.")
		result_hex_string = hex(ord('s'))[2:] + self.as_long(len(the_string)-2) # todo: int to bytes conversion

	return self.adaptor.create( HEX, result_hex_string + ''.join([hex(ord(c))[2:] for c in the_string[1:-1]]) )
		

def patchInErrorReporter(self, reporterObject):
	'''
	Applies monkey patch to overload error reporting methods, all reporterObject\'s methods overload methods of this recognizer.
	Not too pythonic, but handy.
	'''
	import functools
	[setattr(self,method, functools.partial(getattr(reporterObject,method).im_func,self) ) for method in dir(reporterObject)\
                                if callable(getattr(reporterObject, method))]

}

@init {
from pycasm.syntax.errors import StandardErrorReporter
self.patchInErrorReporter(StandardErrorReporter())
import opcode
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
		^(SYM NAME) -> ^({self.expandSymname($NAME.text)})
	|	HEX
	|	GEN -> ^({self.expandGenerative($GEN)})
	|	block
	;
