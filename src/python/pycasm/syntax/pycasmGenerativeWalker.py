# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmGenerativeWalker.g 2011-06-23 13:21:11

import sys
from antlr3 import *
from antlr3.tree import *
from antlr3.compat import set, frozenset



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




class pycasmGenerativeWalker(TreeParser):
    grammarFileName = "/root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmGenerativeWalker.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 18, 2009 10:09:25")
    antlr_version_str = "3.1.3 Mar 18, 2009 10:09:25"
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(pycasmGenerativeWalker, self).__init__(input, state, *args, **kwargs)



               
        from pycasm.syntax.errors import StandardErrorReporter
        self.patchInErrorReporter(StandardErrorReporter())




        self._adaptor = None
        self.adaptor = CommonTreeAdaptor()
                


        
    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)

     
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



    class root_return(TreeRuleReturnScope):
        def __init__(self):
            super(pycasmGenerativeWalker.root_return, self).__init__()

            self.tree = None




    # $ANTLR start "root"
    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmGenerativeWalker.g:80:1: root : ^( ROOT ( block )? ) ;
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
                # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmGenerativeWalker.g:81:2: ( ^( ROOT ( block )? ) )
                # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmGenerativeWalker.g:82:3: ^( ROOT ( block )? )
                pass 
                _last = self.input.LT(1)
                _save_last_1 = _last
                _first_1 = None
                _last = self.input.LT(1)
                ROOT1=self.match(self.input, ROOT, self.FOLLOW_ROOT_in_root66)


                if self._state.backtracking == 0:

                    if _first_0 is None:
                        _first_0 = ROOT1

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmGenerativeWalker.g:82:10: ( block )?
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == BLOCK) :
                        alt1 = 1
                    if alt1 == 1:
                        # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmGenerativeWalker.g:0:0: block
                        pass 
                        _last = self.input.LT(1)
                        self._state.following.append(self.FOLLOW_block_in_root68)
                        block2 = self.block()

                        self._state.following.pop()
                        if self._state.backtracking == 0:

                             
                            if _first_1 is None:
                                _first_1 = block2.tree


                        if self._state.backtracking == 0:

                            retval.tree = _first_0
                            if self._adaptor.getParent(retval.tree) is not None and self._adaptor.isNil(self._adaptor.getParent(retval.tree)):
                                retval.tree = self._adaptor.getParent(retval.tree)



                    self.match(self.input, UP, None)
                _last = _save_last_1


                if self._state.backtracking == 0:

                    retval.tree = _first_0
                    if self._adaptor.getParent(retval.tree) is not None and self._adaptor.isNil(self._adaptor.getParent(retval.tree)):
                        retval.tree = self._adaptor.getParent(retval.tree)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return retval

    # $ANTLR end "root"

    class block_return(TreeRuleReturnScope):
        def __init__(self):
            super(pycasmGenerativeWalker.block_return, self).__init__()

            self.tree = None




    # $ANTLR start "block"
    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmGenerativeWalker.g:85:1: block : ^( BLOCK ( block_child )+ ) ;
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
                # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmGenerativeWalker.g:86:2: ( ^( BLOCK ( block_child )+ ) )
                # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmGenerativeWalker.g:87:3: ^( BLOCK ( block_child )+ )
                pass 
                _last = self.input.LT(1)
                _save_last_1 = _last
                _first_1 = None
                _last = self.input.LT(1)
                BLOCK3=self.match(self.input, BLOCK, self.FOLLOW_BLOCK_in_block84)


                if self._state.backtracking == 0:

                    if _first_0 is None:
                        _first_0 = BLOCK3

                self.match(self.input, DOWN, None)
                # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmGenerativeWalker.g:87:11: ( block_child )+
                cnt2 = 0
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == BLOCK or LA2_0 == GEN or LA2_0 == HEX) :
                        alt2 = 1


                    if alt2 == 1:
                        # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmGenerativeWalker.g:0:0: block_child
                        pass 
                        _last = self.input.LT(1)
                        self._state.following.append(self.FOLLOW_block_child_in_block86)
                        block_child4 = self.block_child()

                        self._state.following.pop()
                        if self._state.backtracking == 0:

                             
                            if _first_1 is None:
                                _first_1 = block_child4.tree


                        if self._state.backtracking == 0:

                            retval.tree = _first_0
                            if self._adaptor.getParent(retval.tree) is not None and self._adaptor.isNil(self._adaptor.getParent(retval.tree)):
                                retval.tree = self._adaptor.getParent(retval.tree)

                    else:
                        if cnt2 >= 1:
                            break #loop2

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(2, self.input)
                        raise eee

                    cnt2 += 1

                self.match(self.input, UP, None)
                _last = _save_last_1


                if self._state.backtracking == 0:

                    retval.tree = _first_0
                    if self._adaptor.getParent(retval.tree) is not None and self._adaptor.isNil(self._adaptor.getParent(retval.tree)):
                        retval.tree = self._adaptor.getParent(retval.tree)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return retval

    # $ANTLR end "block"

    class block_child_return(TreeRuleReturnScope):
        def __init__(self):
            super(pycasmGenerativeWalker.block_child_return, self).__init__()

            self.tree = None




    # $ANTLR start "block_child"
    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmGenerativeWalker.g:90:1: block_child : ( HEX | GEN -> ^() | block );
    def block_child(self, ):

        retval = self.block_child_return()
        retval.start = self.input.LT(1)

        root_0 = None

        _first_0 = None
        _last = None

        HEX5 = None
        GEN6 = None
        block7 = None


        HEX5_tree = None
        GEN6_tree = None
        stream_GEN = RewriteRuleNodeStream(self._adaptor, "token GEN")

        try:
            try:
                # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmGenerativeWalker.g:91:2: ( HEX | GEN -> ^() | block )
                alt3 = 3
                LA3 = self.input.LA(1)
                if LA3 == HEX:
                    alt3 = 1
                elif LA3 == GEN:
                    alt3 = 2
                elif LA3 == BLOCK:
                    alt3 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 3, 0, self.input)

                    raise nvae

                if alt3 == 1:
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmGenerativeWalker.g:92:3: HEX
                    pass 
                    _last = self.input.LT(1)
                    HEX5=self.match(self.input, HEX, self.FOLLOW_HEX_in_block_child101)
                     
                    if self._state.backtracking == 0:

                        if _first_0 is None:
                            _first_0 = HEX5



                    if self._state.backtracking == 0:

                        retval.tree = _first_0
                        if self._adaptor.getParent(retval.tree) is not None and self._adaptor.isNil(self._adaptor.getParent(retval.tree)):
                            retval.tree = self._adaptor.getParent(retval.tree)

                elif alt3 == 2:
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmGenerativeWalker.g:93:4: GEN
                    pass 
                    _last = self.input.LT(1)
                    GEN6=self.match(self.input, GEN, self.FOLLOW_GEN_in_block_child106) 
                    if self._state.backtracking == 0:
                        stream_GEN.add(GEN6)

                    # AST Rewrite
                    # elements: 
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 93:8: -> ^()
                        # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmGenerativeWalker.g:93:11: ^()
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self.expandGenerative(GEN6), root_1)

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = self._adaptor.rulePostProcessing(root_0)
                        self.input.replaceChildren(
                            self._adaptor.getParent(retval.start),
                            self._adaptor.getChildIndex(retval.start),
                            self._adaptor.getChildIndex(_last),
                            retval.tree
                            )



                elif alt3 == 3:
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmGenerativeWalker.g:94:4: block
                    pass 
                    _last = self.input.LT(1)
                    self._state.following.append(self.FOLLOW_block_in_block_child117)
                    block7 = self.block()

                    self._state.following.pop()
                    if self._state.backtracking == 0:

                         
                        if _first_0 is None:
                            _first_0 = block7.tree


                    if self._state.backtracking == 0:

                        retval.tree = _first_0
                        if self._adaptor.getParent(retval.tree) is not None and self._adaptor.isNil(self._adaptor.getParent(retval.tree)):
                            retval.tree = self._adaptor.getParent(retval.tree)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return retval

    # $ANTLR end "block_child"


    # Delegated rules


 

    FOLLOW_ROOT_in_root66 = frozenset([2])
    FOLLOW_block_in_root68 = frozenset([3])
    FOLLOW_BLOCK_in_block84 = frozenset([2])
    FOLLOW_block_child_in_block86 = frozenset([3, 6, 8, 34])
    FOLLOW_HEX_in_block_child101 = frozenset([1])
    FOLLOW_GEN_in_block_child106 = frozenset([1])
    FOLLOW_block_in_block_child117 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(pycasmGenerativeWalker)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
