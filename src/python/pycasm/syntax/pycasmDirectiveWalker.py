# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmDirectiveWalker.g 2011-06-23 13:21:09

import sys
from antlr3 import *
from antlr3.tree import *
from antlr3.compat import set, frozenset

 
import antlr3
from pycasm.language import rootScope
from pycasm.semantics import SemanticException, RestrictedScope



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
Alpha=16
DOT_DOT_BODY=20
Type=26
DOT_DOT_NAME=13
DOT_DOT_ARGS=18
AlphaNum=31
TYPED_VALUE=27
DOT_END=10
HexAlpha=32
HEX_DIGIT=24
DEDENT=4
Digit=30
HEX_DQUAD=22
EOF=-1
ROOT=33
HexDigit=25
INDENT=5
SYM=35
NAME=11
WS=14
NEWLINE=9
NonWS=19
HEX=34
BLOCK=6
ARGS=7
GEN=8
DOT_NAME=12
INDENT_OR_DEDENT=29
COMMENT=15
HEX_QUAD=21
DOT_ARGS=17
STRING=28
HEX_PAIR=23

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "DEDENT", "INDENT", "BLOCK", "ARGS", "GEN", "NEWLINE", "DOT_END", "NAME", 
    "DOT_NAME", "DOT_DOT_NAME", "WS", "COMMENT", "Alpha", "DOT_ARGS", "DOT_DOT_ARGS", 
    "NonWS", "DOT_DOT_BODY", "HEX_QUAD", "HEX_DQUAD", "HEX_PAIR", "HEX_DIGIT", 
    "HexDigit", "Type", "TYPED_VALUE", "STRING", "INDENT_OR_DEDENT", "Digit", 
    "AlphaNum", "HexAlpha", "ROOT", "HEX", "SYM"
]




class pycasmDirectiveWalker(TreeParser):
    grammarFileName = "/root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmDirectiveWalker.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 18, 2009 10:09:25")
    antlr_version_str = "3.1.3 Mar 18, 2009 10:09:25"
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(pycasmDirectiveWalker, self).__init__(input, state, *args, **kwargs)



               
        from pycasm.syntax.errors import StandardErrorReporter
        self.patchInErrorReporter(StandardErrorReporter())
        self.scopeCountersStack = [0]
        self.scopesStack = [rootScope]




        self._adaptor = None
        self.adaptor = CommonTreeAdaptor()
                


        
    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)

     
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


    class root_return(TreeRuleReturnScope):
        def __init__(self):
            super(pycasmDirectiveWalker.root_return, self).__init__()

            self.tree = None




    # $ANTLR start "root"
    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmDirectiveWalker.g:98:1: root : ^( ROOT ( block )? ) ;
    def root(self, ):

        retval = self.root_return()
        retval.start = self.input.LT(1)

        root_0 = None

        _first_0 = None
        _last = None

        ROOT1 = None
        block2 = None


        ROOT1_tree = None

        try:
            try:
                # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmDirectiveWalker.g:99:2: ( ^( ROOT ( block )? ) )
                # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmDirectiveWalker.g:100:3: ^( ROOT ( block )? )
                pass 
                root_0 = self._adaptor.nil()

                _last = self.input.LT(1)
                _save_last_1 = _last
                _first_1 = None
                root_1 = self._adaptor.nil()
                _last = self.input.LT(1)
                ROOT1=self.match(self.input, ROOT, self.FOLLOW_ROOT_in_root64)

                ROOT1_tree = self._adaptor.dupNode(ROOT1)

                root_1 = self._adaptor.becomeRoot(ROOT1_tree, root_1)



                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmDirectiveWalker.g:100:10: ( block )?
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == BLOCK) :
                        alt1 = 1
                    if alt1 == 1:
                        # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmDirectiveWalker.g:100:10: block
                        pass 
                        _last = self.input.LT(1)
                        self._state.following.append(self.FOLLOW_block_in_root66)
                        block2 = self.block()

                        self._state.following.pop()

                        self._adaptor.addChild(root_1, block2.tree)






                    self.match(self.input, UP, None)
                self._adaptor.addChild(root_0, root_1)
                _last = _save_last_1







                retval.tree = self._adaptor.rulePostProcessing(root_0)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return retval

    # $ANTLR end "root"

    class block_return(TreeRuleReturnScope):
        def __init__(self):
            super(pycasmDirectiveWalker.block_return, self).__init__()

            self.tree = None




    # $ANTLR start "block"
    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmDirectiveWalker.g:103:1: block : ^( BLOCK ( block_child )* ) ;
    def block(self, ):

        retval = self.block_return()
        retval.start = self.input.LT(1)

        root_0 = None

        _first_0 = None
        _last = None

        BLOCK3 = None
        block_child4 = None


        BLOCK3_tree = None

        try:
            try:
                # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmDirectiveWalker.g:112:2: ( ^( BLOCK ( block_child )* ) )
                # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmDirectiveWalker.g:113:3: ^( BLOCK ( block_child )* )
                pass 
                root_0 = self._adaptor.nil()

                _last = self.input.LT(1)
                _save_last_1 = _last
                _first_1 = None
                root_1 = self._adaptor.nil()
                _last = self.input.LT(1)
                BLOCK3=self.match(self.input, BLOCK, self.FOLLOW_BLOCK_in_block87)

                BLOCK3_tree = self._adaptor.dupNode(BLOCK3)

                root_1 = self._adaptor.becomeRoot(BLOCK3_tree, root_1)



                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmDirectiveWalker.g:113:11: ( block_child )*
                    while True: #loop2
                        alt2 = 2
                        LA2_0 = self.input.LA(1)

                        if (LA2_0 == BLOCK or LA2_0 == GEN or (DOT_NAME <= LA2_0 <= DOT_DOT_NAME) or (HEX <= LA2_0 <= SYM)) :
                            alt2 = 1


                        if alt2 == 1:
                            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmDirectiveWalker.g:113:11: block_child
                            pass 
                            _last = self.input.LT(1)
                            self._state.following.append(self.FOLLOW_block_child_in_block89)
                            block_child4 = self.block_child()

                            self._state.following.pop()

                            self._adaptor.addChild(root_1, block_child4.tree)




                        else:
                            break #loop2

                    self.match(self.input, UP, None)
                self._adaptor.addChild(root_0, root_1)
                _last = _save_last_1







                retval.tree = self._adaptor.rulePostProcessing(root_0)

                #action start
                        
                if self.scopesStack:
                	numberOfDirectives = self.scopeCountersStack.pop()
                	lastRestrictedScope = self.scopesStack.pop()
                	#if isinstance(lastRestrictedScope, RestrictedScope):
                	#	if len(lastRestrictedScope.getOrder()) != numberOfDirectives:
                	#		raise SemanticException('Number of directives isn\'t adequate to current scope number of directives:'+str(lastRestrictedScope.getOrder())+' vs '+str(numberOfDirectives))

                #action end

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return retval

    # $ANTLR end "block"

    class block_child_return(TreeRuleReturnScope):
        def __init__(self):
            super(pycasmDirectiveWalker.block_child_return, self).__init__()

            self.tree = None




    # $ANTLR start "block_child"
    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmDirectiveWalker.g:116:1: block_child : ( directive | dot_dot_directive | ^( SYM NAME ) | HEX | GEN | block );
    def block_child(self, ):

        retval = self.block_child_return()
        retval.start = self.input.LT(1)

        root_0 = None

        _first_0 = None
        _last = None

        SYM7 = None
        NAME8 = None
        HEX9 = None
        GEN10 = None
        directive5 = None

        dot_dot_directive6 = None

        block11 = None


        SYM7_tree = None
        NAME8_tree = None
        HEX9_tree = None
        GEN10_tree = None

        try:
            try:
                # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmDirectiveWalker.g:117:2: ( directive | dot_dot_directive | ^( SYM NAME ) | HEX | GEN | block )
                alt3 = 6
                LA3 = self.input.LA(1)
                if LA3 == DOT_NAME:
                    alt3 = 1
                elif LA3 == DOT_DOT_NAME:
                    alt3 = 2
                elif LA3 == SYM:
                    alt3 = 3
                elif LA3 == HEX:
                    alt3 = 4
                elif LA3 == GEN:
                    alt3 = 5
                elif LA3 == BLOCK:
                    alt3 = 6
                else:
                    nvae = NoViableAltException("", 3, 0, self.input)

                    raise nvae

                if alt3 == 1:
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmDirectiveWalker.g:118:3: directive
                    pass 
                    root_0 = self._adaptor.nil()

                    _last = self.input.LT(1)
                    self._state.following.append(self.FOLLOW_directive_in_block_child104)
                    directive5 = self.directive()

                    self._state.following.pop()

                    self._adaptor.addChild(root_0, directive5.tree)




                elif alt3 == 2:
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmDirectiveWalker.g:119:4: dot_dot_directive
                    pass 
                    root_0 = self._adaptor.nil()

                    _last = self.input.LT(1)
                    self._state.following.append(self.FOLLOW_dot_dot_directive_in_block_child109)
                    dot_dot_directive6 = self.dot_dot_directive()

                    self._state.following.pop()

                    self._adaptor.addChild(root_0, dot_dot_directive6.tree)




                elif alt3 == 3:
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmDirectiveWalker.g:120:4: ^( SYM NAME )
                    pass 
                    root_0 = self._adaptor.nil()

                    _last = self.input.LT(1)
                    _save_last_1 = _last
                    _first_1 = None
                    root_1 = self._adaptor.nil()
                    _last = self.input.LT(1)
                    SYM7=self.match(self.input, SYM, self.FOLLOW_SYM_in_block_child115)

                    SYM7_tree = self._adaptor.dupNode(SYM7)

                    root_1 = self._adaptor.becomeRoot(SYM7_tree, root_1)



                    self.match(self.input, DOWN, None)
                    _last = self.input.LT(1)
                    NAME8=self.match(self.input, NAME, self.FOLLOW_NAME_in_block_child117)

                    NAME8_tree = self._adaptor.dupNode(NAME8)

                    self._adaptor.addChild(root_1, NAME8_tree)


                    self.match(self.input, UP, None)
                    self._adaptor.addChild(root_0, root_1)
                    _last = _save_last_1





                elif alt3 == 4:
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmDirectiveWalker.g:121:4: HEX
                    pass 
                    root_0 = self._adaptor.nil()

                    _last = self.input.LT(1)
                    HEX9=self.match(self.input, HEX, self.FOLLOW_HEX_in_block_child123)

                    HEX9_tree = self._adaptor.dupNode(HEX9)

                    self._adaptor.addChild(root_0, HEX9_tree)





                elif alt3 == 5:
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmDirectiveWalker.g:122:4: GEN
                    pass 
                    root_0 = self._adaptor.nil()

                    _last = self.input.LT(1)
                    GEN10=self.match(self.input, GEN, self.FOLLOW_GEN_in_block_child128)

                    GEN10_tree = self._adaptor.dupNode(GEN10)

                    self._adaptor.addChild(root_0, GEN10_tree)





                elif alt3 == 6:
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmDirectiveWalker.g:123:4: block
                    pass 
                    root_0 = self._adaptor.nil()

                    _last = self.input.LT(1)
                    self._state.following.append(self.FOLLOW_block_in_block_child133)
                    block11 = self.block()

                    self._state.following.pop()

                    self._adaptor.addChild(root_0, block11.tree)





                retval.tree = self._adaptor.rulePostProcessing(root_0)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return retval

    # $ANTLR end "block_child"

    class dot_dot_directive_return(TreeRuleReturnScope):
        def __init__(self):
            super(pycasmDirectiveWalker.dot_dot_directive_return, self).__init__()

            self.tree = None




    # $ANTLR start "dot_dot_directive"
    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmDirectiveWalker.g:126:1: dot_dot_directive : ^( DOT_DOT_NAME ( DOT_DOT_ARGS )? ( DOT_DOT_BODY )? ) ->;
    def dot_dot_directive(self, ):

        retval = self.dot_dot_directive_return()
        retval.start = self.input.LT(1)

        root_0 = None

        _first_0 = None
        _last = None

        DOT_DOT_NAME12 = None
        DOT_DOT_ARGS13 = None
        DOT_DOT_BODY14 = None

        DOT_DOT_NAME12_tree = None
        DOT_DOT_ARGS13_tree = None
        DOT_DOT_BODY14_tree = None
        stream_DOT_DOT_BODY = RewriteRuleNodeStream(self._adaptor, "token DOT_DOT_BODY")
        stream_DOT_DOT_NAME = RewriteRuleNodeStream(self._adaptor, "token DOT_DOT_NAME")
        stream_DOT_DOT_ARGS = RewriteRuleNodeStream(self._adaptor, "token DOT_DOT_ARGS")

        try:
            try:
                # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmDirectiveWalker.g:127:2: ( ^( DOT_DOT_NAME ( DOT_DOT_ARGS )? ( DOT_DOT_BODY )? ) ->)
                # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmDirectiveWalker.g:128:3: ^( DOT_DOT_NAME ( DOT_DOT_ARGS )? ( DOT_DOT_BODY )? )
                pass 
                _last = self.input.LT(1)
                _save_last_1 = _last
                _first_1 = None
                root_1 = self._adaptor.nil()
                _last = self.input.LT(1)
                DOT_DOT_NAME12=self.match(self.input, DOT_DOT_NAME, self.FOLLOW_DOT_DOT_NAME_in_dot_dot_directive148) 
                stream_DOT_DOT_NAME.add(DOT_DOT_NAME12)


                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmDirectiveWalker.g:128:18: ( DOT_DOT_ARGS )?
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == DOT_DOT_ARGS) :
                        alt4 = 1
                    if alt4 == 1:
                        # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmDirectiveWalker.g:128:18: DOT_DOT_ARGS
                        pass 
                        _last = self.input.LT(1)
                        DOT_DOT_ARGS13=self.match(self.input, DOT_DOT_ARGS, self.FOLLOW_DOT_DOT_ARGS_in_dot_dot_directive150) 
                        stream_DOT_DOT_ARGS.add(DOT_DOT_ARGS13)





                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmDirectiveWalker.g:128:32: ( DOT_DOT_BODY )?
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == DOT_DOT_BODY) :
                        alt5 = 1
                    if alt5 == 1:
                        # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmDirectiveWalker.g:128:32: DOT_DOT_BODY
                        pass 
                        _last = self.input.LT(1)
                        DOT_DOT_BODY14=self.match(self.input, DOT_DOT_BODY, self.FOLLOW_DOT_DOT_BODY_in_dot_dot_directive153) 
                        stream_DOT_DOT_BODY.add(DOT_DOT_BODY14)






                    self.match(self.input, UP, None)
                self._adaptor.addChild(root_0, root_1)
                _last = _save_last_1

                #action start
                   
                # look up scope
                name = DOT_DOT_NAME12.getText()[2:]
                if name:
                	d = rootScope.getDirective(name)
                	if d:
                		d.invoke(DOT_DOT_BODY14, DOT_DOT_ARGS13)
                	else:
                		raise SemanticException("Undefined unrestricted directive with name:"+name+'.')
                else:
                	raise SemanticException("Undefined unrestricted directive with empty name.")
                		
                #action end

                # AST Rewrite
                # elements: 
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 149:3: ->
                root_0 = None


                retval.tree = root_0




                retval.tree = self._adaptor.rulePostProcessing(root_0)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return retval

    # $ANTLR end "dot_dot_directive"

    class directive_return(TreeRuleReturnScope):
        def __init__(self):
            super(pycasmDirectiveWalker.directive_return, self).__init__()

            self.tree = None




    # $ANTLR start "directive"
    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmDirectiveWalker.g:152:1: directive : ^( DOT_NAME ^( ARGS ( DOT_ARGS )* ) ( block )? ) -> ^() ;
    def directive(self, ):

        retval = self.directive_return()
        retval.start = self.input.LT(1)

        root_0 = None

        _first_0 = None
        _last = None

        DOT_NAME15 = None
        ARGS16 = None
        DOT_ARGS17 = None
        block18 = None


        DOT_NAME15_tree = None
        ARGS16_tree = None
        DOT_ARGS17_tree = None
        stream_ARGS = RewriteRuleNodeStream(self._adaptor, "token ARGS")
        stream_DOT_NAME = RewriteRuleNodeStream(self._adaptor, "token DOT_NAME")
        stream_DOT_ARGS = RewriteRuleNodeStream(self._adaptor, "token DOT_ARGS")
        stream_block = RewriteRuleSubtreeStream(self._adaptor, "rule block")
               
        ifBlockMatched = False

        try:
            try:
                # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmDirectiveWalker.g:159:2: ( ^( DOT_NAME ^( ARGS ( DOT_ARGS )* ) ( block )? ) -> ^() )
                # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmDirectiveWalker.g:160:3: ^( DOT_NAME ^( ARGS ( DOT_ARGS )* ) ( block )? )
                pass 
                _last = self.input.LT(1)
                _save_last_1 = _last
                _first_1 = None
                root_1 = self._adaptor.nil()
                _last = self.input.LT(1)
                DOT_NAME15=self.match(self.input, DOT_NAME, self.FOLLOW_DOT_NAME_in_directive208) 
                stream_DOT_NAME.add(DOT_NAME15)


                self.match(self.input, DOWN, None)
                _last = self.input.LT(1)
                _save_last_2 = _last
                _first_2 = None
                root_2 = self._adaptor.nil()
                _last = self.input.LT(1)
                ARGS16=self.match(self.input, ARGS, self.FOLLOW_ARGS_in_directive211) 
                stream_ARGS.add(ARGS16)


                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmDirectiveWalker.g:160:21: ( DOT_ARGS )*
                    while True: #loop6
                        alt6 = 2
                        LA6_0 = self.input.LA(1)

                        if (LA6_0 == DOT_ARGS) :
                            alt6 = 1


                        if alt6 == 1:
                            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmDirectiveWalker.g:160:21: DOT_ARGS
                            pass 
                            _last = self.input.LT(1)
                            DOT_ARGS17=self.match(self.input, DOT_ARGS, self.FOLLOW_DOT_ARGS_in_directive213) 
                            stream_DOT_ARGS.add(DOT_ARGS17)




                        else:
                            break #loop6

                    self.match(self.input, UP, None)
                self._adaptor.addChild(root_1, root_2)
                _last = _save_last_2

                # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmDirectiveWalker.g:161:4: ( block )?
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == BLOCK) :
                    alt7 = 1
                if alt7 == 1:
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmDirectiveWalker.g:162:4: block
                    pass 
                    #action start
                        
                    self.scopeCountersStack.append(0)
                    #self.scopesStack.append( self.scopesStack[-1].getDirective(DOT_NAME15.getText()[1:]).getRestrictedScope() ) # what the heck
                    d = rootScope.getDirective(DOT_NAME15.getText()[1:])
                    if not d:
                    	raise SemanticException("No directive with name "+DOT_NAME15.getText()+" in rootScope.")
                    self.scopesStack.append( d.getRestrictedScope() )
                    			
                    #action end
                    _last = self.input.LT(1)
                    self._state.following.append(self.FOLLOW_block_in_directive230)
                    block18 = self.block()

                    self._state.following.pop()
                    stream_block.add(block18.tree)
                    #action start
                        
                    ifBlockMatched = True
                    			
                    #action end






                self.match(self.input, UP, None)
                self._adaptor.addChild(root_0, root_1)
                _last = _save_last_1


                # AST Rewrite
                # elements: 
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 176:3: -> ^()
                # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmDirectiveWalker.g:176:6: ^()
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self.expandDirective(self.scopeCountersStack[-1], DOT_NAME15.getText(), ARGS16 if ARGS16.children else None, block18.tree if ifBlockMatched else None), root_1)

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0




                retval.tree = self._adaptor.rulePostProcessing(root_0)

                #action start
                        
                self.scopeCountersStack[-1] += 1

                #action end

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return retval

    # $ANTLR end "directive"


    # Delegated rules


 

    FOLLOW_ROOT_in_root64 = frozenset([2])
    FOLLOW_block_in_root66 = frozenset([3])
    FOLLOW_BLOCK_in_block87 = frozenset([2])
    FOLLOW_block_child_in_block89 = frozenset([3, 6, 8, 12, 13, 34, 35])
    FOLLOW_directive_in_block_child104 = frozenset([1])
    FOLLOW_dot_dot_directive_in_block_child109 = frozenset([1])
    FOLLOW_SYM_in_block_child115 = frozenset([2])
    FOLLOW_NAME_in_block_child117 = frozenset([3])
    FOLLOW_HEX_in_block_child123 = frozenset([1])
    FOLLOW_GEN_in_block_child128 = frozenset([1])
    FOLLOW_block_in_block_child133 = frozenset([1])
    FOLLOW_DOT_DOT_NAME_in_dot_dot_directive148 = frozenset([2])
    FOLLOW_DOT_DOT_ARGS_in_dot_dot_directive150 = frozenset([3, 20])
    FOLLOW_DOT_DOT_BODY_in_dot_dot_directive153 = frozenset([3])
    FOLLOW_DOT_NAME_in_directive208 = frozenset([2])
    FOLLOW_ARGS_in_directive211 = frozenset([2])
    FOLLOW_DOT_ARGS_in_directive213 = frozenset([3, 17])
    FOLLOW_block_in_directive230 = frozenset([3])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(pycasmDirectiveWalker)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
