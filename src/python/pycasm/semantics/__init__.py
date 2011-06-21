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

__all__ = ['Function', 'Directive', 'InlineDirective', 'Generative', 'Type', 'Scope']

class SemanticException(Exception):
	def __init__(self, message):
		super(SemanticException, self).__init__(message)


class Function(object):
	'''AST->AST via invokeCommon(body_ast=None)'''
	def __init__(self, ast2astPythonFunction):
		self.invokeCommon = ast2astPythonFunction


class Directive(Function):

	def __init__(self, ast2astPythonFunction, name):
		super(Directive, self).__init__(ast2astPythonFunction)
		self.name = name

	def __initFromCopy__(self, directive):
		return self.__init__(directive.invokeCommon, directive.name)

	def getName(self):
		return self.name

	def invoke(self, body_ast=None, args_ast=None):
			if args_ast:
				return self.invokeCommon(body_ast, args_ast)
			else:
				return self.invokeCommon(body_ast)

class InlineDirective(Directive):
	'''Every inline directive is also online directive'''
	def invokeInline(self, args_ast):
		pass


class Generative(Function):

	def __init__(self, ast2astPythonFunction):
		super(Generative, self).__init__(ast2astPythonFunction)

	def getHexAst(self, body):
		'''Returns nothing but the ast of hex nodes.'''
		# transform to body?
		self.invokeCommon(body)


class Type(Generative):

	def __init__(self, generative, prefix=None, suffix=None):
		super(Type, self).__init__(generative)
		if prefix is None and suffix is None:
			print('type generative error')
			raise RuntimeError() # todo
		if prefix is not None and suffix is not None:
			print('type generative error #2')
			raise RuntimeError() # todo
		self.prefix = prefix
		self.suffix = suffix

	def getPrefix(self):
		return self.prefix

	def getSuffix(self):
		return self.suffix


class UnrestrictedDirective(Directive):
	'''
	Always ruturns empty ast.(?)
	Doesn't conforms to strict order inside template.
	Also a dot-dot directive for it starts with two dots in pycasm syntax.
	'''
	def __init__(self, directive):
		super(UnrestrictedDirective, self).__init__( directive.invokeCommon, directive.getName())


class Scope(object):

	def __init__(self):
		self.opnames = {}
		self.types = {}
		self.directives = {}

	def __str__(self):
		import pprint
		pf = pprint.pformat
		return '''# OPNAMES

'''+pf(self.opnames)+'''
\n# TYPES

'''+pf(self.types)+'''
\n# DIRECTIVES

'''+pf(self.directives)
		
	def getType(self, type_name):
		pass

	def addType(self, type):
		# todo: all types are defined by prefix, fix it.
		self.types[type.getPrefix()] = type

	def addTypes(self, types):
		pass

	def getDirective(self, directive_name):
		return self.directives.get(directive_name)

	def addDirective(self, directive):
		self.directives[directive.getName()] = directive

	def addDirectives(self, directives):
		for d in directives:
			self.addDirective(d)

	def getOpname(self, opname):
		pass

	def addOpname(self, opname):
		pass

	def addOpnames(self, opnames):
		pass


class RestrictedScope(Scope):

	def __init__(self, order=[]):
		super(RestrictedScope, self).__init__()
		self.DirectivesNamesOrder = order

	def getOrder(self):
		return self.DirectivesNamesOrder

	def getDirectiveOrders(self, name):
		return [i for i,x in enumerate(self.DirectivesNamesOrder) if x == name]


class TemplateDirective(Directive):
	'''
	Restricts the order of arguments in body_ast.
	That is, uses RestrictedScope.
	'''
	def __init__(self, python_function, name, restrictedScope=RestrictedScope()):
		if restrictedScope is None:
			raise ValueError('TemplateDirective constructor requires restrictedScope as a parameter.')
		super(TemplateDirective, self).__init__(python_function, name)
		self.restrictedScope = restrictedScope

	def getRestrictedScope(self):
		return self.restrictedScope

