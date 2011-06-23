# $ANTLR 3.0.1 /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g 2011-06-23 12:22:35

from antlr3 import *
from antlr3.compat import set, frozenset
         
import decimal
infinity = decimal.Decimal('Infinity')



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
Alpha=15
DOT_DOT_BODY=19
Type=25
DOT_DOT_NAME=12
DOT_DOT_ARGS=17
AlphaNum=30
TYPED_VALUE=26
DOT_END=9
HexAlpha=31
HEX_DIGIT=23
DEDENT=4
Digit=29
HEX_DQUAD=21
Tokens=32
EOF=-1
HexDigit=24
INDENT=5
NAME=10
WS=13
NonWS=18
BLOCK=6
ARGS=7
GEN=8
DOT_NAME=11
INDENT_OR_DEDENT=28
COMMENT=14
HEX_QUAD=20
DOT_ARGS=16
STRING=27
HEX_PAIR=22

class pycasmLexerLexer(Lexer):

    grammarFileName = "/root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g"

    def __init__(self, input=None):
        Lexer.__init__(self, input)
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
        self.dfa18 = self.DFA18(
            self, 18,
            eot = self.DFA18_eot,
            eof = self.DFA18_eof,
            min = self.DFA18_min,
            max = self.DFA18_max,
            accept = self.DFA18_accept,
            special = self.DFA18_special,
            transition = self.DFA18_transition
            )
        self.dfa21 = self.DFA21(
            self, 21,
            eot = self.DFA21_eot,
            eof = self.DFA21_eof,
            min = self.DFA21_min,
            max = self.DFA21_max,
            accept = self.DFA21_accept,
            special = self.DFA21_special,
            transition = self.DFA21_transition
            )


               
        # INDENT-DEDENT generation.
        self.indentStack = []
        self.numberOfSpaces = 0
        self.tokens = []
        self.lookBehindToken = None
        from pycasm.syntax.errors import StandardErrorReporter
        self.patchInErrorReporter(StandardErrorReporter())



              
    def getColumn(self):
    	return self.getCharPositionInLine()
    	#return self._state.tokenStartCharPositionInLine # is it different?
    
    # Emit multiple tokens at once.
    def emit(self, token=None):
    	Lexer.emit(self, token)
    	self.tokens.append(self._state.token) # token may be None but not the self._state.token
    	self.lookBehindToken = self._state.token
    
    def nextToken(self):
    	Lexer.nextToken(self)
    	try:
    		return self.tokens.pop(0)
    	except IndexError:
    		return EOF_TOKEN
    
    # Error handling
    def patchInErrorReporter(self, reporterObject):
    	'''
    	Applies monkey patch to overload error reporting methods, all reporterObject\'s methods overload methods of this recognizer.
    	Not too pythonic, but handy.
    	'''
    	import functools
    	[setattr(self, method, functools.partial(getattr(reporterObject,method).im_func, self) ) for method in dir(reporterObject)\
                                    if callable(getattr(reporterObject, method))]
    



    # $ANTLR start DOT_END
    def mDOT_END(self, ):

        try:
            self.type = DOT_END

            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:87:2: ( '.end' )
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:88:3: '.end'
            self.match(".end")






        finally:

            pass

    # $ANTLR end DOT_END



    # $ANTLR start DOT_NAME
    def mDOT_NAME(self, ):

        try:
            self.type = DOT_NAME

            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:92:2: ( '.' NAME )
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:93:3: '.' NAME
            self.match(u'.')

            self.mNAME()





        finally:

            pass

    # $ANTLR end DOT_NAME



    # $ANTLR start DOT_DOT_NAME
    def mDOT_DOT_NAME(self, ):

        try:
            self.type = DOT_DOT_NAME

            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:97:2: ( '..' NAME )
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:98:3: '..' NAME
            self.match("..")


            self.mNAME()





        finally:

            pass

    # $ANTLR end DOT_DOT_NAME



    # $ANTLR start COMMENT
    def mCOMMENT(self, ):

        try:
            self.type = COMMENT

                   
            self.channel=HIDDEN

            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:105:2: ({...}? => ( WS )* '#' (~ '\\n' )* ( '\\n' )* | {...}? => ( WS )* '#' (~ '\\n' )* )
            alt6 = 2
            alt6 = self.dfa6.predict(self.input)
            if alt6 == 1:
                # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:105:7: {...}? => ( WS )* '#' (~ '\\n' )* ( '\\n' )*
                if not (self.getColumn() == 0):
                    raise FailedPredicateException(self.input, "COMMENT", "self.getColumn() == 0")

                # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:105:35: ( WS )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == u'\t' or LA1_0 == u' ') :
                        alt1 = 1


                    if alt1 == 1:
                        # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:105:35: WS
                        self.mWS()



                    else:
                        break #loop1


                self.match(u'#')

                # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:105:43: (~ '\\n' )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if ((u'\u0000' <= LA2_0 <= u'\t') or (u'\u000B' <= LA2_0 <= u'\uFFFE')) :
                        alt2 = 1


                    if alt2 == 1:
                        # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:105:44: ~ '\\n'
                        if (u'\u0000' <= self.input.LA(1) <= u'\t') or (u'\u000B' <= self.input.LA(1) <= u'\uFFFE'):
                            self.input.consume();

                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse




                    else:
                        break #loop2


                # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:105:52: ( '\\n' )*
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == u'\n') :
                        alt3 = 1


                    if alt3 == 1:
                        # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:105:52: '\\n'
                        self.match(u'\n')



                    else:
                        break #loop3




            elif alt6 == 2:
                # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:106:7: {...}? => ( WS )* '#' (~ '\\n' )*
                if not (self.getColumn() > 0 ):
                    raise FailedPredicateException(self.input, "COMMENT", "self.getColumn() > 0 ")

                # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:106:35: ( WS )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == u'\t' or LA4_0 == u' ') :
                        alt4 = 1


                    if alt4 == 1:
                        # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:106:35: WS
                        self.mWS()



                    else:
                        break #loop4


                self.match(u'#')

                # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:106:43: (~ '\\n' )*
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if ((u'\u0000' <= LA5_0 <= u'\t') or (u'\u000B' <= LA5_0 <= u'\uFFFE')) :
                        alt5 = 1


                    if alt5 == 1:
                        # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:106:44: ~ '\\n'
                        if (u'\u0000' <= self.input.LA(1) <= u'\t') or (u'\u000B' <= self.input.LA(1) <= u'\uFFFE'):
                            self.input.consume();

                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse




                    else:
                        break #loop5





        finally:

            pass

    # $ANTLR end COMMENT



    # $ANTLR start DOT_ARGS
    def mDOT_ARGS(self, ):

        try:
            self.type = DOT_ARGS

            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:110:2: ({...}? =>~ ( Alpha | '\\n' | '\\r' ) (~ ( '\\n' | '\\r' | '#' ) )+ )
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:111:2: {...}? =>~ ( Alpha | '\\n' | '\\r' ) (~ ( '\\n' | '\\r' | '#' ) )+
            if not (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     ):
                raise FailedPredicateException(self.input, "DOT_ARGS", " self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     ")

            if (u'\u0000' <= self.input.LA(1) <= u'\t') or (u'\u000B' <= self.input.LA(1) <= u'\f') or (u'\u000E' <= self.input.LA(1) <= u'@') or (u'[' <= self.input.LA(1) <= u'`') or (u'{' <= self.input.LA(1) <= u'\uFFFE'):
                self.input.consume();

            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse


            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:111:102: (~ ( '\\n' | '\\r' | '#' ) )+
            cnt7 = 0
            while True: #loop7
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if ((u'\u0000' <= LA7_0 <= u'\t') or (u'\u000B' <= LA7_0 <= u'\f') or (u'\u000E' <= LA7_0 <= u'"') or (u'$' <= LA7_0 <= u'\uFFFE')) :
                    alt7 = 1


                if alt7 == 1:
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:111:102: ~ ( '\\n' | '\\r' | '#' )
                    if (u'\u0000' <= self.input.LA(1) <= u'\t') or (u'\u000B' <= self.input.LA(1) <= u'\f') or (u'\u000E' <= self.input.LA(1) <= u'"') or (u'$' <= self.input.LA(1) <= u'\uFFFE'):
                        self.input.consume();

                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    if cnt7 >= 1:
                        break #loop7

                    eee = EarlyExitException(7, self.input)
                    raise eee

                cnt7 += 1






        finally:

            pass

    # $ANTLR end DOT_ARGS



    # $ANTLR start DOT_DOT_ARGS
    def mDOT_DOT_ARGS(self, ):

        try:
            self.type = DOT_DOT_ARGS

            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:115:2: ({...}? =>~ ( Alpha | '\\n' | '\\r' ) (~ ( '\\n' | '\\r' | '#' ) )+ )
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:116:2: {...}? =>~ ( Alpha | '\\n' | '\\r' ) (~ ( '\\n' | '\\r' | '#' ) )+
            if not (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] ):
                raise FailedPredicateException(self.input, "DOT_DOT_ARGS", " self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] ")

            if (u'\u0000' <= self.input.LA(1) <= u'\t') or (u'\u000B' <= self.input.LA(1) <= u'\f') or (u'\u000E' <= self.input.LA(1) <= u'@') or (u'[' <= self.input.LA(1) <= u'`') or (u'{' <= self.input.LA(1) <= u'\uFFFE'):
                self.input.consume();

            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse


            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:116:102: (~ ( '\\n' | '\\r' | '#' ) )+
            cnt8 = 0
            while True: #loop8
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if ((u'\u0000' <= LA8_0 <= u'\t') or (u'\u000B' <= LA8_0 <= u'\f') or (u'\u000E' <= LA8_0 <= u'"') or (u'$' <= LA8_0 <= u'\uFFFE')) :
                    alt8 = 1


                if alt8 == 1:
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:116:102: ~ ( '\\n' | '\\r' | '#' )
                    if (u'\u0000' <= self.input.LA(1) <= u'\t') or (u'\u000B' <= self.input.LA(1) <= u'\f') or (u'\u000E' <= self.input.LA(1) <= u'"') or (u'$' <= self.input.LA(1) <= u'\uFFFE'):
                        self.input.consume();

                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    if cnt8 >= 1:
                        break #loop8

                    eee = EarlyExitException(8, self.input)
                    raise eee

                cnt8 += 1






        finally:

            pass

    # $ANTLR end DOT_DOT_ARGS



    # $ANTLR start DOT_DOT_BODY
    def mDOT_DOT_BODY(self, ):

        try:
            self.type = DOT_DOT_BODY

                   
            self.numberOfSpacesInPythonBlock = 0
            self.minNumberOfSpacesInPythonBlock = infinity

            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:124:2: ({...}? => ( ( '\\r' )? '\\n' ( ' ' | '\\t' )* ({...}? => ( NonWS ( NonWS | WS )* ) )? )* )
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:124:4: {...}? => ( ( '\\r' )? '\\n' ( ' ' | '\\t' )* ({...}? => ( NonWS ( NonWS | WS )* ) )? )*
            if not (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME, DOT_DOT_ARGS] ):
                raise FailedPredicateException(self.input, "DOT_DOT_BODY", " self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME, DOT_DOT_ARGS] ")

            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:125:3: ( ( '\\r' )? '\\n' ( ' ' | '\\t' )* ({...}? => ( NonWS ( NonWS | WS )* ) )? )*
            while True: #loop13
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if (LA13_0 == u'\n' or LA13_0 == u'\r') :
                    alt13 = 1


                if alt13 == 1:
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:125:4: ( '\\r' )? '\\n' ( ' ' | '\\t' )* ({...}? => ( NonWS ( NonWS | WS )* ) )?
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:125:4: ( '\\r' )?
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == u'\r') :
                        alt9 = 1
                    if alt9 == 1:
                        # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:125:4: '\\r'
                        self.match(u'\r')




                    self.match(u'\n')

                    #action start
                    self.numberOfSpacesInPythonBlock = 0 
                    #action end
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:127:7: ( ' ' | '\\t' )*
                    while True: #loop10
                        alt10 = 3
                        LA10_0 = self.input.LA(1)

                        if (LA10_0 == u' ') :
                            alt10 = 1
                        elif (LA10_0 == u'\t') :
                            alt10 = 2


                        if alt10 == 1:
                            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:128:5: ' '
                            self.match(u' ')

                            #action start
                            self.numberOfSpacesInPythonBlock += 1 
                            #action end


                        elif alt10 == 2:
                            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:129:5: '\\t'
                            self.match(u'\t')

                            #action start
                            self.numberOfSpacesInPythonBlock += 8 
                            #action end


                        else:
                            break #loop10


                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:131:7: ({...}? => ( NonWS ( NonWS | WS )* ) )?
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if ((u'\u0000' <= LA12_0 <= u'\b') or (u'\u000B' <= LA12_0 <= u'\f') or (u'\u000E' <= LA12_0 <= u'\u001F') or (u'!' <= LA12_0 <= u'\uFFFE')) and (min(self.minNumberOfSpacesInPythonBlock, self.numberOfSpacesInPythonBlock) > self.numberOfSpaces ):
                        alt12 = 1
                    if alt12 == 1:
                        # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:132:4: {...}? => ( NonWS ( NonWS | WS )* )
                        if not (min(self.minNumberOfSpacesInPythonBlock, self.numberOfSpacesInPythonBlock) > self.numberOfSpaces ):
                            raise FailedPredicateException(self.input, "DOT_DOT_BODY", " min(self.minNumberOfSpacesInPythonBlock, self.numberOfSpacesInPythonBlock) > self.numberOfSpaces ")

                        # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:132:109: ( NonWS ( NonWS | WS )* )
                        # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:133:5: NonWS ( NonWS | WS )*
                        self.mNonWS()

                        # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:133:11: ( NonWS | WS )*
                        while True: #loop11
                            alt11 = 2
                            LA11_0 = self.input.LA(1)

                            if ((u'\u0000' <= LA11_0 <= u'\t') or (u'\u000B' <= LA11_0 <= u'\f') or (u'\u000E' <= LA11_0 <= u'\uFFFE')) :
                                alt11 = 1


                            if alt11 == 1:
                                # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:
                                if (u'\u0000' <= self.input.LA(1) <= u'\t') or (u'\u000B' <= self.input.LA(1) <= u'\f') or (u'\u000E' <= self.input.LA(1) <= u'\uFFFE'):
                                    self.input.consume();

                                else:
                                    mse = MismatchedSetException(None, self.input)
                                    self.recover(mse)
                                    raise mse




                            else:
                                break #loop11


                        #action start
                        self.minNumberOfSpacesInPythonBlock = min(self.minNumberOfSpacesInPythonBlock, self.numberOfSpacesInPythonBlock) 
                        #action end








                else:
                    break #loop13






        finally:

            pass

    # $ANTLR end DOT_DOT_BODY



    # $ANTLR start HEX_DQUAD
    def mHEX_DQUAD(self, ):

        try:
            self.type = HEX_DQUAD

            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:141:2: ( HEX_QUAD HEX_QUAD )
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:142:3: HEX_QUAD HEX_QUAD
            self.mHEX_QUAD()

            self.mHEX_QUAD()





        finally:

            pass

    # $ANTLR end HEX_DQUAD



    # $ANTLR start HEX_QUAD
    def mHEX_QUAD(self, ):

        try:
            self.type = HEX_QUAD

            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:146:2: ( HEX_PAIR HEX_PAIR )
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:147:3: HEX_PAIR HEX_PAIR
            self.mHEX_PAIR()

            self.mHEX_PAIR()





        finally:

            pass

    # $ANTLR end HEX_QUAD



    # $ANTLR start HEX_PAIR
    def mHEX_PAIR(self, ):

        try:
            self.type = HEX_PAIR

            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:151:2: ( HEX_DIGIT HEX_DIGIT )
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:152:3: HEX_DIGIT HEX_DIGIT
            self.mHEX_DIGIT()

            self.mHEX_DIGIT()





        finally:

            pass

    # $ANTLR end HEX_PAIR



    # $ANTLR start HEX_DIGIT
    def mHEX_DIGIT(self, ):

        try:
            self.type = HEX_DIGIT

            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:156:2: ( HexDigit )
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:157:3: HexDigit
            self.mHexDigit()





        finally:

            pass

    # $ANTLR end HEX_DIGIT



    # $ANTLR start TYPED_VALUE
    def mTYPED_VALUE(self, ):

        try:
            self.type = TYPED_VALUE

            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:168:2: ( Type '\\'' (~ ( '\\'' ) )* '\\'' )
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:169:3: Type '\\'' (~ ( '\\'' ) )* '\\''
            self.mType()

            self.match(u'\'')

            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:169:13: (~ ( '\\'' ) )*
            while True: #loop14
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if ((u'\u0000' <= LA14_0 <= u'&') or (u'(' <= LA14_0 <= u'\uFFFE')) :
                    alt14 = 1


                if alt14 == 1:
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:169:13: ~ ( '\\'' )
                    if (u'\u0000' <= self.input.LA(1) <= u'&') or (u'(' <= self.input.LA(1) <= u'\uFFFE'):
                        self.input.consume();

                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop14


            self.match(u'\'')





        finally:

            pass

    # $ANTLR end TYPED_VALUE



    # $ANTLR start STRING
    def mSTRING(self, ):

        try:
            self.type = STRING

            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:173:2: ( '\\'' (~ ( '\\'' ) )+ '\\'' )
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:173:4: '\\'' (~ ( '\\'' ) )+ '\\''
            self.match(u'\'')

            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:173:9: (~ ( '\\'' ) )+
            cnt15 = 0
            while True: #loop15
                alt15 = 2
                LA15_0 = self.input.LA(1)

                if ((u'\u0000' <= LA15_0 <= u'&') or (u'(' <= LA15_0 <= u'\uFFFE')) :
                    alt15 = 1


                if alt15 == 1:
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:173:9: ~ ( '\\'' )
                    if (u'\u0000' <= self.input.LA(1) <= u'&') or (u'(' <= self.input.LA(1) <= u'\uFFFE'):
                        self.input.consume();

                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    if cnt15 >= 1:
                        break #loop15

                    eee = EarlyExitException(15, self.input)
                    raise eee

                cnt15 += 1


            self.match(u'\'')





        finally:

            pass

    # $ANTLR end STRING



    # $ANTLR start NAME
    def mNAME(self, ):

        try:
            self.type = NAME

            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:176:6: ( ( Alpha | '_' )+ )
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:177:3: ( Alpha | '_' )+
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:177:3: ( Alpha | '_' )+
            cnt16 = 0
            while True: #loop16
                alt16 = 2
                LA16_0 = self.input.LA(1)

                if ((u'A' <= LA16_0 <= u'Z') or LA16_0 == u'_' or (u'a' <= LA16_0 <= u'z')) :
                    alt16 = 1


                if alt16 == 1:
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:
                    if (u'A' <= self.input.LA(1) <= u'Z') or self.input.LA(1) == u'_' or (u'a' <= self.input.LA(1) <= u'z'):
                        self.input.consume();

                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    if cnt16 >= 1:
                        break #loop16

                    eee = EarlyExitException(16, self.input)
                    raise eee

                cnt16 += 1






        finally:

            pass

    # $ANTLR end NAME



    # $ANTLR start INDENT_OR_DEDENT
    def mINDENT_OR_DEDENT(self, ):

        try:
            self.type = INDENT_OR_DEDENT

                   
            self.numberOfSpaces = 0

            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:184:2: ( ( ( ( '\\r' )? '\\n' ) | '\\t' | ' ' )* ( ( '\\r' )? '\\n' ) ( ' ' | '\\t' )* )
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:185:3: ( ( ( '\\r' )? '\\n' ) | '\\t' | ' ' )* ( ( '\\r' )? '\\n' ) ( ' ' | '\\t' )*
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:185:3: ( ( ( '\\r' )? '\\n' ) | '\\t' | ' ' )*
            while True: #loop18
                alt18 = 4
                alt18 = self.dfa18.predict(self.input)
                if alt18 == 1:
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:185:5: ( ( '\\r' )? '\\n' )
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:185:5: ( ( '\\r' )? '\\n' )
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:185:7: ( '\\r' )? '\\n'
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:185:7: ( '\\r' )?
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if (LA17_0 == u'\r') :
                        alt17 = 1
                    if alt17 == 1:
                        # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:185:8: '\\r'
                        self.match(u'\r')




                    self.match(u'\n')






                elif alt18 == 2:
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:185:24: '\\t'
                    self.match(u'\t')



                elif alt18 == 3:
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:185:31: ' '
                    self.match(u' ')



                else:
                    break #loop18


            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:186:3: ( ( '\\r' )? '\\n' )
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:186:5: ( '\\r' )? '\\n'
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:186:5: ( '\\r' )?
            alt19 = 2
            LA19_0 = self.input.LA(1)

            if (LA19_0 == u'\r') :
                alt19 = 1
            if alt19 == 1:
                # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:186:6: '\\r'
                self.match(u'\r')




            self.match(u'\n')




            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:187:3: ( ' ' | '\\t' )*
            while True: #loop20
                alt20 = 3
                LA20_0 = self.input.LA(1)

                if (LA20_0 == u' ') :
                    alt20 = 1
                elif (LA20_0 == u'\t') :
                    alt20 = 2


                if alt20 == 1:
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:187:5: ' '
                    self.match(u' ')

                    #action start
                    self.numberOfSpaces += 1 
                    #action end


                elif alt20 == 2:
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:188:5: '\\t'
                    self.match(u'\t')

                    #action start
                              
                    self.numberOfSpaces += 8 
                    self.numberOfSpaces -= (self.numberOfSpaces % 8)
                    			
                    #action end


                else:
                    break #loop20


            #action start
              
            		
            self.emit(ClassicToken(NEWLINE, '\n'))
            
            if self.numberOfSpaces!=0 and (len(self.indentStack)==0 or self.numberOfSpaces > self.indentStack[-1]):
            	t = ClassicToken(INDENT, '>')
            	t.setCharPositionInLine( self.indentStack[-1] if len(self.indentStack) else 0 )
            	t.setLine( self.input.getLine() )
            	self.emit(t)
            	self.indentStack.append(self.numberOfSpaces)
            else:
            	while len(self.indentStack)!=0 and self.numberOfSpaces < self.indentStack[-1]:
            		del self.indentStack[-1]
            		t = ClassicToken(DEDENT, '<')
            		t.setCharPositionInLine( self.indentStack[-1] if len(self.indentStack) else 0 )
            		t.setLine( self.input.getLine() )
            		self.emit(t)
            	ss = self.indentStack[-1] if len(self.indentStack)!=0 else 0
            	if self.numberOfSpaces != ss:
            		self.raiseRecognitionException(MismatchedTokenException(' ' if self.numberOfSpaces < ss else '{backspace}',self.input), "Uneven indent. Make it larger or smaller (f.e. "+str(ss)+").")
            	
            #action end




        finally:

            pass

    # $ANTLR end INDENT_OR_DEDENT



    # $ANTLR start WS
    def mWS(self, ):

        try:
            self.type = WS

            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:216:4: ( ( ' ' | '\\t' ) )
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:216:6: ( ' ' | '\\t' )
            if self.input.LA(1) == u'\t' or self.input.LA(1) == u' ':
                self.input.consume();

            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse






        finally:

            pass

    # $ANTLR end WS



    # $ANTLR start NonWS
    def mNonWS(self, ):

        try:
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:223:2: (~ ( WS | '\\n' | '\\r' ) )
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:224:3: ~ ( WS | '\\n' | '\\r' )
            if (u'\u0000' <= self.input.LA(1) <= u'\b') or (u'\u000B' <= self.input.LA(1) <= u'\f') or (u'\u000E' <= self.input.LA(1) <= u'\u001F') or (u'!' <= self.input.LA(1) <= u'\uFFFE'):
                self.input.consume();

            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse






        finally:

            pass

    # $ANTLR end NonWS



    # $ANTLR start AlphaNum
    def mAlphaNum(self, ):

        try:
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:229:9: ( ( Alpha | Digit ) )
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:230:3: ( Alpha | Digit )
            if (u'0' <= self.input.LA(1) <= u'9') or (u'A' <= self.input.LA(1) <= u'Z') or (u'a' <= self.input.LA(1) <= u'z'):
                self.input.consume();

            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse






        finally:

            pass

    # $ANTLR end AlphaNum



    # $ANTLR start Type
    def mType(self, ):

        try:
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:234:6: ( 's' | 't' )
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:
            if (u's' <= self.input.LA(1) <= u't'):
                self.input.consume();

            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse






        finally:

            pass

    # $ANTLR end Type



    # $ANTLR start Alpha
    def mAlpha(self, ):

        try:
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:240:2: ( ( 'a' .. 'z' | 'A' .. 'Z' ) )
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:241:3: ( 'a' .. 'z' | 'A' .. 'Z' )
            if (u'A' <= self.input.LA(1) <= u'Z') or (u'a' <= self.input.LA(1) <= u'z'):
                self.input.consume();

            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse






        finally:

            pass

    # $ANTLR end Alpha



    # $ANTLR start HexAlpha
    def mHexAlpha(self, ):

        try:
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:246:2: ( ( 'a' .. 'f' | 'A' .. 'F' ) )
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:247:3: ( 'a' .. 'f' | 'A' .. 'F' )
            if (u'A' <= self.input.LA(1) <= u'F') or (u'a' <= self.input.LA(1) <= u'f'):
                self.input.consume();

            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse






        finally:

            pass

    # $ANTLR end HexAlpha



    # $ANTLR start HexDigit
    def mHexDigit(self, ):

        try:
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:252:2: ( ( HexAlpha | Digit ) )
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:253:3: ( HexAlpha | Digit )
            if (u'0' <= self.input.LA(1) <= u'9') or (u'A' <= self.input.LA(1) <= u'F') or (u'a' <= self.input.LA(1) <= u'f'):
                self.input.consume();

            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse






        finally:

            pass

    # $ANTLR end HexDigit



    # $ANTLR start Digit
    def mDigit(self, ):

        try:
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:257:7: ( '0' .. '9' )
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:258:3: '0' .. '9'
            self.matchRange(u'0', u'9')





        finally:

            pass

    # $ANTLR end Digit



    def mTokens(self):
        # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:1:8: ( DOT_END | DOT_NAME | DOT_DOT_NAME | COMMENT | DOT_ARGS | DOT_DOT_ARGS | DOT_DOT_BODY | HEX_DQUAD | HEX_QUAD | HEX_PAIR | HEX_DIGIT | TYPED_VALUE | STRING | NAME | INDENT_OR_DEDENT | WS )
        alt21 = 16
        alt21 = self.dfa21.predict(self.input)
        if alt21 == 1:
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:1:10: DOT_END
            self.mDOT_END()



        elif alt21 == 2:
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:1:18: DOT_NAME
            self.mDOT_NAME()



        elif alt21 == 3:
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:1:27: DOT_DOT_NAME
            self.mDOT_DOT_NAME()



        elif alt21 == 4:
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:1:40: COMMENT
            self.mCOMMENT()



        elif alt21 == 5:
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:1:48: DOT_ARGS
            self.mDOT_ARGS()



        elif alt21 == 6:
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:1:57: DOT_DOT_ARGS
            self.mDOT_DOT_ARGS()



        elif alt21 == 7:
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:1:70: DOT_DOT_BODY
            self.mDOT_DOT_BODY()



        elif alt21 == 8:
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:1:83: HEX_DQUAD
            self.mHEX_DQUAD()



        elif alt21 == 9:
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:1:93: HEX_QUAD
            self.mHEX_QUAD()



        elif alt21 == 10:
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:1:102: HEX_PAIR
            self.mHEX_PAIR()



        elif alt21 == 11:
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:1:111: HEX_DIGIT
            self.mHEX_DIGIT()



        elif alt21 == 12:
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:1:121: TYPED_VALUE
            self.mTYPED_VALUE()



        elif alt21 == 13:
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:1:133: STRING
            self.mSTRING()



        elif alt21 == 14:
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:1:140: NAME
            self.mNAME()



        elif alt21 == 15:
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:1:145: INDENT_OR_DEDENT
            self.mINDENT_OR_DEDENT()



        elif alt21 == 16:
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:1:162: WS
            self.mWS()








    # lookup tables for DFA #6

    DFA6_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA6_eof = DFA.unpack(
        u"\5\uffff"
        )

    DFA6_min = DFA.unpack(
        u"\2\11\1\0\2\uffff"
        )

    DFA6_max = DFA.unpack(
        u"\2\43\1\0\2\uffff"
        )

    DFA6_accept = DFA.unpack(
        u"\3\uffff\1\1\1\2"
        )

    DFA6_special = DFA.unpack(
        u"\1\0\1\2\1\1\2\uffff"
        )

            
    DFA6_transition = [
        DFA.unpack(u"\1\1\26\uffff\1\1\2\uffff\1\2"),
        DFA.unpack(u"\1\1\26\uffff\1\1\2\uffff\1\2"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #6

    class DFA6(DFA):
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
                if (LA6_0 == u'\t' or LA6_0 == u' ') and ((self.getColumn() > 0  or self.getColumn() == 0)):
                    s = 1

                elif (LA6_0 == u'#') and ((self.getColumn() > 0  or self.getColumn() == 0)):
                    s = 2

                 
                input.seek(index6_0)
                if s >= 0:
                    return s
            elif s == 1: 
                LA6_2 = input.LA(1)

                 
                index6_2 = input.index()
                input.rewind()
                s = -1
                if (self.getColumn() == 0):
                    s = 3

                elif (self.getColumn() > 0 ):
                    s = 4

                 
                input.seek(index6_2)
                if s >= 0:
                    return s
            elif s == 2: 
                LA6_1 = input.LA(1)

                 
                index6_1 = input.index()
                input.rewind()
                s = -1
                if (LA6_1 == u'#') and ((self.getColumn() > 0  or self.getColumn() == 0)):
                    s = 2

                elif (LA6_1 == u'\t' or LA6_1 == u' ') and ((self.getColumn() > 0  or self.getColumn() == 0)):
                    s = 1

                 
                input.seek(index6_1)
                if s >= 0:
                    return s

            nvae = NoViableAltException(self_.getDescription(), 6, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #18

    DFA18_eot = DFA.unpack(
        u"\2\uffff\1\7\2\uffff\2\7\2\uffff"
        )

    DFA18_eof = DFA.unpack(
        u"\11\uffff"
        )

    DFA18_min = DFA.unpack(
        u"\1\11\1\12\1\11\2\uffff\2\11\2\uffff"
        )

    DFA18_max = DFA.unpack(
        u"\1\40\1\12\1\40\2\uffff\2\40\2\uffff"
        )

    DFA18_accept = DFA.unpack(
        u"\3\uffff\1\2\1\3\2\uffff\1\4\1\1"
        )

    DFA18_special = DFA.unpack(
        u"\11\uffff"
        )

            
    DFA18_transition = [
        DFA.unpack(u"\1\3\1\2\2\uffff\1\1\22\uffff\1\4"),
        DFA.unpack(u"\1\2"),
        DFA.unpack(u"\1\6\1\10\2\uffff\1\10\22\uffff\1\5"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\6\1\10\2\uffff\1\10\22\uffff\1\5"),
        DFA.unpack(u"\1\6\1\10\2\uffff\1\10\22\uffff\1\5"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #18

    DFA18 = DFA
    # lookup tables for DFA #21

    DFA21_eot = DFA.unpack(
        u"\1\7\1\uffff\1\23\1\31\1\34\1\uffff\1\40\2\uffff\1\34\2\15\2\uffff"
        u"\1\23\1\50\1\52\1\53\1\50\2\uffff\2\50\1\uffff\1\54\4\uffff\1\55"
        u"\2\40\1\uffff\1\50\1\uffff\2\60\1\uffff\1\63\1\64\1\uffff\1\70"
        u"\4\uffff\1\50\1\74\1\uffff\1\15\5\uffff\1\100\3\uffff\1\102\1\uffff"
        u"\2\104\4\uffff\1\50\1\uffff\1\15\1\uffff\1\50\1\15\1\50\1\15\1"
        u"\115\1\106\1\uffff"
        )

    DFA21_eof = DFA.unpack(
        u"\116\uffff"
        )

    DFA21_min = DFA.unpack(
        u"\5\0\1\12\1\0\1\uffff\1\0\1\60\1\47\2\0\1\uffff\5\0\2\uffff\2\0"
        u"\1\uffff\1\0\4\uffff\5\0\1\uffff\2\60\1\uffff\12\0\1\uffff\2\60"
        u"\2\0\2\uffff\2\0\2\uffff\2\0\2\60\3\uffff\2\0\1\uffff\1\60\1\uffff"
        u"\1\0\1\60\1\0\1\60\1\0\1\101\1\0"
        )

    DFA21_max = DFA.unpack(
        u"\5\ufffe\1\12\1\ufffe\1\uffff\1\ufffe\1\172\1\47\2\ufffe\1\uffff"
        u"\5\ufffe\2\uffff\2\ufffe\1\uffff\1\ufffe\4\uffff\3\ufffe\1\0\1"
        u"\ufffe\1\uffff\1\172\1\146\1\uffff\2\ufffe\1\0\1\ufffe\4\0\2\ufffe"
        u"\1\uffff\2\146\2\0\2\uffff\1\ufffe\1\0\2\uffff\1\ufffe\1\0\1\172"
        u"\1\146\3\uffff\1\0\1\ufffe\1\uffff\1\146\1\uffff\1\ufffe\1\146"
        u"\1\ufffe\1\146\1\ufffe\1\172\1\0"
        )

    DFA21_accept = DFA.unpack(
        u"\7\uffff\1\7\5\uffff\1\16\5\uffff\1\20\1\17\2\uffff\1\4\1\uffff"
        u"\3\4\1\13\5\uffff\1\15\2\uffff\1\14\12\uffff\1\12\4\uffff\1\5\1"
        u"\6\2\uffff\2\2\4\uffff\1\3\1\1\1\2\2\uffff\1\11\1\uffff\1\10\7"
        u"\uffff"
        )

    DFA21_special = DFA.unpack(
        u"\1\11\1\2\1\44\1\45\1\12\1\uffff\1\13\1\uffff\1\4\2\uffff\1\46"
        u"\1\15\1\uffff\1\43\1\5\1\42\1\27\1\37\2\uffff\1\53\1\47\1\uffff"
        u"\1\1\4\uffff\1\3\1\25\1\24\1\26\1\16\4\uffff\1\40\1\0\1\36\1\41"
        u"\1\21\1\22\1\14\1\32\1\50\1\7\3\uffff\1\34\1\17\2\uffff\1\10\1"
        u"\20\2\uffff\1\23\1\35\5\uffff\1\33\1\52\3\uffff\1\31\1\uffff\1"
        u"\51\1\uffff\1\6\1\uffff\1\30"
        )

            
    DFA21_transition = [
        DFA.unpack(u"\11\14\1\2\1\6\2\14\1\5\22\14\1\16\2\14\1\3\3\14\1\10"
        u"\6\14\1\1\1\14\12\4\7\14\6\11\24\15\4\14\1\13\1\14\6\11\14\15\2"
        u"\12\6\15\uff84\14"),
        DFA.unpack(u"\12\22\1\uffff\2\22\1\uffff\25\22\1\uffff\12\22\1\17"
        u"\22\22\32\21\4\22\1\21\1\22\4\21\1\20\25\21\uff84\22"),
        DFA.unpack(u"\11\22\1\25\1\24\2\22\1\24\22\22\1\26\2\22\1\27\uffdb"
        u"\22"),
        DFA.unpack(u"\12\30\1\33\2\30\1\32\25\30\1\32\uffdb\30"),
        DFA.unpack(u"\12\22\1\uffff\2\22\1\uffff\25\22\1\uffff\14\22\12\35"
        u"\7\22\6\35\32\22\6\35\uff98\22"),
        DFA.unpack(u"\1\6"),
        DFA.unpack(u"\11\7\1\37\1\6\2\7\1\5\22\7\1\36\uffde\7"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\41\1\42\2\41\1\42\25\41\1\42\3\41\1\22\uffd7\41"),
        DFA.unpack(u"\12\44\7\uffff\6\43\24\15\4\uffff\1\15\1\uffff\6\43"
        u"\24\15"),
        DFA.unpack(u"\1\45"),
        DFA.unpack(u"\12\22\1\uffff\2\22\1\uffff\25\22\1\uffff\35\22\32\46"
        u"\4\22\1\46\1\22\32\46\uff84\22"),
        DFA.unpack(u"\12\22\1\uffff\2\22\1\uffff\25\22\1\uffff\uffdb\22"),
        DFA.unpack(u""),
        DFA.unpack(u"\11\22\1\25\1\24\2\22\1\24\22\22\1\26\2\22\1\27\uffdb"
        u"\22"),
        DFA.unpack(u"\12\22\1\uffff\2\22\1\uffff\25\22\1\uffff\35\22\32\47"
        u"\4\22\1\47\1\22\32\47\uff84\22"),
        DFA.unpack(u"\12\22\1\uffff\2\22\1\uffff\25\22\1\uffff\35\22\32\21"
        u"\4\22\1\21\1\22\15\21\1\51\14\21\uff84\22"),
        DFA.unpack(u"\12\22\1\uffff\2\22\1\uffff\25\22\1\uffff\35\22\32\21"
        u"\4\22\1\21\1\22\32\21\uff84\22"),
        DFA.unpack(u"\12\22\1\uffff\2\22\1\uffff\25\22\1\uffff\uffdb\22"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\11\22\1\25\1\24\2\22\1\24\22\22\1\26\2\22\1\27\uffdb"
        u"\22"),
        DFA.unpack(u"\11\22\1\25\1\24\2\22\1\24\22\22\1\26\2\22\1\27\uffdb"
        u"\22"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\30\1\33\2\30\1\32\25\30\1\32\uffdb\30"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\22\1\uffff\2\22\1\uffff\25\22\1\uffff\14\22\12\56"
        u"\7\22\6\56\32\22\6\56\uff98\22"),
        DFA.unpack(u"\11\7\1\37\1\6\2\7\1\5\22\7\1\36\uffde\7"),
        DFA.unpack(u"\11\7\1\37\1\6\2\7\1\5\22\7\1\36\uffde\7"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\12\41\1\42\2\41\1\42\25\41\1\42\3\41\1\57\uffd7\41"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\62\7\uffff\6\61\24\15\4\uffff\1\15\1\uffff\6\61"
        u"\24\15"),
        DFA.unpack(u"\12\62\7\uffff\6\62\32\uffff\6\62"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\22\1\uffff\2\22\1\uffff\25\22\1\uffff\35\22\32\46"
        u"\4\22\1\46\1\22\32\46\uff84\22"),
        DFA.unpack(u"\12\22\1\uffff\2\22\1\uffff\25\22\1\uffff\35\22\32\47"
        u"\4\22\1\47\1\22\32\47\uff84\22"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\12\22\1\uffff\2\22\1\uffff\25\22\1\uffff\35\22\32\21"
        u"\4\22\1\21\1\22\3\21\1\67\26\21\uff84\22"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\12\22\1\uffff\2\22\1\uffff\25\22\1\uffff\14\22\12\73"
        u"\7\22\6\73\32\22\6\73\uff98\22"),
        DFA.unpack(u"\12\22\1\uffff\2\22\1\uffff\25\22\1\uffff\uffdb\22"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\76\7\uffff\6\75\32\uffff\6\75"),
        DFA.unpack(u"\12\76\7\uffff\6\76\32\uffff\6\76"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\22\1\uffff\2\22\1\uffff\25\22\1\uffff\35\22\32\21"
        u"\4\22\1\21\1\22\32\21\uff84\22"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\22\1\uffff\2\22\1\uffff\25\22\1\uffff\14\22\12\103"
        u"\7\22\6\103\32\22\6\103\uff98\22"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\12\106\7\uffff\6\105\24\15\4\uffff\1\15\1\uffff\6\105"
        u"\24\15"),
        DFA.unpack(u"\12\106\7\uffff\6\106\32\uffff\6\106"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\12\22\1\uffff\2\22\1\uffff\25\22\1\uffff\14\22\12\107"
        u"\7\22\6\107\32\22\6\107\uff98\22"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\106\7\uffff\6\110\32\uffff\6\110"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\22\1\uffff\2\22\1\uffff\25\22\1\uffff\14\22\12\111"
        u"\7\22\6\111\32\22\6\111\uff98\22"),
        DFA.unpack(u"\12\106\7\uffff\6\112\32\uffff\6\112"),
        DFA.unpack(u"\12\22\1\uffff\2\22\1\uffff\25\22\1\uffff\14\22\12\113"
        u"\7\22\6\113\32\22\6\113\uff98\22"),
        DFA.unpack(u"\12\106\7\uffff\6\114\32\uffff\6\114"),
        DFA.unpack(u"\12\22\1\uffff\2\22\1\uffff\25\22\1\uffff\uffdb\22"),
        DFA.unpack(u"\32\15\4\uffff\1\15\1\uffff\32\15"),
        DFA.unpack(u"\1\uffff")
    ]

    # class definition for DFA #21

    class DFA21(DFA):
        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA21_39 = input.LA(1)

                 
                index21_39 = input.index()
                input.rewind()
                s = -1
                if ((u'A' <= LA21_39 <= u'Z') or LA21_39 == u'_' or (u'a' <= LA21_39 <= u'z')):
                    s = 39

                elif ((u'\u0000' <= LA21_39 <= u'\t') or (u'\u000B' <= LA21_39 <= u'\f') or (u'\u000E' <= LA21_39 <= u'"') or (u'$' <= LA21_39 <= u'@') or (u'[' <= LA21_39 <= u'^') or LA21_39 == u'`' or (u'{' <= LA21_39 <= u'\uFFFE')) and ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]      or self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] )):
                    s = 18

                else:
                    s = 52

                 
                input.seek(index21_39)
                if s >= 0:
                    return s
            elif s == 1: 
                LA21_24 = input.LA(1)

                 
                index21_24 = input.index()
                input.rewind()
                s = -1
                if (LA21_24 == u'\n') and (self.getColumn() == 0):
                    s = 27

                elif ((u'\u0000' <= LA21_24 <= u'\t') or (u'\u000B' <= LA21_24 <= u'\f') or (u'\u000E' <= LA21_24 <= u'"') or (u'$' <= LA21_24 <= u'\uFFFE')) and ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]      or self.getColumn() > 0  or self.getColumn() == 0 or self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] )):
                    s = 24

                elif (LA21_24 == u'\r' or LA21_24 == u'#') and ((self.getColumn() > 0  or self.getColumn() == 0)):
                    s = 26

                else:
                    s = 44

                 
                input.seek(index21_24)
                if s >= 0:
                    return s
            elif s == 2: 
                LA21_1 = input.LA(1)

                 
                index21_1 = input.index()
                input.rewind()
                s = -1
                if (LA21_1 == u'.'):
                    s = 15

                elif (LA21_1 == u'e'):
                    s = 16

                elif ((u'A' <= LA21_1 <= u'Z') or LA21_1 == u'_' or (u'a' <= LA21_1 <= u'd') or (u'f' <= LA21_1 <= u'z')):
                    s = 17

                elif ((u'\u0000' <= LA21_1 <= u'\t') or (u'\u000B' <= LA21_1 <= u'\f') or (u'\u000E' <= LA21_1 <= u'"') or (u'$' <= LA21_1 <= u'-') or (u'/' <= LA21_1 <= u'@') or (u'[' <= LA21_1 <= u'^') or LA21_1 == u'`' or (u'{' <= LA21_1 <= u'\uFFFE')) and ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]      or self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] )):
                    s = 18

                 
                input.seek(index21_1)
                if s >= 0:
                    return s
            elif s == 3: 
                LA21_29 = input.LA(1)

                 
                index21_29 = input.index()
                input.rewind()
                s = -1
                if ((u'0' <= LA21_29 <= u'9') or (u'A' <= LA21_29 <= u'F') or (u'a' <= LA21_29 <= u'f')):
                    s = 46

                elif ((u'\u0000' <= LA21_29 <= u'\t') or (u'\u000B' <= LA21_29 <= u'\f') or (u'\u000E' <= LA21_29 <= u'"') or (u'$' <= LA21_29 <= u'/') or (u':' <= LA21_29 <= u'@') or (u'G' <= LA21_29 <= u'`') or (u'g' <= LA21_29 <= u'\uFFFE')) and ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]      or self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] )):
                    s = 18

                else:
                    s = 45

                 
                input.seek(index21_29)
                if s >= 0:
                    return s
            elif s == 4: 
                LA21_8 = input.LA(1)

                 
                index21_8 = input.index()
                input.rewind()
                s = -1
                if ((u'\u0000' <= LA21_8 <= u'\t') or (u'\u000B' <= LA21_8 <= u'\f') or (u'\u000E' <= LA21_8 <= u'"') or (u'$' <= LA21_8 <= u'&') or (u'(' <= LA21_8 <= u'\uFFFE')):
                    s = 33

                elif (LA21_8 == u'\n' or LA21_8 == u'\r' or LA21_8 == u'#'):
                    s = 34

                elif (LA21_8 == u'\'') and ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]      or self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] )):
                    s = 18

                 
                input.seek(index21_8)
                if s >= 0:
                    return s
            elif s == 5: 
                LA21_15 = input.LA(1)

                 
                index21_15 = input.index()
                input.rewind()
                s = -1
                if ((u'A' <= LA21_15 <= u'Z') or LA21_15 == u'_' or (u'a' <= LA21_15 <= u'z')):
                    s = 39

                elif ((u'\u0000' <= LA21_15 <= u'\t') or (u'\u000B' <= LA21_15 <= u'\f') or (u'\u000E' <= LA21_15 <= u'"') or (u'$' <= LA21_15 <= u'@') or (u'[' <= LA21_15 <= u'^') or LA21_15 == u'`' or (u'{' <= LA21_15 <= u'\uFFFE')) and ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]      or self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] )):
                    s = 18

                else:
                    s = 40

                 
                input.seek(index21_15)
                if s >= 0:
                    return s
            elif s == 6: 
                LA21_75 = input.LA(1)

                 
                index21_75 = input.index()
                input.rewind()
                s = -1
                if ((u'\u0000' <= LA21_75 <= u'\t') or (u'\u000B' <= LA21_75 <= u'\f') or (u'\u000E' <= LA21_75 <= u'"') or (u'$' <= LA21_75 <= u'\uFFFE')) and ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]      or self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] )):
                    s = 18

                else:
                    s = 77

                 
                input.seek(index21_75)
                if s >= 0:
                    return s
            elif s == 7: 
                LA21_47 = input.LA(1)

                 
                index21_47 = input.index()
                input.rewind()
                s = -1
                if ((u'\u0000' <= LA21_47 <= u'\t') or (u'\u000B' <= LA21_47 <= u'\f') or (u'\u000E' <= LA21_47 <= u'"') or (u'$' <= LA21_47 <= u'\uFFFE')) and ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]      or self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] )):
                    s = 18

                else:
                    s = 60

                 
                input.seek(index21_47)
                if s >= 0:
                    return s
            elif s == 8: 
                LA21_55 = input.LA(1)

                 
                index21_55 = input.index()
                input.rewind()
                s = -1
                if ((u'A' <= LA21_55 <= u'Z') or LA21_55 == u'_' or (u'a' <= LA21_55 <= u'z')):
                    s = 17

                elif ((u'\u0000' <= LA21_55 <= u'\t') or (u'\u000B' <= LA21_55 <= u'\f') or (u'\u000E' <= LA21_55 <= u'"') or (u'$' <= LA21_55 <= u'@') or (u'[' <= LA21_55 <= u'^') or LA21_55 == u'`' or (u'{' <= LA21_55 <= u'\uFFFE')) and ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]      or self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] )):
                    s = 18

                else:
                    s = 64

                 
                input.seek(index21_55)
                if s >= 0:
                    return s
            elif s == 9: 
                LA21_0 = input.LA(1)

                 
                index21_0 = input.index()
                input.rewind()
                s = -1
                if (LA21_0 == u'.'):
                    s = 1

                elif (LA21_0 == u'\t'):
                    s = 2

                elif (LA21_0 == u'#') and ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]      or self.getColumn() > 0  or self.getColumn() == 0 or self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] )):
                    s = 3

                elif ((u'0' <= LA21_0 <= u'9')):
                    s = 4

                elif (LA21_0 == u'\r'):
                    s = 5

                elif (LA21_0 == u'\n'):
                    s = 6

                elif (LA21_0 == u'\''):
                    s = 8

                elif ((u'A' <= LA21_0 <= u'F') or (u'a' <= LA21_0 <= u'f')):
                    s = 9

                elif ((u's' <= LA21_0 <= u't')):
                    s = 10

                elif (LA21_0 == u'_'):
                    s = 11

                elif ((u'\u0000' <= LA21_0 <= u'\b') or (u'\u000B' <= LA21_0 <= u'\f') or (u'\u000E' <= LA21_0 <= u'\u001F') or (u'!' <= LA21_0 <= u'"') or (u'$' <= LA21_0 <= u'&') or (u'(' <= LA21_0 <= u'-') or LA21_0 == u'/' or (u':' <= LA21_0 <= u'@') or (u'[' <= LA21_0 <= u'^') or LA21_0 == u'`' or (u'{' <= LA21_0 <= u'\uFFFE')) and ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]      or self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] )):
                    s = 12

                elif ((u'G' <= LA21_0 <= u'Z') or (u'g' <= LA21_0 <= u'r') or (u'u' <= LA21_0 <= u'z')):
                    s = 13

                elif (LA21_0 == u' '):
                    s = 14

                else:
                    s = 7

                 
                input.seek(index21_0)
                if s >= 0:
                    return s
            elif s == 10: 
                LA21_4 = input.LA(1)

                 
                index21_4 = input.index()
                input.rewind()
                s = -1
                if ((u'0' <= LA21_4 <= u'9') or (u'A' <= LA21_4 <= u'F') or (u'a' <= LA21_4 <= u'f')):
                    s = 29

                elif ((u'\u0000' <= LA21_4 <= u'\t') or (u'\u000B' <= LA21_4 <= u'\f') or (u'\u000E' <= LA21_4 <= u'"') or (u'$' <= LA21_4 <= u'/') or (u':' <= LA21_4 <= u'@') or (u'G' <= LA21_4 <= u'`') or (u'g' <= LA21_4 <= u'\uFFFE')) and ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]      or self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] )):
                    s = 18

                else:
                    s = 28

                 
                input.seek(index21_4)
                if s >= 0:
                    return s
            elif s == 11: 
                LA21_6 = input.LA(1)

                 
                index21_6 = input.index()
                input.rewind()
                s = -1
                if (LA21_6 == u' '):
                    s = 30

                elif (LA21_6 == u'\t'):
                    s = 31

                elif ((u'\u0000' <= LA21_6 <= u'\b') or (u'\u000B' <= LA21_6 <= u'\f') or (u'\u000E' <= LA21_6 <= u'\u001F') or (u'!' <= LA21_6 <= u'\uFFFE')) and (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME, DOT_DOT_ARGS] ):
                    s = 7

                elif (LA21_6 == u'\r'):
                    s = 5

                elif (LA21_6 == u'\n'):
                    s = 6

                else:
                    s = 32

                 
                input.seek(index21_6)
                if s >= 0:
                    return s
            elif s == 12: 
                LA21_44 = input.LA(1)

                 
                index21_44 = input.index()
                input.rewind()
                s = -1
                if ((self.getColumn() > 0  or self.getColumn() == 0)):
                    s = 27

                elif (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     ):
                    s = 53

                elif (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] ):
                    s = 54

                 
                input.seek(index21_44)
                if s >= 0:
                    return s
            elif s == 13: 
                LA21_12 = input.LA(1)

                 
                index21_12 = input.index()
                input.rewind()
                s = -1
                if ((u'\u0000' <= LA21_12 <= u'\t') or (u'\u000B' <= LA21_12 <= u'\f') or (u'\u000E' <= LA21_12 <= u'"') or (u'$' <= LA21_12 <= u'\uFFFE')) and ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]      or self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] )):
                    s = 18

                 
                input.seek(index21_12)
                if s >= 0:
                    return s
            elif s == 14: 
                LA21_33 = input.LA(1)

                 
                index21_33 = input.index()
                input.rewind()
                s = -1
                if (LA21_33 == u'\''):
                    s = 47

                elif ((u'\u0000' <= LA21_33 <= u'\t') or (u'\u000B' <= LA21_33 <= u'\f') or (u'\u000E' <= LA21_33 <= u'"') or (u'$' <= LA21_33 <= u'&') or (u'(' <= LA21_33 <= u'\uFFFE')):
                    s = 33

                elif (LA21_33 == u'\n' or LA21_33 == u'\r' or LA21_33 == u'#'):
                    s = 34

                else:
                    s = 40

                 
                input.seek(index21_33)
                if s >= 0:
                    return s
            elif s == 15: 
                LA21_52 = input.LA(1)

                 
                index21_52 = input.index()
                input.rewind()
                s = -1
                if (not ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]      or self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] ))):
                    s = 63

                elif (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     ):
                    s = 53

                elif (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] ):
                    s = 54

                 
                input.seek(index21_52)
                if s >= 0:
                    return s
            elif s == 16: 
                LA21_56 = input.LA(1)

                 
                index21_56 = input.index()
                input.rewind()
                s = -1
                if (not ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]      or self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] ))):
                    s = 65

                elif (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     ):
                    s = 53

                elif (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] ):
                    s = 54

                 
                input.seek(index21_56)
                if s >= 0:
                    return s
            elif s == 17: 
                LA21_42 = input.LA(1)

                 
                index21_42 = input.index()
                input.rewind()
                s = -1
                if (not ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]      or self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] ))):
                    s = 57

                elif (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     ):
                    s = 53

                elif (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] ):
                    s = 54

                 
                input.seek(index21_42)
                if s >= 0:
                    return s
            elif s == 18: 
                LA21_43 = input.LA(1)

                 
                index21_43 = input.index()
                input.rewind()
                s = -1
                if (not ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]      or self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] ))):
                    s = 58

                elif (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     ):
                    s = 53

                elif (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] ):
                    s = 54

                 
                input.seek(index21_43)
                if s >= 0:
                    return s
            elif s == 19: 
                LA21_59 = input.LA(1)

                 
                index21_59 = input.index()
                input.rewind()
                s = -1
                if ((u'0' <= LA21_59 <= u'9') or (u'A' <= LA21_59 <= u'F') or (u'a' <= LA21_59 <= u'f')):
                    s = 67

                elif ((u'\u0000' <= LA21_59 <= u'\t') or (u'\u000B' <= LA21_59 <= u'\f') or (u'\u000E' <= LA21_59 <= u'"') or (u'$' <= LA21_59 <= u'/') or (u':' <= LA21_59 <= u'@') or (u'G' <= LA21_59 <= u'`') or (u'g' <= LA21_59 <= u'\uFFFE')) and ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]      or self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] )):
                    s = 18

                else:
                    s = 66

                 
                input.seek(index21_59)
                if s >= 0:
                    return s
            elif s == 20: 
                LA21_31 = input.LA(1)

                 
                index21_31 = input.index()
                input.rewind()
                s = -1
                if (LA21_31 == u'\r'):
                    s = 5

                elif (LA21_31 == u'\n'):
                    s = 6

                elif (LA21_31 == u'\t'):
                    s = 31

                elif (LA21_31 == u' '):
                    s = 30

                elif ((u'\u0000' <= LA21_31 <= u'\b') or (u'\u000B' <= LA21_31 <= u'\f') or (u'\u000E' <= LA21_31 <= u'\u001F') or (u'!' <= LA21_31 <= u'\uFFFE')) and (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME, DOT_DOT_ARGS] ):
                    s = 7

                else:
                    s = 32

                 
                input.seek(index21_31)
                if s >= 0:
                    return s
            elif s == 21: 
                LA21_30 = input.LA(1)

                 
                index21_30 = input.index()
                input.rewind()
                s = -1
                if (LA21_30 == u'\r'):
                    s = 5

                elif (LA21_30 == u'\n'):
                    s = 6

                elif (LA21_30 == u'\t'):
                    s = 31

                elif (LA21_30 == u' '):
                    s = 30

                elif ((u'\u0000' <= LA21_30 <= u'\b') or (u'\u000B' <= LA21_30 <= u'\f') or (u'\u000E' <= LA21_30 <= u'\u001F') or (u'!' <= LA21_30 <= u'\uFFFE')) and (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME, DOT_DOT_ARGS] ):
                    s = 7

                else:
                    s = 32

                 
                input.seek(index21_30)
                if s >= 0:
                    return s
            elif s == 22: 
                LA21_32 = input.LA(1)

                 
                index21_32 = input.index()
                input.rewind()
                s = -1
                if (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME, DOT_DOT_ARGS] ):
                    s = 7

                elif (True):
                    s = 20

                 
                input.seek(index21_32)
                if s >= 0:
                    return s
            elif s == 23: 
                LA21_17 = input.LA(1)

                 
                index21_17 = input.index()
                input.rewind()
                s = -1
                if ((u'A' <= LA21_17 <= u'Z') or LA21_17 == u'_' or (u'a' <= LA21_17 <= u'z')):
                    s = 17

                elif ((u'\u0000' <= LA21_17 <= u'\t') or (u'\u000B' <= LA21_17 <= u'\f') or (u'\u000E' <= LA21_17 <= u'"') or (u'$' <= LA21_17 <= u'@') or (u'[' <= LA21_17 <= u'^') or LA21_17 == u'`' or (u'{' <= LA21_17 <= u'\uFFFE')) and ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]      or self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] )):
                    s = 18

                else:
                    s = 43

                 
                input.seek(index21_17)
                if s >= 0:
                    return s
            elif s == 24: 
                LA21_77 = input.LA(1)

                 
                index21_77 = input.index()
                input.rewind()
                s = -1
                if (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     ):
                    s = 53

                elif (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] ):
                    s = 54

                elif (True):
                    s = 70

                 
                input.seek(index21_77)
                if s >= 0:
                    return s
            elif s == 25: 
                LA21_71 = input.LA(1)

                 
                index21_71 = input.index()
                input.rewind()
                s = -1
                if ((u'0' <= LA21_71 <= u'9') or (u'A' <= LA21_71 <= u'F') or (u'a' <= LA21_71 <= u'f')):
                    s = 73

                elif ((u'\u0000' <= LA21_71 <= u'\t') or (u'\u000B' <= LA21_71 <= u'\f') or (u'\u000E' <= LA21_71 <= u'"') or (u'$' <= LA21_71 <= u'/') or (u':' <= LA21_71 <= u'@') or (u'G' <= LA21_71 <= u'`') or (u'g' <= LA21_71 <= u'\uFFFE')) and ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]      or self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] )):
                    s = 18

                else:
                    s = 40

                 
                input.seek(index21_71)
                if s >= 0:
                    return s
            elif s == 26: 
                LA21_45 = input.LA(1)

                 
                index21_45 = input.index()
                input.rewind()
                s = -1
                if (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     ):
                    s = 53

                elif (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] ):
                    s = 54

                elif (True):
                    s = 48

                 
                input.seek(index21_45)
                if s >= 0:
                    return s
            elif s == 27: 
                LA21_66 = input.LA(1)

                 
                index21_66 = input.index()
                input.rewind()
                s = -1
                if (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     ):
                    s = 53

                elif (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] ):
                    s = 54

                elif (True):
                    s = 68

                 
                input.seek(index21_66)
                if s >= 0:
                    return s
            elif s == 28: 
                LA21_51 = input.LA(1)

                 
                index21_51 = input.index()
                input.rewind()
                s = -1
                if (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     ):
                    s = 53

                elif (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] ):
                    s = 54

                elif (True):
                    s = 13

                 
                input.seek(index21_51)
                if s >= 0:
                    return s
            elif s == 29: 
                LA21_60 = input.LA(1)

                 
                index21_60 = input.index()
                input.rewind()
                s = -1
                if (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     ):
                    s = 53

                elif (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] ):
                    s = 54

                elif (True):
                    s = 34

                 
                input.seek(index21_60)
                if s >= 0:
                    return s
            elif s == 30: 
                LA21_40 = input.LA(1)

                 
                index21_40 = input.index()
                input.rewind()
                s = -1
                if (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     ):
                    s = 53

                elif (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] ):
                    s = 54

                 
                input.seek(index21_40)
                if s >= 0:
                    return s
            elif s == 31: 
                LA21_18 = input.LA(1)

                 
                index21_18 = input.index()
                input.rewind()
                s = -1
                if ((u'\u0000' <= LA21_18 <= u'\t') or (u'\u000B' <= LA21_18 <= u'\f') or (u'\u000E' <= LA21_18 <= u'"') or (u'$' <= LA21_18 <= u'\uFFFE')) and ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]      or self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] )):
                    s = 18

                else:
                    s = 40

                 
                input.seek(index21_18)
                if s >= 0:
                    return s
            elif s == 32: 
                LA21_38 = input.LA(1)

                 
                index21_38 = input.index()
                input.rewind()
                s = -1
                if ((u'A' <= LA21_38 <= u'Z') or LA21_38 == u'_' or (u'a' <= LA21_38 <= u'z')):
                    s = 38

                elif ((u'\u0000' <= LA21_38 <= u'\t') or (u'\u000B' <= LA21_38 <= u'\f') or (u'\u000E' <= LA21_38 <= u'"') or (u'$' <= LA21_38 <= u'@') or (u'[' <= LA21_38 <= u'^') or LA21_38 == u'`' or (u'{' <= LA21_38 <= u'\uFFFE')) and ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]      or self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] )):
                    s = 18

                else:
                    s = 51

                 
                input.seek(index21_38)
                if s >= 0:
                    return s
            elif s == 33: 
                LA21_41 = input.LA(1)

                 
                index21_41 = input.index()
                input.rewind()
                s = -1
                if (LA21_41 == u'd'):
                    s = 55

                elif ((u'A' <= LA21_41 <= u'Z') or LA21_41 == u'_' or (u'a' <= LA21_41 <= u'c') or (u'e' <= LA21_41 <= u'z')):
                    s = 17

                elif ((u'\u0000' <= LA21_41 <= u'\t') or (u'\u000B' <= LA21_41 <= u'\f') or (u'\u000E' <= LA21_41 <= u'"') or (u'$' <= LA21_41 <= u'@') or (u'[' <= LA21_41 <= u'^') or LA21_41 == u'`' or (u'{' <= LA21_41 <= u'\uFFFE')) and ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]      or self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] )):
                    s = 18

                else:
                    s = 56

                 
                input.seek(index21_41)
                if s >= 0:
                    return s
            elif s == 34: 
                LA21_16 = input.LA(1)

                 
                index21_16 = input.index()
                input.rewind()
                s = -1
                if (LA21_16 == u'n'):
                    s = 41

                elif ((u'A' <= LA21_16 <= u'Z') or LA21_16 == u'_' or (u'a' <= LA21_16 <= u'm') or (u'o' <= LA21_16 <= u'z')):
                    s = 17

                elif ((u'\u0000' <= LA21_16 <= u'\t') or (u'\u000B' <= LA21_16 <= u'\f') or (u'\u000E' <= LA21_16 <= u'"') or (u'$' <= LA21_16 <= u'@') or (u'[' <= LA21_16 <= u'^') or LA21_16 == u'`' or (u'{' <= LA21_16 <= u'\uFFFE')) and ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]      or self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] )):
                    s = 18

                else:
                    s = 42

                 
                input.seek(index21_16)
                if s >= 0:
                    return s
            elif s == 35: 
                LA21_14 = input.LA(1)

                 
                index21_14 = input.index()
                input.rewind()
                s = -1
                if (LA21_14 == u'\n' or LA21_14 == u'\r'):
                    s = 20

                elif (LA21_14 == u'\t'):
                    s = 21

                elif (LA21_14 == u' '):
                    s = 22

                elif (LA21_14 == u'#') and ((self.getColumn() > 0  or self.getColumn() == 0)):
                    s = 23

                elif ((u'\u0000' <= LA21_14 <= u'\b') or (u'\u000B' <= LA21_14 <= u'\f') or (u'\u000E' <= LA21_14 <= u'\u001F') or (u'!' <= LA21_14 <= u'"') or (u'$' <= LA21_14 <= u'\uFFFE')) and ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]      or self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] )):
                    s = 18

                else:
                    s = 19

                 
                input.seek(index21_14)
                if s >= 0:
                    return s
            elif s == 36: 
                LA21_2 = input.LA(1)

                 
                index21_2 = input.index()
                input.rewind()
                s = -1
                if (LA21_2 == u'\n' or LA21_2 == u'\r'):
                    s = 20

                elif (LA21_2 == u'\t'):
                    s = 21

                elif (LA21_2 == u' '):
                    s = 22

                elif (LA21_2 == u'#') and ((self.getColumn() > 0  or self.getColumn() == 0)):
                    s = 23

                elif ((u'\u0000' <= LA21_2 <= u'\b') or (u'\u000B' <= LA21_2 <= u'\f') or (u'\u000E' <= LA21_2 <= u'\u001F') or (u'!' <= LA21_2 <= u'"') or (u'$' <= LA21_2 <= u'\uFFFE')) and ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]      or self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] )):
                    s = 18

                else:
                    s = 19

                 
                input.seek(index21_2)
                if s >= 0:
                    return s
            elif s == 37: 
                LA21_3 = input.LA(1)

                 
                index21_3 = input.index()
                input.rewind()
                s = -1
                if ((u'\u0000' <= LA21_3 <= u'\t') or (u'\u000B' <= LA21_3 <= u'\f') or (u'\u000E' <= LA21_3 <= u'"') or (u'$' <= LA21_3 <= u'\uFFFE')) and ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]      or self.getColumn() > 0  or self.getColumn() == 0 or self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] )):
                    s = 24

                elif (LA21_3 == u'\r' or LA21_3 == u'#') and ((self.getColumn() > 0  or self.getColumn() == 0)):
                    s = 26

                elif (LA21_3 == u'\n') and (self.getColumn() == 0):
                    s = 27

                else:
                    s = 25

                 
                input.seek(index21_3)
                if s >= 0:
                    return s
            elif s == 38: 
                LA21_11 = input.LA(1)

                 
                index21_11 = input.index()
                input.rewind()
                s = -1
                if ((u'A' <= LA21_11 <= u'Z') or LA21_11 == u'_' or (u'a' <= LA21_11 <= u'z')):
                    s = 38

                elif ((u'\u0000' <= LA21_11 <= u'\t') or (u'\u000B' <= LA21_11 <= u'\f') or (u'\u000E' <= LA21_11 <= u'"') or (u'$' <= LA21_11 <= u'@') or (u'[' <= LA21_11 <= u'^') or LA21_11 == u'`' or (u'{' <= LA21_11 <= u'\uFFFE')) and ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]      or self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] )):
                    s = 18

                else:
                    s = 13

                 
                input.seek(index21_11)
                if s >= 0:
                    return s
            elif s == 39: 
                LA21_22 = input.LA(1)

                 
                index21_22 = input.index()
                input.rewind()
                s = -1
                if (LA21_22 == u'\n' or LA21_22 == u'\r'):
                    s = 20

                elif (LA21_22 == u'\t'):
                    s = 21

                elif (LA21_22 == u' '):
                    s = 22

                elif (LA21_22 == u'#') and ((self.getColumn() > 0  or self.getColumn() == 0)):
                    s = 23

                elif ((u'\u0000' <= LA21_22 <= u'\b') or (u'\u000B' <= LA21_22 <= u'\f') or (u'\u000E' <= LA21_22 <= u'\u001F') or (u'!' <= LA21_22 <= u'"') or (u'$' <= LA21_22 <= u'\uFFFE')) and ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]      or self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] )):
                    s = 18

                else:
                    s = 40

                 
                input.seek(index21_22)
                if s >= 0:
                    return s
            elif s == 40: 
                LA21_46 = input.LA(1)

                 
                index21_46 = input.index()
                input.rewind()
                s = -1
                if ((u'0' <= LA21_46 <= u'9') or (u'A' <= LA21_46 <= u'F') or (u'a' <= LA21_46 <= u'f')):
                    s = 59

                elif ((u'\u0000' <= LA21_46 <= u'\t') or (u'\u000B' <= LA21_46 <= u'\f') or (u'\u000E' <= LA21_46 <= u'"') or (u'$' <= LA21_46 <= u'/') or (u':' <= LA21_46 <= u'@') or (u'G' <= LA21_46 <= u'`') or (u'g' <= LA21_46 <= u'\uFFFE')) and ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]      or self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] )):
                    s = 18

                else:
                    s = 40

                 
                input.seek(index21_46)
                if s >= 0:
                    return s
            elif s == 41: 
                LA21_73 = input.LA(1)

                 
                index21_73 = input.index()
                input.rewind()
                s = -1
                if ((u'0' <= LA21_73 <= u'9') or (u'A' <= LA21_73 <= u'F') or (u'a' <= LA21_73 <= u'f')):
                    s = 75

                elif ((u'\u0000' <= LA21_73 <= u'\t') or (u'\u000B' <= LA21_73 <= u'\f') or (u'\u000E' <= LA21_73 <= u'"') or (u'$' <= LA21_73 <= u'/') or (u':' <= LA21_73 <= u'@') or (u'G' <= LA21_73 <= u'`') or (u'g' <= LA21_73 <= u'\uFFFE')) and ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]      or self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] )):
                    s = 18

                else:
                    s = 40

                 
                input.seek(index21_73)
                if s >= 0:
                    return s
            elif s == 42: 
                LA21_67 = input.LA(1)

                 
                index21_67 = input.index()
                input.rewind()
                s = -1
                if ((u'0' <= LA21_67 <= u'9') or (u'A' <= LA21_67 <= u'F') or (u'a' <= LA21_67 <= u'f')):
                    s = 71

                elif ((u'\u0000' <= LA21_67 <= u'\t') or (u'\u000B' <= LA21_67 <= u'\f') or (u'\u000E' <= LA21_67 <= u'"') or (u'$' <= LA21_67 <= u'/') or (u':' <= LA21_67 <= u'@') or (u'G' <= LA21_67 <= u'`') or (u'g' <= LA21_67 <= u'\uFFFE')) and ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]      or self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] )):
                    s = 18

                else:
                    s = 40

                 
                input.seek(index21_67)
                if s >= 0:
                    return s
            elif s == 43: 
                LA21_21 = input.LA(1)

                 
                index21_21 = input.index()
                input.rewind()
                s = -1
                if (LA21_21 == u'\n' or LA21_21 == u'\r'):
                    s = 20

                elif (LA21_21 == u'\t'):
                    s = 21

                elif (LA21_21 == u' '):
                    s = 22

                elif (LA21_21 == u'#') and ((self.getColumn() > 0  or self.getColumn() == 0)):
                    s = 23

                elif ((u'\u0000' <= LA21_21 <= u'\b') or (u'\u000B' <= LA21_21 <= u'\f') or (u'\u000E' <= LA21_21 <= u'\u001F') or (u'!' <= LA21_21 <= u'"') or (u'$' <= LA21_21 <= u'\uFFFE')) and ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]      or self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] )):
                    s = 18

                else:
                    s = 40

                 
                input.seek(index21_21)
                if s >= 0:
                    return s

            nvae = NoViableAltException(self_.getDescription(), 21, _s, input)
            self_.error(nvae)
            raise nvae
 

