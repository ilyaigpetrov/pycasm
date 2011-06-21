# $ANTLR 3.1.3 Mar 17, 2009 19:23:44 G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g 2011-06-22 00:39:53

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



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
SYM=49
INDENT=5
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
NEWLINE=21
NonWS=43
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




class pycasmParser(Parser):
    grammarFileName = "G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 17, 2009 19:23:44")
    antlr_version_str = "3.1.3 Mar 17, 2009 19:23:44"
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(pycasmParser, self).__init__(input, state, *args, **kwargs)

        self._state.ruleMemo = {}
        self.dfa4 = self.DFA4(
            self, 4,
            eot = self.DFA4_eot,
            eof = self.DFA4_eof,
            min = self.DFA4_min,
            max = self.DFA4_max,
            accept = self.DFA4_accept,
            special = self.DFA4_special,
            transition = self.DFA4_transition
            )

        self.dfa6 = self.DFA6(
            self, 6,
            eot = self.DFA6_eot,
            eof = self.DFA6_eof,
            min = self.DFA6_min,
            max = self.DFA6_max,
            accept = self.DFA6_accept,
            special = self.DFA6_special,
            transition = self.DFA6_transition
            )

        self.dfa7 = self.DFA7(
            self, 7,
            eot = self.DFA7_eot,
            eof = self.DFA7_eof,
            min = self.DFA7_min,
            max = self.DFA7_max,
            accept = self.DFA7_accept,
            special = self.DFA7_special,
            transition = self.DFA7_transition
            )



               
        from pycasm.syntax.errors import StandardErrorReporter
        self.patchInErrorReporter(StandardErrorReporter())




        self._adaptor = None
        self.adaptor = CommonTreeAdaptor()
                


        
    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)

              
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


    class root_return(ParserRuleReturnScope):
        def __init__(self):
            super(pycasmParser.root_return, self).__init__()

            self.tree = None




    # $ANTLR start "root"
    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:38:1: root : ( block | ( sp )+ )? EOF -> ^( ROOT ( block )? ) ;
    def root(self, ):

        retval = self.root_return()
        retval.start = self.input.LT(1)
        root_StartIndex = self.input.index()
        root_0 = None

        EOF3 = None
        block1 = None

        sp2 = None


        EOF3_tree = None
        stream_EOF = RewriteRuleTokenStream(self._adaptor, "token EOF")
        stream_sp = RewriteRuleSubtreeStream(self._adaptor, "rule sp")
        stream_block = RewriteRuleSubtreeStream(self._adaptor, "rule block")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 1):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:39:2: ( ( block | ( sp )+ )? EOF -> ^( ROOT ( block )? ) )
                # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:40:3: ( block | ( sp )+ )? EOF
                pass 
                # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:40:3: ( block | ( sp )+ )?
                alt2 = 3
                LA2 = self.input.LA(1)
                if LA2 == INDENT or LA2 == HEX_QUAD or LA2 == HEX_DQUAD or LA2 == HEX_PAIR or LA2 == TYPED_VALUE or LA2 == STRING or LA2 == DOT_NAME or LA2 == NAME or LA2 == DOT_DOT_NAME:
                    alt2 = 1
                elif LA2 == NEWLINE:
                    LA2_2 = self.input.LA(2)

                    if (self.synpred1_pycasmParser()) :
                        alt2 = 1
                    elif (self.synpred3_pycasmParser()) :
                        alt2 = 2
                elif LA2 == WS:
                    LA2_3 = self.input.LA(2)

                    if (self.synpred1_pycasmParser()) :
                        alt2 = 1
                    elif (self.synpred3_pycasmParser()) :
                        alt2 = 2
                if alt2 == 1:
                    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:40:4: block
                    pass 
                    self._state.following.append(self.FOLLOW_block_in_root72)
                    block1 = self.block()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_block.add(block1.tree)


                elif alt2 == 2:
                    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:40:11: ( sp )+
                    pass 
                    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:40:11: ( sp )+
                    cnt1 = 0
                    while True: #loop1
                        alt1 = 2
                        LA1_0 = self.input.LA(1)

                        if ((NEWLINE <= LA1_0 <= WS)) :
                            alt1 = 1


                        if alt1 == 1:
                            # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:0:0: sp
                            pass 
                            self._state.following.append(self.FOLLOW_sp_in_root75)
                            sp2 = self.sp()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_sp.add(sp2.tree)


                        else:
                            if cnt1 >= 1:
                                break #loop1

                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            eee = EarlyExitException(1, self.input)
                            raise eee

                        cnt1 += 1



                EOF3=self.match(self.input, EOF, self.FOLLOW_EOF_in_root80) 
                if self._state.backtracking == 0:
                    stream_EOF.add(EOF3)

                # AST Rewrite
                # elements: block
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
                    # 41:3: -> ^( ROOT ( block )? )
                    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:41:6: ^( ROOT ( block )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ROOT, "ROOT"), root_1)

                    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:41:13: ( block )?
                    if stream_block.hasNext():
                        self._adaptor.addChild(root_1, stream_block.nextTree())


                    stream_block.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 1, root_StartIndex, success)

            pass
        return retval

    # $ANTLR end "root"

    class sp_return(ParserRuleReturnScope):
        def __init__(self):
            super(pycasmParser.sp_return, self).__init__()

            self.tree = None




    # $ANTLR start "sp"
    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:44:1: sp : ( WS | NEWLINE )+ ->;
    def sp(self, ):

        retval = self.sp_return()
        retval.start = self.input.LT(1)
        sp_StartIndex = self.input.index()
        root_0 = None

        WS4 = None
        NEWLINE5 = None

        WS4_tree = None
        NEWLINE5_tree = None
        stream_WS = RewriteRuleTokenStream(self._adaptor, "token WS")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 2):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:44:4: ( ( WS | NEWLINE )+ ->)
                # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:45:3: ( WS | NEWLINE )+
                pass 
                # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:45:3: ( WS | NEWLINE )+
                cnt3 = 0
                while True: #loop3
                    alt3 = 3
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == WS) :
                        LA3_2 = self.input.LA(2)

                        if (self.synpred4_pycasmParser()) :
                            alt3 = 1


                    elif (LA3_0 == NEWLINE) :
                        LA3_3 = self.input.LA(2)

                        if (self.synpred5_pycasmParser()) :
                            alt3 = 2




                    if alt3 == 1:
                        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:45:4: WS
                        pass 
                        WS4=self.match(self.input, WS, self.FOLLOW_WS_in_sp104) 
                        if self._state.backtracking == 0:
                            stream_WS.add(WS4)


                    elif alt3 == 2:
                        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:45:7: NEWLINE
                        pass 
                        NEWLINE5=self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_sp106) 
                        if self._state.backtracking == 0:
                            stream_NEWLINE.add(NEWLINE5)


                    else:
                        if cnt3 >= 1:
                            break #loop3

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(3, self.input)
                        raise eee

                    cnt3 += 1

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
                    # 45:17: ->
                    root_0 = None


                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 2, sp_StartIndex, success)

            pass
        return retval

    # $ANTLR end "sp"

    class block_return(ParserRuleReturnScope):
        def __init__(self):
            super(pycasmParser.block_return, self).__init__()

            self.tree = None




    # $ANTLR start "block"
    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:48:1: block : h= block_head ( block_chain )* -> { not isinstance($h.tree, type(None)) }? ^( BLOCK block_head ( block_chain )* ) ->;
    def block(self, ):

        retval = self.block_return()
        retval.start = self.input.LT(1)
        block_StartIndex = self.input.index()
        root_0 = None

        h = None

        block_chain6 = None


        stream_block_chain = RewriteRuleSubtreeStream(self._adaptor, "rule block_chain")
        stream_block_head = RewriteRuleSubtreeStream(self._adaptor, "rule block_head")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 3):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:49:2: (h= block_head ( block_chain )* -> { not isinstance($h.tree, type(None)) }? ^( BLOCK block_head ( block_chain )* ) ->)
                # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:50:3: h= block_head ( block_chain )*
                pass 
                self._state.following.append(self.FOLLOW_block_head_in_block125)
                h = self.block_head()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_block_head.add(h.tree)
                # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:51:3: ( block_chain )*
                while True: #loop4
                    alt4 = 2
                    alt4 = self.dfa4.predict(self.input)
                    if alt4 == 1:
                        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:0:0: block_chain
                        pass 
                        self._state.following.append(self.FOLLOW_block_chain_in_block129)
                        block_chain6 = self.block_chain()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_block_chain.add(block_chain6.tree)


                    else:
                        break #loop4

                # AST Rewrite
                # elements: block_head, block_chain
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
                    if not isinstance(h.tree, type(None)) :
                        # 52:3: -> { not isinstance($h.tree, type(None)) }? ^( BLOCK block_head ( block_chain )* )
                        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:52:47: ^( BLOCK block_head ( block_chain )* )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(BLOCK, "BLOCK"), root_1)

                        self._adaptor.addChild(root_1, stream_block_head.nextTree())
                        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:52:66: ( block_chain )*
                        while stream_block_chain.hasNext():
                            self._adaptor.addChild(root_1, stream_block_chain.nextTree())


                        stream_block_chain.reset();

                        self._adaptor.addChild(root_0, root_1)


                    else: 
                        # 53:3: ->
                        root_0 = None

                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 3, block_StartIndex, success)

            pass
        return retval

    # $ANTLR end "block"

    class block_head_return(ParserRuleReturnScope):
        def __init__(self):
            super(pycasmParser.block_head_return, self).__init__()

            self.tree = None




    # $ANTLR start "block_head"
    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:56:1: block_head : ( chain_element | block_chain );
    def block_head(self, ):

        retval = self.block_head_return()
        retval.start = self.input.LT(1)
        block_head_StartIndex = self.input.index()
        root_0 = None

        chain_element7 = None

        block_chain8 = None



        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 4):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:57:2: ( chain_element | block_chain )
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if ((HEX_QUAD <= LA5_0 <= HEX_PAIR) or (TYPED_VALUE <= LA5_0 <= STRING) or LA5_0 == NAME) :
                    alt5 = 1
                elif (LA5_0 == DOT_NAME) and ((self.input.LT(1).getCharPositionInLine() == 0 or self.input.LT(-1) and self.input.LT(-1).getType() in [INDENT, DEDENT, NEWLINE] )):
                    alt5 = 2
                elif (LA5_0 == INDENT or (NEWLINE <= LA5_0 <= WS) or LA5_0 == DOT_DOT_NAME) :
                    alt5 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 5, 0, self.input)

                    raise nvae

                if alt5 == 1:
                    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:58:3: chain_element
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_chain_element_in_block_head162)
                    chain_element7 = self.chain_element()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, chain_element7.tree)


                elif alt5 == 2:
                    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:59:4: block_chain
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_block_chain_in_block_head167)
                    block_chain8 = self.block_chain()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, block_chain8.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 4, block_head_StartIndex, success)

            pass
        return retval

    # $ANTLR end "block_head"

    class block_chain_return(ParserRuleReturnScope):
        def __init__(self):
            super(pycasmParser.block_chain_return, self).__init__()

            self.tree = None




    # $ANTLR start "block_chain"
    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:62:1: block_chain : ( space_element )+ ( chain_element )? ;
    def block_chain(self, ):

        retval = self.block_chain_return()
        retval.start = self.input.LT(1)
        block_chain_StartIndex = self.input.index()
        root_0 = None

        space_element9 = None

        chain_element10 = None



        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 5):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:63:2: ( ( space_element )+ ( chain_element )? )
                # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:64:3: ( space_element )+ ( chain_element )?
                pass 
                root_0 = self._adaptor.nil()

                # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:64:3: ( space_element )+
                cnt6 = 0
                while True: #loop6
                    alt6 = 2
                    alt6 = self.dfa6.predict(self.input)
                    if alt6 == 1:
                        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:0:0: space_element
                        pass 
                        self._state.following.append(self.FOLLOW_space_element_in_block_chain180)
                        space_element9 = self.space_element()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, space_element9.tree)


                    else:
                        if cnt6 >= 1:
                            break #loop6

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(6, self.input)
                        raise eee

                    cnt6 += 1
                # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:64:18: ( chain_element )?
                alt7 = 2
                alt7 = self.dfa7.predict(self.input)
                if alt7 == 1:
                    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:0:0: chain_element
                    pass 
                    self._state.following.append(self.FOLLOW_chain_element_in_block_chain183)
                    chain_element10 = self.chain_element()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, chain_element10.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 5, block_chain_StartIndex, success)

            pass
        return retval

    # $ANTLR end "block_chain"

    class chain_element_return(ParserRuleReturnScope):
        def __init__(self):
            super(pycasmParser.chain_element_return, self).__init__()

            self.tree = None




    # $ANTLR start "chain_element"
    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:67:1: chain_element : ( sym_name | generative | hex_code );
    def chain_element(self, ):

        retval = self.chain_element_return()
        retval.start = self.input.LT(1)
        chain_element_StartIndex = self.input.index()
        root_0 = None

        sym_name11 = None

        generative12 = None

        hex_code13 = None



        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 6):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:68:2: ( sym_name | generative | hex_code )
                alt8 = 3
                LA8 = self.input.LA(1)
                if LA8 == NAME:
                    alt8 = 1
                elif LA8 == TYPED_VALUE or LA8 == STRING:
                    alt8 = 2
                elif LA8 == HEX_QUAD or LA8 == HEX_DQUAD or LA8 == HEX_PAIR:
                    alt8 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 8, 0, self.input)

                    raise nvae

                if alt8 == 1:
                    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:68:4: sym_name
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_sym_name_in_chain_element195)
                    sym_name11 = self.sym_name()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, sym_name11.tree)


                elif alt8 == 2:
                    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:69:4: generative
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_generative_in_chain_element200)
                    generative12 = self.generative()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, generative12.tree)


                elif alt8 == 3:
                    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:70:4: hex_code
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_hex_code_in_chain_element205)
                    hex_code13 = self.hex_code()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, hex_code13.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 6, chain_element_StartIndex, success)

            pass
        return retval

    # $ANTLR end "chain_element"

    class space_element_return(ParserRuleReturnScope):
        def __init__(self):
            super(pycasmParser.space_element_return, self).__init__()

            self.tree = None




    # $ANTLR start "space_element"
    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:73:1: space_element : ( directive | unrestricted_directive | ( NEWLINE )? INDENT block ( NEWLINE )? ( DEDENT )? | sp );
    def space_element(self, ):

        retval = self.space_element_return()
        retval.start = self.input.LT(1)
        space_element_StartIndex = self.input.index()
        root_0 = None

        NEWLINE16 = None
        INDENT17 = None
        NEWLINE19 = None
        DEDENT20 = None
        directive14 = None

        unrestricted_directive15 = None

        block18 = None

        sp21 = None


        NEWLINE16_tree = None
        INDENT17_tree = None
        NEWLINE19_tree = None
        DEDENT20_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 7):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:74:2: ( directive | unrestricted_directive | ( NEWLINE )? INDENT block ( NEWLINE )? ( DEDENT )? | sp )
                alt12 = 4
                LA12_0 = self.input.LA(1)

                if (LA12_0 == DOT_NAME) and ((self.input.LT(1).getCharPositionInLine() == 0 or self.input.LT(-1) and self.input.LT(-1).getType() in [INDENT, DEDENT, NEWLINE] )):
                    alt12 = 1
                elif (LA12_0 == DOT_DOT_NAME) :
                    alt12 = 2
                elif (LA12_0 == NEWLINE) :
                    LA12_3 = self.input.LA(2)

                    if (self.synpred17_pycasmParser()) :
                        alt12 = 3
                    elif (True) :
                        alt12 = 4
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 12, 3, self.input)

                        raise nvae

                elif (LA12_0 == INDENT) :
                    alt12 = 3
                elif (LA12_0 == WS) :
                    alt12 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 12, 0, self.input)

                    raise nvae

                if alt12 == 1:
                    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:75:3: directive
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_directive_in_space_element218)
                    directive14 = self.directive()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, directive14.tree)


                elif alt12 == 2:
                    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:76:4: unrestricted_directive
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_unrestricted_directive_in_space_element223)
                    unrestricted_directive15 = self.unrestricted_directive()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, unrestricted_directive15.tree)


                elif alt12 == 3:
                    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:77:4: ( NEWLINE )? INDENT block ( NEWLINE )? ( DEDENT )?
                    pass 
                    root_0 = self._adaptor.nil()

                    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:77:4: ( NEWLINE )?
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == NEWLINE) :
                        alt9 = 1
                    if alt9 == 1:
                        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:0:0: NEWLINE
                        pass 
                        NEWLINE16=self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_space_element228)
                        if self._state.backtracking == 0:

                            NEWLINE16_tree = self._adaptor.createWithPayload(NEWLINE16)
                            self._adaptor.addChild(root_0, NEWLINE16_tree)




                    INDENT17=self.match(self.input, INDENT, self.FOLLOW_INDENT_in_space_element231)
                    self._state.following.append(self.FOLLOW_block_in_space_element234)
                    block18 = self.block()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, block18.tree)
                    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:77:27: ( NEWLINE )?
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == NEWLINE) :
                        LA10_1 = self.input.LA(2)

                        if (self.synpred15_pycasmParser()) :
                            alt10 = 1
                    if alt10 == 1:
                        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:0:0: NEWLINE
                        pass 
                        NEWLINE19=self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_space_element236)
                        if self._state.backtracking == 0:

                            NEWLINE19_tree = self._adaptor.createWithPayload(NEWLINE19)
                            self._adaptor.addChild(root_0, NEWLINE19_tree)




                    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:77:42: ( DEDENT )?
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == DEDENT) :
                        LA11_1 = self.input.LA(2)

                        if (self.synpred16_pycasmParser()) :
                            alt11 = 1
                    if alt11 == 1:
                        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:0:0: DEDENT
                        pass 
                        DEDENT20=self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_space_element239)





                elif alt12 == 4:
                    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:78:4: sp
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_sp_in_space_element246)
                    sp21 = self.sp()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, sp21.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 7, space_element_StartIndex, success)

            pass
        return retval

    # $ANTLR end "space_element"

    class unrestricted_directive_return(ParserRuleReturnScope):
        def __init__(self):
            super(pycasmParser.unrestricted_directive_return, self).__init__()

            self.tree = None




    # $ANTLR start "unrestricted_directive"
    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:81:1: unrestricted_directive : DOT_DOT_NAME ( DOT_DOT_ARGS )? ( DOT_DOT_BODY )? -> ^( DOT_DOT_NAME ( DOT_DOT_ARGS )? ( DOT_DOT_BODY )? ) ;
    def unrestricted_directive(self, ):

        retval = self.unrestricted_directive_return()
        retval.start = self.input.LT(1)
        unrestricted_directive_StartIndex = self.input.index()
        root_0 = None

        DOT_DOT_NAME22 = None
        DOT_DOT_ARGS23 = None
        DOT_DOT_BODY24 = None

        DOT_DOT_NAME22_tree = None
        DOT_DOT_ARGS23_tree = None
        DOT_DOT_BODY24_tree = None
        stream_DOT_DOT_BODY = RewriteRuleTokenStream(self._adaptor, "token DOT_DOT_BODY")
        stream_DOT_DOT_NAME = RewriteRuleTokenStream(self._adaptor, "token DOT_DOT_NAME")
        stream_DOT_DOT_ARGS = RewriteRuleTokenStream(self._adaptor, "token DOT_DOT_ARGS")

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 8):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:82:2: ( DOT_DOT_NAME ( DOT_DOT_ARGS )? ( DOT_DOT_BODY )? -> ^( DOT_DOT_NAME ( DOT_DOT_ARGS )? ( DOT_DOT_BODY )? ) )
                # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:83:3: DOT_DOT_NAME ( DOT_DOT_ARGS )? ( DOT_DOT_BODY )?
                pass 
                DOT_DOT_NAME22=self.match(self.input, DOT_DOT_NAME, self.FOLLOW_DOT_DOT_NAME_in_unrestricted_directive259) 
                if self._state.backtracking == 0:
                    stream_DOT_DOT_NAME.add(DOT_DOT_NAME22)
                # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:83:16: ( DOT_DOT_ARGS )?
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if (LA13_0 == DOT_DOT_ARGS) :
                    alt13 = 1
                if alt13 == 1:
                    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:0:0: DOT_DOT_ARGS
                    pass 
                    DOT_DOT_ARGS23=self.match(self.input, DOT_DOT_ARGS, self.FOLLOW_DOT_DOT_ARGS_in_unrestricted_directive261) 
                    if self._state.backtracking == 0:
                        stream_DOT_DOT_ARGS.add(DOT_DOT_ARGS23)



                # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:83:30: ( DOT_DOT_BODY )?
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if (LA14_0 == DOT_DOT_BODY) :
                    alt14 = 1
                if alt14 == 1:
                    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:0:0: DOT_DOT_BODY
                    pass 
                    DOT_DOT_BODY24=self.match(self.input, DOT_DOT_BODY, self.FOLLOW_DOT_DOT_BODY_in_unrestricted_directive264) 
                    if self._state.backtracking == 0:
                        stream_DOT_DOT_BODY.add(DOT_DOT_BODY24)




                # AST Rewrite
                # elements: DOT_DOT_NAME, DOT_DOT_ARGS, DOT_DOT_BODY
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
                    # 83:44: -> ^( DOT_DOT_NAME ( DOT_DOT_ARGS )? ( DOT_DOT_BODY )? )
                    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:83:47: ^( DOT_DOT_NAME ( DOT_DOT_ARGS )? ( DOT_DOT_BODY )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_DOT_DOT_NAME.nextNode(), root_1)

                    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:83:62: ( DOT_DOT_ARGS )?
                    if stream_DOT_DOT_ARGS.hasNext():
                        self._adaptor.addChild(root_1, stream_DOT_DOT_ARGS.nextNode())


                    stream_DOT_DOT_ARGS.reset();
                    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:83:76: ( DOT_DOT_BODY )?
                    if stream_DOT_DOT_BODY.hasNext():
                        self._adaptor.addChild(root_1, stream_DOT_DOT_BODY.nextNode())


                    stream_DOT_DOT_BODY.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 8, unrestricted_directive_StartIndex, success)

            pass
        return retval

    # $ANTLR end "unrestricted_directive"

    class directive_return(ParserRuleReturnScope):
        def __init__(self):
            super(pycasmParser.directive_return, self).__init__()

            self.tree = None




    # $ANTLR start "directive"
    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:86:1: directive : {...}? => ( directive_header ( NEWLINE INDENT block ( NEWLINE )? ( DEDENT )? ( DOT_END ( WS )+ ( NAME ) )? | NEWLINE )? ) -> ^( ( block )? ) ;
    def directive(self, ):

        retval = self.directive_return()
        retval.start = self.input.LT(1)
        directive_StartIndex = self.input.index()
        root_0 = None

        NEWLINE26 = None
        INDENT27 = None
        NEWLINE29 = None
        DEDENT30 = None
        DOT_END31 = None
        WS32 = None
        NAME33 = None
        NEWLINE34 = None
        directive_header25 = None

        block28 = None


        NEWLINE26_tree = None
        INDENT27_tree = None
        NEWLINE29_tree = None
        DEDENT30_tree = None
        DOT_END31_tree = None
        WS32_tree = None
        NAME33_tree = None
        NEWLINE34_tree = None
        stream_NAME = RewriteRuleTokenStream(self._adaptor, "token NAME")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_WS = RewriteRuleTokenStream(self._adaptor, "token WS")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_DOT_END = RewriteRuleTokenStream(self._adaptor, "token DOT_END")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_directive_header = RewriteRuleSubtreeStream(self._adaptor, "rule directive_header")
        stream_block = RewriteRuleSubtreeStream(self._adaptor, "rule block")
        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 9):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:87:2: ({...}? => ( directive_header ( NEWLINE INDENT block ( NEWLINE )? ( DEDENT )? ( DOT_END ( WS )+ ( NAME ) )? | NEWLINE )? ) -> ^( ( block )? ) )
                # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:88:3: {...}? => ( directive_header ( NEWLINE INDENT block ( NEWLINE )? ( DEDENT )? ( DOT_END ( WS )+ ( NAME ) )? | NEWLINE )? )
                pass 
                if not ((self.input.LT(1).getCharPositionInLine() == 0 or self.input.LT(-1) and self.input.LT(-1).getType() in [INDENT, DEDENT, NEWLINE] )):
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    raise FailedPredicateException(self.input, "directive", " self.input.LT(1).getCharPositionInLine() == 0 or self.input.LT(-1) and self.input.LT(-1).getType() in [INDENT, DEDENT, NEWLINE] ")

                # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:89:6: ( directive_header ( NEWLINE INDENT block ( NEWLINE )? ( DEDENT )? ( DOT_END ( WS )+ ( NAME ) )? | NEWLINE )? )
                # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:90:3: directive_header ( NEWLINE INDENT block ( NEWLINE )? ( DEDENT )? ( DOT_END ( WS )+ ( NAME ) )? | NEWLINE )?
                pass 
                self._state.following.append(self.FOLLOW_directive_header_in_directive300)
                directive_header25 = self.directive_header()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_directive_header.add(directive_header25.tree)
                # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:91:4: ( NEWLINE INDENT block ( NEWLINE )? ( DEDENT )? ( DOT_END ( WS )+ ( NAME ) )? | NEWLINE )?
                alt19 = 3
                LA19_0 = self.input.LA(1)

                if (LA19_0 == NEWLINE) :
                    LA19_1 = self.input.LA(2)

                    if (LA19_1 == INDENT) :
                        alt19 = 1
                    elif (self.synpred25_pycasmParser()) :
                        alt19 = 2
                if alt19 == 1:
                    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:91:5: NEWLINE INDENT block ( NEWLINE )? ( DEDENT )? ( DOT_END ( WS )+ ( NAME ) )?
                    pass 
                    NEWLINE26=self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_directive306) 
                    if self._state.backtracking == 0:
                        stream_NEWLINE.add(NEWLINE26)
                    INDENT27=self.match(self.input, INDENT, self.FOLLOW_INDENT_in_directive308) 
                    if self._state.backtracking == 0:
                        stream_INDENT.add(INDENT27)
                    self._state.following.append(self.FOLLOW_block_in_directive310)
                    block28 = self.block()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_block.add(block28.tree)
                    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:91:26: ( NEWLINE )?
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if (LA15_0 == NEWLINE) :
                        LA15_1 = self.input.LA(2)

                        if (self.synpred20_pycasmParser()) :
                            alt15 = 1
                    if alt15 == 1:
                        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:0:0: NEWLINE
                        pass 
                        NEWLINE29=self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_directive312) 
                        if self._state.backtracking == 0:
                            stream_NEWLINE.add(NEWLINE29)



                    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:91:35: ( DEDENT )?
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (LA16_0 == DEDENT) :
                        LA16_1 = self.input.LA(2)

                        if (self.synpred21_pycasmParser()) :
                            alt16 = 1
                    if alt16 == 1:
                        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:0:0: DEDENT
                        pass 
                        DEDENT30=self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_directive315) 
                        if self._state.backtracking == 0:
                            stream_DEDENT.add(DEDENT30)



                    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:92:5: ( DOT_END ( WS )+ ( NAME ) )?
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if (LA18_0 == DOT_END) :
                        LA18_1 = self.input.LA(2)

                        if (self.synpred23_pycasmParser()) :
                            alt18 = 1
                    if alt18 == 1:
                        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:92:6: DOT_END ( WS )+ ( NAME )
                        pass 
                        DOT_END31=self.match(self.input, DOT_END, self.FOLLOW_DOT_END_in_directive323) 
                        if self._state.backtracking == 0:
                            stream_DOT_END.add(DOT_END31)
                        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:92:14: ( WS )+
                        cnt17 = 0
                        while True: #loop17
                            alt17 = 2
                            LA17_0 = self.input.LA(1)

                            if (LA17_0 == WS) :
                                alt17 = 1


                            if alt17 == 1:
                                # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:0:0: WS
                                pass 
                                WS32=self.match(self.input, WS, self.FOLLOW_WS_in_directive325) 
                                if self._state.backtracking == 0:
                                    stream_WS.add(WS32)


                            else:
                                if cnt17 >= 1:
                                    break #loop17

                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed

                                eee = EarlyExitException(17, self.input)
                                raise eee

                            cnt17 += 1
                        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:93:6: ( NAME )
                        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:93:7: NAME
                        pass 
                        NAME33=self.match(self.input, NAME, self.FOLLOW_NAME_in_directive334) 
                        if self._state.backtracking == 0:
                            stream_NAME.add(NAME33)
                        if self._state.backtracking == 0:
                                   
                            dh = directive_header25.tree.toString()[1:]
                            if not dh.startswith(NAME33.text):
                            	self.reportError(".end directive must have argument of the same name as directive '"+dh+"', compare with '"+NAME33.text+"'.") # dirty
                            						









                elif alt19 == 2:
                    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:101:6: NEWLINE
                    pass 
                    NEWLINE34=self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_directive363) 
                    if self._state.backtracking == 0:
                        stream_NEWLINE.add(NEWLINE34)







                # AST Rewrite
                # elements: block
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
                    # 103:6: -> ^( ( block )? )
                    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:103:9: ^( ( block )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(directive_header25.tree, root_1)

                    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:103:36: ( block )?
                    if stream_block.hasNext():
                        self._adaptor.addChild(root_1, stream_block.nextTree())


                    stream_block.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 9, directive_StartIndex, success)

            pass
        return retval

    # $ANTLR end "directive"

    class directive_header_return(ParserRuleReturnScope):
        def __init__(self):
            super(pycasmParser.directive_header_return, self).__init__()

            self.tree = None




    # $ANTLR start "directive_header"
    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:106:1: directive_header : DOT_NAME ( DOT_ARGS )? -> ^( DOT_NAME ^( ARGS ( DOT_ARGS )? ) ) ;
    def directive_header(self, ):

        retval = self.directive_header_return()
        retval.start = self.input.LT(1)
        directive_header_StartIndex = self.input.index()
        root_0 = None

        DOT_NAME35 = None
        DOT_ARGS36 = None

        DOT_NAME35_tree = None
        DOT_ARGS36_tree = None
        stream_DOT_NAME = RewriteRuleTokenStream(self._adaptor, "token DOT_NAME")
        stream_DOT_ARGS = RewriteRuleTokenStream(self._adaptor, "token DOT_ARGS")

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 10):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:107:2: ( DOT_NAME ( DOT_ARGS )? -> ^( DOT_NAME ^( ARGS ( DOT_ARGS )? ) ) )
                # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:108:3: DOT_NAME ( DOT_ARGS )?
                pass 
                DOT_NAME35=self.match(self.input, DOT_NAME, self.FOLLOW_DOT_NAME_in_directive_header397) 
                if self._state.backtracking == 0:
                    stream_DOT_NAME.add(DOT_NAME35)
                # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:108:12: ( DOT_ARGS )?
                alt20 = 2
                LA20_0 = self.input.LA(1)

                if (LA20_0 == DOT_ARGS) :
                    alt20 = 1
                if alt20 == 1:
                    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:0:0: DOT_ARGS
                    pass 
                    DOT_ARGS36=self.match(self.input, DOT_ARGS, self.FOLLOW_DOT_ARGS_in_directive_header399) 
                    if self._state.backtracking == 0:
                        stream_DOT_ARGS.add(DOT_ARGS36)




                # AST Rewrite
                # elements: DOT_ARGS, DOT_NAME
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
                    # 108:22: -> ^( DOT_NAME ^( ARGS ( DOT_ARGS )? ) )
                    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:108:25: ^( DOT_NAME ^( ARGS ( DOT_ARGS )? ) )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_DOT_NAME.nextNode(), root_1)

                    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:108:36: ^( ARGS ( DOT_ARGS )? )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(ARGS, "ARGS"), root_2)

                    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:108:43: ( DOT_ARGS )?
                    if stream_DOT_ARGS.hasNext():
                        self._adaptor.addChild(root_2, stream_DOT_ARGS.nextNode())


                    stream_DOT_ARGS.reset();

                    self._adaptor.addChild(root_1, root_2)

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 10, directive_header_StartIndex, success)

            pass
        return retval

    # $ANTLR end "directive_header"

    class sym_name_return(ParserRuleReturnScope):
        def __init__(self):
            super(pycasmParser.sym_name_return, self).__init__()

            self.tree = None




    # $ANTLR start "sym_name"
    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:111:1: sym_name : NAME -> ^( SYM NAME ) ;
    def sym_name(self, ):

        retval = self.sym_name_return()
        retval.start = self.input.LT(1)
        sym_name_StartIndex = self.input.index()
        root_0 = None

        NAME37 = None

        NAME37_tree = None
        stream_NAME = RewriteRuleTokenStream(self._adaptor, "token NAME")

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 11):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:112:2: ( NAME -> ^( SYM NAME ) )
                # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:113:3: NAME
                pass 
                NAME37=self.match(self.input, NAME, self.FOLLOW_NAME_in_sym_name426) 
                if self._state.backtracking == 0:
                    stream_NAME.add(NAME37)

                # AST Rewrite
                # elements: NAME
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
                    # 113:8: -> ^( SYM NAME )
                    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:113:11: ^( SYM NAME )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(SYM, "SYM"), root_1)

                    self._adaptor.addChild(root_1, stream_NAME.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 11, sym_name_StartIndex, success)

            pass
        return retval

    # $ANTLR end "sym_name"

    class generative_return(ParserRuleReturnScope):
        def __init__(self):
            super(pycasmParser.generative_return, self).__init__()

            self.tree = None




    # $ANTLR start "generative"
    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:116:1: generative : (c= STRING | c= TYPED_VALUE ) -> ^() ;
    def generative(self, ):

        retval = self.generative_return()
        retval.start = self.input.LT(1)
        generative_StartIndex = self.input.index()
        root_0 = None

        c = None

        c_tree = None
        stream_TYPED_VALUE = RewriteRuleTokenStream(self._adaptor, "token TYPED_VALUE")
        stream_STRING = RewriteRuleTokenStream(self._adaptor, "token STRING")

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 12):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:117:2: ( (c= STRING | c= TYPED_VALUE ) -> ^() )
                # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:118:2: (c= STRING | c= TYPED_VALUE )
                pass 
                # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:118:2: (c= STRING | c= TYPED_VALUE )
                alt21 = 2
                LA21_0 = self.input.LA(1)

                if (LA21_0 == STRING) :
                    alt21 = 1
                elif (LA21_0 == TYPED_VALUE) :
                    alt21 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 21, 0, self.input)

                    raise nvae

                if alt21 == 1:
                    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:119:3: c= STRING
                    pass 
                    c=self.match(self.input, STRING, self.FOLLOW_STRING_in_generative452) 
                    if self._state.backtracking == 0:
                        stream_STRING.add(c)


                elif alt21 == 2:
                    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:120:4: c= TYPED_VALUE
                    pass 
                    c=self.match(self.input, TYPED_VALUE, self.FOLLOW_TYPED_VALUE_in_generative459) 
                    if self._state.backtracking == 0:
                        stream_TYPED_VALUE.add(c)




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
                    # 121:4: -> ^()
                    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:121:7: ^()
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self.adaptor.create(GEN, c.text), root_1)

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 12, generative_StartIndex, success)

            pass
        return retval

    # $ANTLR end "generative"

    class hex_code_return(ParserRuleReturnScope):
        def __init__(self):
            super(pycasmParser.hex_code_return, self).__init__()

            self.tree = None




    # $ANTLR start "hex_code"
    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:124:1: hex_code : (h= HEX_PAIR | h= HEX_QUAD | h= HEX_DQUAD ) -> ^() ;
    def hex_code(self, ):

        retval = self.hex_code_return()
        retval.start = self.input.LT(1)
        hex_code_StartIndex = self.input.index()
        root_0 = None

        h = None

        h_tree = None
        stream_HEX_DQUAD = RewriteRuleTokenStream(self._adaptor, "token HEX_DQUAD")
        stream_HEX_QUAD = RewriteRuleTokenStream(self._adaptor, "token HEX_QUAD")
        stream_HEX_PAIR = RewriteRuleTokenStream(self._adaptor, "token HEX_PAIR")

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 13):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:124:9: ( (h= HEX_PAIR | h= HEX_QUAD | h= HEX_DQUAD ) -> ^() )
                # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:125:2: (h= HEX_PAIR | h= HEX_QUAD | h= HEX_DQUAD )
                pass 
                # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:125:2: (h= HEX_PAIR | h= HEX_QUAD | h= HEX_DQUAD )
                alt22 = 3
                LA22 = self.input.LA(1)
                if LA22 == HEX_PAIR:
                    alt22 = 1
                elif LA22 == HEX_QUAD:
                    alt22 = 2
                elif LA22 == HEX_DQUAD:
                    alt22 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 22, 0, self.input)

                    raise nvae

                if alt22 == 1:
                    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:125:4: h= HEX_PAIR
                    pass 
                    h=self.match(self.input, HEX_PAIR, self.FOLLOW_HEX_PAIR_in_hex_code482) 
                    if self._state.backtracking == 0:
                        stream_HEX_PAIR.add(h)


                elif alt22 == 2:
                    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:126:4: h= HEX_QUAD
                    pass 
                    h=self.match(self.input, HEX_QUAD, self.FOLLOW_HEX_QUAD_in_hex_code489) 
                    if self._state.backtracking == 0:
                        stream_HEX_QUAD.add(h)


                elif alt22 == 3:
                    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:127:4: h= HEX_DQUAD
                    pass 
                    h=self.match(self.input, HEX_DQUAD, self.FOLLOW_HEX_DQUAD_in_hex_code496) 
                    if self._state.backtracking == 0:
                        stream_HEX_DQUAD.add(h)




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
                    # 129:4: -> ^()
                    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:129:7: ^()
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self.adaptor.create(HEX, h.text), root_1)

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 13, hex_code_StartIndex, success)

            pass
        return retval

    # $ANTLR end "hex_code"

    # $ANTLR start "synpred1_pycasmParser"
    def synpred1_pycasmParser_fragment(self, ):
        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:40:4: ( block )
        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:40:4: block
        pass 
        self._state.following.append(self.FOLLOW_block_in_synpred1_pycasmParser72)
        self.block()

        self._state.following.pop()


    # $ANTLR end "synpred1_pycasmParser"



    # $ANTLR start "synpred3_pycasmParser"
    def synpred3_pycasmParser_fragment(self, ):
        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:40:11: ( ( sp )+ )
        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:40:11: ( sp )+
        pass 
        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:40:11: ( sp )+
        cnt23 = 0
        while True: #loop23
            alt23 = 2
            LA23_0 = self.input.LA(1)

            if ((NEWLINE <= LA23_0 <= WS)) :
                alt23 = 1


            if alt23 == 1:
                # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:0:0: sp
                pass 
                self._state.following.append(self.FOLLOW_sp_in_synpred3_pycasmParser75)
                self.sp()

                self._state.following.pop()


            else:
                if cnt23 >= 1:
                    break #loop23

                if self._state.backtracking > 0:
                    raise BacktrackingFailed

                eee = EarlyExitException(23, self.input)
                raise eee

            cnt23 += 1


    # $ANTLR end "synpred3_pycasmParser"



    # $ANTLR start "synpred4_pycasmParser"
    def synpred4_pycasmParser_fragment(self, ):
        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:45:4: ( WS )
        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:45:4: WS
        pass 
        self.match(self.input, WS, self.FOLLOW_WS_in_synpred4_pycasmParser104)


    # $ANTLR end "synpred4_pycasmParser"



    # $ANTLR start "synpred5_pycasmParser"
    def synpred5_pycasmParser_fragment(self, ):
        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:45:7: ( NEWLINE )
        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:45:7: NEWLINE
        pass 
        self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_synpred5_pycasmParser106)


    # $ANTLR end "synpred5_pycasmParser"



    # $ANTLR start "synpred6_pycasmParser"
    def synpred6_pycasmParser_fragment(self, ):
        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:51:3: ( block_chain )
        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:51:3: block_chain
        pass 
        self._state.following.append(self.FOLLOW_block_chain_in_synpred6_pycasmParser129)
        self.block_chain()

        self._state.following.pop()


    # $ANTLR end "synpred6_pycasmParser"



    # $ANTLR start "synpred8_pycasmParser"
    def synpred8_pycasmParser_fragment(self, ):
        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:64:3: ( space_element )
        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:64:3: space_element
        pass 
        self._state.following.append(self.FOLLOW_space_element_in_synpred8_pycasmParser180)
        self.space_element()

        self._state.following.pop()


    # $ANTLR end "synpred8_pycasmParser"



    # $ANTLR start "synpred9_pycasmParser"
    def synpred9_pycasmParser_fragment(self, ):
        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:64:18: ( chain_element )
        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:64:18: chain_element
        pass 
        self._state.following.append(self.FOLLOW_chain_element_in_synpred9_pycasmParser183)
        self.chain_element()

        self._state.following.pop()


    # $ANTLR end "synpred9_pycasmParser"



    # $ANTLR start "synpred12_pycasmParser"
    def synpred12_pycasmParser_fragment(self, ):
        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:75:3: ( directive )
        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:75:3: directive
        pass 
        self._state.following.append(self.FOLLOW_directive_in_synpred12_pycasmParser218)
        self.directive()

        self._state.following.pop()


    # $ANTLR end "synpred12_pycasmParser"



    # $ANTLR start "synpred15_pycasmParser"
    def synpred15_pycasmParser_fragment(self, ):
        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:77:27: ( NEWLINE )
        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:77:27: NEWLINE
        pass 
        self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_synpred15_pycasmParser236)


    # $ANTLR end "synpred15_pycasmParser"



    # $ANTLR start "synpred16_pycasmParser"
    def synpred16_pycasmParser_fragment(self, ):
        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:77:36: ( DEDENT )
        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:77:36: DEDENT
        pass 
        self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_synpred16_pycasmParser239)


    # $ANTLR end "synpred16_pycasmParser"



    # $ANTLR start "synpred17_pycasmParser"
    def synpred17_pycasmParser_fragment(self, ):
        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:77:4: ( ( NEWLINE )? INDENT block ( NEWLINE )? ( DEDENT )? )
        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:77:4: ( NEWLINE )? INDENT block ( NEWLINE )? ( DEDENT )?
        pass 
        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:77:4: ( NEWLINE )?
        alt24 = 2
        LA24_0 = self.input.LA(1)

        if (LA24_0 == NEWLINE) :
            alt24 = 1
        if alt24 == 1:
            # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:0:0: NEWLINE
            pass 
            self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_synpred17_pycasmParser228)



        self.match(self.input, INDENT, self.FOLLOW_INDENT_in_synpred17_pycasmParser231)
        self._state.following.append(self.FOLLOW_block_in_synpred17_pycasmParser234)
        self.block()

        self._state.following.pop()
        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:77:27: ( NEWLINE )?
        alt25 = 2
        LA25_0 = self.input.LA(1)

        if (LA25_0 == NEWLINE) :
            alt25 = 1
        if alt25 == 1:
            # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:0:0: NEWLINE
            pass 
            self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_synpred17_pycasmParser236)



        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:77:42: ( DEDENT )?
        alt26 = 2
        LA26_0 = self.input.LA(1)

        if (LA26_0 == DEDENT) :
            alt26 = 1
        if alt26 == 1:
            # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:0:0: DEDENT
            pass 
            self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_synpred17_pycasmParser239)





    # $ANTLR end "synpred17_pycasmParser"



    # $ANTLR start "synpred20_pycasmParser"
    def synpred20_pycasmParser_fragment(self, ):
        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:91:26: ( NEWLINE )
        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:91:26: NEWLINE
        pass 
        self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_synpred20_pycasmParser312)


    # $ANTLR end "synpred20_pycasmParser"



    # $ANTLR start "synpred21_pycasmParser"
    def synpred21_pycasmParser_fragment(self, ):
        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:91:35: ( DEDENT )
        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:91:35: DEDENT
        pass 
        self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_synpred21_pycasmParser315)


    # $ANTLR end "synpred21_pycasmParser"



    # $ANTLR start "synpred23_pycasmParser"
    def synpred23_pycasmParser_fragment(self, ):
        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:92:6: ( DOT_END ( WS )+ ( NAME ) )
        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:92:6: DOT_END ( WS )+ ( NAME )
        pass 
        self.match(self.input, DOT_END, self.FOLLOW_DOT_END_in_synpred23_pycasmParser323)
        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:92:14: ( WS )+
        cnt27 = 0
        while True: #loop27
            alt27 = 2
            LA27_0 = self.input.LA(1)

            if (LA27_0 == WS) :
                alt27 = 1


            if alt27 == 1:
                # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:0:0: WS
                pass 
                self.match(self.input, WS, self.FOLLOW_WS_in_synpred23_pycasmParser325)


            else:
                if cnt27 >= 1:
                    break #loop27

                if self._state.backtracking > 0:
                    raise BacktrackingFailed

                eee = EarlyExitException(27, self.input)
                raise eee

            cnt27 += 1
        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:93:6: ( NAME )
        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:93:7: NAME
        pass 
        self.match(self.input, NAME, self.FOLLOW_NAME_in_synpred23_pycasmParser334)





    # $ANTLR end "synpred23_pycasmParser"



    # $ANTLR start "synpred25_pycasmParser"
    def synpred25_pycasmParser_fragment(self, ):
        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:101:6: ( NEWLINE )
        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmParser.g:101:6: NEWLINE
        pass 
        self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_synpred25_pycasmParser363)


    # $ANTLR end "synpred25_pycasmParser"




    # Delegated rules

    def synpred25_pycasmParser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred25_pycasmParser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred23_pycasmParser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred23_pycasmParser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred8_pycasmParser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred8_pycasmParser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred16_pycasmParser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred16_pycasmParser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred20_pycasmParser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred20_pycasmParser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred5_pycasmParser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred5_pycasmParser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred4_pycasmParser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred4_pycasmParser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred3_pycasmParser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred3_pycasmParser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred17_pycasmParser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred17_pycasmParser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred21_pycasmParser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred21_pycasmParser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred6_pycasmParser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred6_pycasmParser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred15_pycasmParser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred15_pycasmParser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred1_pycasmParser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred1_pycasmParser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred9_pycasmParser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred9_pycasmParser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred12_pycasmParser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred12_pycasmParser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success



    # lookup tables for DFA #4

    DFA4_eot = DFA.unpack(
        u"\20\uffff"
        )

    DFA4_eof = DFA.unpack(
        u"\1\1\17\uffff"
        )

    DFA4_min = DFA.unpack(
        u"\1\4\1\uffff\1\0\7\uffff\4\0\2\uffff"
        )

    DFA4_max = DFA.unpack(
        u"\1\34\1\uffff\1\0\7\uffff\4\0\2\uffff"
        )

    DFA4_accept = DFA.unpack(
        u"\1\uffff\1\2\15\uffff\1\1"
        )

    DFA4_special = DFA.unpack(
        u"\1\0\1\uffff\1\1\7\uffff\1\2\1\3\1\4\1\5\2\uffff"
        )

            
    DFA4_transition = [
        DFA.unpack(u"\1\1\1\14\3\uffff\3\1\2\uffff\1\1\1\uffff\2\1\1\uffff"
        u"\1\12\1\1\1\2\1\15\5\uffff\1\13"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #4

    class DFA4(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA4_0 = input.LA(1)

                 
                index4_0 = input.index()
                input.rewind()
                s = -1
                if (LA4_0 == EOF or LA4_0 == DEDENT or (HEX_QUAD <= LA4_0 <= HEX_PAIR) or LA4_0 == DOT_END or (TYPED_VALUE <= LA4_0 <= STRING) or LA4_0 == NAME):
                    s = 1

                elif (LA4_0 == NEWLINE):
                    s = 2

                elif (LA4_0 == DOT_NAME) and ((self.input.LT(1).getCharPositionInLine() == 0 or self.input.LT(-1) and self.input.LT(-1).getType() in [INDENT, DEDENT, NEWLINE] )):
                    s = 10

                elif (LA4_0 == DOT_DOT_NAME):
                    s = 11

                elif (LA4_0 == INDENT):
                    s = 12

                elif (LA4_0 == WS):
                    s = 13

                 
                input.seek(index4_0)
                if s >= 0:
                    return s
            elif s == 1: 
                LA4_2 = input.LA(1)

                 
                index4_2 = input.index()
                input.rewind()
                s = -1
                if (self.synpred6_pycasmParser()):
                    s = 15

                elif (True):
                    s = 1

                 
                input.seek(index4_2)
                if s >= 0:
                    return s
            elif s == 2: 
                LA4_10 = input.LA(1)

                 
                index4_10 = input.index()
                input.rewind()
                s = -1
                if (((self.synpred6_pycasmParser()) and ((self.input.LT(1).getCharPositionInLine() == 0 or self.input.LT(-1) and self.input.LT(-1).getType() in [INDENT, DEDENT, NEWLINE] )))):
                    s = 15

                elif ((self.input.LT(1).getCharPositionInLine() == 0 or self.input.LT(-1) and self.input.LT(-1).getType() in [INDENT, DEDENT, NEWLINE] )):
                    s = 1

                 
                input.seek(index4_10)
                if s >= 0:
                    return s
            elif s == 3: 
                LA4_11 = input.LA(1)

                 
                index4_11 = input.index()
                input.rewind()
                s = -1
                if (self.synpred6_pycasmParser()):
                    s = 15

                elif (True):
                    s = 1

                 
                input.seek(index4_11)
                if s >= 0:
                    return s
            elif s == 4: 
                LA4_12 = input.LA(1)

                 
                index4_12 = input.index()
                input.rewind()
                s = -1
                if (self.synpred6_pycasmParser()):
                    s = 15

                elif (True):
                    s = 1

                 
                input.seek(index4_12)
                if s >= 0:
                    return s
            elif s == 5: 
                LA4_13 = input.LA(1)

                 
                index4_13 = input.index()
                input.rewind()
                s = -1
                if (self.synpred6_pycasmParser()):
                    s = 15

                elif (True):
                    s = 1

                 
                input.seek(index4_13)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 4, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #6

    DFA6_eot = DFA.unpack(
        u"\20\uffff"
        )

    DFA6_eof = DFA.unpack(
        u"\1\1\17\uffff"
        )

    DFA6_min = DFA.unpack(
        u"\1\4\7\uffff\1\0\1\uffff\4\0\2\uffff"
        )

    DFA6_max = DFA.unpack(
        u"\1\34\7\uffff\1\0\1\uffff\4\0\2\uffff"
        )

    DFA6_accept = DFA.unpack(
        u"\1\uffff\1\2\15\uffff\1\1"
        )

    DFA6_special = DFA.unpack(
        u"\1\0\7\uffff\1\1\1\uffff\1\2\1\3\1\4\1\5\2\uffff"
        )

            
    DFA6_transition = [
        DFA.unpack(u"\1\1\1\14\3\uffff\3\1\2\uffff\1\1\1\uffff\2\1\1\uffff"
        u"\1\12\1\1\1\10\1\15\5\uffff\1\13"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #6

    class DFA6(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA6_0 = input.LA(1)

                 
                index6_0 = input.index()
                input.rewind()
                s = -1
                if (LA6_0 == EOF or LA6_0 == DEDENT or (HEX_QUAD <= LA6_0 <= HEX_PAIR) or LA6_0 == DOT_END or (TYPED_VALUE <= LA6_0 <= STRING) or LA6_0 == NAME):
                    s = 1

                elif (LA6_0 == NEWLINE):
                    s = 8

                elif (LA6_0 == DOT_NAME) and ((self.input.LT(1).getCharPositionInLine() == 0 or self.input.LT(-1) and self.input.LT(-1).getType() in [INDENT, DEDENT, NEWLINE] )):
                    s = 10

                elif (LA6_0 == DOT_DOT_NAME):
                    s = 11

                elif (LA6_0 == INDENT):
                    s = 12

                elif (LA6_0 == WS):
                    s = 13

                 
                input.seek(index6_0)
                if s >= 0:
                    return s
            elif s == 1: 
                LA6_8 = input.LA(1)

                 
                index6_8 = input.index()
                input.rewind()
                s = -1
                if (self.synpred8_pycasmParser()):
                    s = 15

                elif (True):
                    s = 1

                 
                input.seek(index6_8)
                if s >= 0:
                    return s
            elif s == 2: 
                LA6_10 = input.LA(1)

                 
                index6_10 = input.index()
                input.rewind()
                s = -1
                if (((self.synpred8_pycasmParser()) and ((self.input.LT(1).getCharPositionInLine() == 0 or self.input.LT(-1) and self.input.LT(-1).getType() in [INDENT, DEDENT, NEWLINE] )))):
                    s = 15

                elif ((self.input.LT(1).getCharPositionInLine() == 0 or self.input.LT(-1) and self.input.LT(-1).getType() in [INDENT, DEDENT, NEWLINE] )):
                    s = 1

                 
                input.seek(index6_10)
                if s >= 0:
                    return s
            elif s == 3: 
                LA6_11 = input.LA(1)

                 
                index6_11 = input.index()
                input.rewind()
                s = -1
                if (self.synpred8_pycasmParser()):
                    s = 15

                elif (True):
                    s = 1

                 
                input.seek(index6_11)
                if s >= 0:
                    return s
            elif s == 4: 
                LA6_12 = input.LA(1)

                 
                index6_12 = input.index()
                input.rewind()
                s = -1
                if (self.synpred8_pycasmParser()):
                    s = 15

                elif (True):
                    s = 1

                 
                input.seek(index6_12)
                if s >= 0:
                    return s
            elif s == 5: 
                LA6_13 = input.LA(1)

                 
                index6_13 = input.index()
                input.rewind()
                s = -1
                if (self.synpred8_pycasmParser()):
                    s = 15

                elif (True):
                    s = 1

                 
                input.seek(index6_13)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 6, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #7

    DFA7_eot = DFA.unpack(
        u"\13\uffff"
        )

    DFA7_eof = DFA.unpack(
        u"\1\7\12\uffff"
        )

    DFA7_min = DFA.unpack(
        u"\1\4\6\0\4\uffff"
        )

    DFA7_max = DFA.unpack(
        u"\1\34\6\0\4\uffff"
        )

    DFA7_accept = DFA.unpack(
        u"\7\uffff\3\2\1\1"
        )

    DFA7_special = DFA.unpack(
        u"\1\3\1\2\1\6\1\5\1\4\1\0\1\1\4\uffff"
        )

            
    DFA7_transition = [
        DFA.unpack(u"\1\7\1\11\3\uffff\1\5\1\6\1\4\2\uffff\1\11\1\uffff"
        u"\1\3\1\2\1\uffff\1\10\1\1\1\7\1\11\5\uffff\1\11"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #7

    class DFA7(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA7_5 = input.LA(1)

                 
                index7_5 = input.index()
                input.rewind()
                s = -1
                if (self.synpred9_pycasmParser()):
                    s = 10

                elif (True):
                    s = 9

                 
                input.seek(index7_5)
                if s >= 0:
                    return s
            elif s == 1: 
                LA7_6 = input.LA(1)

                 
                index7_6 = input.index()
                input.rewind()
                s = -1
                if (self.synpred9_pycasmParser()):
                    s = 10

                elif (True):
                    s = 9

                 
                input.seek(index7_6)
                if s >= 0:
                    return s
            elif s == 2: 
                LA7_1 = input.LA(1)

                 
                index7_1 = input.index()
                input.rewind()
                s = -1
                if (self.synpred9_pycasmParser()):
                    s = 10

                elif (True):
                    s = 9

                 
                input.seek(index7_1)
                if s >= 0:
                    return s
            elif s == 3: 
                LA7_0 = input.LA(1)

                 
                index7_0 = input.index()
                input.rewind()
                s = -1
                if (LA7_0 == NAME):
                    s = 1

                elif (LA7_0 == STRING):
                    s = 2

                elif (LA7_0 == TYPED_VALUE):
                    s = 3

                elif (LA7_0 == HEX_PAIR):
                    s = 4

                elif (LA7_0 == HEX_QUAD):
                    s = 5

                elif (LA7_0 == HEX_DQUAD):
                    s = 6

                elif (LA7_0 == EOF or LA7_0 == DEDENT or LA7_0 == NEWLINE):
                    s = 7

                elif (LA7_0 == DOT_NAME) and ((self.input.LT(1).getCharPositionInLine() == 0 or self.input.LT(-1) and self.input.LT(-1).getType() in [INDENT, DEDENT, NEWLINE] )):
                    s = 8

                elif (LA7_0 == INDENT or LA7_0 == DOT_END or LA7_0 == WS or LA7_0 == DOT_DOT_NAME):
                    s = 9

                 
                input.seek(index7_0)
                if s >= 0:
                    return s
            elif s == 4: 
                LA7_4 = input.LA(1)

                 
                index7_4 = input.index()
                input.rewind()
                s = -1
                if (self.synpred9_pycasmParser()):
                    s = 10

                elif (True):
                    s = 9

                 
                input.seek(index7_4)
                if s >= 0:
                    return s
            elif s == 5: 
                LA7_3 = input.LA(1)

                 
                index7_3 = input.index()
                input.rewind()
                s = -1
                if (self.synpred9_pycasmParser()):
                    s = 10

                elif (True):
                    s = 9

                 
                input.seek(index7_3)
                if s >= 0:
                    return s
            elif s == 6: 
                LA7_2 = input.LA(1)

                 
                index7_2 = input.index()
                input.rewind()
                s = -1
                if (self.synpred9_pycasmParser()):
                    s = 10

                elif (True):
                    s = 9

                 
                input.seek(index7_2)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 7, _s, input)
            self_.error(nvae)
            raise nvae
 

    FOLLOW_block_in_root72 = frozenset([])
    FOLLOW_sp_in_root75 = frozenset([21, 22])
    FOLLOW_EOF_in_root80 = frozenset([1])
    FOLLOW_WS_in_sp104 = frozenset([1, 21, 22])
    FOLLOW_NEWLINE_in_sp106 = frozenset([1, 21, 22])
    FOLLOW_block_head_in_block125 = frozenset([1, 5, 19, 21, 22, 28])
    FOLLOW_block_chain_in_block129 = frozenset([1, 5, 19, 21, 22, 28])
    FOLLOW_chain_element_in_block_head162 = frozenset([1])
    FOLLOW_block_chain_in_block_head167 = frozenset([1])
    FOLLOW_space_element_in_block_chain180 = frozenset([1, 5, 9, 10, 11, 16, 17, 19, 20, 21, 22, 28])
    FOLLOW_chain_element_in_block_chain183 = frozenset([1])
    FOLLOW_sym_name_in_chain_element195 = frozenset([1])
    FOLLOW_generative_in_chain_element200 = frozenset([1])
    FOLLOW_hex_code_in_chain_element205 = frozenset([1])
    FOLLOW_directive_in_space_element218 = frozenset([1])
    FOLLOW_unrestricted_directive_in_space_element223 = frozenset([1])
    FOLLOW_NEWLINE_in_space_element228 = frozenset([5])
    FOLLOW_INDENT_in_space_element231 = frozenset([5, 9, 10, 11, 16, 17, 19, 20, 21, 22, 28])
    FOLLOW_block_in_space_element234 = frozenset([1, 4, 21])
    FOLLOW_NEWLINE_in_space_element236 = frozenset([1, 4])
    FOLLOW_DEDENT_in_space_element239 = frozenset([1])
    FOLLOW_sp_in_space_element246 = frozenset([1])
    FOLLOW_DOT_DOT_NAME_in_unrestricted_directive259 = frozenset([1, 41, 42])
    FOLLOW_DOT_DOT_ARGS_in_unrestricted_directive261 = frozenset([1, 42])
    FOLLOW_DOT_DOT_BODY_in_unrestricted_directive264 = frozenset([1])
    FOLLOW_directive_header_in_directive300 = frozenset([1, 21])
    FOLLOW_NEWLINE_in_directive306 = frozenset([5])
    FOLLOW_INDENT_in_directive308 = frozenset([5, 9, 10, 11, 16, 17, 19, 20, 21, 22, 28])
    FOLLOW_block_in_directive310 = frozenset([1, 4, 14, 21])
    FOLLOW_NEWLINE_in_directive312 = frozenset([1, 4, 14])
    FOLLOW_DEDENT_in_directive315 = frozenset([1, 14])
    FOLLOW_DOT_END_in_directive323 = frozenset([22])
    FOLLOW_WS_in_directive325 = frozenset([20, 22])
    FOLLOW_NAME_in_directive334 = frozenset([1])
    FOLLOW_NEWLINE_in_directive363 = frozenset([1])
    FOLLOW_DOT_NAME_in_directive_header397 = frozenset([1, 45])
    FOLLOW_DOT_ARGS_in_directive_header399 = frozenset([1])
    FOLLOW_NAME_in_sym_name426 = frozenset([1])
    FOLLOW_STRING_in_generative452 = frozenset([1])
    FOLLOW_TYPED_VALUE_in_generative459 = frozenset([1])
    FOLLOW_HEX_PAIR_in_hex_code482 = frozenset([1])
    FOLLOW_HEX_QUAD_in_hex_code489 = frozenset([1])
    FOLLOW_HEX_DQUAD_in_hex_code496 = frozenset([1])
    FOLLOW_block_in_synpred1_pycasmParser72 = frozenset([1])
    FOLLOW_sp_in_synpred3_pycasmParser75 = frozenset([1, 21, 22])
    FOLLOW_WS_in_synpred4_pycasmParser104 = frozenset([1])
    FOLLOW_NEWLINE_in_synpred5_pycasmParser106 = frozenset([1])
    FOLLOW_block_chain_in_synpred6_pycasmParser129 = frozenset([1])
    FOLLOW_space_element_in_synpred8_pycasmParser180 = frozenset([1])
    FOLLOW_chain_element_in_synpred9_pycasmParser183 = frozenset([1])
    FOLLOW_directive_in_synpred12_pycasmParser218 = frozenset([1])
    FOLLOW_NEWLINE_in_synpred15_pycasmParser236 = frozenset([1])
    FOLLOW_DEDENT_in_synpred16_pycasmParser239 = frozenset([1])
    FOLLOW_NEWLINE_in_synpred17_pycasmParser228 = frozenset([5])
    FOLLOW_INDENT_in_synpred17_pycasmParser231 = frozenset([5, 9, 10, 11, 16, 17, 19, 20, 21, 22, 28])
    FOLLOW_block_in_synpred17_pycasmParser234 = frozenset([1, 4, 21])
    FOLLOW_NEWLINE_in_synpred17_pycasmParser236 = frozenset([1, 4])
    FOLLOW_DEDENT_in_synpred17_pycasmParser239 = frozenset([1])
    FOLLOW_NEWLINE_in_synpred20_pycasmParser312 = frozenset([1])
    FOLLOW_DEDENT_in_synpred21_pycasmParser315 = frozenset([1])
    FOLLOW_DOT_END_in_synpred23_pycasmParser323 = frozenset([22])
    FOLLOW_WS_in_synpred23_pycasmParser325 = frozenset([20, 22])
    FOLLOW_NAME_in_synpred23_pycasmParser334 = frozenset([1])
    FOLLOW_NEWLINE_in_synpred25_pycasmParser363 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("pycasmParser", pycasmParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
