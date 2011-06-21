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

from pycasm.semantics import Directive, RestrictedScope, Scope, TemplateDirective, UnrestrictedDirective, SemanticException, Generative, Type
import antlr3
import re
import marshal
adaptor = antlr3.tree.CommonTreeAdaptor()

# Builtin scopes
rootScope = Scope()

# Builtin types

def s_function(body_ast):
	# currently body_ast looks like this ^(GEN 'some string')
	if body_ast.children:
		the_string = body_ast.getChild(0).getText()
	else:
		raise SemanticException("AST for pycasm type has some bizzare structure.")
	print("String extracted:"+the_string)
	return body_ast

s_generative = Generative(s_function)
s_type = Type(s_generative, prefix='s')

rootScope.addType(s_type)


# Builtin directives

# COMMON

def reflect(ast):
	return ast

def args2body(body_ast, args_ast):
	args = str(args_ast)
	re.sub(r'^[ \t]*(.*)', lambda m:m.group(1) ,args) # dirty
	return 'def'+args+str(body_ast)

# BASIC UNRESTRICTED DIRECTIVES

def defPythonFunction(body_ast, args_ast):
	body_ast = args2body(body_ast, args_ast)
	m = re.match(r'^def +([^(]+)\(([^)]*)\):', body_ast)
	if not m:
		raise SemanticException("Could't retrieve a name from dot-dot def directive. See body_ast:"+body_ast)
	fname = m.group(1)
	argument = m.group(2)
	body_ast = re.sub(fname, 'directive_'+fname, body_ast, 1)
	ss = (body_ast+'\n_ = directive_'+fname).replace('\r\n','\n')
	exec(ss) in globals(), locals()
	rootScope.addDirective( TemplateDirective(_, fname) )
	return

defDirective = Directive(defPythonFunction, 'def')
defUnrestricted = UnrestrictedDirective(defDirective)
rootScope.addDirective(defUnrestricted)

# BASIC DIRECTIVES

from pycasm.syntax.pycasmParser import HEX, BLOCK

def codeobject(body_ast):
	h = adaptor.createFromType(HEX, '63')
	body_ast.children.insert(0, h)
	return body_ast
	
co_scope = RestrictedScope(
		[
		'argcount',
		'nlocals',
		'stacksize',
		'flags',
		'code ',
		'consts',
		'names',
		'varnames',
		'freevars',
		'cellvars',
		'filename',
		'name',
		'firstlineno',
		'lnotab'
		]
)
	
rootScope.addDirectives(
[
	TemplateDirective(codeobject, 'codeobject', restrictedScope=co_scope),
	TemplateDirective(reflect, 'pycfile', restrictedScope=RestrictedScope(['python','stamp','codeobject']))
]
)