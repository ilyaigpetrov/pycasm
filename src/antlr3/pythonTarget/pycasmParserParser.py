# $ANTLR 3.0.1 pycasmParser.g 2011-06-23 12:23:15

from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
DOT_DOT_BODY=13
DOT_DOT_NAME=11
DOT_DOT_ARGS=12
TYPED_VALUE=19
DOT_END=14
DEDENT=10
HEX_DQUAD=22
EOF=-1
ROOT=4
SYM=6
INDENT=9
NAME=15
WS=7
NEWLINE=8
HEX=5
DOT_NAME=16
HEX_QUAD=21
DOT_ARGS=17
HEX_PAIR=20
STRING=18

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "ROOT", "HEX", "SYM", "WS", "NEWLINE", "INDENT", "DEDENT", "DOT_DOT_NAME", 
    "DOT_DOT_ARGS", "DOT_DOT_BODY", "DOT_END", "NAME", "DOT_NAME", "DOT_ARGS", 
    "STRING", "TYPED_VALUE", "HEX_PAIR", "HEX_QUAD", "HEX_DQUAD"
]



class pycasmParserParser(Parser):
    grammarFileName = "pycasmParser.g"
    tokenNames = tokenNames

    def __init__(self, input):
        Parser.__init__(self, input)
        self.ruleMemo = {}


               
        from pycasm.syntax.errors import StandardErrorReporter
        self.patchInErrorReporter(StandardErrorReporter())


                
        self.adaptor = CommonTreeAdaptor()



              
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


    class root_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start root
    # pycasmParser.g:64:1: root : ( block | ( sp )+ )? EOF -> ^( ROOT ( block )? ) ;
    def root(self, ):

        retval = self.root_return()
        retval.start = self.input.LT(1)
        root_StartIndex = self.input.index()
        root_0 = None

        EOF3 = None
        block1 = None

        sp2 = None


        EOF3_tree = None
        stream_EOF = RewriteRuleTokenStream(self.adaptor, "token EOF")
        stream_sp = RewriteRuleSubtreeStream(self.adaptor, "rule sp")
        stream_block = RewriteRuleSubtreeStream(self.adaptor, "rule block")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 1):
                    return retval

                # pycasmParser.g:65:2: ( ( block | ( sp )+ )? EOF -> ^( ROOT ( block )? ) )
                # pycasmParser.g:66:3: ( block | ( sp )+ )? EOF
                # pycasmParser.g:66:3: ( block | ( sp )+ )?
                alt2 = 3
                LA2 = self.input.LA(1)
                if LA2 == INDENT or LA2 == DOT_DOT_NAME or LA2 == NAME or LA2 == DOT_NAME or LA2 == STRING or LA2 == TYPED_VALUE or LA2 == HEX_PAIR or LA2 == HEX_QUAD or LA2 == HEX_DQUAD:
                    alt2 = 1
                elif LA2 == NEWLINE:
                    LA2_2 = self.input.LA(2)

                    if (self.synpred1()) :
                        alt2 = 1
                    elif (self.synpred3()) :
                        alt2 = 2
                elif LA2 == WS:
                    LA2_3 = self.input.LA(2)

                    if (self.synpred1()) :
                        alt2 = 1
                    elif (self.synpred3()) :
                        alt2 = 2
                if alt2 == 1:
                    # pycasmParser.g:66:4: block
                    self.following.append(self.FOLLOW_block_in_root75)
                    block1 = self.block()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_block.add(block1.tree)


                elif alt2 == 2:
                    # pycasmParser.g:66:11: ( sp )+
                    # pycasmParser.g:66:11: ( sp )+
                    cnt1 = 0
                    while True: #loop1
                        alt1 = 2
                        LA1_0 = self.input.LA(1)

                        if ((WS <= LA1_0 <= NEWLINE)) :
                            alt1 = 1


                        if alt1 == 1:
                            # pycasmParser.g:0:0: sp
                            self.following.append(self.FOLLOW_sp_in_root78)
                            sp2 = self.sp()
                            self.following.pop()
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_sp.add(sp2.tree)


                        else:
                            if cnt1 >= 1:
                                break #loop1

                            if self.backtracking > 0:
                                self.failed = True
                                return retval

                            eee = EarlyExitException(1, self.input)
                            raise eee

                        cnt1 += 1





                EOF3 = self.input.LT(1)
                self.match(self.input, EOF, self.FOLLOW_EOF_in_root83)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_EOF.add(EOF3)
                # AST Rewrite
                # elements: block
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                    root_0 = self.adaptor.nil()
                    # 67:3: -> ^( ROOT ( block )? )
                    # pycasmParser.g:67:6: ^( ROOT ( block )? )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(ROOT, "ROOT"), root_1)

                    # pycasmParser.g:67:13: ( block )?
                    if stream_block.hasNext():
                        self.adaptor.addChild(root_1, stream_block.next())


                    stream_block.reset();

                    self.adaptor.addChild(root_0, root_1)






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 1, root_StartIndex)

            pass

        return retval

    # $ANTLR end root

    class sp_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start sp
    # pycasmParser.g:70:1: sp : ( WS | NEWLINE )+ ->;
    def sp(self, ):

        retval = self.sp_return()
        retval.start = self.input.LT(1)
        sp_StartIndex = self.input.index()
        root_0 = None

        WS4 = None
        NEWLINE5 = None

        WS4_tree = None
        NEWLINE5_tree = None
        stream_WS = RewriteRuleTokenStream(self.adaptor, "token WS")
        stream_NEWLINE = RewriteRuleTokenStream(self.adaptor, "token NEWLINE")

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 2):
                    return retval

                # pycasmParser.g:70:4: ( ( WS | NEWLINE )+ ->)
                # pycasmParser.g:71:3: ( WS | NEWLINE )+
                # pycasmParser.g:71:3: ( WS | NEWLINE )+
                cnt3 = 0
                while True: #loop3
                    alt3 = 3
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == WS) :
                        LA3_2 = self.input.LA(2)

                        if (self.synpred4()) :
                            alt3 = 1


                    elif (LA3_0 == NEWLINE) :
                        LA3_3 = self.input.LA(2)

                        if (self.synpred5()) :
                            alt3 = 2




                    if alt3 == 1:
                        # pycasmParser.g:71:4: WS
                        WS4 = self.input.LT(1)
                        self.match(self.input, WS, self.FOLLOW_WS_in_sp107)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_WS.add(WS4)


                    elif alt3 == 2:
                        # pycasmParser.g:71:7: NEWLINE
                        NEWLINE5 = self.input.LT(1)
                        self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_sp109)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_NEWLINE.add(NEWLINE5)


                    else:
                        if cnt3 >= 1:
                            break #loop3

                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        eee = EarlyExitException(3, self.input)
                        raise eee

                    cnt3 += 1


                # AST Rewrite
                # elements: 
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                    root_0 = self.adaptor.nil()
                    # 71:17: ->
                    root_0 = self.adaptor.nil()





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 2, sp_StartIndex)

            pass

        return retval

    # $ANTLR end sp

    class block_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start block
    # pycasmParser.g:74:1: block : h= block_head ( block_chain )* -> { not isinstance($h.tree, type(None)) }? ^( BLOCK block_head ( block_chain )* ) ->;
    def block(self, ):

        retval = self.block_return()
        retval.start = self.input.LT(1)
        block_StartIndex = self.input.index()
        root_0 = None

        h = None

        block_chain6 = None


        stream_block_chain = RewriteRuleSubtreeStream(self.adaptor, "rule block_chain")
        stream_block_head = RewriteRuleSubtreeStream(self.adaptor, "rule block_head")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 3):
                    return retval

                # pycasmParser.g:75:2: (h= block_head ( block_chain )* -> { not isinstance($h.tree, type(None)) }? ^( BLOCK block_head ( block_chain )* ) ->)
                # pycasmParser.g:76:3: h= block_head ( block_chain )*
                self.following.append(self.FOLLOW_block_head_in_block128)
                h = self.block_head()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_block_head.add(h.tree)
                # pycasmParser.g:77:3: ( block_chain )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == NEWLINE) :
                        LA4_2 = self.input.LA(2)

                        if (self.synpred6()) :
                            alt4 = 1


                    elif (LA4_0 == DOT_NAME) and (self.input.LT(1).getCharPositionInLine() == 0 or self.input.LT(-1) and self.input.LT(-1).getType() in [INDENT, DEDENT, NEWLINE] ):
                        LA4_3 = self.input.LA(2)

                        if ((self.synpred6() and self.input.LT(1).getCharPositionInLine() == 0 or self.input.LT(-1) and self.input.LT(-1).getType() in [INDENT, DEDENT, NEWLINE] )) :
                            alt4 = 1


                    elif (LA4_0 == DOT_DOT_NAME) :
                        LA4_4 = self.input.LA(2)

                        if (self.synpred6()) :
                            alt4 = 1


                    elif (LA4_0 == INDENT) :
                        LA4_5 = self.input.LA(2)

                        if (self.synpred6()) :
                            alt4 = 1


                    elif (LA4_0 == WS) :
                        LA4_6 = self.input.LA(2)

                        if (self.synpred6()) :
                            alt4 = 1




                    if alt4 == 1:
                        # pycasmParser.g:0:0: block_chain
                        self.following.append(self.FOLLOW_block_chain_in_block132)
                        block_chain6 = self.block_chain()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_block_chain.add(block_chain6.tree)


                    else:
                        break #loop4


                # AST Rewrite
                # elements: block_chain, block_head
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                    root_0 = self.adaptor.nil()
                    if not isinstance(h.tree, type(None)) :
                        # 78:3: -> { not isinstance($h.tree, type(None)) }? ^( BLOCK block_head ( block_chain )* )
                        # pycasmParser.g:78:47: ^( BLOCK block_head ( block_chain )* )
                        root_1 = self.adaptor.nil()
                        self.adaptor.addChild(root_1, stream_block_head.next())
                        # pycasmParser.g:78:66: ( block_chain )*
                        while stream_block_chain.hasNext():
                            self.adaptor.addChild(root_1, stream_block_chain.next())


                        stream_block_chain.reset();

                        self.adaptor.addChild(root_0, root_1)


                    else: 
                        # 79:3: ->
                        root_0 = self.adaptor.nil()



                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 3, block_StartIndex)

            pass

        return retval

    # $ANTLR end block

    class block_head_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start block_head
    # pycasmParser.g:82:1: block_head : ( chain_element | block_chain );
    def block_head(self, ):

        retval = self.block_head_return()
        retval.start = self.input.LT(1)
        block_head_StartIndex = self.input.index()
        root_0 = None

        chain_element7 = None

        block_chain8 = None



        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 4):
                    return retval

                # pycasmParser.g:83:2: ( chain_element | block_chain )
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == NAME or (STRING <= LA5_0 <= HEX_DQUAD)) :
                    alt5 = 1
                elif (LA5_0 == DOT_NAME) and (self.input.LT(1).getCharPositionInLine() == 0 or self.input.LT(-1) and self.input.LT(-1).getType() in [INDENT, DEDENT, NEWLINE] ):
                    alt5 = 2
                elif ((WS <= LA5_0 <= INDENT) or LA5_0 == DOT_DOT_NAME) :
                    alt5 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("82:1: block_head : ( chain_element | block_chain );", 5, 0, self.input)

                    raise nvae

                if alt5 == 1:
                    # pycasmParser.g:84:3: chain_element
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_chain_element_in_block_head165)
                    chain_element7 = self.chain_element()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, chain_element7.tree)


                elif alt5 == 2:
                    # pycasmParser.g:85:4: block_chain
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_block_chain_in_block_head170)
                    block_chain8 = self.block_chain()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, block_chain8.tree)


                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 4, block_head_StartIndex)

            pass

        return retval

    # $ANTLR end block_head

    class block_chain_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start block_chain
    # pycasmParser.g:88:1: block_chain : ( space_element )+ ( chain_element )? ;
    def block_chain(self, ):

        retval = self.block_chain_return()
        retval.start = self.input.LT(1)
        block_chain_StartIndex = self.input.index()
        root_0 = None

        space_element9 = None

        chain_element10 = None



        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 5):
                    return retval

                # pycasmParser.g:89:2: ( ( space_element )+ ( chain_element )? )
                # pycasmParser.g:90:3: ( space_element )+ ( chain_element )?
                root_0 = self.adaptor.nil()

                # pycasmParser.g:90:3: ( space_element )+
                cnt6 = 0
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == NEWLINE) :
                        LA6_2 = self.input.LA(2)

                        if (self.synpred8()) :
                            alt6 = 1


                    elif (LA6_0 == DOT_NAME) and (self.input.LT(1).getCharPositionInLine() == 0 or self.input.LT(-1) and self.input.LT(-1).getType() in [INDENT, DEDENT, NEWLINE] ):
                        LA6_3 = self.input.LA(2)

                        if ((self.synpred8() and self.input.LT(1).getCharPositionInLine() == 0 or self.input.LT(-1) and self.input.LT(-1).getType() in [INDENT, DEDENT, NEWLINE] )) :
                            alt6 = 1


                    elif (LA6_0 == DOT_DOT_NAME) :
                        LA6_4 = self.input.LA(2)

                        if (self.synpred8()) :
                            alt6 = 1


                    elif (LA6_0 == INDENT) :
                        LA6_5 = self.input.LA(2)

                        if (self.synpred8()) :
                            alt6 = 1


                    elif (LA6_0 == WS) :
                        LA6_6 = self.input.LA(2)

                        if (self.synpred8()) :
                            alt6 = 1




                    if alt6 == 1:
                        # pycasmParser.g:0:0: space_element
                        self.following.append(self.FOLLOW_space_element_in_block_chain183)
                        space_element9 = self.space_element()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, space_element9.tree)


                    else:
                        if cnt6 >= 1:
                            break #loop6

                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        eee = EarlyExitException(6, self.input)
                        raise eee

                    cnt6 += 1


                # pycasmParser.g:90:18: ( chain_element )?
                alt7 = 2
                LA7 = self.input.LA(1)
                if LA7 == NAME:
                    LA7_1 = self.input.LA(2)

                    if (self.synpred9()) :
                        alt7 = 1
                elif LA7 == STRING:
                    LA7_2 = self.input.LA(2)

                    if (self.synpred9()) :
                        alt7 = 1
                elif LA7 == TYPED_VALUE:
                    LA7_3 = self.input.LA(2)

                    if (self.synpred9()) :
                        alt7 = 1
                elif LA7 == HEX_PAIR:
                    LA7_4 = self.input.LA(2)

                    if (self.synpred9()) :
                        alt7 = 1
                elif LA7 == HEX_QUAD:
                    LA7_5 = self.input.LA(2)

                    if (self.synpred9()) :
                        alt7 = 1
                elif LA7 == HEX_DQUAD:
                    LA7_6 = self.input.LA(2)

                    if (self.synpred9()) :
                        alt7 = 1
                if alt7 == 1:
                    # pycasmParser.g:0:0: chain_element
                    self.following.append(self.FOLLOW_chain_element_in_block_chain186)
                    chain_element10 = self.chain_element()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, chain_element10.tree)






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 5, block_chain_StartIndex)

            pass

        return retval

    # $ANTLR end block_chain

    class chain_element_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start chain_element
    # pycasmParser.g:93:1: chain_element : ( sym_name | generative | hex_code );
    def chain_element(self, ):

        retval = self.chain_element_return()
        retval.start = self.input.LT(1)
        chain_element_StartIndex = self.input.index()
        root_0 = None

        sym_name11 = None

        generative12 = None

        hex_code13 = None



        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 6):
                    return retval

                # pycasmParser.g:94:2: ( sym_name | generative | hex_code )
                alt8 = 3
                LA8 = self.input.LA(1)
                if LA8 == NAME:
                    alt8 = 1
                elif LA8 == STRING or LA8 == TYPED_VALUE:
                    alt8 = 2
                elif LA8 == HEX_PAIR or LA8 == HEX_QUAD or LA8 == HEX_DQUAD:
                    alt8 = 3
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("93:1: chain_element : ( sym_name | generative | hex_code );", 8, 0, self.input)

                    raise nvae

                if alt8 == 1:
                    # pycasmParser.g:94:4: sym_name
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_sym_name_in_chain_element198)
                    sym_name11 = self.sym_name()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, sym_name11.tree)


                elif alt8 == 2:
                    # pycasmParser.g:95:4: generative
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_generative_in_chain_element203)
                    generative12 = self.generative()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, generative12.tree)


                elif alt8 == 3:
                    # pycasmParser.g:96:4: hex_code
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_hex_code_in_chain_element208)
                    hex_code13 = self.hex_code()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, hex_code13.tree)


                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 6, chain_element_StartIndex)

            pass

        return retval

    # $ANTLR end chain_element

    class space_element_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start space_element
    # pycasmParser.g:99:1: space_element : ( directive | unrestricted_directive | ( NEWLINE )? INDENT block ( NEWLINE )? ( DEDENT )? | sp );
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

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 7):
                    return retval

                # pycasmParser.g:100:2: ( directive | unrestricted_directive | ( NEWLINE )? INDENT block ( NEWLINE )? ( DEDENT )? | sp )
                alt12 = 4
                LA12_0 = self.input.LA(1)

                if (LA12_0 == DOT_NAME) and (self.input.LT(1).getCharPositionInLine() == 0 or self.input.LT(-1) and self.input.LT(-1).getType() in [INDENT, DEDENT, NEWLINE] ):
                    alt12 = 1
                elif (LA12_0 == DOT_DOT_NAME) :
                    alt12 = 2
                elif (LA12_0 == NEWLINE) :
                    LA12_3 = self.input.LA(2)

                    if (self.synpred17()) :
                        alt12 = 3
                    elif (True) :
                        alt12 = 4
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("99:1: space_element : ( directive | unrestricted_directive | ( NEWLINE )? INDENT block ( NEWLINE )? ( DEDENT )? | sp );", 12, 3, self.input)

                        raise nvae

                elif (LA12_0 == INDENT) :
                    alt12 = 3
                elif (LA12_0 == WS) :
                    alt12 = 4
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("99:1: space_element : ( directive | unrestricted_directive | ( NEWLINE )? INDENT block ( NEWLINE )? ( DEDENT )? | sp );", 12, 0, self.input)

                    raise nvae

                if alt12 == 1:
                    # pycasmParser.g:101:3: directive
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_directive_in_space_element221)
                    directive14 = self.directive()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, directive14.tree)


                elif alt12 == 2:
                    # pycasmParser.g:102:4: unrestricted_directive
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_unrestricted_directive_in_space_element226)
                    unrestricted_directive15 = self.unrestricted_directive()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, unrestricted_directive15.tree)


                elif alt12 == 3:
                    # pycasmParser.g:103:4: ( NEWLINE )? INDENT block ( NEWLINE )? ( DEDENT )?
                    root_0 = self.adaptor.nil()

                    # pycasmParser.g:103:4: ( NEWLINE )?
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == NEWLINE) :
                        alt9 = 1
                    if alt9 == 1:
                        # pycasmParser.g:0:0: NEWLINE
                        NEWLINE16 = self.input.LT(1)
                        self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_space_element231)
                        if self.failed:
                            return retval

                        NEWLINE16_tree = self.adaptor.createWithPayload(NEWLINE16)
                        self.adaptor.addChild(root_0, NEWLINE16_tree)




                    INDENT17 = self.input.LT(1)
                    self.match(self.input, INDENT, self.FOLLOW_INDENT_in_space_element234)
                    if self.failed:
                        return retval
                    self.following.append(self.FOLLOW_block_in_space_element237)
                    block18 = self.block()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, block18.tree)
                    # pycasmParser.g:103:27: ( NEWLINE )?
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == NEWLINE) :
                        LA10_1 = self.input.LA(2)

                        if (self.synpred15()) :
                            alt10 = 1
                    if alt10 == 1:
                        # pycasmParser.g:0:0: NEWLINE
                        NEWLINE19 = self.input.LT(1)
                        self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_space_element239)
                        if self.failed:
                            return retval

                        NEWLINE19_tree = self.adaptor.createWithPayload(NEWLINE19)
                        self.adaptor.addChild(root_0, NEWLINE19_tree)




                    # pycasmParser.g:103:42: ( DEDENT )?
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == DEDENT) :
                        LA11_1 = self.input.LA(2)

                        if (self.synpred16()) :
                            alt11 = 1
                    if alt11 == 1:
                        # pycasmParser.g:0:0: DEDENT
                        DEDENT20 = self.input.LT(1)
                        self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_space_element242)
                        if self.failed:
                            return retval





                elif alt12 == 4:
                    # pycasmParser.g:104:4: sp
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_sp_in_space_element249)
                    sp21 = self.sp()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, sp21.tree)


                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 7, space_element_StartIndex)

            pass

        return retval

    # $ANTLR end space_element

    class unrestricted_directive_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start unrestricted_directive
    # pycasmParser.g:107:1: unrestricted_directive : DOT_DOT_NAME ( DOT_DOT_ARGS )? ( DOT_DOT_BODY )? -> ^( DOT_DOT_NAME ( DOT_DOT_ARGS )? ( DOT_DOT_BODY )? ) ;
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
        stream_DOT_DOT_BODY = RewriteRuleTokenStream(self.adaptor, "token DOT_DOT_BODY")
        stream_DOT_DOT_NAME = RewriteRuleTokenStream(self.adaptor, "token DOT_DOT_NAME")
        stream_DOT_DOT_ARGS = RewriteRuleTokenStream(self.adaptor, "token DOT_DOT_ARGS")

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 8):
                    return retval

                # pycasmParser.g:108:2: ( DOT_DOT_NAME ( DOT_DOT_ARGS )? ( DOT_DOT_BODY )? -> ^( DOT_DOT_NAME ( DOT_DOT_ARGS )? ( DOT_DOT_BODY )? ) )
                # pycasmParser.g:109:3: DOT_DOT_NAME ( DOT_DOT_ARGS )? ( DOT_DOT_BODY )?
                DOT_DOT_NAME22 = self.input.LT(1)
                self.match(self.input, DOT_DOT_NAME, self.FOLLOW_DOT_DOT_NAME_in_unrestricted_directive262)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_DOT_DOT_NAME.add(DOT_DOT_NAME22)
                # pycasmParser.g:109:16: ( DOT_DOT_ARGS )?
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if (LA13_0 == DOT_DOT_ARGS) :
                    alt13 = 1
                if alt13 == 1:
                    # pycasmParser.g:0:0: DOT_DOT_ARGS
                    DOT_DOT_ARGS23 = self.input.LT(1)
                    self.match(self.input, DOT_DOT_ARGS, self.FOLLOW_DOT_DOT_ARGS_in_unrestricted_directive264)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_DOT_DOT_ARGS.add(DOT_DOT_ARGS23)



                # pycasmParser.g:109:30: ( DOT_DOT_BODY )?
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if (LA14_0 == DOT_DOT_BODY) :
                    alt14 = 1
                if alt14 == 1:
                    # pycasmParser.g:0:0: DOT_DOT_BODY
                    DOT_DOT_BODY24 = self.input.LT(1)
                    self.match(self.input, DOT_DOT_BODY, self.FOLLOW_DOT_DOT_BODY_in_unrestricted_directive267)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_DOT_DOT_BODY.add(DOT_DOT_BODY24)



                # AST Rewrite
                # elements: DOT_DOT_NAME, DOT_DOT_ARGS, DOT_DOT_BODY
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                    root_0 = self.adaptor.nil()
                    # 109:44: -> ^( DOT_DOT_NAME ( DOT_DOT_ARGS )? ( DOT_DOT_BODY )? )
                    # pycasmParser.g:109:47: ^( DOT_DOT_NAME ( DOT_DOT_ARGS )? ( DOT_DOT_BODY )? )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(stream_DOT_DOT_NAME.next(), root_1)

                    # pycasmParser.g:109:62: ( DOT_DOT_ARGS )?
                    if stream_DOT_DOT_ARGS.hasNext():
                        self.adaptor.addChild(root_1, stream_DOT_DOT_ARGS.next())


                    stream_DOT_DOT_ARGS.reset();
                    # pycasmParser.g:109:76: ( DOT_DOT_BODY )?
                    if stream_DOT_DOT_BODY.hasNext():
                        self.adaptor.addChild(root_1, stream_DOT_DOT_BODY.next())


                    stream_DOT_DOT_BODY.reset();

                    self.adaptor.addChild(root_0, root_1)






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 8, unrestricted_directive_StartIndex)

            pass

        return retval

    # $ANTLR end unrestricted_directive

    class directive_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start directive
    # pycasmParser.g:112:1: directive : {...}? => ( directive_header ( NEWLINE INDENT block ( NEWLINE )? ( DEDENT )? ( DOT_END ( WS )+ ( NAME ) )? | NEWLINE )? ) -> ^( ( block )? ) ;
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
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_DEDENT = RewriteRuleTokenStream(self.adaptor, "token DEDENT")
        stream_WS = RewriteRuleTokenStream(self.adaptor, "token WS")
        stream_NEWLINE = RewriteRuleTokenStream(self.adaptor, "token NEWLINE")
        stream_DOT_END = RewriteRuleTokenStream(self.adaptor, "token DOT_END")
        stream_INDENT = RewriteRuleTokenStream(self.adaptor, "token INDENT")
        stream_directive_header = RewriteRuleSubtreeStream(self.adaptor, "rule directive_header")
        stream_block = RewriteRuleSubtreeStream(self.adaptor, "rule block")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 9):
                    return retval

                # pycasmParser.g:113:2: ({...}? => ( directive_header ( NEWLINE INDENT block ( NEWLINE )? ( DEDENT )? ( DOT_END ( WS )+ ( NAME ) )? | NEWLINE )? ) -> ^( ( block )? ) )
                # pycasmParser.g:114:3: {...}? => ( directive_header ( NEWLINE INDENT block ( NEWLINE )? ( DEDENT )? ( DOT_END ( WS )+ ( NAME ) )? | NEWLINE )? )
                if not (self.input.LT(1).getCharPositionInLine() == 0 or self.input.LT(-1) and self.input.LT(-1).getType() in [INDENT, DEDENT, NEWLINE] ):
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    raise FailedPredicateException(self.input, "directive", " self.input.LT(1).getCharPositionInLine() == 0 or self.input.LT(-1) and self.input.LT(-1).getType() in [INDENT, DEDENT, NEWLINE] ")

                # pycasmParser.g:115:6: ( directive_header ( NEWLINE INDENT block ( NEWLINE )? ( DEDENT )? ( DOT_END ( WS )+ ( NAME ) )? | NEWLINE )? )
                # pycasmParser.g:116:3: directive_header ( NEWLINE INDENT block ( NEWLINE )? ( DEDENT )? ( DOT_END ( WS )+ ( NAME ) )? | NEWLINE )?
                self.following.append(self.FOLLOW_directive_header_in_directive303)
                directive_header25 = self.directive_header()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_directive_header.add(directive_header25.tree)
                # pycasmParser.g:117:4: ( NEWLINE INDENT block ( NEWLINE )? ( DEDENT )? ( DOT_END ( WS )+ ( NAME ) )? | NEWLINE )?
                alt19 = 3
                LA19_0 = self.input.LA(1)

                if (LA19_0 == NEWLINE) :
                    LA19_1 = self.input.LA(2)

                    if (LA19_1 == INDENT) :
                        alt19 = 1
                    elif (self.synpred25()) :
                        alt19 = 2
                if alt19 == 1:
                    # pycasmParser.g:117:5: NEWLINE INDENT block ( NEWLINE )? ( DEDENT )? ( DOT_END ( WS )+ ( NAME ) )?
                    NEWLINE26 = self.input.LT(1)
                    self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_directive309)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_NEWLINE.add(NEWLINE26)
                    INDENT27 = self.input.LT(1)
                    self.match(self.input, INDENT, self.FOLLOW_INDENT_in_directive311)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_INDENT.add(INDENT27)
                    self.following.append(self.FOLLOW_block_in_directive313)
                    block28 = self.block()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_block.add(block28.tree)
                    # pycasmParser.g:117:26: ( NEWLINE )?
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if (LA15_0 == NEWLINE) :
                        LA15_1 = self.input.LA(2)

                        if (self.synpred20()) :
                            alt15 = 1
                    if alt15 == 1:
                        # pycasmParser.g:0:0: NEWLINE
                        NEWLINE29 = self.input.LT(1)
                        self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_directive315)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_NEWLINE.add(NEWLINE29)



                    # pycasmParser.g:117:35: ( DEDENT )?
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (LA16_0 == DEDENT) :
                        LA16_1 = self.input.LA(2)

                        if (self.synpred21()) :
                            alt16 = 1
                    if alt16 == 1:
                        # pycasmParser.g:0:0: DEDENT
                        DEDENT30 = self.input.LT(1)
                        self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_directive318)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_DEDENT.add(DEDENT30)



                    # pycasmParser.g:118:5: ( DOT_END ( WS )+ ( NAME ) )?
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if (LA18_0 == DOT_END) :
                        LA18_1 = self.input.LA(2)

                        if (self.synpred23()) :
                            alt18 = 1
                    if alt18 == 1:
                        # pycasmParser.g:118:6: DOT_END ( WS )+ ( NAME )
                        DOT_END31 = self.input.LT(1)
                        self.match(self.input, DOT_END, self.FOLLOW_DOT_END_in_directive326)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_DOT_END.add(DOT_END31)
                        # pycasmParser.g:118:14: ( WS )+
                        cnt17 = 0
                        while True: #loop17
                            alt17 = 2
                            LA17_0 = self.input.LA(1)

                            if (LA17_0 == WS) :
                                alt17 = 1


                            if alt17 == 1:
                                # pycasmParser.g:0:0: WS
                                WS32 = self.input.LT(1)
                                self.match(self.input, WS, self.FOLLOW_WS_in_directive328)
                                if self.failed:
                                    return retval
                                if self.backtracking == 0:
                                    stream_WS.add(WS32)


                            else:
                                if cnt17 >= 1:
                                    break #loop17

                                if self.backtracking > 0:
                                    self.failed = True
                                    return retval

                                eee = EarlyExitException(17, self.input)
                                raise eee

                            cnt17 += 1


                        # pycasmParser.g:119:6: ( NAME )
                        # pycasmParser.g:119:7: NAME
                        NAME33 = self.input.LT(1)
                        self.match(self.input, NAME, self.FOLLOW_NAME_in_directive337)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_NAME.add(NAME33)
                        if self.backtracking == 0:
                                   
                            dh = directive_header25.tree.toString()[1:]
                            if not dh.startswith(NAME33.text):
                            	self.reportError(".end directive must have argument of the same name as directive '"+dh+"', compare with '"+NAME33.text+"'.") # dirty
                            						









                elif alt19 == 2:
                    # pycasmParser.g:127:6: NEWLINE
                    NEWLINE34 = self.input.LT(1)
                    self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_directive366)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_NEWLINE.add(NEWLINE34)






                # AST Rewrite
                # elements: block
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                    root_0 = self.adaptor.nil()
                    # 129:6: -> ^( ( block )? )
                    # pycasmParser.g:129:9: ^( ( block )? )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(directive_header25.tree, root_1)

                    # pycasmParser.g:129:36: ( block )?
                    if stream_block.hasNext():
                        self.adaptor.addChild(root_1, stream_block.next())


                    stream_block.reset();

                    self.adaptor.addChild(root_0, root_1)






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 9, directive_StartIndex)

            pass

        return retval

    # $ANTLR end directive

    class directive_header_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start directive_header
    # pycasmParser.g:132:1: directive_header : DOT_NAME ( DOT_ARGS )? -> ^( DOT_NAME ^( ARGS ( DOT_ARGS )? ) ) ;
    def directive_header(self, ):

        retval = self.directive_header_return()
        retval.start = self.input.LT(1)
        directive_header_StartIndex = self.input.index()
        root_0 = None

        DOT_NAME35 = None
        DOT_ARGS36 = None

        DOT_NAME35_tree = None
        DOT_ARGS36_tree = None
        stream_DOT_NAME = RewriteRuleTokenStream(self.adaptor, "token DOT_NAME")
        stream_DOT_ARGS = RewriteRuleTokenStream(self.adaptor, "token DOT_ARGS")

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 10):
                    return retval

                # pycasmParser.g:133:2: ( DOT_NAME ( DOT_ARGS )? -> ^( DOT_NAME ^( ARGS ( DOT_ARGS )? ) ) )
                # pycasmParser.g:134:3: DOT_NAME ( DOT_ARGS )?
                DOT_NAME35 = self.input.LT(1)
                self.match(self.input, DOT_NAME, self.FOLLOW_DOT_NAME_in_directive_header400)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_DOT_NAME.add(DOT_NAME35)
                # pycasmParser.g:134:12: ( DOT_ARGS )?
                alt20 = 2
                LA20_0 = self.input.LA(1)

                if (LA20_0 == DOT_ARGS) :
                    alt20 = 1
                if alt20 == 1:
                    # pycasmParser.g:0:0: DOT_ARGS
                    DOT_ARGS36 = self.input.LT(1)
                    self.match(self.input, DOT_ARGS, self.FOLLOW_DOT_ARGS_in_directive_header402)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_DOT_ARGS.add(DOT_ARGS36)



                # AST Rewrite
                # elements: DOT_ARGS, DOT_NAME
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                    root_0 = self.adaptor.nil()
                    # 134:22: -> ^( DOT_NAME ^( ARGS ( DOT_ARGS )? ) )
                    # pycasmParser.g:134:25: ^( DOT_NAME ^( ARGS ( DOT_ARGS )? ) )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(stream_DOT_NAME.next(), root_1)

                    # pycasmParser.g:134:36: ^( ARGS ( DOT_ARGS )? )
                    root_2 = self.adaptor.nil()
                    # pycasmParser.g:134:43: ( DOT_ARGS )?
                    if stream_DOT_ARGS.hasNext():
                        self.adaptor.addChild(root_2, stream_DOT_ARGS.next())


                    stream_DOT_ARGS.reset();

                    self.adaptor.addChild(root_1, root_2)

                    self.adaptor.addChild(root_0, root_1)






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 10, directive_header_StartIndex)

            pass

        return retval

    # $ANTLR end directive_header

    class sym_name_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start sym_name
    # pycasmParser.g:137:1: sym_name : NAME -> ^( SYM NAME ) ;
    def sym_name(self, ):

        retval = self.sym_name_return()
        retval.start = self.input.LT(1)
        sym_name_StartIndex = self.input.index()
        root_0 = None

        NAME37 = None

        NAME37_tree = None
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 11):
                    return retval

                # pycasmParser.g:138:2: ( NAME -> ^( SYM NAME ) )
                # pycasmParser.g:139:3: NAME
                NAME37 = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_sym_name429)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_NAME.add(NAME37)
                # AST Rewrite
                # elements: NAME
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                    root_0 = self.adaptor.nil()
                    # 139:8: -> ^( SYM NAME )
                    # pycasmParser.g:139:11: ^( SYM NAME )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(SYM, "SYM"), root_1)

                    self.adaptor.addChild(root_1, stream_NAME.next())

                    self.adaptor.addChild(root_0, root_1)






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 11, sym_name_StartIndex)

            pass

        return retval

    # $ANTLR end sym_name

    class generative_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start generative
    # pycasmParser.g:142:1: generative : (c= STRING | c= TYPED_VALUE ) -> ^() ;
    def generative(self, ):

        retval = self.generative_return()
        retval.start = self.input.LT(1)
        generative_StartIndex = self.input.index()
        root_0 = None

        c = None

        c_tree = None
        stream_TYPED_VALUE = RewriteRuleTokenStream(self.adaptor, "token TYPED_VALUE")
        stream_STRING = RewriteRuleTokenStream(self.adaptor, "token STRING")

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 12):
                    return retval

                # pycasmParser.g:143:2: ( (c= STRING | c= TYPED_VALUE ) -> ^() )
                # pycasmParser.g:144:2: (c= STRING | c= TYPED_VALUE )
                # pycasmParser.g:144:2: (c= STRING | c= TYPED_VALUE )
                alt21 = 2
                LA21_0 = self.input.LA(1)

                if (LA21_0 == STRING) :
                    alt21 = 1
                elif (LA21_0 == TYPED_VALUE) :
                    alt21 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("144:2: (c= STRING | c= TYPED_VALUE )", 21, 0, self.input)

                    raise nvae

                if alt21 == 1:
                    # pycasmParser.g:145:3: c= STRING
                    c = self.input.LT(1)
                    self.match(self.input, STRING, self.FOLLOW_STRING_in_generative455)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_STRING.add(c)


                elif alt21 == 2:
                    # pycasmParser.g:146:4: c= TYPED_VALUE
                    c = self.input.LT(1)
                    self.match(self.input, TYPED_VALUE, self.FOLLOW_TYPED_VALUE_in_generative462)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_TYPED_VALUE.add(c)



                # AST Rewrite
                # elements: 
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                    root_0 = self.adaptor.nil()
                    # 147:4: -> ^()
                    # pycasmParser.g:147:7: ^()
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.create(GEN, c.text), root_1)

                    self.adaptor.addChild(root_0, root_1)






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 12, generative_StartIndex)

            pass

        return retval

    # $ANTLR end generative

    class hex_code_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start hex_code
    # pycasmParser.g:150:1: hex_code : (h= HEX_PAIR | h= HEX_QUAD | h= HEX_DQUAD ) -> ^() ;
    def hex_code(self, ):

        retval = self.hex_code_return()
        retval.start = self.input.LT(1)
        hex_code_StartIndex = self.input.index()
        root_0 = None

        h = None

        h_tree = None
        stream_HEX_DQUAD = RewriteRuleTokenStream(self.adaptor, "token HEX_DQUAD")
        stream_HEX_QUAD = RewriteRuleTokenStream(self.adaptor, "token HEX_QUAD")
        stream_HEX_PAIR = RewriteRuleTokenStream(self.adaptor, "token HEX_PAIR")

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 13):
                    return retval

                # pycasmParser.g:150:9: ( (h= HEX_PAIR | h= HEX_QUAD | h= HEX_DQUAD ) -> ^() )
                # pycasmParser.g:151:2: (h= HEX_PAIR | h= HEX_QUAD | h= HEX_DQUAD )
                # pycasmParser.g:151:2: (h= HEX_PAIR | h= HEX_QUAD | h= HEX_DQUAD )
                alt22 = 3
                LA22 = self.input.LA(1)
                if LA22 == HEX_PAIR:
                    alt22 = 1
                elif LA22 == HEX_QUAD:
                    alt22 = 2
                elif LA22 == HEX_DQUAD:
                    alt22 = 3
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("151:2: (h= HEX_PAIR | h= HEX_QUAD | h= HEX_DQUAD )", 22, 0, self.input)

                    raise nvae

                if alt22 == 1:
                    # pycasmParser.g:151:4: h= HEX_PAIR
                    h = self.input.LT(1)
                    self.match(self.input, HEX_PAIR, self.FOLLOW_HEX_PAIR_in_hex_code485)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_HEX_PAIR.add(h)


                elif alt22 == 2:
                    # pycasmParser.g:152:4: h= HEX_QUAD
                    h = self.input.LT(1)
                    self.match(self.input, HEX_QUAD, self.FOLLOW_HEX_QUAD_in_hex_code492)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_HEX_QUAD.add(h)


                elif alt22 == 3:
                    # pycasmParser.g:153:4: h= HEX_DQUAD
                    h = self.input.LT(1)
                    self.match(self.input, HEX_DQUAD, self.FOLLOW_HEX_DQUAD_in_hex_code499)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_HEX_DQUAD.add(h)



                # AST Rewrite
                # elements: 
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                    root_0 = self.adaptor.nil()
                    # 155:4: -> ^()
                    # pycasmParser.g:155:7: ^()
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.create(HEX, h.text), root_1)

                    self.adaptor.addChild(root_0, root_1)






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 13, hex_code_StartIndex)

            pass

        return retval

    # $ANTLR end hex_code

    # $ANTLR start synpred1
    def synpred1_fragment(self, ):
        # pycasmParser.g:66:4: ( block )
        # pycasmParser.g:66:4: block
        self.following.append(self.FOLLOW_block_in_synpred175)
        self.block()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred1



    # $ANTLR start synpred3
    def synpred3_fragment(self, ):
        # pycasmParser.g:66:11: ( ( sp )+ )
        # pycasmParser.g:66:11: ( sp )+
        # pycasmParser.g:66:11: ( sp )+
        cnt23 = 0
        while True: #loop23
            alt23 = 2
            LA23_0 = self.input.LA(1)

            if ((WS <= LA23_0 <= NEWLINE)) :
                alt23 = 1


            if alt23 == 1:
                # pycasmParser.g:0:0: sp
                self.following.append(self.FOLLOW_sp_in_synpred378)
                self.sp()
                self.following.pop()
                if self.failed:
                    return 


            else:
                if cnt23 >= 1:
                    break #loop23

                if self.backtracking > 0:
                    self.failed = True
                    return 

                eee = EarlyExitException(23, self.input)
                raise eee

            cnt23 += 1




    # $ANTLR end synpred3



    # $ANTLR start synpred4
    def synpred4_fragment(self, ):
        # pycasmParser.g:71:4: ( WS )
        # pycasmParser.g:71:4: WS
        self.match(self.input, WS, self.FOLLOW_WS_in_synpred4107)
        if self.failed:
            return 


    # $ANTLR end synpred4



    # $ANTLR start synpred5
    def synpred5_fragment(self, ):
        # pycasmParser.g:71:7: ( NEWLINE )
        # pycasmParser.g:71:7: NEWLINE
        self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_synpred5109)
        if self.failed:
            return 


    # $ANTLR end synpred5



    # $ANTLR start synpred6
    def synpred6_fragment(self, ):
        # pycasmParser.g:77:3: ( block_chain )
        # pycasmParser.g:77:3: block_chain
        self.following.append(self.FOLLOW_block_chain_in_synpred6132)
        self.block_chain()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred6



    # $ANTLR start synpred8
    def synpred8_fragment(self, ):
        # pycasmParser.g:90:3: ( space_element )
        # pycasmParser.g:90:3: space_element
        self.following.append(self.FOLLOW_space_element_in_synpred8183)
        self.space_element()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred8



    # $ANTLR start synpred9
    def synpred9_fragment(self, ):
        # pycasmParser.g:90:18: ( chain_element )
        # pycasmParser.g:90:18: chain_element
        self.following.append(self.FOLLOW_chain_element_in_synpred9186)
        self.chain_element()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred9



    # $ANTLR start synpred12
    def synpred12_fragment(self, ):
        # pycasmParser.g:101:3: ( directive )
        # pycasmParser.g:101:3: directive
        self.following.append(self.FOLLOW_directive_in_synpred12221)
        self.directive()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred12



    # $ANTLR start synpred15
    def synpred15_fragment(self, ):
        # pycasmParser.g:103:27: ( NEWLINE )
        # pycasmParser.g:103:27: NEWLINE
        self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_synpred15239)
        if self.failed:
            return 


    # $ANTLR end synpred15



    # $ANTLR start synpred16
    def synpred16_fragment(self, ):
        # pycasmParser.g:103:36: ( DEDENT )
        # pycasmParser.g:103:36: DEDENT
        self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_synpred16242)
        if self.failed:
            return 


    # $ANTLR end synpred16



    # $ANTLR start synpred17
    def synpred17_fragment(self, ):
        # pycasmParser.g:103:4: ( ( NEWLINE )? INDENT block ( NEWLINE )? ( DEDENT )? )
        # pycasmParser.g:103:4: ( NEWLINE )? INDENT block ( NEWLINE )? ( DEDENT )?
        # pycasmParser.g:103:4: ( NEWLINE )?
        alt24 = 2
        LA24_0 = self.input.LA(1)

        if (LA24_0 == NEWLINE) :
            alt24 = 1
        if alt24 == 1:
            # pycasmParser.g:0:0: NEWLINE
            self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_synpred17231)
            if self.failed:
                return 



        self.match(self.input, INDENT, self.FOLLOW_INDENT_in_synpred17234)
        if self.failed:
            return 
        self.following.append(self.FOLLOW_block_in_synpred17237)
        self.block()
        self.following.pop()
        if self.failed:
            return 
        # pycasmParser.g:103:27: ( NEWLINE )?
        alt25 = 2
        LA25_0 = self.input.LA(1)

        if (LA25_0 == NEWLINE) :
            alt25 = 1
        if alt25 == 1:
            # pycasmParser.g:0:0: NEWLINE
            self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_synpred17239)
            if self.failed:
                return 



        # pycasmParser.g:103:42: ( DEDENT )?
        alt26 = 2
        LA26_0 = self.input.LA(1)

        if (LA26_0 == DEDENT) :
            alt26 = 1
        if alt26 == 1:
            # pycasmParser.g:0:0: DEDENT
            self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_synpred17242)
            if self.failed:
                return 





    # $ANTLR end synpred17



    # $ANTLR start synpred20
    def synpred20_fragment(self, ):
        # pycasmParser.g:117:26: ( NEWLINE )
        # pycasmParser.g:117:26: NEWLINE
        self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_synpred20315)
        if self.failed:
            return 


    # $ANTLR end synpred20



    # $ANTLR start synpred21
    def synpred21_fragment(self, ):
        # pycasmParser.g:117:35: ( DEDENT )
        # pycasmParser.g:117:35: DEDENT
        self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_synpred21318)
        if self.failed:
            return 


    # $ANTLR end synpred21



    # $ANTLR start synpred23
    def synpred23_fragment(self, ):
        # pycasmParser.g:118:6: ( DOT_END ( WS )+ ( NAME ) )
        # pycasmParser.g:118:6: DOT_END ( WS )+ ( NAME )
        self.match(self.input, DOT_END, self.FOLLOW_DOT_END_in_synpred23326)
        if self.failed:
            return 
        # pycasmParser.g:118:14: ( WS )+
        cnt27 = 0
        while True: #loop27
            alt27 = 2
            LA27_0 = self.input.LA(1)

            if (LA27_0 == WS) :
                alt27 = 1


            if alt27 == 1:
                # pycasmParser.g:0:0: WS
                self.match(self.input, WS, self.FOLLOW_WS_in_synpred23328)
                if self.failed:
                    return 


            else:
                if cnt27 >= 1:
                    break #loop27

                if self.backtracking > 0:
                    self.failed = True
                    return 

                eee = EarlyExitException(27, self.input)
                raise eee

            cnt27 += 1


        # pycasmParser.g:119:6: ( NAME )
        # pycasmParser.g:119:7: NAME
        self.match(self.input, NAME, self.FOLLOW_NAME_in_synpred23337)
        if self.failed:
            return 





    # $ANTLR end synpred23



    # $ANTLR start synpred25
    def synpred25_fragment(self, ):
        # pycasmParser.g:127:6: ( NEWLINE )
        # pycasmParser.g:127:6: NEWLINE
        self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_synpred25366)
        if self.failed:
            return 


    # $ANTLR end synpred25



    def synpred5(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred5_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred6(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred6_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred8(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred8_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred1(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred1_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred3(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred3_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred4(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred4_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred20(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred20_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred9(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred9_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred15(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred15_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred25(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred25_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred16(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred16_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred17(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred17_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred23(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred23_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred12(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred12_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred21(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred21_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success



 

    FOLLOW_block_in_root75 = frozenset([])
    FOLLOW_sp_in_root78 = frozenset([7, 8])
    FOLLOW_EOF_in_root83 = frozenset([1])
    FOLLOW_WS_in_sp107 = frozenset([1, 7, 8])
    FOLLOW_NEWLINE_in_sp109 = frozenset([1, 7, 8])
    FOLLOW_block_head_in_block128 = frozenset([1, 7, 8, 9, 11, 16])
    FOLLOW_block_chain_in_block132 = frozenset([1, 7, 8, 9, 11, 16])
    FOLLOW_chain_element_in_block_head165 = frozenset([1])
    FOLLOW_block_chain_in_block_head170 = frozenset([1])
    FOLLOW_space_element_in_block_chain183 = frozenset([1, 7, 8, 9, 11, 15, 16, 18, 19, 20, 21, 22])
    FOLLOW_chain_element_in_block_chain186 = frozenset([1])
    FOLLOW_sym_name_in_chain_element198 = frozenset([1])
    FOLLOW_generative_in_chain_element203 = frozenset([1])
    FOLLOW_hex_code_in_chain_element208 = frozenset([1])
    FOLLOW_directive_in_space_element221 = frozenset([1])
    FOLLOW_unrestricted_directive_in_space_element226 = frozenset([1])
    FOLLOW_NEWLINE_in_space_element231 = frozenset([9])
    FOLLOW_INDENT_in_space_element234 = frozenset([7, 8, 9, 11, 15, 16, 18, 19, 20, 21, 22])
    FOLLOW_block_in_space_element237 = frozenset([1, 8, 10])
    FOLLOW_NEWLINE_in_space_element239 = frozenset([1, 10])
    FOLLOW_DEDENT_in_space_element242 = frozenset([1])
    FOLLOW_sp_in_space_element249 = frozenset([1])
    FOLLOW_DOT_DOT_NAME_in_unrestricted_directive262 = frozenset([1, 12, 13])
    FOLLOW_DOT_DOT_ARGS_in_unrestricted_directive264 = frozenset([1, 13])
    FOLLOW_DOT_DOT_BODY_in_unrestricted_directive267 = frozenset([1])
    FOLLOW_directive_header_in_directive303 = frozenset([1, 8])
    FOLLOW_NEWLINE_in_directive309 = frozenset([9])
    FOLLOW_INDENT_in_directive311 = frozenset([7, 8, 9, 11, 15, 16, 18, 19, 20, 21, 22])
    FOLLOW_block_in_directive313 = frozenset([1, 8, 10, 14])
    FOLLOW_NEWLINE_in_directive315 = frozenset([1, 10, 14])
    FOLLOW_DEDENT_in_directive318 = frozenset([1, 14])
    FOLLOW_DOT_END_in_directive326 = frozenset([7])
    FOLLOW_WS_in_directive328 = frozenset([7, 15])
    FOLLOW_NAME_in_directive337 = frozenset([1])
    FOLLOW_NEWLINE_in_directive366 = frozenset([1])
    FOLLOW_DOT_NAME_in_directive_header400 = frozenset([1, 17])
    FOLLOW_DOT_ARGS_in_directive_header402 = frozenset([1])
    FOLLOW_NAME_in_sym_name429 = frozenset([1])
    FOLLOW_STRING_in_generative455 = frozenset([1])
    FOLLOW_TYPED_VALUE_in_generative462 = frozenset([1])
    FOLLOW_HEX_PAIR_in_hex_code485 = frozenset([1])
    FOLLOW_HEX_QUAD_in_hex_code492 = frozenset([1])
    FOLLOW_HEX_DQUAD_in_hex_code499 = frozenset([1])
    FOLLOW_block_in_synpred175 = frozenset([1])
    FOLLOW_sp_in_synpred378 = frozenset([1, 7, 8])
    FOLLOW_WS_in_synpred4107 = frozenset([1])
    FOLLOW_NEWLINE_in_synpred5109 = frozenset([1])
    FOLLOW_block_chain_in_synpred6132 = frozenset([1])
    FOLLOW_space_element_in_synpred8183 = frozenset([1])
    FOLLOW_chain_element_in_synpred9186 = frozenset([1])
    FOLLOW_directive_in_synpred12221 = frozenset([1])
    FOLLOW_NEWLINE_in_synpred15239 = frozenset([1])
    FOLLOW_DEDENT_in_synpred16242 = frozenset([1])
    FOLLOW_NEWLINE_in_synpred17231 = frozenset([9])
    FOLLOW_INDENT_in_synpred17234 = frozenset([7, 8, 9, 11, 15, 16, 18, 19, 20, 21, 22])
    FOLLOW_block_in_synpred17237 = frozenset([1, 8, 10])
    FOLLOW_NEWLINE_in_synpred17239 = frozenset([1, 10])
    FOLLOW_DEDENT_in_synpred17242 = frozenset([1])
    FOLLOW_NEWLINE_in_synpred20315 = frozenset([1])
    FOLLOW_DEDENT_in_synpred21318 = frozenset([1])
    FOLLOW_DOT_END_in_synpred23326 = frozenset([7])
    FOLLOW_WS_in_synpred23328 = frozenset([7, 15])
    FOLLOW_NAME_in_synpred23337 = frozenset([1])
    FOLLOW_NEWLINE_in_synpred25366 = frozenset([1])

