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

parser grammar pycasmParser;

options
{
backtrack=true;
output=AST;
memoize=true;
tokenVocab=pycasmLexer;
language=Python;
}

tokens {
ROOT;
HEX;
SYM;
}

@members {
def patchInErrorReporter(self, reporterObject):
	'''
	Applies monkey patch to overload error reporting methods, all reporterObject\'s methods overload methods of this recognizer.
	Not too pythonic, but handy.
	'''
	import functools
	[setattr(self,method, functools.partial(getattr(reporterObject,method).im_func,self) ) for method in dir(reporterObject)\
                                if callable(getattr(reporterObject, method))]

def reportError(self, e):
	super(self.__class__, self).reportError(e)
	#raise e
}

@init {
from pycasm.syntax.errors import StandardErrorReporter
self.patchInErrorReporter(StandardErrorReporter())
}

root
	:
		(block| sp+)? EOF
		-> ^(ROOT block?)
	;

sp	:
		(WS|NEWLINE)+ ->
	;

block
	:
		h=block_head
		block_chain*
		-> { not isinstance($h.tree, type(None)) }? ^(BLOCK block_head block_chain*)
		->
	;

block_head
	:
		chain_element
	|	block_chain
	;

block_chain
	:
		space_element+ chain_element?
	;

chain_element
	:	sym_name
	|	generative
	|	hex_code
	;

space_element
	:
		directive
	|	unrestricted_directive
	|	NEWLINE? INDENT! block NEWLINE? DEDENT!?
	|	sp
	;

unrestricted_directive
	:
		DOT_DOT_NAME DOT_DOT_ARGS? DOT_DOT_BODY? -> ^(DOT_DOT_NAME DOT_DOT_ARGS? DOT_DOT_BODY?)
	;

directive
	:
		{ self.input.LT(1).getCharPositionInLine() == 0 or self.input.LT(-1) and self.input.LT(-1).getType() in [INDENT, DEDENT, NEWLINE] }?
	=> 	(
		directive_header
			(NEWLINE INDENT block NEWLINE? DEDENT?
				(DOT_END WS+
					(NAME
						{
						dh = $directive_header.tree.toString()[1:]
						if not dh.startswith($NAME.text):
							self.reportError(".end directive must have argument of the same name as directive '"+dh+"', compare with '"+$NAME.text+"'.") # dirty
						}
					)
				)?
			| NEWLINE
			)?
		)  -> ^({$directive_header.tree} block?)
	;

directive_header
	:	
		DOT_NAME DOT_ARGS? -> ^(DOT_NAME ^(ARGS DOT_ARGS?))
	;

sym_name
	:
		NAME -> ^(SYM NAME)
	;

generative
	:
	(
		c=STRING
	|	c=TYPED_VALUE
	)	-> ^({self.adaptor.create(GEN, $c.text)})
	;

hex_code:
	(	h=HEX_PAIR
	|	h=HEX_QUAD
	|	h=HEX_DQUAD
	//|	h=HEX_SEQUENCE
	) -> ^({self.adaptor.create(HEX, $h.text)})
	;
