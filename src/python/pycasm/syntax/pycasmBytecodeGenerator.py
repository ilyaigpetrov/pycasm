# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmBytecodeGenerator.g 2011-06-23 13:21:12

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




class pycasmBytecodeGenerator(TreeParser):
    grammarFileName = "/root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmBytecodeGenerator.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 18, 2009 10:09:25")
    antlr_version_str = "3.1.3 Mar 18, 2009 10:09:25"
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(pycasmBytecodeGenerator, self).__init__(input, state, *args, **kwargs)






                


        

              
    result = ''



    # $ANTLR start "root"
    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmBytecodeGenerator.g:39:1: root returns [bytecode] : ^( ROOT ( block )? ) ;
    def root(self, ):

        bytecode = None

        try:
            try:
                # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmBytecodeGenerator.g:49:2: ( ^( ROOT ( block )? ) )
                # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmBytecodeGenerator.g:50:3: ^( ROOT ( block )? )
                pass 
                self.match(self.input, ROOT, self.FOLLOW_ROOT_in_root55)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmBytecodeGenerator.g:50:10: ( block )?
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == BLOCK) :
                        alt1 = 1
                    if alt1 == 1:
                        # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmBytecodeGenerator.g:50:10: block
                        pass 
                        self._state.following.append(self.FOLLOW_block_in_root57)
                        self.block()

                        self._state.following.pop()




                    self.match(self.input, UP, None)




                #action start
                        
                try:
                	bytecode = self.result.decode('hex')
                except TypeError,e:
                	# Here we could point to the exact character in self.result which can\'t be converted to bytecode.
                	print(e.message)
                	print("Result hex string:"+self.result)

                #action end

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return bytecode

    # $ANTLR end "root"


    # $ANTLR start "block"
    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmBytecodeGenerator.g:53:1: block : ^( BLOCK ( block_child )+ ) ;
    def block(self, ):

        try:
            try:
                # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmBytecodeGenerator.g:54:2: ( ^( BLOCK ( block_child )+ ) )
                # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmBytecodeGenerator.g:55:3: ^( BLOCK ( block_child )+ )
                pass 
                self.match(self.input, BLOCK, self.FOLLOW_BLOCK_in_block73)

                self.match(self.input, DOWN, None)
                # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmBytecodeGenerator.g:55:11: ( block_child )+
                cnt2 = 0
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == BLOCK or LA2_0 == HEX) :
                        alt2 = 1


                    if alt2 == 1:
                        # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmBytecodeGenerator.g:55:11: block_child
                        pass 
                        self._state.following.append(self.FOLLOW_block_child_in_block75)
                        self.block_child()

                        self._state.following.pop()


                    else:
                        if cnt2 >= 1:
                            break #loop2

                        eee = EarlyExitException(2, self.input)
                        raise eee

                    cnt2 += 1

                self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "block"


    # $ANTLR start "block_child"
    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmBytecodeGenerator.g:58:1: block_child : ( HEX | block );
    def block_child(self, ):

        HEX1 = None

        try:
            try:
                # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmBytecodeGenerator.g:59:2: ( HEX | block )
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == HEX) :
                    alt3 = 1
                elif (LA3_0 == BLOCK) :
                    alt3 = 2
                else:
                    nvae = NoViableAltException("", 3, 0, self.input)

                    raise nvae

                if alt3 == 1:
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmBytecodeGenerator.g:60:3: HEX
                    pass 
                    HEX1=self.match(self.input, HEX, self.FOLLOW_HEX_in_block_child90)
                    #action start
                    self.result += HEX1.text
                    #action end


                elif alt3 == 2:
                    # /root/Desktop/pycasm/pycasm//src/antlr3/pythonTarget/pycasmBytecodeGenerator.g:61:4: block
                    pass 
                    self._state.following.append(self.FOLLOW_block_in_block_child97)
                    self.block()

                    self._state.following.pop()



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "block_child"


    # Delegated rules


 

    FOLLOW_ROOT_in_root55 = frozenset([2])
    FOLLOW_block_in_root57 = frozenset([3])
    FOLLOW_BLOCK_in_block73 = frozenset([2])
    FOLLOW_block_child_in_block75 = frozenset([3, 6, 34])
    FOLLOW_HEX_in_block_child90 = frozenset([1])
    FOLLOW_block_in_block_child97 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(pycasmBytecodeGenerator)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
