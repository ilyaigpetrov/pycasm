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

lexer grammar pycasmLexer;

options {
language=Python;
}

tokens {
DEDENT;
INDENT;
BLOCK;
ARGS;
GEN;
NEWLINE;
}

@header {
import decimal
infinity = decimal.Decimal('Infinity')
}

@members {
def getColumn(self):
	return self.getCharPositionInLine()
	#return self._state.tokenStartCharPositionInLine # is it different?

# Emit multiple tokens at once.
def emit(self, token=None):
	Lexer.emit(self, token)
	self.tokens.append(self._state.token) # token may be None but not the self._state.token
	self.lookBehindToken = self._state.token

def nextToken(self):
	Lexer.nextToken(self)
	try:
		return self.tokens.pop(0)
	except IndexError:
		return EOF_TOKEN

# Error handling
def patchInErrorReporter(self, reporterObject):
	'''
	Applies monkey patch to overload error reporting methods, all reporterObject\'s methods overload methods of this recognizer.
	Not too pythonic, but handy.
	'''
	import functools
	[setattr(self, method, functools.partial(getattr(reporterObject,method).im_func, self) ) for method in dir(reporterObject)\
                                if callable(getattr(reporterObject, method))]

}

@init {
# INDENT-DEDENT generation.
self.indentStack = []
self.numberOfSpaces = 0
self.tokens = []
self.lookBehindToken = None
from pycasm.syntax.errors import StandardErrorReporter
self.patchInErrorReporter(StandardErrorReporter())
}

DOT_END
	:		
		'.end'
	;

DOT_NAME
	:
		'.' NAME
	;

DOT_DOT_NAME
	:
		'..' NAME
	;

COMMENT
@init {
$channel=HIDDEN
}
	:    {self.getColumn() == 0}? => WS* '#' (~'\n')* '\n'*
	|    {self.getColumn() > 0 }? => WS* '#' (~'\n')*
	;

DOT_ARGS
	:
	{ self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     }?=> ~(Alpha|'\n'|'\r') ~('\n'|'\r'|'#')+
	;

DOT_DOT_ARGS
	:
	{ self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] }?=> ~(Alpha|'\n'|'\r') ~('\n'|'\r'|'#')+
	;

DOT_DOT_BODY
@init {
self.numberOfSpacesInPythonBlock = 0
self.minNumberOfSpacesInPythonBlock = infinity
}
	:	{ self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME, DOT_DOT_ARGS] }? =>
		('\r'? '\n'
		    { self.numberOfSpacesInPythonBlock = 0 }
		    (
			 ' '  { self.numberOfSpacesInPythonBlock += 1 }
			|'\t' { self.numberOfSpacesInPythonBlock += 8 }
		    )*
		    (
			{ min(self.minNumberOfSpacesInPythonBlock, self.numberOfSpacesInPythonBlock) > self.numberOfSpaces }? => (
				NonWS (NonWS|WS)*
				{ self.minNumberOfSpacesInPythonBlock = min(self.minNumberOfSpacesInPythonBlock, self.numberOfSpacesInPythonBlock) }
			)
		    )?
		)*
	;

HEX_DQUAD
	:
		HEX_QUAD HEX_QUAD
	;

HEX_QUAD
	:
		HEX_PAIR HEX_PAIR
	;

HEX_PAIR
	:
		HEX_DIGIT HEX_DIGIT
	;

HEX_DIGIT
	:
		HexDigit
	;

// This token conflicts with lookbehind and antlr's prediction -- commented it out for now.
//HEX_SEQUENCE
// used to declare string content as sequence of bytes in hex
//	:
//		HexDigit+
//	;

TYPED_VALUE
	:
		Type '\'' ~('\'')* '\''
	;

STRING
	:	'\'' ~('\'')+ '\''
	;

NAME	:
		(Alpha|'_')+
	;

INDENT_OR_DEDENT
@init {
self.numberOfSpaces = 0
}
	:
		( ( ('\r')? '\n' ) | '\t' | ' ' )*
		( ('\r')? '\n' )
		( ' '  	{ self.numberOfSpaces += 1 }
		| '\t'	{
			  self.numberOfSpaces += 8 
			  self.numberOfSpaces -= (self.numberOfSpaces \% 8)
			}
		)*
	{
		
		self.emit(ClassicToken(NEWLINE, '\n'))
		
		if self.numberOfSpaces!=0 and (len(self.indentStack)==0 or self.numberOfSpaces > self.indentStack[-1]):
			t = ClassicToken(INDENT, '>')
			t.setCharPositionInLine( self.indentStack[-1] if len(self.indentStack) else 0 )
			t.setLine( self.input.getLine() )
			self.emit(t)
			self.indentStack.append(self.numberOfSpaces)
		else:
			while len(self.indentStack)!=0 and self.numberOfSpaces < self.indentStack[-1]:
				del self.indentStack[-1]
				t = ClassicToken(DEDENT, '<')
				t.setCharPositionInLine( self.indentStack[-1] if len(self.indentStack) else 0 )
				t.setLine( self.input.getLine() )
				self.emit(t)
			ss = self.indentStack[-1] if len(self.indentStack)!=0 else 0
			if self.numberOfSpaces != ss:
				self.raiseRecognitionException(MismatchedTokenException(' ' if self.numberOfSpaces < ss else '{backspace}',self.input), "Uneven indent. Make it larger or smaller (f.e. "+str(ss)+").")
	}
	;

WS	:	(' '|'\t')
	;

// Fragments

fragment
NonWS
	:
		~(WS|'\n'|'\r')
	;


fragment
AlphaNum:
		(Alpha|Digit)
	;

fragment
Type	:	
		's'|'t'
	;

fragment
Alpha
	:
		('a'..'z'|'A'..'Z')
	;

fragment
HexAlpha
	:
		('a'..'f'|'A'..'F')
	;

fragment
HexDigit
	:
		(HexAlpha|Digit)
	;

fragment
Digit	:
		'0'..'9'
	;
