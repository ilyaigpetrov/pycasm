# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmSymnameWalker.g 2011-06-23 13:21:10

import sys
from antlr3 import *
from antlr3.tree import *
from antlr3.compat import set, frozenset

         
import opcode
from pycasm.semantics import SemanticException
import re



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




class pycasmSymnameWalker(TreeParser):
    grammarFileName = "/root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmSymnameWalker.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 18, 2009 10:09:25")
    antlr_version_str = "3.1.3 Mar 18, 2009 10:09:25"
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(pycasmSymnameWalker, self).__init__(input, state, *args, **kwargs)



               
        from pycasm.syntax.errors import StandardErrorReporter
        self.patchInErrorReporter(StandardErrorReporter())
        import opcode




        self._adaptor = None
        self.adaptor = CommonTreeAdaptor()
                


        
    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)

     

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



    class root_return(TreeRuleReturnScope):
        def __init__(self):
            super(pycasmSymnameWalker.root_return, self).__init__()

            self.tree = None




    # $ANTLR start "root"
    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmSymnameWalker.g:115:1: root : ^( ROOT ( block )? ) ;
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
                # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmSymnameWalker.g:116:2: ( ^( ROOT ( block )? ) )
                # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmSymnameWalker.g:117:3: ^( ROOT ( block )? )
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
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmSymnameWalker.g:117:10: ( block )?
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == BLOCK) :
                        alt1 = 1
                    if alt1 == 1:
                        # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmSymnameWalker.g:117:10: block
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
            super(pycasmSymnameWalker.block_return, self).__init__()

            self.tree = None




    # $ANTLR start "block"
    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmSymnameWalker.g:120:1: block : ^( BLOCK ( block_child )+ ) ;
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
                # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmSymnameWalker.g:121:2: ( ^( BLOCK ( block_child )+ ) )
                # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmSymnameWalker.g:122:3: ^( BLOCK ( block_child )+ )
                pass 
                root_0 = self._adaptor.nil()

                _last = self.input.LT(1)
                _save_last_1 = _last
                _first_1 = None
                root_1 = self._adaptor.nil()
                _last = self.input.LT(1)
                BLOCK3=self.match(self.input, BLOCK, self.FOLLOW_BLOCK_in_block82)

                BLOCK3_tree = self._adaptor.dupNode(BLOCK3)

                root_1 = self._adaptor.becomeRoot(BLOCK3_tree, root_1)



                self.match(self.input, DOWN, None)
                # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmSymnameWalker.g:122:11: ( block_child )+
                cnt2 = 0
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == BLOCK or LA2_0 == GEN or (HEX <= LA2_0 <= SYM)) :
                        alt2 = 1


                    if alt2 == 1:
                        # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmSymnameWalker.g:122:11: block_child
                        pass 
                        _last = self.input.LT(1)
                        self._state.following.append(self.FOLLOW_block_child_in_block84)
                        block_child4 = self.block_child()

                        self._state.following.pop()

                        self._adaptor.addChild(root_1, block_child4.tree)




                    else:
                        if cnt2 >= 1:
                            break #loop2

                        eee = EarlyExitException(2, self.input)
                        raise eee

                    cnt2 += 1

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

    # $ANTLR end "block"

    class block_child_return(TreeRuleReturnScope):
        def __init__(self):
            super(pycasmSymnameWalker.block_child_return, self).__init__()

            self.tree = None




    # $ANTLR start "block_child"
    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmSymnameWalker.g:125:1: block_child : ( ^( SYM NAME ) -> ^() | HEX | GEN -> ^() | block );
    def block_child(self, ):

        retval = self.block_child_return()
        retval.start = self.input.LT(1)

        root_0 = None

        _first_0 = None
        _last = None

        SYM5 = None
        NAME6 = None
        HEX7 = None
        GEN8 = None
        block9 = None


        SYM5_tree = None
        NAME6_tree = None
        HEX7_tree = None
        GEN8_tree = None
        stream_NAME = RewriteRuleNodeStream(self._adaptor, "token NAME")
        stream_GEN = RewriteRuleNodeStream(self._adaptor, "token GEN")
        stream_SYM = RewriteRuleNodeStream(self._adaptor, "token SYM")

        try:
            try:
                # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmSymnameWalker.g:126:2: ( ^( SYM NAME ) -> ^() | HEX | GEN -> ^() | block )
                alt3 = 4
                LA3 = self.input.LA(1)
                if LA3 == SYM:
                    alt3 = 1
                elif LA3 == HEX:
                    alt3 = 2
                elif LA3 == GEN:
                    alt3 = 3
                elif LA3 == BLOCK:
                    alt3 = 4
                else:
                    nvae = NoViableAltException("", 3, 0, self.input)

                    raise nvae

                if alt3 == 1:
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmSymnameWalker.g:127:3: ^( SYM NAME )
                    pass 
                    _last = self.input.LT(1)
                    _save_last_1 = _last
                    _first_1 = None
                    root_1 = self._adaptor.nil()
                    _last = self.input.LT(1)
                    SYM5=self.match(self.input, SYM, self.FOLLOW_SYM_in_block_child100) 
                    stream_SYM.add(SYM5)


                    self.match(self.input, DOWN, None)
                    _last = self.input.LT(1)
                    NAME6=self.match(self.input, NAME, self.FOLLOW_NAME_in_block_child102) 
                    stream_NAME.add(NAME6)

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
                    # 127:15: -> ^()
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmSymnameWalker.g:127:18: ^()
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self.expandSymname(NAME6.text), root_1)

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt3 == 2:
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmSymnameWalker.g:128:4: HEX
                    pass 
                    root_0 = self._adaptor.nil()

                    _last = self.input.LT(1)
                    HEX7=self.match(self.input, HEX, self.FOLLOW_HEX_in_block_child114)

                    HEX7_tree = self._adaptor.dupNode(HEX7)

                    self._adaptor.addChild(root_0, HEX7_tree)





                elif alt3 == 3:
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmSymnameWalker.g:129:4: GEN
                    pass 
                    _last = self.input.LT(1)
                    GEN8=self.match(self.input, GEN, self.FOLLOW_GEN_in_block_child119) 
                    stream_GEN.add(GEN8)

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
                    # 129:8: -> ^()
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmSymnameWalker.g:129:11: ^()
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self.expandGenerative(GEN8), root_1)

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt3 == 4:
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmSymnameWalker.g:130:4: block
                    pass 
                    root_0 = self._adaptor.nil()

                    _last = self.input.LT(1)
                    self._state.following.append(self.FOLLOW_block_in_block_child130)
                    block9 = self.block()

                    self._state.following.pop()

                    self._adaptor.addChild(root_0, block9.tree)





                retval.tree = self._adaptor.rulePostProcessing(root_0)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return retval

    # $ANTLR end "block_child"


    # Delegated rules


 

    FOLLOW_ROOT_in_root64 = frozenset([2])
    FOLLOW_block_in_root66 = frozenset([3])
    FOLLOW_BLOCK_in_block82 = frozenset([2])
    FOLLOW_block_child_in_block84 = frozenset([3, 6, 8, 34, 35])
    FOLLOW_SYM_in_block_child100 = frozenset([2])
    FOLLOW_NAME_in_block_child102 = frozenset([3])
    FOLLOW_HEX_in_block_child114 = frozenset([1])
    FOLLOW_GEN_in_block_child119 = frozenset([1])
    FOLLOW_block_in_block_child130 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(pycasmSymnameWalker)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
