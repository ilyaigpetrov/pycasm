// $ANTLR 3.1.3 Mar 17, 2009 19:23:44 G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmSymnameWalker.g 2011-05-08 12:08:41

package pycasm.parser;


import org.antlr.runtime.*;
import org.antlr.runtime.tree.*;import java.util.Stack;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;

public class pycasmSymnameWalker extends TreeParser {
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


        public pycasmSymnameWalker(TreeNodeStream input) {
            this(input, new RecognizerSharedState());
        }
        public pycasmSymnameWalker(TreeNodeStream input, RecognizerSharedState state) {
            super(input, state);
             
        }
        
    protected TreeAdaptor adaptor = new CommonTreeAdaptor();

    public void setTreeAdaptor(TreeAdaptor adaptor) {
        this.adaptor = adaptor;
    }
    public TreeAdaptor getTreeAdaptor() {
        return adaptor;
    }

    public String[] getTokenNames() { return pycasmSymnameWalker.tokenNames; }
    public String getGrammarFileName() { return "G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmSymnameWalker.g"; }


    public CommonTree expandSymname(String symname) {
    	// look scope
    	// expand name in hex codes
    	// dirty hack to make it work follows
    	Map<String,String> opcodes = new HashMap<String,String>() {{
    		put("STOP_CODE", "0");
    		put("POP_TOP", "1");
    		put("ROT_TWO", "2");
    		put("ROT_THREE", "3");
    		put("DUP_TOP", "4");
    		put("ROT_FOUR", "5");
    		put("NOP", "9");
    		put("UNARY_POSITIVE", "a");
    		put("UNARY_NEGATIVE", "b");
    		put("UNARY_NOT", "c");
    		put("UNARY_CONVERT", "d");
    		put("UNARY_INVERT", "f");
    		put("LIST_APPEND", "12");
    		put("BINARY_POWER", "13");
    		put("BINARY_MULTIPLY", "14");
    		put("BINARY_DIVIDE", "15");
    		put("BINARY_MODULO", "16");
    		put("BINARY_ADD", "17");
    		put("BINARY_SUBTRACT", "18");
    		put("BINARY_SUBSCR", "19");
    		put("BINARY_FLOOR_DIVIDE", "1a");
    		put("BINARY_TRUE_DIVIDE", "1b");
    		put("INPLACE_FLOOR_DIVIDE", "1c");
    		put("INPLACE_TRUE_DIVIDE", "1d");
    		put("SLICE+0", "1e");
    		put("SLICE+1", "1f");
    		put("SLICE+2", "20");
    		put("SLICE+3", "21");
    		put("STORE_SLICE+0", "28");
    		put("STORE_SLICE+1", "29");
    		put("STORE_SLICE+2", "2a");
    		put("STORE_SLICE+3", "2b");
    		put("DELETE_SLICE+0", "32");
    		put("DELETE_SLICE+1", "33");
    		put("DELETE_SLICE+2", "34");
    		put("DELETE_SLICE+3", "35");
    		put("INPLACE_ADD", "37");
    		put("INPLACE_SUBTRACT", "38");
    		put("INPLACE_MULTIPLY", "39");
    		put("INPLACE_DIVIDE", "3a");
    		put("INPLACE_MODULO", "3b");
    		put("STORE_SUBSCR", "3c");
    		put("DELETE_SUBSCR", "3d");
    		put("BINARY_LSHIFT", "3e");
    		put("BINARY_RSHIFT", "3f");
    		put("BINARY_AND", "40");
    		put("BINARY_XOR", "41");
    		put("BINARY_OR", "42");
    		put("INPLACE_POWER", "43");
    		put("GET_ITER", "44");
    		put("PRINT_EXPR", "46");
    		put("PRINT_ITEM", "47");
    		put("PRINT_NEWLINE", "48");
    		put("PRINT_ITEM_TO", "49");
    		put("PRINT_NEWLINE_TO", "4a");
    		put("INPLACE_LSHIFT", "4b");
    		put("INPLACE_RSHIFT", "4c");
    		put("INPLACE_AND", "4d");
    		put("INPLACE_XOR", "4e");
    		put("INPLACE_OR", "4f");
    		put("BREAK_LOOP", "50");
    		put("WITH_CLEANUP", "51");
    		put("LOAD_LOCALS", "52");
    		put("RETURN_VALUE", "53");
    		put("IMPORT_STAR", "54");
    		put("EXEC_STMT", "55");
    		put("YIELD_VALUE", "56");
    		put("POP_BLOCK", "57");
    		put("END_FINALLY", "58");
    		put("BUILD_CLASS", "59");
    		put("STORE_NAME", "5a");
    		put("DELETE_NAME", "5b");
    		put("UNPACK_SEQUENCE", "5c");
    		put("FOR_ITER", "5d");
    		put("STORE_ATTR", "5f");
    		put("DELETE_ATTR", "60");
    		put("STORE_GLOBAL", "61");
    		put("DELETE_GLOBAL", "62");
    		put("DUP_TOPX", "63");
    		put("LOAD_CONST", "64");
    		put("LOAD_NAME", "65");
    		put("BUILD_TUPLE", "66");
    		put("BUILD_LIST", "67");
    		put("BUILD_MAP", "68");
    		put("LOAD_ATTR", "69");
    		put("COMPARE_OP", "6a");
    		put("IMPORT_NAME", "6b");
    		put("IMPORT_FROM", "6c");
    		put("JUMP_FORWARD", "6e");
    		put("JUMP_IF_FALSE", "6f");
    		put("JUMP_IF_TRUE", "70");
    		put("JUMP_ABSOLUTE", "71");
    		put("LOAD_GLOBAL", "74");
    		put("CONTINUE_LOOP", "77");
    		put("SETUP_LOOP", "78");
    		put("SETUP_EXCEPT", "79");
    		put("SETUP_FINALLY", "7a");
    		put("LOAD_FAST", "7c");
    		put("STORE_FAST", "7d");
    		put("DELETE_FAST", "7e");
    		put("RAISE_VARARGS", "82");
    		put("CALL_FUNCTION", "83");
    		put("MAKE_FUNCTION", "84");
    		put("BUILD_SLICE", "85");
    		put("MAKE_CLOSURE", "86");
    		put("LOAD_CLOSURE", "87");
    		put("LOAD_DEREF", "88");
    		put("STORE_DEREF", "89");
    		put("CALL_FUNCTION_VAR", "8c");
    		put("CALL_FUNCTION_KW", "8d");
    		put("CALL_FUNCTION_VAR_KW", "8e");
    		put("EXTENDED_ARG", "8f");
    	}};
    	return (CommonTree)adaptor.create( HEX, opcodes.get(symname.toUpperCase()) );
    }
    // Debug.
    boolean isDebug = true;
    // Overriden parser's methods for error decoration.
    public String getErrorMessage(RecognitionException e,
                                  String[] tokenNames) {
        String debugMsg = "\n";

        List stack = getRuleInvocationStack(e, this.getClass().getName());
        debugMsg = "\nrule stack:" + stack + debugMsg;
        
        debugMsg += "type:" + e.getClass().getName() +"\n";

        if ( e instanceof NoViableAltException ) {
    		// Lookahead is not consistent with any of the alternatives.
    		NoViableAltException nvae = (NoViableAltException)e;
    		debugMsg = "no viable alt; token="+e.token+
             " (decision="+nvae.decisionNumber+
             " state "+nvae.stateNumber+")"+
             " decision=<<"+nvae.grammarDecisionDescription+">>\n";
        }
        else if ( e instanceof EarlyExitException ) {
        	// Some repetition rule (..)+ can't be matched.
        	// F.e. happens when .end without a name is encountered.
        	debugMsg += "previous token:" + input.LT(-1) + "\n" +
        	"hint: seems like some required token that must follow the previous accepted is missing\n";
        }

        String inputContext =
            input.LT(-3) == null ? "" : ((Tree)input.LT(-3)).getText()+" "+
            input.LT(-2) == null ? "" : ((Tree)input.LT(-2)).getText()+" "+
            input.LT(-1) == null ? "" : ((Tree)input.LT(-1)).getText()+" >>>"+
            ((Tree)input.LT(1)).getText()+"<<< "+
            ((Tree)input.LT(2)).getText()+" "+
            ((Tree)input.LT(3)).getText();

        debugMsg += "antlr message:" + super.getErrorMessage(e, tokenNames);
        debugMsg += "\ncontext:"+inputContext;

        String msg = "";
        if(isDebug)
        	msg = debugMsg;
        else
    		msg = "stumbled after '"+e.token.getText()+"', more details:\n"+debugMsg;
        return msg;
    }
    // Adds additional details to token string representation.
    public String getTokenErrorDisplay(Token t) {
        return t.toString();
    }
    public String getErrorHeader(RecognitionException e) {
    	String h = super.getErrorHeader(e);
    	return "\nDIRECTIVE WALKER ERROR: " + h;
    }
    // Rocovery methods.
    private String BitSetString(BitSet bs) {
    	String acc = "";
    	for(int i :  bs.toArray()) {
    		acc += " " + tokenNames[i];
    	}
    	return acc;
    }
    @Override
    protected Object recoverFromMismatchedToken(IntStream input, int ttype, BitSet follow) throws RecognitionException {
    	if(isDebug)
    		System.out.println("follow:"+BitSetString(follow));
    	throw new MismatchedTokenException(ttype, input);
    }
    @Override
    public Object recoverFromMismatchedSet(IntStream input, RecognitionException e, BitSet follow) throws RecognitionException {
    	if(isDebug)
    		System.out.println("follow:"+BitSetString(follow));
    	throw e;
    }


    public static class root_return extends TreeRuleReturnScope {
        CommonTree tree;
        public Object getTree() { return tree; }
    };

    // $ANTLR start "root"
    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmSymnameWalker.g:238:1: root : ^( ROOT ( block )? ) ;
    public final pycasmSymnameWalker.root_return root() throws RecognitionException {
        pycasmSymnameWalker.root_return retval = new pycasmSymnameWalker.root_return();
        retval.start = input.LT(1);

        CommonTree root_0 = null;

        CommonTree _first_0 = null;
        CommonTree _last = null;

        CommonTree ROOT1=null;
        pycasmSymnameWalker.block_return block2 = null;


        CommonTree ROOT1_tree=null;

        try {
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmSymnameWalker.g:239:2: ( ^( ROOT ( block )? ) )
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmSymnameWalker.g:240:3: ^( ROOT ( block )? )
            {
            _last = (CommonTree)input.LT(1);
            {
            CommonTree _save_last_1 = _last;
            CommonTree _first_1 = null;
            _last = (CommonTree)input.LT(1);
            ROOT1=(CommonTree)match(input,ROOT,FOLLOW_ROOT_in_root66); if (state.failed) return retval;


            if ( state.backtracking==0 )
            if ( _first_0==null ) _first_0 = ROOT1;
            if ( input.LA(1)==Token.DOWN ) {
                match(input, Token.DOWN, null); if (state.failed) return retval;
                // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmSymnameWalker.g:240:10: ( block )?
                int alt1=2;
                int LA1_0 = input.LA(1);

                if ( (LA1_0==BLOCK) ) {
                    alt1=1;
                }
                switch (alt1) {
                    case 1 :
                        // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmSymnameWalker.g:0:0: block
                        {
                        _last = (CommonTree)input.LT(1);
                        pushFollow(FOLLOW_block_in_root68);
                        block2=block();

                        state._fsp--;
                        if (state.failed) return retval;
                        if ( state.backtracking==0 ) 
                         
                        if ( _first_1==null ) _first_1 = block2.tree;

                        if ( state.backtracking==0 ) {
                        retval.tree = (CommonTree)_first_0;
                        if ( adaptor.getParent(retval.tree)!=null && adaptor.isNil( adaptor.getParent(retval.tree) ) )
                            retval.tree = (CommonTree)adaptor.getParent(retval.tree);}
                        }
                        break;

                }


                match(input, Token.UP, null); if (state.failed) return retval;
            }_last = _save_last_1;
            }


            if ( state.backtracking==0 ) {
            retval.tree = (CommonTree)_first_0;
            if ( adaptor.getParent(retval.tree)!=null && adaptor.isNil( adaptor.getParent(retval.tree) ) )
                retval.tree = (CommonTree)adaptor.getParent(retval.tree);}
            }

        }

        catch (RecognitionException e) {
          this.reportError(e);
          throw e;
        }
        finally {
        }
        return retval;
    }
    // $ANTLR end "root"

    public static class block_return extends TreeRuleReturnScope {
        CommonTree tree;
        public Object getTree() { return tree; }
    };

    // $ANTLR start "block"
    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmSymnameWalker.g:243:1: block : ^( BLOCK ( block_child )+ ) ;
    public final pycasmSymnameWalker.block_return block() throws RecognitionException {
        pycasmSymnameWalker.block_return retval = new pycasmSymnameWalker.block_return();
        retval.start = input.LT(1);

        CommonTree root_0 = null;

        CommonTree _first_0 = null;
        CommonTree _last = null;

        CommonTree BLOCK3=null;
        pycasmSymnameWalker.block_child_return block_child4 = null;


        CommonTree BLOCK3_tree=null;

        try {
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmSymnameWalker.g:244:2: ( ^( BLOCK ( block_child )+ ) )
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmSymnameWalker.g:245:3: ^( BLOCK ( block_child )+ )
            {
            _last = (CommonTree)input.LT(1);
            {
            CommonTree _save_last_1 = _last;
            CommonTree _first_1 = null;
            _last = (CommonTree)input.LT(1);
            BLOCK3=(CommonTree)match(input,BLOCK,FOLLOW_BLOCK_in_block84); if (state.failed) return retval;


            if ( state.backtracking==0 )
            if ( _first_0==null ) _first_0 = BLOCK3;
            match(input, Token.DOWN, null); if (state.failed) return retval;
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmSymnameWalker.g:245:11: ( block_child )+
            int cnt2=0;
            loop2:
            do {
                int alt2=2;
                int LA2_0 = input.LA(1);

                if ( (LA2_0==BLOCK||LA2_0==GEN||(LA2_0>=HEX && LA2_0<=SYM)) ) {
                    alt2=1;
                }


                switch (alt2) {
            	case 1 :
            	    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmSymnameWalker.g:0:0: block_child
            	    {
            	    _last = (CommonTree)input.LT(1);
            	    pushFollow(FOLLOW_block_child_in_block86);
            	    block_child4=block_child();

            	    state._fsp--;
            	    if (state.failed) return retval;
            	    if ( state.backtracking==0 ) 
            	     
            	    if ( _first_1==null ) _first_1 = block_child4.tree;

            	    if ( state.backtracking==0 ) {
            	    retval.tree = (CommonTree)_first_0;
            	    if ( adaptor.getParent(retval.tree)!=null && adaptor.isNil( adaptor.getParent(retval.tree) ) )
            	        retval.tree = (CommonTree)adaptor.getParent(retval.tree);}
            	    }
            	    break;

            	default :
            	    if ( cnt2 >= 1 ) break loop2;
            	    if (state.backtracking>0) {state.failed=true; return retval;}
                        EarlyExitException eee =
                            new EarlyExitException(2, input);
                        throw eee;
                }
                cnt2++;
            } while (true);


            match(input, Token.UP, null); if (state.failed) return retval;_last = _save_last_1;
            }


            if ( state.backtracking==0 ) {
            retval.tree = (CommonTree)_first_0;
            if ( adaptor.getParent(retval.tree)!=null && adaptor.isNil( adaptor.getParent(retval.tree) ) )
                retval.tree = (CommonTree)adaptor.getParent(retval.tree);}
            }

        }

        catch (RecognitionException e) {
          this.reportError(e);
          throw e;
        }
        finally {
        }
        return retval;
    }
    // $ANTLR end "block"

    public static class block_child_return extends TreeRuleReturnScope {
        CommonTree tree;
        public Object getTree() { return tree; }
    };

    // $ANTLR start "block_child"
    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmSymnameWalker.g:248:1: block_child : ( ^( SYM NAME ) -> ^() | HEX | GEN | block );
    public final pycasmSymnameWalker.block_child_return block_child() throws RecognitionException {
        pycasmSymnameWalker.block_child_return retval = new pycasmSymnameWalker.block_child_return();
        retval.start = input.LT(1);

        CommonTree root_0 = null;

        CommonTree _first_0 = null;
        CommonTree _last = null;

        CommonTree SYM5=null;
        CommonTree NAME6=null;
        CommonTree HEX7=null;
        CommonTree GEN8=null;
        pycasmSymnameWalker.block_return block9 = null;


        CommonTree SYM5_tree=null;
        CommonTree NAME6_tree=null;
        CommonTree HEX7_tree=null;
        CommonTree GEN8_tree=null;
        RewriteRuleNodeStream stream_NAME=new RewriteRuleNodeStream(adaptor,"token NAME");
        RewriteRuleNodeStream stream_SYM=new RewriteRuleNodeStream(adaptor,"token SYM");

        try {
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmSymnameWalker.g:249:2: ( ^( SYM NAME ) -> ^() | HEX | GEN | block )
            int alt3=4;
            switch ( input.LA(1) ) {
            case SYM:
                {
                alt3=1;
                }
                break;
            case HEX:
                {
                alt3=2;
                }
                break;
            case GEN:
                {
                alt3=3;
                }
                break;
            case BLOCK:
                {
                alt3=4;
                }
                break;
            default:
                if (state.backtracking>0) {state.failed=true; return retval;}
                NoViableAltException nvae =
                    new NoViableAltException("", 3, 0, input);

                throw nvae;
            }

            switch (alt3) {
                case 1 :
                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmSymnameWalker.g:250:3: ^( SYM NAME )
                    {
                    _last = (CommonTree)input.LT(1);
                    {
                    CommonTree _save_last_1 = _last;
                    CommonTree _first_1 = null;
                    _last = (CommonTree)input.LT(1);
                    SYM5=(CommonTree)match(input,SYM,FOLLOW_SYM_in_block_child102); if (state.failed) return retval; 
                    if ( state.backtracking==0 ) stream_SYM.add(SYM5);


                    if ( state.backtracking==0 )
                    if ( _first_0==null ) _first_0 = SYM5;
                    match(input, Token.DOWN, null); if (state.failed) return retval;
                    _last = (CommonTree)input.LT(1);
                    NAME6=(CommonTree)match(input,NAME,FOLLOW_NAME_in_block_child104); if (state.failed) return retval; 
                    if ( state.backtracking==0 ) stream_NAME.add(NAME6);


                    match(input, Token.UP, null); if (state.failed) return retval;_last = _save_last_1;
                    }



                    // AST REWRITE
                    // elements: 
                    // token labels: 
                    // rule labels: retval
                    // token list labels: 
                    // rule list labels: 
                    // wildcard labels: 
                    if ( state.backtracking==0 ) {
                    retval.tree = root_0;
                    RewriteRuleSubtreeStream stream_retval=new RewriteRuleSubtreeStream(adaptor,"rule retval",retval!=null?retval.tree:null);

                    root_0 = (CommonTree)adaptor.nil();
                    // 250:15: -> ^()
                    {
                        // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmSymnameWalker.g:250:18: ^()
                        {
                        CommonTree root_1 = (CommonTree)adaptor.nil();
                        root_1 = (CommonTree)adaptor.becomeRoot(expandSymname((NAME6!=null?NAME6.getText():null)), root_1);

                        adaptor.addChild(root_0, root_1);
                        }

                    }

                    retval.tree = (CommonTree)adaptor.rulePostProcessing(root_0);
                    input.replaceChildren(adaptor.getParent(retval.start),
                                          adaptor.getChildIndex(retval.start),
                                          adaptor.getChildIndex(_last),
                                          retval.tree);}
                    }
                    break;
                case 2 :
                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmSymnameWalker.g:251:4: HEX
                    {
                    _last = (CommonTree)input.LT(1);
                    HEX7=(CommonTree)match(input,HEX,FOLLOW_HEX_in_block_child116); if (state.failed) return retval;
                     
                    if ( state.backtracking==0 )
                    if ( _first_0==null ) _first_0 = HEX7;

                    if ( state.backtracking==0 ) {
                    retval.tree = (CommonTree)_first_0;
                    if ( adaptor.getParent(retval.tree)!=null && adaptor.isNil( adaptor.getParent(retval.tree) ) )
                        retval.tree = (CommonTree)adaptor.getParent(retval.tree);}
                    }
                    break;
                case 3 :
                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmSymnameWalker.g:252:4: GEN
                    {
                    _last = (CommonTree)input.LT(1);
                    GEN8=(CommonTree)match(input,GEN,FOLLOW_GEN_in_block_child121); if (state.failed) return retval;
                     
                    if ( state.backtracking==0 )
                    if ( _first_0==null ) _first_0 = GEN8;

                    if ( state.backtracking==0 ) {
                    retval.tree = (CommonTree)_first_0;
                    if ( adaptor.getParent(retval.tree)!=null && adaptor.isNil( adaptor.getParent(retval.tree) ) )
                        retval.tree = (CommonTree)adaptor.getParent(retval.tree);}
                    }
                    break;
                case 4 :
                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmSymnameWalker.g:253:4: block
                    {
                    _last = (CommonTree)input.LT(1);
                    pushFollow(FOLLOW_block_in_block_child126);
                    block9=block();

                    state._fsp--;
                    if (state.failed) return retval;
                    if ( state.backtracking==0 ) 
                     
                    if ( _first_0==null ) _first_0 = block9.tree;

                    if ( state.backtracking==0 ) {
                    retval.tree = (CommonTree)_first_0;
                    if ( adaptor.getParent(retval.tree)!=null && adaptor.isNil( adaptor.getParent(retval.tree) ) )
                        retval.tree = (CommonTree)adaptor.getParent(retval.tree);}
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
        return retval;
    }
    // $ANTLR end "block_child"

    // Delegated rules


 

    public static final BitSet FOLLOW_ROOT_in_root66 = new BitSet(new long[]{0x0000000000000004L});
    public static final BitSet FOLLOW_block_in_root68 = new BitSet(new long[]{0x0000000000000008L});
    public static final BitSet FOLLOW_BLOCK_in_block84 = new BitSet(new long[]{0x0000000000000004L});
    public static final BitSet FOLLOW_block_child_in_block86 = new BitSet(new long[]{0x0000000060000148L});
    public static final BitSet FOLLOW_SYM_in_block_child102 = new BitSet(new long[]{0x0000000000000004L});
    public static final BitSet FOLLOW_NAME_in_block_child104 = new BitSet(new long[]{0x0000000000000008L});
    public static final BitSet FOLLOW_HEX_in_block_child116 = new BitSet(new long[]{0x0000000000000002L});
    public static final BitSet FOLLOW_GEN_in_block_child121 = new BitSet(new long[]{0x0000000000000002L});
    public static final BitSet FOLLOW_block_in_block_child126 = new BitSet(new long[]{0x0000000000000002L});

}