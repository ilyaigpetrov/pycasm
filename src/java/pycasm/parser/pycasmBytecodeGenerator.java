// $ANTLR 3.1.3 Mar 17, 2009 19:23:44 G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmBytecodeGenerator.g 2011-05-08 12:08:42

package pycasm.parser;
import java.io.*;


import org.antlr.runtime.*;
import org.antlr.runtime.tree.*;import java.util.Stack;
import java.util.List;
import java.util.ArrayList;

public class pycasmBytecodeGenerator extends TreeParser {
    public static final String[] tokenNames = new String[] {
        "<invalid>", "<EOR>", "<DOWN>", "<UP>", "DEDENT", "INDENT", "BLOCK", "ARGS", "GEN", "HEX_PAIR", "HEX_DQUAD", "HEX_EIGHT", "HEX_QUAD", "HEX_DIGIT", "HexDigit", "DOT_END", "Type", "TYPED_VALUE", "STRING", "Alpha", "DOT_NAME", "NAME", "NEWLINE", "WS", "COMMENT", "NON_WS_SEQUENCE", "HexAlpha", "Digit", "ROOT", "HEX", "SYM"
    };
    public static final int Alpha=19;
    public static final int Type=16;
    public static final int TYPED_VALUE=17;
    public static final int DOT_END=15;
    public static final int HexAlpha=26;
    public static final int HEX_DIGIT=13;
    public static final int DEDENT=4;
    public static final int Digit=27;
    public static final int HEX_DQUAD=10;
    public static final int EOF=-1;
    public static final int ROOT=28;
    public static final int HexDigit=14;
    public static final int SYM=30;
    public static final int INDENT=5;
    public static final int NAME=21;
    public static final int HEX_EIGHT=11;
    public static final int WS=23;
    public static final int NEWLINE=22;
    public static final int HEX=29;
    public static final int BLOCK=6;
    public static final int NON_WS_SEQUENCE=25;
    public static final int ARGS=7;
    public static final int GEN=8;
    public static final int DOT_NAME=20;
    public static final int COMMENT=24;
    public static final int HEX_QUAD=12;
    public static final int HEX_PAIR=9;
    public static final int STRING=18;

    // delegates
    // delegators


        public pycasmBytecodeGenerator(TreeNodeStream input) {
            this(input, new RecognizerSharedState());
        }
        public pycasmBytecodeGenerator(TreeNodeStream input, RecognizerSharedState state) {
            super(input, state);
             
        }
        

    public String[] getTokenNames() { return pycasmBytecodeGenerator.tokenNames; }
    public String getGrammarFileName() { return "G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmBytecodeGenerator.g"; }


    public static byte[] hexStringToByteArray(String s) {
    	int len = s.length();
    	byte[] data = new byte[len / 2];
    	for (int i = 0; i < len; i += 2) {
    		data[i / 2] = (byte) ((Character.digit(s.charAt(i), 16) << 4)
    							 + Character.digit(s.charAt(i+1), 16));
    	}
    	return data;
    }

    StringBuilder result;
    FileOutputStream out;



    // $ANTLR start "root"
    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmBytecodeGenerator.g:36:1: root returns [byte[] bytecode] : ^( ROOT ( block )? ) ;
    public final byte[] root() throws RecognitionException {
        byte[] bytecode = null;


        	result = new StringBuilder();

        try {
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmBytecodeGenerator.g:43:2: ( ^( ROOT ( block )? ) )
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmBytecodeGenerator.g:44:3: ^( ROOT ( block )? )
            {
            match(input,ROOT,FOLLOW_ROOT_in_root63); 

            if ( input.LA(1)==Token.DOWN ) {
                match(input, Token.DOWN, null); 
                // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmBytecodeGenerator.g:44:10: ( block )?
                int alt1=2;
                int LA1_0 = input.LA(1);

                if ( (LA1_0==BLOCK) ) {
                    alt1=1;
                }
                switch (alt1) {
                    case 1 :
                        // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmBytecodeGenerator.g:44:10: block
                        {
                        pushFollow(FOLLOW_block_in_root65);
                        block();

                        state._fsp--;


                        }
                        break;

                }


                match(input, Token.UP, null); 
            }

            }


            	bytecode = hexStringToByteArray(result.toString());

        }

        catch (RecognitionException e) {
        	this.reportError(e);
        	throw e;
        }
        finally {
        }
        return bytecode;
    }
    // $ANTLR end "root"


    // $ANTLR start "block"
    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmBytecodeGenerator.g:47:1: block : ^( BLOCK ( block_child )+ ) ;
    public final void block() throws RecognitionException {
        try {
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmBytecodeGenerator.g:48:2: ( ^( BLOCK ( block_child )+ ) )
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmBytecodeGenerator.g:49:3: ^( BLOCK ( block_child )+ )
            {
            match(input,BLOCK,FOLLOW_BLOCK_in_block81); 

            match(input, Token.DOWN, null); 
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmBytecodeGenerator.g:49:11: ( block_child )+
            int cnt2=0;
            loop2:
            do {
                int alt2=2;
                int LA2_0 = input.LA(1);

                if ( (LA2_0==BLOCK||LA2_0==HEX) ) {
                    alt2=1;
                }


                switch (alt2) {
            	case 1 :
            	    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmBytecodeGenerator.g:49:11: block_child
            	    {
            	    pushFollow(FOLLOW_block_child_in_block83);
            	    block_child();

            	    state._fsp--;


            	    }
            	    break;

            	default :
            	    if ( cnt2 >= 1 ) break loop2;
                        EarlyExitException eee =
                            new EarlyExitException(2, input);
                        throw eee;
                }
                cnt2++;
            } while (true);


            match(input, Token.UP, null); 

            }

        }

        catch (RecognitionException e) {
        	this.reportError(e);
        	throw e;
        }
        finally {
        }
        return ;
    }
    // $ANTLR end "block"


    // $ANTLR start "block_child"
    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmBytecodeGenerator.g:52:1: block_child : ( HEX | block );
    public final void block_child() throws RecognitionException {
        CommonTree HEX1=null;

        try {
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmBytecodeGenerator.g:53:2: ( HEX | block )
            int alt3=2;
            int LA3_0 = input.LA(1);

            if ( (LA3_0==HEX) ) {
                alt3=1;
            }
            else if ( (LA3_0==BLOCK) ) {
                alt3=2;
            }
            else {
                NoViableAltException nvae =
                    new NoViableAltException("", 3, 0, input);

                throw nvae;
            }
            switch (alt3) {
                case 1 :
                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmBytecodeGenerator.g:54:3: HEX
                    {
                    HEX1=(CommonTree)match(input,HEX,FOLLOW_HEX_in_block_child98); 
                    result.append( (HEX1!=null?HEX1.getText():null) );

                    }
                    break;
                case 2 :
                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmBytecodeGenerator.g:55:4: block
                    {
                    pushFollow(FOLLOW_block_in_block_child105);
                    block();

                    state._fsp--;


                    }
                    break;

            }
        }

        catch (RecognitionException e) {
        	this.reportError(e);
        	throw e;
        }
        finally {
        }
        return ;
    }
    // $ANTLR end "block_child"

    // Delegated rules


 

    public static final BitSet FOLLOW_ROOT_in_root63 = new BitSet(new long[]{0x0000000000000004L});
    public static final BitSet FOLLOW_block_in_root65 = new BitSet(new long[]{0x0000000000000008L});
    public static final BitSet FOLLOW_BLOCK_in_block81 = new BitSet(new long[]{0x0000000000000004L});
    public static final BitSet FOLLOW_block_child_in_block83 = new BitSet(new long[]{0x0000000020000048L});
    public static final BitSet FOLLOW_HEX_in_block_child98 = new BitSet(new long[]{0x0000000000000002L});
    public static final BitSet FOLLOW_block_in_block_child105 = new BitSet(new long[]{0x0000000000000002L});

}