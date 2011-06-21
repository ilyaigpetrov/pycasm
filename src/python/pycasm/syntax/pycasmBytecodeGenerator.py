# $ANTLR 3.1.3 Mar 17, 2009 19:23:44 G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmBytecodeGenerator.g 2011-06-22 00:39:56

import sys
from antlr3 import *
from antlr3.tree import *
from antlr3.compat import set, frozenset


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




class pycasmBytecodeGenerator(TreeParser):
    grammarFileName = "G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmBytecodeGenerator.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 17, 2009 19:23:44")
    antlr_version_str = "3.1.3 Mar 17, 2009 19:23:44"
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(pycasmBytecodeGenerator, self).__init__(input, state, *args, **kwargs)






                


        

              
    result = ''



    # $ANTLR start "root"
    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmBytecodeGenerator.g:13:1: root returns [bytecode] : ^( ROOT ( block )? ) ;
    def root(self, ):

        bytecode = None

        try:
            try:
                # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmBytecodeGenerator.g:23:2: ( ^( ROOT ( block )? ) )
                # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmBytecodeGenerator.g:24:3: ^( ROOT ( block )? )
                pass 
                self.match(self.input, ROOT, self.FOLLOW_ROOT_in_root52)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmBytecodeGenerator.g:24:10: ( block )?
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == BLOCK) :
                        alt1 = 1
                    if alt1 == 1:
                        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmBytecodeGenerator.g:24:10: block
                        pass 
                        self._state.following.append(self.FOLLOW_block_in_root54)
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
    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmBytecodeGenerator.g:27:1: block : ^( BLOCK ( block_child )+ ) ;
    def block(self, ):

        try:
            try:
                # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmBytecodeGenerator.g:28:2: ( ^( BLOCK ( block_child )+ ) )
                # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmBytecodeGenerator.g:29:3: ^( BLOCK ( block_child )+ )
                pass 
                self.match(self.input, BLOCK, self.FOLLOW_BLOCK_in_block70)

                self.match(self.input, DOWN, None)
                # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmBytecodeGenerator.g:29:11: ( block_child )+
                cnt2 = 0
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == BLOCK or LA2_0 == HEX) :
                        alt2 = 1


                    if alt2 == 1:
                        # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmBytecodeGenerator.g:29:11: block_child
                        pass 
                        self._state.following.append(self.FOLLOW_block_child_in_block72)
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
    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmBytecodeGenerator.g:32:1: block_child : ( HEX | block );
    def block_child(self, ):

        HEX1 = None

        try:
            try:
                # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmBytecodeGenerator.g:33:2: ( HEX | block )
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
                    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmBytecodeGenerator.g:34:3: HEX
                    pass 
                    HEX1=self.match(self.input, HEX, self.FOLLOW_HEX_in_block_child87)
                    #action start
                    self.result += HEX1.text
                    #action end


                elif alt3 == 2:
                    # G:\\storage\\workspace\\unpyc\\pycasm_\\\\src\\antlr3\\pythonTarget\\pycasmBytecodeGenerator.g:35:4: block
                    pass 
                    self._state.following.append(self.FOLLOW_block_in_block_child94)
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


 

    FOLLOW_ROOT_in_root52 = frozenset([2])
    FOLLOW_block_in_root54 = frozenset([3])
    FOLLOW_BLOCK_in_block70 = frozenset([2])
    FOLLOW_block_child_in_block72 = frozenset([3, 6, 48])
    FOLLOW_HEX_in_block_child87 = frozenset([1])
    FOLLOW_block_in_block_child94 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(pycasmBytecodeGenerator)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
