print('''
 ok, we want to work with pycasm lanuage from python
 to create new directives, dot-dot-directives and whatever
''')
from pycasm.language import rootScope
print(' rootScope is unrestricted, see isinstance(rootScope, RestrictedScope): ')
from pycasm.semantics import RestrictedScope, TemplateDirective
print( isinstance(rootScope, RestrictedScope) )
print(' False, cool, go on.')
print('''
 Now see what is in rootScope:
''')
print(rootScope)
print('''
 Bunch of directives, will we take some?
 pycfile and def are my of favourites, I\'ll show you why.
''')
print('''
 def first. Like python's def this is used for declaration
 of new functions which are called directives in pycasm.
 Every directive starts with a dot. There is subclass of
 directives which even starts with two dots, but they are
 too much to explain for now.
 
 Ugh, that is a fluff, I'll show you an example instead.
 
 ..def IWouldLikeAllPeopleScreamAAAAAroundMe():
    print("I would like to say hello to my grandma. Hi, grandma! Haven't seen you so much.")
	return adaprot.create(AAAA,'AAAA') # what a disgusting shit!

 Body is in python, caption is not. But pretends to be.
 I've shown def syntax in pycasm, but we are in python now, so don't try it.
 However from here we can do like this.

 rootScope.addDirective(
	TemplateDirective(lambda:adaptor.create(HEX,'AAAA'), 'cream')
 )

 This should work fine -- try it. Call ready() when ready to go on.
 You can cheat.
''')
import antlr3
adaptor = antlr3.tree.CommonTreeAdaptor()
from pycasm.syntax.pycasmParser import HEX

def cheat():
	rootScope.addDirective(
		TemplateDirective(lambda:adaptor.create(HEX,'AAAA'), 'scream')
	)
	ready()

TemplateDirective(lambda:adaptor.create(HEX,'AAAA'), 'scream')
	
def ready():
	print('''
 Fine. Lets call it: rootScope.getDirective('scream').invoke()
 
 It returns some tree structure (Abstract Common Tree, you know),
 which is converted to bytecode afterwards.
 
''')


















