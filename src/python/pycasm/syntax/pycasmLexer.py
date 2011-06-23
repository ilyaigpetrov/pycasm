# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g 2011-06-23 13:21:06

import sys
from antlr3 import *
from antlr3.compat import set, frozenset
         
import decimal
infinity = decimal.Decimal('Infinity')



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
HexDigit=25
INDENT=5
NAME=11
WS=14
NEWLINE=9
NonWS=19
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


class pycasmLexer(Lexer):

    grammarFileName = "/root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 18, 2009 10:09:25")
    antlr_version_str = "3.1.3 Mar 18, 2009 10:09:25"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(pycasmLexer, self).__init__(input, state)


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




    # $ANTLR start "DOT_END"
    def mDOT_END(self, ):

        try:
            _type = DOT_END
            _channel = DEFAULT_CHANNEL

            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:88:2: ( '.end' )
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:89:3: '.end'
            pass 
            self.match(".end")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DOT_END"



    # $ANTLR start "DOT_NAME"
    def mDOT_NAME(self, ):

        try:
            _type = DOT_NAME
            _channel = DEFAULT_CHANNEL

            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:93:2: ( '.' NAME )
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:94:3: '.' NAME
            pass 
            self.match(46)
            self.mNAME()



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DOT_NAME"



    # $ANTLR start "DOT_DOT_NAME"
    def mDOT_DOT_NAME(self, ):

        try:
            _type = DOT_DOT_NAME
            _channel = DEFAULT_CHANNEL

            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:98:2: ( '..' NAME )
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:99:3: '..' NAME
            pass 
            self.match("..")
            self.mNAME()



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DOT_DOT_NAME"



    # $ANTLR start "COMMENT"
    def mCOMMENT(self, ):

        try:
            _type = COMMENT
            _channel = DEFAULT_CHANNEL

                   
            _channel=HIDDEN

            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:106:2: ({...}? => ( WS )* '#' (~ '\\n' )* ( '\\n' )* | {...}? => ( WS )* '#' (~ '\\n' )* )
            alt6 = 2
            alt6 = self.dfa6.predict(self.input)
            if alt6 == 1:
                # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:106:7: {...}? => ( WS )* '#' (~ '\\n' )* ( '\\n' )*
                pass 
                if not ((self.getColumn() == 0)):
                    raise FailedPredicateException(self.input, "COMMENT", "self.getColumn() == 0")

                # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:106:35: ( WS )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == 9 or LA1_0 == 32) :
                        alt1 = 1


                    if alt1 == 1:
                        # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:106:35: WS
                        pass 
                        self.mWS()


                    else:
                        break #loop1
                self.match(35)
                # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:106:43: (~ '\\n' )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if ((0 <= LA2_0 <= 9) or (11 <= LA2_0 <= 65535)) :
                        alt2 = 1


                    if alt2 == 1:
                        # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:106:44: ~ '\\n'
                        pass 
                        if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 65535):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse



                    else:
                        break #loop2
                # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:106:52: ( '\\n' )*
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == 10) :
                        alt3 = 1


                    if alt3 == 1:
                        # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:106:52: '\\n'
                        pass 
                        self.match(10)


                    else:
                        break #loop3


            elif alt6 == 2:
                # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:107:7: {...}? => ( WS )* '#' (~ '\\n' )*
                pass 
                if not ((self.getColumn() > 0 )):
                    raise FailedPredicateException(self.input, "COMMENT", "self.getColumn() > 0 ")

                # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:107:35: ( WS )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == 9 or LA4_0 == 32) :
                        alt4 = 1


                    if alt4 == 1:
                        # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:107:35: WS
                        pass 
                        self.mWS()


                    else:
                        break #loop4
                self.match(35)
                # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:107:43: (~ '\\n' )*
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if ((0 <= LA5_0 <= 9) or (11 <= LA5_0 <= 65535)) :
                        alt5 = 1


                    if alt5 == 1:
                        # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:107:44: ~ '\\n'
                        pass 
                        if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 65535):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse



                    else:
                        break #loop5


            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COMMENT"



    # $ANTLR start "DOT_ARGS"
    def mDOT_ARGS(self, ):

        try:
            _type = DOT_ARGS
            _channel = DEFAULT_CHANNEL

            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:111:2: ({...}? =>~ ( Alpha | '\\n' | '\\r' ) (~ ( '\\n' | '\\r' | '#' ) )+ )
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:112:2: {...}? =>~ ( Alpha | '\\n' | '\\r' ) (~ ( '\\n' | '\\r' | '#' ) )+
            pass 
            if not ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     )):
                raise FailedPredicateException(self.input, "DOT_ARGS", " self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     ")

            if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 64) or (91 <= self.input.LA(1) <= 96) or (123 <= self.input.LA(1) <= 65535):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:112:102: (~ ( '\\n' | '\\r' | '#' ) )+
            cnt7 = 0
            while True: #loop7
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if ((0 <= LA7_0 <= 9) or (11 <= LA7_0 <= 12) or (14 <= LA7_0 <= 34) or (36 <= LA7_0 <= 65535)) :
                    alt7 = 1


                if alt7 == 1:
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:112:102: ~ ( '\\n' | '\\r' | '#' )
                    pass 
                    if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 34) or (36 <= self.input.LA(1) <= 65535):
                        self.input.consume()
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



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DOT_ARGS"



    # $ANTLR start "DOT_DOT_ARGS"
    def mDOT_DOT_ARGS(self, ):

        try:
            _type = DOT_DOT_ARGS
            _channel = DEFAULT_CHANNEL

            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:116:2: ({...}? =>~ ( Alpha | '\\n' | '\\r' ) (~ ( '\\n' | '\\r' | '#' ) )+ )
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:117:2: {...}? =>~ ( Alpha | '\\n' | '\\r' ) (~ ( '\\n' | '\\r' | '#' ) )+
            pass 
            if not ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] )):
                raise FailedPredicateException(self.input, "DOT_DOT_ARGS", " self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] ")

            if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 64) or (91 <= self.input.LA(1) <= 96) or (123 <= self.input.LA(1) <= 65535):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:117:102: (~ ( '\\n' | '\\r' | '#' ) )+
            cnt8 = 0
            while True: #loop8
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if ((0 <= LA8_0 <= 9) or (11 <= LA8_0 <= 12) or (14 <= LA8_0 <= 34) or (36 <= LA8_0 <= 65535)) :
                    alt8 = 1


                if alt8 == 1:
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:117:102: ~ ( '\\n' | '\\r' | '#' )
                    pass 
                    if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 34) or (36 <= self.input.LA(1) <= 65535):
                        self.input.consume()
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



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DOT_DOT_ARGS"



    # $ANTLR start "DOT_DOT_BODY"
    def mDOT_DOT_BODY(self, ):

        try:
            _type = DOT_DOT_BODY
            _channel = DEFAULT_CHANNEL

                   
            self.numberOfSpacesInPythonBlock = 0
            self.minNumberOfSpacesInPythonBlock = infinity

            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:125:2: ({...}? => ( ( '\\r' )? '\\n' ( ' ' | '\\t' )* ({...}? => ( NonWS ( NonWS | WS )* ) )? )* )
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:125:4: {...}? => ( ( '\\r' )? '\\n' ( ' ' | '\\t' )* ({...}? => ( NonWS ( NonWS | WS )* ) )? )*
            pass 
            if not ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME, DOT_DOT_ARGS] )):
                raise FailedPredicateException(self.input, "DOT_DOT_BODY", " self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME, DOT_DOT_ARGS] ")

            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:126:3: ( ( '\\r' )? '\\n' ( ' ' | '\\t' )* ({...}? => ( NonWS ( NonWS | WS )* ) )? )*
            while True: #loop13
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if (LA13_0 == 10 or LA13_0 == 13) :
                    alt13 = 1


                if alt13 == 1:
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:126:4: ( '\\r' )? '\\n' ( ' ' | '\\t' )* ({...}? => ( NonWS ( NonWS | WS )* ) )?
                    pass 
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:126:4: ( '\\r' )?
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == 13) :
                        alt9 = 1
                    if alt9 == 1:
                        # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:126:4: '\\r'
                        pass 
                        self.match(13)



                    self.match(10)
                    #action start
                    self.numberOfSpacesInPythonBlock = 0 
                    #action end
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:128:7: ( ' ' | '\\t' )*
                    while True: #loop10
                        alt10 = 3
                        LA10_0 = self.input.LA(1)

                        if (LA10_0 == 32) :
                            alt10 = 1
                        elif (LA10_0 == 9) :
                            alt10 = 2


                        if alt10 == 1:
                            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:129:5: ' '
                            pass 
                            self.match(32)
                            #action start
                            self.numberOfSpacesInPythonBlock += 1 
                            #action end


                        elif alt10 == 2:
                            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:130:5: '\\t'
                            pass 
                            self.match(9)
                            #action start
                            self.numberOfSpacesInPythonBlock += 8 
                            #action end


                        else:
                            break #loop10
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:132:7: ({...}? => ( NonWS ( NonWS | WS )* ) )?
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if ((0 <= LA12_0 <= 8) or (11 <= LA12_0 <= 12) or (14 <= LA12_0 <= 31) or (33 <= LA12_0 <= 65535)) and ((min(self.minNumberOfSpacesInPythonBlock, self.numberOfSpacesInPythonBlock) > self.numberOfSpaces )):
                        alt12 = 1
                    if alt12 == 1:
                        # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:133:4: {...}? => ( NonWS ( NonWS | WS )* )
                        pass 
                        if not ((min(self.minNumberOfSpacesInPythonBlock, self.numberOfSpacesInPythonBlock) > self.numberOfSpaces )):
                            raise FailedPredicateException(self.input, "DOT_DOT_BODY", " min(self.minNumberOfSpacesInPythonBlock, self.numberOfSpacesInPythonBlock) > self.numberOfSpaces ")

                        # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:133:109: ( NonWS ( NonWS | WS )* )
                        # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:134:5: NonWS ( NonWS | WS )*
                        pass 
                        self.mNonWS()
                        # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:134:11: ( NonWS | WS )*
                        while True: #loop11
                            alt11 = 2
                            LA11_0 = self.input.LA(1)

                            if ((0 <= LA11_0 <= 9) or (11 <= LA11_0 <= 12) or (14 <= LA11_0 <= 65535)) :
                                alt11 = 1


                            if alt11 == 1:
                                # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:
                                pass 
                                if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 65535):
                                    self.input.consume()
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



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DOT_DOT_BODY"



    # $ANTLR start "HEX_DQUAD"
    def mHEX_DQUAD(self, ):

        try:
            _type = HEX_DQUAD
            _channel = DEFAULT_CHANNEL

            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:142:2: ( HEX_QUAD HEX_QUAD )
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:143:3: HEX_QUAD HEX_QUAD
            pass 
            self.mHEX_QUAD()
            self.mHEX_QUAD()



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "HEX_DQUAD"



    # $ANTLR start "HEX_QUAD"
    def mHEX_QUAD(self, ):

        try:
            _type = HEX_QUAD
            _channel = DEFAULT_CHANNEL

            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:147:2: ( HEX_PAIR HEX_PAIR )
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:148:3: HEX_PAIR HEX_PAIR
            pass 
            self.mHEX_PAIR()
            self.mHEX_PAIR()



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "HEX_QUAD"



    # $ANTLR start "HEX_PAIR"
    def mHEX_PAIR(self, ):

        try:
            _type = HEX_PAIR
            _channel = DEFAULT_CHANNEL

            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:152:2: ( HEX_DIGIT HEX_DIGIT )
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:153:3: HEX_DIGIT HEX_DIGIT
            pass 
            self.mHEX_DIGIT()
            self.mHEX_DIGIT()



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "HEX_PAIR"



    # $ANTLR start "HEX_DIGIT"
    def mHEX_DIGIT(self, ):

        try:
            _type = HEX_DIGIT
            _channel = DEFAULT_CHANNEL

            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:157:2: ( HexDigit )
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:158:3: HexDigit
            pass 
            self.mHexDigit()



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "HEX_DIGIT"



    # $ANTLR start "TYPED_VALUE"
    def mTYPED_VALUE(self, ):

        try:
            _type = TYPED_VALUE
            _channel = DEFAULT_CHANNEL

            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:169:2: ( Type '\\'' (~ ( '\\'' ) )* '\\'' )
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:170:3: Type '\\'' (~ ( '\\'' ) )* '\\''
            pass 
            self.mType()
            self.match(39)
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:170:13: (~ ( '\\'' ) )*
            while True: #loop14
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if ((0 <= LA14_0 <= 38) or (40 <= LA14_0 <= 65535)) :
                    alt14 = 1


                if alt14 == 1:
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:170:13: ~ ( '\\'' )
                    pass 
                    if (0 <= self.input.LA(1) <= 38) or (40 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop14
            self.match(39)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "TYPED_VALUE"



    # $ANTLR start "STRING"
    def mSTRING(self, ):

        try:
            _type = STRING
            _channel = DEFAULT_CHANNEL

            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:174:2: ( '\\'' (~ ( '\\'' ) )+ '\\'' )
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:174:4: '\\'' (~ ( '\\'' ) )+ '\\''
            pass 
            self.match(39)
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:174:9: (~ ( '\\'' ) )+
            cnt15 = 0
            while True: #loop15
                alt15 = 2
                LA15_0 = self.input.LA(1)

                if ((0 <= LA15_0 <= 38) or (40 <= LA15_0 <= 65535)) :
                    alt15 = 1


                if alt15 == 1:
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:174:9: ~ ( '\\'' )
                    pass 
                    if (0 <= self.input.LA(1) <= 38) or (40 <= self.input.LA(1) <= 65535):
                        self.input.consume()
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
            self.match(39)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STRING"



    # $ANTLR start "NAME"
    def mNAME(self, ):

        try:
            _type = NAME
            _channel = DEFAULT_CHANNEL

            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:177:6: ( ( Alpha | '_' )+ )
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:178:3: ( Alpha | '_' )+
            pass 
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:178:3: ( Alpha | '_' )+
            cnt16 = 0
            while True: #loop16
                alt16 = 2
                LA16_0 = self.input.LA(1)

                if ((65 <= LA16_0 <= 90) or LA16_0 == 95 or (97 <= LA16_0 <= 122)) :
                    alt16 = 1


                if alt16 == 1:
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:
                    pass 
                    if (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                        self.input.consume()
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



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NAME"



    # $ANTLR start "INDENT_OR_DEDENT"
    def mINDENT_OR_DEDENT(self, ):

        try:
            _type = INDENT_OR_DEDENT
            _channel = DEFAULT_CHANNEL

                   
            self.numberOfSpaces = 0

            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:185:2: ( ( ( ( '\\r' )? '\\n' ) | '\\t' | ' ' )* ( ( '\\r' )? '\\n' ) ( ' ' | '\\t' )* )
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:186:3: ( ( ( '\\r' )? '\\n' ) | '\\t' | ' ' )* ( ( '\\r' )? '\\n' ) ( ' ' | '\\t' )*
            pass 
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:186:3: ( ( ( '\\r' )? '\\n' ) | '\\t' | ' ' )*
            while True: #loop18
                alt18 = 4
                alt18 = self.dfa18.predict(self.input)
                if alt18 == 1:
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:186:5: ( ( '\\r' )? '\\n' )
                    pass 
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:186:5: ( ( '\\r' )? '\\n' )
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:186:7: ( '\\r' )? '\\n'
                    pass 
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:186:7: ( '\\r' )?
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if (LA17_0 == 13) :
                        alt17 = 1
                    if alt17 == 1:
                        # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:186:8: '\\r'
                        pass 
                        self.match(13)



                    self.match(10)





                elif alt18 == 2:
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:186:24: '\\t'
                    pass 
                    self.match(9)


                elif alt18 == 3:
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:186:31: ' '
                    pass 
                    self.match(32)


                else:
                    break #loop18
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:187:3: ( ( '\\r' )? '\\n' )
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:187:5: ( '\\r' )? '\\n'
            pass 
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:187:5: ( '\\r' )?
            alt19 = 2
            LA19_0 = self.input.LA(1)

            if (LA19_0 == 13) :
                alt19 = 1
            if alt19 == 1:
                # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:187:6: '\\r'
                pass 
                self.match(13)



            self.match(10)



            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:188:3: ( ' ' | '\\t' )*
            while True: #loop20
                alt20 = 3
                LA20_0 = self.input.LA(1)

                if (LA20_0 == 32) :
                    alt20 = 1
                elif (LA20_0 == 9) :
                    alt20 = 2


                if alt20 == 1:
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:188:5: ' '
                    pass 
                    self.match(32)
                    #action start
                    self.numberOfSpaces += 1 
                    #action end


                elif alt20 == 2:
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:189:5: '\\t'
                    pass 
                    self.match(9)
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



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INDENT_OR_DEDENT"



    # $ANTLR start "WS"
    def mWS(self, ):

        try:
            _type = WS
            _channel = DEFAULT_CHANNEL

            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:217:4: ( ( ' ' | '\\t' ) )
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:217:6: ( ' ' | '\\t' )
            pass 
            if self.input.LA(1) == 9 or self.input.LA(1) == 32:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WS"



    # $ANTLR start "NonWS"
    def mNonWS(self, ):

        try:
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:224:2: (~ ( WS | '\\n' | '\\r' ) )
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:225:3: ~ ( WS | '\\n' | '\\r' )
            pass 
            if (0 <= self.input.LA(1) <= 8) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 31) or (33 <= self.input.LA(1) <= 65535):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "NonWS"



    # $ANTLR start "AlphaNum"
    def mAlphaNum(self, ):

        try:
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:230:9: ( ( Alpha | Digit ) )
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:231:3: ( Alpha | Digit )
            pass 
            if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "AlphaNum"



    # $ANTLR start "Type"
    def mType(self, ):

        try:
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:235:6: ( 's' | 't' )
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:
            pass 
            if (115 <= self.input.LA(1) <= 116):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "Type"



    # $ANTLR start "Alpha"
    def mAlpha(self, ):

        try:
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:241:2: ( ( 'a' .. 'z' | 'A' .. 'Z' ) )
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:242:3: ( 'a' .. 'z' | 'A' .. 'Z' )
            pass 
            if (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "Alpha"



    # $ANTLR start "HexAlpha"
    def mHexAlpha(self, ):

        try:
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:247:2: ( ( 'a' .. 'f' | 'A' .. 'F' ) )
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:248:3: ( 'a' .. 'f' | 'A' .. 'F' )
            pass 
            if (65 <= self.input.LA(1) <= 70) or (97 <= self.input.LA(1) <= 102):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "HexAlpha"



    # $ANTLR start "HexDigit"
    def mHexDigit(self, ):

        try:
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:253:2: ( ( HexAlpha | Digit ) )
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:254:3: ( HexAlpha | Digit )
            pass 
            if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 70) or (97 <= self.input.LA(1) <= 102):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "HexDigit"



    # $ANTLR start "Digit"
    def mDigit(self, ):

        try:
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:258:7: ( '0' .. '9' )
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:259:3: '0' .. '9'
            pass 
            self.matchRange(48, 57)




        finally:

            pass

    # $ANTLR end "Digit"



    def mTokens(self):
        # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:1:8: ( DOT_END | DOT_NAME | DOT_DOT_NAME | COMMENT | DOT_ARGS | DOT_DOT_ARGS | DOT_DOT_BODY | HEX_DQUAD | HEX_QUAD | HEX_PAIR | HEX_DIGIT | TYPED_VALUE | STRING | NAME | INDENT_OR_DEDENT | WS )
        alt21 = 16
        alt21 = self.dfa21.predict(self.input)
        if alt21 == 1:
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:1:10: DOT_END
            pass 
            self.mDOT_END()


        elif alt21 == 2:
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:1:18: DOT_NAME
            pass 
            self.mDOT_NAME()


        elif alt21 == 3:
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:1:27: DOT_DOT_NAME
            pass 
            self.mDOT_DOT_NAME()


        elif alt21 == 4:
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:1:40: COMMENT
            pass 
            self.mCOMMENT()


        elif alt21 == 5:
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:1:48: DOT_ARGS
            pass 
            self.mDOT_ARGS()


        elif alt21 == 6:
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:1:57: DOT_DOT_ARGS
            pass 
            self.mDOT_DOT_ARGS()


        elif alt21 == 7:
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:1:70: DOT_DOT_BODY
            pass 
            self.mDOT_DOT_BODY()


        elif alt21 == 8:
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:1:83: HEX_DQUAD
            pass 
            self.mHEX_DQUAD()


        elif alt21 == 9:
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:1:93: HEX_QUAD
            pass 
            self.mHEX_QUAD()


        elif alt21 == 10:
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:1:102: HEX_PAIR
            pass 
            self.mHEX_PAIR()


        elif alt21 == 11:
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:1:111: HEX_DIGIT
            pass 
            self.mHEX_DIGIT()


        elif alt21 == 12:
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:1:121: TYPED_VALUE
            pass 
            self.mTYPED_VALUE()


        elif alt21 == 13:
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:1:133: STRING
            pass 
            self.mSTRING()


        elif alt21 == 14:
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:1:140: NAME
            pass 
            self.mNAME()


        elif alt21 == 15:
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:1:145: INDENT_OR_DEDENT
            pass 
            self.mINDENT_OR_DEDENT()


        elif alt21 == 16:
            # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmLexer.g:1:162: WS
            pass 
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
        u"\1\2\1\0\1\1\2\uffff"
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
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA6_1 = input.LA(1)

                 
                index6_1 = input.index()
                input.rewind()
                s = -1
                if (LA6_1 == 35) and (((self.getColumn() > 0 ) or (self.getColumn() == 0))):
                    s = 2

                elif (LA6_1 == 9 or LA6_1 == 32) and (((self.getColumn() > 0 ) or (self.getColumn() == 0))):
                    s = 1

                 
                input.seek(index6_1)
                if s >= 0:
                    return s
            elif s == 1: 
                LA6_2 = input.LA(1)

                 
                index6_2 = input.index()
                input.rewind()
                s = -1
                if ((self.getColumn() == 0)):
                    s = 3

                elif ((self.getColumn() > 0 )):
                    s = 4

                 
                input.seek(index6_2)
                if s >= 0:
                    return s
            elif s == 2: 
                LA6_0 = input.LA(1)

                 
                index6_0 = input.index()
                input.rewind()
                s = -1
                if (LA6_0 == 9 or LA6_0 == 32) and (((self.getColumn() > 0 ) or (self.getColumn() == 0))):
                    s = 1

                elif (LA6_0 == 35) and (((self.getColumn() > 0 ) or (self.getColumn() == 0))):
                    s = 2

                 
                input.seek(index6_0)
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

    class DFA18(DFA):
        pass


    # lookup tables for DFA #21

    DFA21_eot = DFA.unpack(
        u"\1\7\1\uffff\1\23\1\31\1\34\1\uffff\1\40\2\uffff\1\34\2\15\2\uffff"
        u"\1\23\1\50\1\51\1\53\1\51\2\uffff\1\51\1\uffff\1\51\1\54\4\uffff"
        u"\1\55\2\40\1\uffff\1\51\1\uffff\2\60\1\uffff\1\63\1\65\2\uffff"
        u"\1\71\3\uffff\1\51\1\73\1\uffff\1\15\2\uffff\1\76\5\uffff\1\100"
        u"\1\uffff\2\102\3\uffff\1\51\1\uffff\1\15\1\uffff\1\51\1\15\1\51"
        u"\1\15\1\113\1\104\1\uffff"
        )

    DFA21_eof = DFA.unpack(
        u"\114\uffff"
        )

    DFA21_min = DFA.unpack(
        u"\5\0\1\12\1\0\1\uffff\1\0\1\60\1\47\2\0\1\uffff\5\0\2\uffff\1\0"
        u"\1\uffff\2\0\4\uffff\5\0\1\uffff\2\60\1\uffff\12\0\1\uffff\2\60"
        u"\3\0\3\uffff\3\0\2\60\2\uffff\2\0\1\uffff\1\60\1\uffff\1\0\1\60"
        u"\1\0\1\60\1\0\1\101\1\0"
        )

    DFA21_max = DFA.unpack(
        u"\5\uffff\1\12\1\uffff\1\uffff\1\uffff\1\172\1\47\2\uffff\1\uffff"
        u"\5\uffff\2\uffff\1\uffff\1\uffff\2\uffff\4\uffff\3\uffff\1\0\1"
        u"\uffff\1\uffff\1\172\1\146\1\uffff\2\uffff\2\0\1\uffff\3\0\2\uffff"
        u"\1\uffff\2\146\1\0\1\uffff\1\0\3\uffff\1\0\1\uffff\1\0\1\172\1"
        u"\146\2\uffff\1\0\1\uffff\1\uffff\1\146\1\uffff\1\uffff\1\146\1"
        u"\uffff\1\146\1\uffff\1\172\1\0"
        )

    DFA21_accept = DFA.unpack(
        u"\7\uffff\1\7\5\uffff\1\16\5\uffff\1\20\1\4\1\uffff\1\17\2\uffff"
        u"\3\4\1\13\5\uffff\1\15\2\uffff\1\14\12\uffff\1\12\5\uffff\1\2\1"
        u"\5\1\6\5\uffff\1\1\1\3\2\uffff\1\11\1\uffff\1\10\7\uffff"
        )

    DFA21_special = DFA.unpack(
        u"\1\14\1\33\1\47\1\13\1\10\1\uffff\1\52\1\uffff\1\3\2\uffff\1\1"
        u"\1\20\1\uffff\1\50\1\0\1\26\1\23\1\21\2\uffff\1\11\1\uffff\1\24"
        u"\1\16\4\uffff\1\27\1\31\1\30\1\5\1\4\4\uffff\1\51\1\2\1\36\1\15"
        u"\1\17\1\37\1\32\1\41\1\22\1\25\3\uffff\1\44\1\53\1\35\3\uffff\1"
        u"\34\1\6\1\43\4\uffff\1\42\1\46\3\uffff\1\7\1\uffff\1\45\1\uffff"
        u"\1\12\1\uffff\1\40"
        )

            
    DFA21_transition = [
        DFA.unpack(u"\11\14\1\2\1\6\2\14\1\5\22\14\1\16\2\14\1\3\3\14\1\10"
        u"\6\14\1\1\1\14\12\4\7\14\6\11\24\15\4\14\1\13\1\14\6\11\14\15\2"
        u"\12\6\15\uff85\14"),
        DFA.unpack(u"\12\22\1\uffff\2\22\1\uffff\25\22\1\uffff\12\22\1\20"
        u"\22\22\32\21\4\22\1\21\1\22\4\21\1\17\25\21\uff85\22"),
        DFA.unpack(u"\11\22\1\25\1\26\2\22\1\26\22\22\1\27\2\22\1\24\uffdc"
        u"\22"),
        DFA.unpack(u"\12\30\1\33\2\30\1\32\25\30\1\32\uffdc\30"),
        DFA.unpack(u"\12\22\1\uffff\2\22\1\uffff\25\22\1\uffff\14\22\12"
        u"\35\7\22\6\35\32\22\6\35\uff99\22"),
        DFA.unpack(u"\1\6"),
        DFA.unpack(u"\11\7\1\36\1\6\2\7\1\5\22\7\1\37\uffdf\7"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\41\1\42\2\41\1\42\25\41\1\42\3\41\1\22\uffd8\41"),
        DFA.unpack(u"\12\44\7\uffff\6\43\24\15\4\uffff\1\15\1\uffff\6\43"
        u"\24\15"),
        DFA.unpack(u"\1\45"),
        DFA.unpack(u"\12\22\1\uffff\2\22\1\uffff\25\22\1\uffff\35\22\32"
        u"\46\4\22\1\46\1\22\32\46\uff85\22"),
        DFA.unpack(u"\12\22\1\uffff\2\22\1\uffff\25\22\1\uffff\uffdc\22"),
        DFA.unpack(u""),
        DFA.unpack(u"\11\22\1\25\1\26\2\22\1\26\22\22\1\27\2\22\1\24\uffdc"
        u"\22"),
        DFA.unpack(u"\12\22\1\uffff\2\22\1\uffff\25\22\1\uffff\35\22\32"
        u"\21\4\22\1\21\1\22\15\21\1\47\14\21\uff85\22"),
        DFA.unpack(u"\12\22\1\uffff\2\22\1\uffff\25\22\1\uffff\35\22\32"
        u"\52\4\22\1\52\1\22\32\52\uff85\22"),
        DFA.unpack(u"\12\22\1\uffff\2\22\1\uffff\25\22\1\uffff\35\22\32"
        u"\21\4\22\1\21\1\22\32\21\uff85\22"),
        DFA.unpack(u"\12\22\1\uffff\2\22\1\uffff\25\22\1\uffff\uffdc\22"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\11\22\1\25\1\26\2\22\1\26\22\22\1\27\2\22\1\24\uffdc"
        u"\22"),
        DFA.unpack(u""),
        DFA.unpack(u"\11\22\1\25\1\26\2\22\1\26\22\22\1\27\2\22\1\24\uffdc"
        u"\22"),
        DFA.unpack(u"\12\30\1\33\2\30\1\32\25\30\1\32\uffdc\30"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\22\1\uffff\2\22\1\uffff\25\22\1\uffff\14\22\12"
        u"\56\7\22\6\56\32\22\6\56\uff99\22"),
        DFA.unpack(u"\11\7\1\36\1\6\2\7\1\5\22\7\1\37\uffdf\7"),
        DFA.unpack(u"\11\7\1\36\1\6\2\7\1\5\22\7\1\37\uffdf\7"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\12\41\1\42\2\41\1\42\25\41\1\42\3\41\1\57\uffd8\41"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\62\7\uffff\6\61\24\15\4\uffff\1\15\1\uffff\6\61"
        u"\24\15"),
        DFA.unpack(u"\12\62\7\uffff\6\62\32\uffff\6\62"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\22\1\uffff\2\22\1\uffff\25\22\1\uffff\35\22\32"
        u"\46\4\22\1\46\1\22\32\46\uff85\22"),
        DFA.unpack(u"\12\22\1\uffff\2\22\1\uffff\25\22\1\uffff\35\22\32"
        u"\21\4\22\1\21\1\22\3\21\1\64\26\21\uff85\22"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\12\22\1\uffff\2\22\1\uffff\25\22\1\uffff\35\22\32"
        u"\52\4\22\1\52\1\22\32\52\uff85\22"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\12\22\1\uffff\2\22\1\uffff\25\22\1\uffff\14\22\12"
        u"\72\7\22\6\72\32\22\6\72\uff99\22"),
        DFA.unpack(u"\12\22\1\uffff\2\22\1\uffff\25\22\1\uffff\uffdc\22"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\75\7\uffff\6\74\32\uffff\6\74"),
        DFA.unpack(u"\12\75\7\uffff\6\75\32\uffff\6\75"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\12\22\1\uffff\2\22\1\uffff\25\22\1\uffff\35\22\32"
        u"\21\4\22\1\21\1\22\32\21\uff85\22"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\12\22\1\uffff\2\22\1\uffff\25\22\1\uffff\14\22\12"
        u"\101\7\22\6\101\32\22\6\101\uff99\22"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\12\104\7\uffff\6\103\24\15\4\uffff\1\15\1\uffff\6"
        u"\103\24\15"),
        DFA.unpack(u"\12\104\7\uffff\6\104\32\uffff\6\104"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\12\22\1\uffff\2\22\1\uffff\25\22\1\uffff\14\22\12"
        u"\105\7\22\6\105\32\22\6\105\uff99\22"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\104\7\uffff\6\106\32\uffff\6\106"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\22\1\uffff\2\22\1\uffff\25\22\1\uffff\14\22\12"
        u"\107\7\22\6\107\32\22\6\107\uff99\22"),
        DFA.unpack(u"\12\104\7\uffff\6\110\32\uffff\6\110"),
        DFA.unpack(u"\12\22\1\uffff\2\22\1\uffff\25\22\1\uffff\14\22\12"
        u"\111\7\22\6\111\32\22\6\111\uff99\22"),
        DFA.unpack(u"\12\104\7\uffff\6\112\32\uffff\6\112"),
        DFA.unpack(u"\12\22\1\uffff\2\22\1\uffff\25\22\1\uffff\uffdc\22"),
        DFA.unpack(u"\32\15\4\uffff\1\15\1\uffff\32\15"),
        DFA.unpack(u"\1\uffff")
    ]

    # class definition for DFA #21

    class DFA21(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA21_15 = input.LA(1)

                 
                index21_15 = input.index()
                input.rewind()
                s = -1
                if (LA21_15 == 110):
                    s = 39

                elif ((65 <= LA21_15 <= 90) or LA21_15 == 95 or (97 <= LA21_15 <= 109) or (111 <= LA21_15 <= 122)):
                    s = 17

                elif ((0 <= LA21_15 <= 9) or (11 <= LA21_15 <= 12) or (14 <= LA21_15 <= 34) or (36 <= LA21_15 <= 64) or (91 <= LA21_15 <= 94) or LA21_15 == 96 or (123 <= LA21_15 <= 65535)) and (((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     ) or (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] ))):
                    s = 18

                else:
                    s = 40

                 
                input.seek(index21_15)
                if s >= 0:
                    return s
            elif s == 1: 
                LA21_11 = input.LA(1)

                 
                index21_11 = input.index()
                input.rewind()
                s = -1
                if ((65 <= LA21_11 <= 90) or LA21_11 == 95 or (97 <= LA21_11 <= 122)):
                    s = 38

                elif ((0 <= LA21_11 <= 9) or (11 <= LA21_11 <= 12) or (14 <= LA21_11 <= 34) or (36 <= LA21_11 <= 64) or (91 <= LA21_11 <= 94) or LA21_11 == 96 or (123 <= LA21_11 <= 65535)) and (((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     ) or (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] ))):
                    s = 18

                else:
                    s = 13

                 
                input.seek(index21_11)
                if s >= 0:
                    return s
            elif s == 2: 
                LA21_39 = input.LA(1)

                 
                index21_39 = input.index()
                input.rewind()
                s = -1
                if (LA21_39 == 100):
                    s = 52

                elif ((65 <= LA21_39 <= 90) or LA21_39 == 95 or (97 <= LA21_39 <= 99) or (101 <= LA21_39 <= 122)):
                    s = 17

                elif ((0 <= LA21_39 <= 9) or (11 <= LA21_39 <= 12) or (14 <= LA21_39 <= 34) or (36 <= LA21_39 <= 64) or (91 <= LA21_39 <= 94) or LA21_39 == 96 or (123 <= LA21_39 <= 65535)) and (((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     ) or (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] ))):
                    s = 18

                else:
                    s = 53

                 
                input.seek(index21_39)
                if s >= 0:
                    return s
            elif s == 3: 
                LA21_8 = input.LA(1)

                 
                index21_8 = input.index()
                input.rewind()
                s = -1
                if ((0 <= LA21_8 <= 9) or (11 <= LA21_8 <= 12) or (14 <= LA21_8 <= 34) or (36 <= LA21_8 <= 38) or (40 <= LA21_8 <= 65535)):
                    s = 33

                elif (LA21_8 == 10 or LA21_8 == 13 or LA21_8 == 35):
                    s = 34

                elif (LA21_8 == 39) and (((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     ) or (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] ))):
                    s = 18

                 
                input.seek(index21_8)
                if s >= 0:
                    return s
            elif s == 4: 
                LA21_33 = input.LA(1)

                 
                index21_33 = input.index()
                input.rewind()
                s = -1
                if (LA21_33 == 39):
                    s = 47

                elif ((0 <= LA21_33 <= 9) or (11 <= LA21_33 <= 12) or (14 <= LA21_33 <= 34) or (36 <= LA21_33 <= 38) or (40 <= LA21_33 <= 65535)):
                    s = 33

                elif (LA21_33 == 10 or LA21_33 == 13 or LA21_33 == 35):
                    s = 34

                else:
                    s = 41

                 
                input.seek(index21_33)
                if s >= 0:
                    return s
            elif s == 5: 
                LA21_32 = input.LA(1)

                 
                index21_32 = input.index()
                input.rewind()
                s = -1
                if ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME, DOT_DOT_ARGS] )):
                    s = 7

                elif (True):
                    s = 22

                 
                input.seek(index21_32)
                if s >= 0:
                    return s
            elif s == 6: 
                LA21_58 = input.LA(1)

                 
                index21_58 = input.index()
                input.rewind()
                s = -1
                if ((48 <= LA21_58 <= 57) or (65 <= LA21_58 <= 70) or (97 <= LA21_58 <= 102)):
                    s = 65

                elif ((0 <= LA21_58 <= 9) or (11 <= LA21_58 <= 12) or (14 <= LA21_58 <= 34) or (36 <= LA21_58 <= 47) or (58 <= LA21_58 <= 64) or (71 <= LA21_58 <= 96) or (103 <= LA21_58 <= 65535)) and (((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     ) or (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] ))):
                    s = 18

                else:
                    s = 64

                 
                input.seek(index21_58)
                if s >= 0:
                    return s
            elif s == 7: 
                LA21_69 = input.LA(1)

                 
                index21_69 = input.index()
                input.rewind()
                s = -1
                if ((48 <= LA21_69 <= 57) or (65 <= LA21_69 <= 70) or (97 <= LA21_69 <= 102)):
                    s = 71

                elif ((0 <= LA21_69 <= 9) or (11 <= LA21_69 <= 12) or (14 <= LA21_69 <= 34) or (36 <= LA21_69 <= 47) or (58 <= LA21_69 <= 64) or (71 <= LA21_69 <= 96) or (103 <= LA21_69 <= 65535)) and (((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     ) or (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] ))):
                    s = 18

                else:
                    s = 41

                 
                input.seek(index21_69)
                if s >= 0:
                    return s
            elif s == 8: 
                LA21_4 = input.LA(1)

                 
                index21_4 = input.index()
                input.rewind()
                s = -1
                if ((48 <= LA21_4 <= 57) or (65 <= LA21_4 <= 70) or (97 <= LA21_4 <= 102)):
                    s = 29

                elif ((0 <= LA21_4 <= 9) or (11 <= LA21_4 <= 12) or (14 <= LA21_4 <= 34) or (36 <= LA21_4 <= 47) or (58 <= LA21_4 <= 64) or (71 <= LA21_4 <= 96) or (103 <= LA21_4 <= 65535)) and (((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     ) or (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] ))):
                    s = 18

                else:
                    s = 28

                 
                input.seek(index21_4)
                if s >= 0:
                    return s
            elif s == 9: 
                LA21_21 = input.LA(1)

                 
                index21_21 = input.index()
                input.rewind()
                s = -1
                if (LA21_21 == 35) and (((self.getColumn() > 0 ) or (self.getColumn() == 0))):
                    s = 20

                elif (LA21_21 == 9):
                    s = 21

                elif (LA21_21 == 10 or LA21_21 == 13):
                    s = 22

                elif (LA21_21 == 32):
                    s = 23

                elif ((0 <= LA21_21 <= 8) or (11 <= LA21_21 <= 12) or (14 <= LA21_21 <= 31) or (33 <= LA21_21 <= 34) or (36 <= LA21_21 <= 65535)) and (((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     ) or (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] ))):
                    s = 18

                else:
                    s = 41

                 
                input.seek(index21_21)
                if s >= 0:
                    return s
            elif s == 10: 
                LA21_73 = input.LA(1)

                 
                index21_73 = input.index()
                input.rewind()
                s = -1
                if ((0 <= LA21_73 <= 9) or (11 <= LA21_73 <= 12) or (14 <= LA21_73 <= 34) or (36 <= LA21_73 <= 65535)) and (((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     ) or (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] ))):
                    s = 18

                else:
                    s = 75

                 
                input.seek(index21_73)
                if s >= 0:
                    return s
            elif s == 11: 
                LA21_3 = input.LA(1)

                 
                index21_3 = input.index()
                input.rewind()
                s = -1
                if ((0 <= LA21_3 <= 9) or (11 <= LA21_3 <= 12) or (14 <= LA21_3 <= 34) or (36 <= LA21_3 <= 65535)) and (((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     ) or (self.getColumn() > 0 ) or (self.getColumn() == 0) or (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] ))):
                    s = 24

                elif (LA21_3 == 13 or LA21_3 == 35) and (((self.getColumn() > 0 ) or (self.getColumn() == 0))):
                    s = 26

                elif (LA21_3 == 10) and ((self.getColumn() == 0)):
                    s = 27

                else:
                    s = 25

                 
                input.seek(index21_3)
                if s >= 0:
                    return s
            elif s == 12: 
                LA21_0 = input.LA(1)

                 
                index21_0 = input.index()
                input.rewind()
                s = -1
                if (LA21_0 == 46):
                    s = 1

                elif (LA21_0 == 9):
                    s = 2

                elif (LA21_0 == 35) and (((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     ) or (self.getColumn() > 0 ) or (self.getColumn() == 0) or (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] ))):
                    s = 3

                elif ((48 <= LA21_0 <= 57)):
                    s = 4

                elif (LA21_0 == 13):
                    s = 5

                elif (LA21_0 == 10):
                    s = 6

                elif (LA21_0 == 39):
                    s = 8

                elif ((65 <= LA21_0 <= 70) or (97 <= LA21_0 <= 102)):
                    s = 9

                elif ((115 <= LA21_0 <= 116)):
                    s = 10

                elif (LA21_0 == 95):
                    s = 11

                elif ((0 <= LA21_0 <= 8) or (11 <= LA21_0 <= 12) or (14 <= LA21_0 <= 31) or (33 <= LA21_0 <= 34) or (36 <= LA21_0 <= 38) or (40 <= LA21_0 <= 45) or LA21_0 == 47 or (58 <= LA21_0 <= 64) or (91 <= LA21_0 <= 94) or LA21_0 == 96 or (123 <= LA21_0 <= 65535)) and (((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     ) or (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] ))):
                    s = 12

                elif ((71 <= LA21_0 <= 90) or (103 <= LA21_0 <= 114) or (117 <= LA21_0 <= 122)):
                    s = 13

                elif (LA21_0 == 32):
                    s = 14

                else:
                    s = 7

                 
                input.seek(index21_0)
                if s >= 0:
                    return s
            elif s == 13: 
                LA21_41 = input.LA(1)

                 
                index21_41 = input.index()
                input.rewind()
                s = -1
                if ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     )):
                    s = 55

                elif ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] )):
                    s = 56

                 
                input.seek(index21_41)
                if s >= 0:
                    return s
            elif s == 14: 
                LA21_24 = input.LA(1)

                 
                index21_24 = input.index()
                input.rewind()
                s = -1
                if ((0 <= LA21_24 <= 9) or (11 <= LA21_24 <= 12) or (14 <= LA21_24 <= 34) or (36 <= LA21_24 <= 65535)) and (((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     ) or (self.getColumn() > 0 ) or (self.getColumn() == 0) or (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] ))):
                    s = 24

                elif (LA21_24 == 13 or LA21_24 == 35) and (((self.getColumn() > 0 ) or (self.getColumn() == 0))):
                    s = 26

                elif (LA21_24 == 10) and ((self.getColumn() == 0)):
                    s = 27

                else:
                    s = 44

                 
                input.seek(index21_24)
                if s >= 0:
                    return s
            elif s == 15: 
                LA21_42 = input.LA(1)

                 
                index21_42 = input.index()
                input.rewind()
                s = -1
                if ((65 <= LA21_42 <= 90) or LA21_42 == 95 or (97 <= LA21_42 <= 122)):
                    s = 42

                elif ((0 <= LA21_42 <= 9) or (11 <= LA21_42 <= 12) or (14 <= LA21_42 <= 34) or (36 <= LA21_42 <= 64) or (91 <= LA21_42 <= 94) or LA21_42 == 96 or (123 <= LA21_42 <= 65535)) and (((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     ) or (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] ))):
                    s = 18

                else:
                    s = 57

                 
                input.seek(index21_42)
                if s >= 0:
                    return s
            elif s == 16: 
                LA21_12 = input.LA(1)

                 
                index21_12 = input.index()
                input.rewind()
                s = -1
                if ((0 <= LA21_12 <= 9) or (11 <= LA21_12 <= 12) or (14 <= LA21_12 <= 34) or (36 <= LA21_12 <= 65535)) and (((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     ) or (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] ))):
                    s = 18

                 
                input.seek(index21_12)
                if s >= 0:
                    return s
            elif s == 17: 
                LA21_18 = input.LA(1)

                 
                index21_18 = input.index()
                input.rewind()
                s = -1
                if ((0 <= LA21_18 <= 9) or (11 <= LA21_18 <= 12) or (14 <= LA21_18 <= 34) or (36 <= LA21_18 <= 65535)) and (((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     ) or (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] ))):
                    s = 18

                else:
                    s = 41

                 
                input.seek(index21_18)
                if s >= 0:
                    return s
            elif s == 18: 
                LA21_46 = input.LA(1)

                 
                index21_46 = input.index()
                input.rewind()
                s = -1
                if ((48 <= LA21_46 <= 57) or (65 <= LA21_46 <= 70) or (97 <= LA21_46 <= 102)):
                    s = 58

                elif ((0 <= LA21_46 <= 9) or (11 <= LA21_46 <= 12) or (14 <= LA21_46 <= 34) or (36 <= LA21_46 <= 47) or (58 <= LA21_46 <= 64) or (71 <= LA21_46 <= 96) or (103 <= LA21_46 <= 65535)) and (((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     ) or (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] ))):
                    s = 18

                else:
                    s = 41

                 
                input.seek(index21_46)
                if s >= 0:
                    return s
            elif s == 19: 
                LA21_17 = input.LA(1)

                 
                index21_17 = input.index()
                input.rewind()
                s = -1
                if ((65 <= LA21_17 <= 90) or LA21_17 == 95 or (97 <= LA21_17 <= 122)):
                    s = 17

                elif ((0 <= LA21_17 <= 9) or (11 <= LA21_17 <= 12) or (14 <= LA21_17 <= 34) or (36 <= LA21_17 <= 64) or (91 <= LA21_17 <= 94) or LA21_17 == 96 or (123 <= LA21_17 <= 65535)) and (((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     ) or (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] ))):
                    s = 18

                else:
                    s = 43

                 
                input.seek(index21_17)
                if s >= 0:
                    return s
            elif s == 20: 
                LA21_23 = input.LA(1)

                 
                index21_23 = input.index()
                input.rewind()
                s = -1
                if (LA21_23 == 35) and (((self.getColumn() > 0 ) or (self.getColumn() == 0))):
                    s = 20

                elif (LA21_23 == 9):
                    s = 21

                elif (LA21_23 == 10 or LA21_23 == 13):
                    s = 22

                elif (LA21_23 == 32):
                    s = 23

                elif ((0 <= LA21_23 <= 8) or (11 <= LA21_23 <= 12) or (14 <= LA21_23 <= 31) or (33 <= LA21_23 <= 34) or (36 <= LA21_23 <= 65535)) and (((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     ) or (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] ))):
                    s = 18

                else:
                    s = 41

                 
                input.seek(index21_23)
                if s >= 0:
                    return s
            elif s == 21: 
                LA21_47 = input.LA(1)

                 
                index21_47 = input.index()
                input.rewind()
                s = -1
                if ((0 <= LA21_47 <= 9) or (11 <= LA21_47 <= 12) or (14 <= LA21_47 <= 34) or (36 <= LA21_47 <= 65535)) and (((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     ) or (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] ))):
                    s = 18

                else:
                    s = 59

                 
                input.seek(index21_47)
                if s >= 0:
                    return s
            elif s == 22: 
                LA21_16 = input.LA(1)

                 
                index21_16 = input.index()
                input.rewind()
                s = -1
                if ((65 <= LA21_16 <= 90) or LA21_16 == 95 or (97 <= LA21_16 <= 122)):
                    s = 42

                elif ((0 <= LA21_16 <= 9) or (11 <= LA21_16 <= 12) or (14 <= LA21_16 <= 34) or (36 <= LA21_16 <= 64) or (91 <= LA21_16 <= 94) or LA21_16 == 96 or (123 <= LA21_16 <= 65535)) and (((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     ) or (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] ))):
                    s = 18

                else:
                    s = 41

                 
                input.seek(index21_16)
                if s >= 0:
                    return s
            elif s == 23: 
                LA21_29 = input.LA(1)

                 
                index21_29 = input.index()
                input.rewind()
                s = -1
                if ((48 <= LA21_29 <= 57) or (65 <= LA21_29 <= 70) or (97 <= LA21_29 <= 102)):
                    s = 46

                elif ((0 <= LA21_29 <= 9) or (11 <= LA21_29 <= 12) or (14 <= LA21_29 <= 34) or (36 <= LA21_29 <= 47) or (58 <= LA21_29 <= 64) or (71 <= LA21_29 <= 96) or (103 <= LA21_29 <= 65535)) and (((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     ) or (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] ))):
                    s = 18

                else:
                    s = 45

                 
                input.seek(index21_29)
                if s >= 0:
                    return s
            elif s == 24: 
                LA21_31 = input.LA(1)

                 
                index21_31 = input.index()
                input.rewind()
                s = -1
                if ((0 <= LA21_31 <= 8) or (11 <= LA21_31 <= 12) or (14 <= LA21_31 <= 31) or (33 <= LA21_31 <= 65535)) and ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME, DOT_DOT_ARGS] )):
                    s = 7

                elif (LA21_31 == 13):
                    s = 5

                elif (LA21_31 == 10):
                    s = 6

                elif (LA21_31 == 32):
                    s = 31

                elif (LA21_31 == 9):
                    s = 30

                else:
                    s = 32

                 
                input.seek(index21_31)
                if s >= 0:
                    return s
            elif s == 25: 
                LA21_30 = input.LA(1)

                 
                index21_30 = input.index()
                input.rewind()
                s = -1
                if ((0 <= LA21_30 <= 8) or (11 <= LA21_30 <= 12) or (14 <= LA21_30 <= 31) or (33 <= LA21_30 <= 65535)) and ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME, DOT_DOT_ARGS] )):
                    s = 7

                elif (LA21_30 == 13):
                    s = 5

                elif (LA21_30 == 10):
                    s = 6

                elif (LA21_30 == 32):
                    s = 31

                elif (LA21_30 == 9):
                    s = 30

                else:
                    s = 32

                 
                input.seek(index21_30)
                if s >= 0:
                    return s
            elif s == 26: 
                LA21_44 = input.LA(1)

                 
                index21_44 = input.index()
                input.rewind()
                s = -1
                if (((self.getColumn() > 0 ) or (self.getColumn() == 0))):
                    s = 27

                elif ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     )):
                    s = 55

                elif ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] )):
                    s = 56

                 
                input.seek(index21_44)
                if s >= 0:
                    return s
            elif s == 27: 
                LA21_1 = input.LA(1)

                 
                index21_1 = input.index()
                input.rewind()
                s = -1
                if (LA21_1 == 101):
                    s = 15

                elif (LA21_1 == 46):
                    s = 16

                elif ((65 <= LA21_1 <= 90) or LA21_1 == 95 or (97 <= LA21_1 <= 100) or (102 <= LA21_1 <= 122)):
                    s = 17

                elif ((0 <= LA21_1 <= 9) or (11 <= LA21_1 <= 12) or (14 <= LA21_1 <= 34) or (36 <= LA21_1 <= 45) or (47 <= LA21_1 <= 64) or (91 <= LA21_1 <= 94) or LA21_1 == 96 or (123 <= LA21_1 <= 65535)) and (((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     ) or (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] ))):
                    s = 18

                 
                input.seek(index21_1)
                if s >= 0:
                    return s
            elif s == 28: 
                LA21_57 = input.LA(1)

                 
                index21_57 = input.index()
                input.rewind()
                s = -1
                if (not ((((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     ) or (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] ))))):
                    s = 63

                elif ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     )):
                    s = 55

                elif ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] )):
                    s = 56

                 
                input.seek(index21_57)
                if s >= 0:
                    return s
            elif s == 29: 
                LA21_53 = input.LA(1)

                 
                index21_53 = input.index()
                input.rewind()
                s = -1
                if (not ((((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     ) or (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] ))))):
                    s = 54

                elif ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     )):
                    s = 55

                elif ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] )):
                    s = 56

                 
                input.seek(index21_53)
                if s >= 0:
                    return s
            elif s == 30: 
                LA21_40 = input.LA(1)

                 
                index21_40 = input.index()
                input.rewind()
                s = -1
                if (not ((((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     ) or (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] ))))):
                    s = 54

                elif ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     )):
                    s = 55

                elif ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] )):
                    s = 56

                 
                input.seek(index21_40)
                if s >= 0:
                    return s
            elif s == 31: 
                LA21_43 = input.LA(1)

                 
                index21_43 = input.index()
                input.rewind()
                s = -1
                if (not ((((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     ) or (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] ))))):
                    s = 54

                elif ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     )):
                    s = 55

                elif ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] )):
                    s = 56

                 
                input.seek(index21_43)
                if s >= 0:
                    return s
            elif s == 32: 
                LA21_75 = input.LA(1)

                 
                index21_75 = input.index()
                input.rewind()
                s = -1
                if ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     )):
                    s = 55

                elif ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] )):
                    s = 56

                elif (True):
                    s = 68

                 
                input.seek(index21_75)
                if s >= 0:
                    return s
            elif s == 33: 
                LA21_45 = input.LA(1)

                 
                index21_45 = input.index()
                input.rewind()
                s = -1
                if ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     )):
                    s = 55

                elif ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] )):
                    s = 56

                elif (True):
                    s = 48

                 
                input.seek(index21_45)
                if s >= 0:
                    return s
            elif s == 34: 
                LA21_64 = input.LA(1)

                 
                index21_64 = input.index()
                input.rewind()
                s = -1
                if ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     )):
                    s = 55

                elif ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] )):
                    s = 56

                elif (True):
                    s = 66

                 
                input.seek(index21_64)
                if s >= 0:
                    return s
            elif s == 35: 
                LA21_59 = input.LA(1)

                 
                index21_59 = input.index()
                input.rewind()
                s = -1
                if ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     )):
                    s = 55

                elif ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] )):
                    s = 56

                elif (True):
                    s = 34

                 
                input.seek(index21_59)
                if s >= 0:
                    return s
            elif s == 36: 
                LA21_51 = input.LA(1)

                 
                index21_51 = input.index()
                input.rewind()
                s = -1
                if ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     )):
                    s = 55

                elif ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] )):
                    s = 56

                elif (True):
                    s = 13

                 
                input.seek(index21_51)
                if s >= 0:
                    return s
            elif s == 37: 
                LA21_71 = input.LA(1)

                 
                index21_71 = input.index()
                input.rewind()
                s = -1
                if ((48 <= LA21_71 <= 57) or (65 <= LA21_71 <= 70) or (97 <= LA21_71 <= 102)):
                    s = 73

                elif ((0 <= LA21_71 <= 9) or (11 <= LA21_71 <= 12) or (14 <= LA21_71 <= 34) or (36 <= LA21_71 <= 47) or (58 <= LA21_71 <= 64) or (71 <= LA21_71 <= 96) or (103 <= LA21_71 <= 65535)) and (((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     ) or (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] ))):
                    s = 18

                else:
                    s = 41

                 
                input.seek(index21_71)
                if s >= 0:
                    return s
            elif s == 38: 
                LA21_65 = input.LA(1)

                 
                index21_65 = input.index()
                input.rewind()
                s = -1
                if ((48 <= LA21_65 <= 57) or (65 <= LA21_65 <= 70) or (97 <= LA21_65 <= 102)):
                    s = 69

                elif ((0 <= LA21_65 <= 9) or (11 <= LA21_65 <= 12) or (14 <= LA21_65 <= 34) or (36 <= LA21_65 <= 47) or (58 <= LA21_65 <= 64) or (71 <= LA21_65 <= 96) or (103 <= LA21_65 <= 65535)) and (((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     ) or (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] ))):
                    s = 18

                else:
                    s = 41

                 
                input.seek(index21_65)
                if s >= 0:
                    return s
            elif s == 39: 
                LA21_2 = input.LA(1)

                 
                index21_2 = input.index()
                input.rewind()
                s = -1
                if (LA21_2 == 35) and (((self.getColumn() > 0 ) or (self.getColumn() == 0))):
                    s = 20

                elif (LA21_2 == 9):
                    s = 21

                elif ((0 <= LA21_2 <= 8) or (11 <= LA21_2 <= 12) or (14 <= LA21_2 <= 31) or (33 <= LA21_2 <= 34) or (36 <= LA21_2 <= 65535)) and (((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     ) or (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] ))):
                    s = 18

                elif (LA21_2 == 10 or LA21_2 == 13):
                    s = 22

                elif (LA21_2 == 32):
                    s = 23

                else:
                    s = 19

                 
                input.seek(index21_2)
                if s >= 0:
                    return s
            elif s == 40: 
                LA21_14 = input.LA(1)

                 
                index21_14 = input.index()
                input.rewind()
                s = -1
                if (LA21_14 == 35) and (((self.getColumn() > 0 ) or (self.getColumn() == 0))):
                    s = 20

                elif (LA21_14 == 9):
                    s = 21

                elif ((0 <= LA21_14 <= 8) or (11 <= LA21_14 <= 12) or (14 <= LA21_14 <= 31) or (33 <= LA21_14 <= 34) or (36 <= LA21_14 <= 65535)) and (((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     ) or (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] ))):
                    s = 18

                elif (LA21_14 == 10 or LA21_14 == 13):
                    s = 22

                elif (LA21_14 == 32):
                    s = 23

                else:
                    s = 19

                 
                input.seek(index21_14)
                if s >= 0:
                    return s
            elif s == 41: 
                LA21_38 = input.LA(1)

                 
                index21_38 = input.index()
                input.rewind()
                s = -1
                if ((65 <= LA21_38 <= 90) or LA21_38 == 95 or (97 <= LA21_38 <= 122)):
                    s = 38

                elif ((0 <= LA21_38 <= 9) or (11 <= LA21_38 <= 12) or (14 <= LA21_38 <= 34) or (36 <= LA21_38 <= 64) or (91 <= LA21_38 <= 94) or LA21_38 == 96 or (123 <= LA21_38 <= 65535)) and (((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     ) or (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] ))):
                    s = 18

                else:
                    s = 51

                 
                input.seek(index21_38)
                if s >= 0:
                    return s
            elif s == 42: 
                LA21_6 = input.LA(1)

                 
                index21_6 = input.index()
                input.rewind()
                s = -1
                if (LA21_6 == 13):
                    s = 5

                elif (LA21_6 == 10):
                    s = 6

                elif (LA21_6 == 9):
                    s = 30

                elif (LA21_6 == 32):
                    s = 31

                elif ((0 <= LA21_6 <= 8) or (11 <= LA21_6 <= 12) or (14 <= LA21_6 <= 31) or (33 <= LA21_6 <= 65535)) and ((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME, DOT_DOT_ARGS] )):
                    s = 7

                else:
                    s = 32

                 
                input.seek(index21_6)
                if s >= 0:
                    return s
            elif s == 43: 
                LA21_52 = input.LA(1)

                 
                index21_52 = input.index()
                input.rewind()
                s = -1
                if ((65 <= LA21_52 <= 90) or LA21_52 == 95 or (97 <= LA21_52 <= 122)):
                    s = 17

                elif ((0 <= LA21_52 <= 9) or (11 <= LA21_52 <= 12) or (14 <= LA21_52 <= 34) or (36 <= LA21_52 <= 64) or (91 <= LA21_52 <= 94) or LA21_52 == 96 or (123 <= LA21_52 <= 65535)) and (((self.lookBehindToken and self.lookBehindToken.getType() in [DOT_NAME]     ) or (self.lookBehindToken and self.lookBehindToken.getType() in [DOT_DOT_NAME] ))):
                    s = 18

                else:
                    s = 62

                 
                input.seek(index21_52)
                if s >= 0:
                    return s

            nvae = NoViableAltException(self_.getDescription(), 21, _s, input)
            self_.error(nvae)
            raise nvae
 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(pycasmLexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
