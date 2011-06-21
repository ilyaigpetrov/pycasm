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
 * This grammar describes the first pycasm transformation step.
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
tree grammar pycasmDirectiveWalker;

options
{
output=AST;
tokenVocab=pycasmParser;
ASTLabelType=CommonTree;
language=Python;
}

@header
{
import antlr3
from pycasm.language import rootScope
from pycasm.semantics import SemanticException, RestrictedScope
}

@members
{
def expandDirective(self, directiveOrder, dotName, args_ast, body_ast):
	# todo: doesn\'t make use of scopes stack, fix 
	name = dotName[1:]
	d = rootScope.getDirective(name)
	if not d:
		raise SemanticException('Directive '+dotName+' is not defined in the root scope.')
	
	if isinstance(rootScope, RestrictedScope):
		# if current scope is restricted check directiveOrder
		o = rootScope.getDirectiveOrders(name)
		if [x for x in o if x == directiveOrder]:
			return d.invoke(body_ast, args_ast)
		print('todo expandDirective #2')
		raise SemamticException('Directive '+dotName+' is out of order of the root scope.\n DirectiveOrder:'+str(directiveOrder)+'.')
	else:
		res = d.invoke(body_ast, args_ast)
		return res

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
self.scopeCountersStack = [0]
self.scopesStack = [rootScope]
}

root
	:
		^(ROOT block?)
	;

block
@after {
if self.scopesStack:
	numberOfDirectives = self.scopeCountersStack.pop()
	lastRestrictedScope = self.scopesStack.pop()
	#if isinstance(lastRestrictedScope, RestrictedScope):
	#	if len(lastRestrictedScope.getOrder()) != numberOfDirectives:
	#		raise SemanticException('Number of directives isn\'t adequate to current scope number of directives:'+str(lastRestrictedScope.getOrder())+' vs '+str(numberOfDirectives))
}
	:
		^(BLOCK block_child*)
	;

block_child
	:
		directive
	|	dot_dot_directive
	|	^(SYM NAME)
	|	HEX
	|	GEN
	|	block
	;

dot_dot_directive
	:	
		^(DOT_DOT_NAME DOT_DOT_ARGS? DOT_DOT_BODY?)

		{
			# look up scope
			name = $DOT_DOT_NAME.getText()[2:]
			if name:
				d = rootScope.getDirective(name)
				if d:
					d.invoke($DOT_DOT_BODY, $DOT_DOT_ARGS)
				else:
					raise SemanticException("Undefined unrestricted directive with name:"+name+'.')
			else:
				raise SemanticException("Undefined unrestricted directive with empty name.")
		}

		// -> ^({self.adaptor.create(HEX,'00')}) // works, but not what I want
		//-> ^() // won't compile
		//-> ^({self.adaptor.nil()}) // gives AttributeError: 'NoneType' object has no attribute 'isNil'
		//-> // AttributeError: 'NoneType' object has no attribute 'isNil'
		//-> ^($block_child) // antlr3.tree.RewriteEmptyStreamException: rule retval
		//-> ^({self.adaptor.nil()} {self.adaptor.nil()}) // gives AttributeError: 'NoneType' object has no attribute 'isNil'
		-> 
	;

directive
@init {
ifBlockMatched = False
}
@after {
self.scopeCountersStack[-1] += 1
}
	:
		^(DOT_NAME ^(ARGS DOT_ARGS*)
			(
			{
			self.scopeCountersStack.append(0)
			#self.scopesStack.append( self.scopesStack[-1].getDirective($DOT_NAME.getText()[1:]).getRestrictedScope() ) # what the heck
			d = rootScope.getDirective($DOT_NAME.getText()[1:])
			if not d:
				raise SemanticException("No directive with name "+$DOT_NAME.getText()+" in rootScope.")
			self.scopesStack.append( d.getRestrictedScope() )
			}
			block
			{
			ifBlockMatched = True
			}
			)?
		)
		-> ^({self.expandDirective(self.scopeCountersStack[-1], $DOT_NAME.getText(), $ARGS if $ARGS.children else None, $block.tree if ifBlockMatched else None)})
	;
