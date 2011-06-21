# $ANTLR 3.1.3 Mar 17, 2009 19:23:44 G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmSymnameWalker.g 2011-06-22 00:39:55

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
DOT_DOT_BODY=42
DOT_DOT_NAME=28
INDENTDEDENT=30
DOT_DOT_ARGS=41
HexAlpha=27
DEDENT=4
EOF=-1
HexDigit=13
INDENT=5
SYM=49
NAME=20
NNN=29
HEX=48
PYTHON_CHAR=35
DIRECTIVE_ARGS=44
DOT_DOT_DIRECTIVE_ARGS=39
ARGS=7
GEN=8
INDENT_OR_DEDENT=34
COMMENT=23
UNRESTRICTED_DIRECTIVE=33
DOT_ARGS=45
HEX_QUAD=9
HEX_PAIR=11
PYTHON_BLOCK=31
DIRECTIVE_ARGUMENT=25
Any=32
Alpha=18
Type=15
AlphaNum=24
TYPED_VALUE=16
DOT_END=14
NONWS=38
HEX_DIGIT=12
P=37
HEX_DQUAD=10
Digit=26
ROOT=47
DOT_DOT_DIRECTIVE_BODY=40
WS=22
NonWS=43
NEWLINE=21
BLOCK=6
PCHAR=36
DOT_NAME=19
HEX_SEQUENCE=46
STRING=17

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "DEDENT", "INDENT", "BLOCK", "ARGS", "GEN", "HEX_QUAD", "HEX_DQUAD", 
    "HEX_PAIR", "HEX_DIGIT", "HexDigit", "DOT_END", "Type", "TYPED_VALUE", 
    "STRING", "Alpha", "DOT_NAME", "NAME", "NEWLINE", "WS", "COMMENT", "AlphaNum", 
    "DIRECTIVE_ARGUMENT", "Digit", "HexAlpha", "DOT_DOT_NAME", "NNN", "INDENTDEDENT", 
    "PYTHON_BLOCK", "Any", "UNRESTRICTED_DIRECTIVE", "INDENT_OR_DEDENT", 
    "PYTHON_CHAR", "PCHAR", "P", "NONWS", "DOT_DOT_DIRECTIVE_ARGS", "DOT_DOT_DIRECTIVE_BODY", 
    "DOT_DOT_ARGS", "DOT_DOT_BODY", "NonWS", "DIRECTIVE_ARGS", "DOT_ARGS", 
    "HEX_SEQUENCE", "ROOT", "HEX", "SYM"
]




class pycasmSymnameWalker(TreeParser):
    grammarFileName = "G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmSymnameWalker.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 17, 2009 19:23:44")
    antlr_version_str = "3.1.3 Mar 17, 2009 19:23:44"
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
    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmSymnameWalker.g:89:1: root : ^( ROOT ( block )? ) ;
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
                # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmSymnameWalker.g:90:2: ( ^( ROOT ( block )? ) )
                # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmSymnameWalker.g:91:3: ^( ROOT ( block )? )
                pass 
                root_0 = self._adaptor.nil()

                _last = self.input.LT(1)
                _save_last_1 = _last
                _first_1 = None
                root_1 = self._adaptor.nil()
                _last = self.input.LT(1)
                ROOT1=self.match(self.input, ROOT, self.FOLLOW_ROOT_in_root61)

                ROOT1_tree = self._adaptor.dupNode(ROOT1)

                root_1 = self._adaptor.becomeRoot(ROOT1_tree, root_1)



                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmSymnameWalker.g:91:10: ( block )?
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == BLOCK) :
                        alt1 = 1
                    if alt1 == 1:
                        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmSymnameWalker.g:91:10: block
                        pass 
                        _last = self.input.LT(1)
                        self._state.following.append(self.FOLLOW_block_in_root63)
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
    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmSymnameWalker.g:94:1: block : ^( BLOCK ( block_child )+ ) ;
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
                # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmSymnameWalker.g:95:2: ( ^( BLOCK ( block_child )+ ) )
                # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmSymnameWalker.g:96:3: ^( BLOCK ( block_child )+ )
                pass 
                root_0 = self._adaptor.nil()

                _last = self.input.LT(1)
                _save_last_1 = _last
                _first_1 = None
                root_1 = self._adaptor.nil()
                _last = self.input.LT(1)
                BLOCK3=self.match(self.input, BLOCK, self.FOLLOW_BLOCK_in_block79)

                BLOCK3_tree = self._adaptor.dupNode(BLOCK3)

                root_1 = self._adaptor.becomeRoot(BLOCK3_tree, root_1)



                self.match(self.input, DOWN, None)
                # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmSymnameWalker.g:96:11: ( block_child )+
                cnt2 = 0
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == BLOCK or LA2_0 == GEN or (HEX <= LA2_0 <= SYM)) :
                        alt2 = 1


                    if alt2 == 1:
                        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmSymnameWalker.g:96:11: block_child
                        pass 
                        _last = self.input.LT(1)
                        self._state.following.append(self.FOLLOW_block_child_in_block81)
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
    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmSymnameWalker.g:99:1: block_child : ( ^( SYM NAME ) -> ^() | HEX | GEN -> ^() | block );
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
                # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmSymnameWalker.g:100:2: ( ^( SYM NAME ) -> ^() | HEX | GEN -> ^() | block )
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
                    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmSymnameWalker.g:101:3: ^( SYM NAME )
                    pass 
                    _last = self.input.LT(1)
                    _save_last_1 = _last
                    _first_1 = None
                    root_1 = self._adaptor.nil()
                    _last = self.input.LT(1)
                    SYM5=self.match(self.input, SYM, self.FOLLOW_SYM_in_block_child97) 
                    stream_SYM.add(SYM5)


                    self.match(self.input, DOWN, None)
                    _last = self.input.LT(1)
                    NAME6=self.match(self.input, NAME, self.FOLLOW_NAME_in_block_child99) 
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
                    # 101:15: -> ^()
                    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmSymnameWalker.g:101:18: ^()
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self.expandSymname(NAME6.text), root_1)

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt3 == 2:
                    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmSymnameWalker.g:102:4: HEX
                    pass 
                    root_0 = self._adaptor.nil()

                    _last = self.input.LT(1)
                    HEX7=self.match(self.input, HEX, self.FOLLOW_HEX_in_block_child111)

                    HEX7_tree = self._adaptor.dupNode(HEX7)

                    self._adaptor.addChild(root_0, HEX7_tree)





                elif alt3 == 3:
                    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmSymnameWalker.g:103:4: GEN
                    pass 
                    _last = self.input.LT(1)
                    GEN8=self.match(self.input, GEN, self.FOLLOW_GEN_in_block_child116) 
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
                    # 103:8: -> ^()
                    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmSymnameWalker.g:103:11: ^()
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self.expandGenerative(GEN8), root_1)

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt3 == 4:
                    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmSymnameWalker.g:104:4: block
                    pass 
                    root_0 = self._adaptor.nil()

                    _last = self.input.LT(1)
                    self._state.following.append(self.FOLLOW_block_in_block_child127)
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


 

    FOLLOW_ROOT_in_root61 = frozenset([2])
    FOLLOW_block_in_root63 = frozenset([3])
    FOLLOW_BLOCK_in_block79 = frozenset([2])
    FOLLOW_block_child_in_block81 = frozenset([3, 6, 8, 48, 49])
    FOLLOW_SYM_in_block_child97 = frozenset([2])
    FOLLOW_NAME_in_block_child99 = frozenset([3])
    FOLLOW_HEX_in_block_child111 = frozenset([1])
    FOLLOW_GEN_in_block_child116 = frozenset([1])
    FOLLOW_block_in_block_child127 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(pycasmSymnameWalker)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
