// $ANTLR 3.1.3 Mar 17, 2009 19:23:44 G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmGenerativeWalker.g 2011-05-08 12:08:41

package pycasm.parser;
import java.text.*;


import org.antlr.runtime.*;
import org.antlr.runtime.tree.*;import java.util.Stack;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;

public class pycasmGenerativeWalker extends TreeParser {
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


        public pycasmGenerativeWalker(TreeNodeStream input) {
            this(input, new RecognizerSharedState());
        }
        public pycasmGenerativeWalker(TreeNodeStream input, RecognizerSharedState state) {
            super(input, state);
             
        }
        
    protected TreeAdaptor adaptor = new CommonTreeAdaptor();

    public void setTreeAdaptor(TreeAdaptor adaptor) {
        this.adaptor = adaptor;
    }
    public TreeAdaptor getTreeAdaptor() {
        return adaptor;
    }

    public String[] getTokenNames() { return pycasmGenerativeWalker.tokenNames; }
    public String getGrammarFileName() { return "G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmGenerativeWalker.g"; }


    CommonTree expandGenerative(CommonTree gentree) {
    	String s = gentree.getText();
    	StringBuilder res = new StringBuilder();
    	if( s.startsWith("s") ) {
    		// String type.
    		s = s.substring(1);
    	} else if( s.startsWith("t") ) {
    		// Dunno what type.
    		s = s.substring(1);
    	}
    	if (s.startsWith("'")) {
    		// ascii to hex
    		CharacterIterator it = new StringCharacterIterator(s.substring(1,s.length()-1));
    		for (char ch=it.first(); ch != CharacterIterator.DONE; ch=it.next())
    			res.append( Integer.toHexString( (short)ch ) );
    	}
    	return (CommonTree)adaptor.create(HEX, res.toString());
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
    	return "\nGENERATIVE WALKER ERROR: " + h;
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
    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmGenerativeWalker.g:121:1: root : ^( ROOT ( block )? ) ;
    public final pycasmGenerativeWalker.root_return root() throws RecognitionException {
        pycasmGenerativeWalker.root_return retval = new pycasmGenerativeWalker.root_return();
        retval.start = input.LT(1);

        CommonTree root_0 = null;

        CommonTree _first_0 = null;
        CommonTree _last = null;

        CommonTree ROOT1=null;
        pycasmGenerativeWalker.block_return block2 = null;


        CommonTree ROOT1_tree=null;

        try {
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmGenerativeWalker.g:122:2: ( ^( ROOT ( block )? ) )
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmGenerativeWalker.g:123:3: ^( ROOT ( block )? )
            {
            _last = (CommonTree)input.LT(1);
            {
            CommonTree _save_last_1 = _last;
            CommonTree _first_1 = null;
            _last = (CommonTree)input.LT(1);
            ROOT1=(CommonTree)match(input,ROOT,FOLLOW_ROOT_in_root65); if (state.failed) return retval;


            if ( state.backtracking==0 )
            if ( _first_0==null ) _first_0 = ROOT1;
            if ( input.LA(1)==Token.DOWN ) {
                match(input, Token.DOWN, null); if (state.failed) return retval;
                // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmGenerativeWalker.g:123:10: ( block )?
                int alt1=2;
                int LA1_0 = input.LA(1);

                if ( (LA1_0==BLOCK) ) {
                    alt1=1;
                }
                switch (alt1) {
                    case 1 :
                        // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmGenerativeWalker.g:0:0: block
                        {
                        _last = (CommonTree)input.LT(1);
                        pushFollow(FOLLOW_block_in_root67);
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
    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmGenerativeWalker.g:126:1: block : ^( BLOCK ( block_child )+ ) ;
    public final pycasmGenerativeWalker.block_return block() throws RecognitionException {
        pycasmGenerativeWalker.block_return retval = new pycasmGenerativeWalker.block_return();
        retval.start = input.LT(1);

        CommonTree root_0 = null;

        CommonTree _first_0 = null;
        CommonTree _last = null;

        CommonTree BLOCK3=null;
        pycasmGenerativeWalker.block_child_return block_child4 = null;


        CommonTree BLOCK3_tree=null;

        try {
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmGenerativeWalker.g:127:2: ( ^( BLOCK ( block_child )+ ) )
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmGenerativeWalker.g:128:3: ^( BLOCK ( block_child )+ )
            {
            _last = (CommonTree)input.LT(1);
            {
            CommonTree _save_last_1 = _last;
            CommonTree _first_1 = null;
            _last = (CommonTree)input.LT(1);
            BLOCK3=(CommonTree)match(input,BLOCK,FOLLOW_BLOCK_in_block83); if (state.failed) return retval;


            if ( state.backtracking==0 )
            if ( _first_0==null ) _first_0 = BLOCK3;
            match(input, Token.DOWN, null); if (state.failed) return retval;
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmGenerativeWalker.g:128:11: ( block_child )+
            int cnt2=0;
            loop2:
            do {
                int alt2=2;
                int LA2_0 = input.LA(1);

                if ( (LA2_0==BLOCK||LA2_0==GEN||LA2_0==HEX) ) {
                    alt2=1;
                }


                switch (alt2) {
            	case 1 :
            	    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmGenerativeWalker.g:0:0: block_child
            	    {
            	    _last = (CommonTree)input.LT(1);
            	    pushFollow(FOLLOW_block_child_in_block85);
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
    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmGenerativeWalker.g:131:1: block_child : ( HEX | GEN -> ^() | block );
    public final pycasmGenerativeWalker.block_child_return block_child() throws RecognitionException {
        pycasmGenerativeWalker.block_child_return retval = new pycasmGenerativeWalker.block_child_return();
        retval.start = input.LT(1);

        CommonTree root_0 = null;

        CommonTree _first_0 = null;
        CommonTree _last = null;

        CommonTree HEX5=null;
        CommonTree GEN6=null;
        pycasmGenerativeWalker.block_return block7 = null;


        CommonTree HEX5_tree=null;
        CommonTree GEN6_tree=null;
        RewriteRuleNodeStream stream_GEN=new RewriteRuleNodeStream(adaptor,"token GEN");

        try {
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmGenerativeWalker.g:132:2: ( HEX | GEN -> ^() | block )
            int alt3=3;
            switch ( input.LA(1) ) {
            case HEX:
                {
                alt3=1;
                }
                break;
            case GEN:
                {
                alt3=2;
                }
                break;
            case BLOCK:
                {
                alt3=3;
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
                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmGenerativeWalker.g:133:3: HEX
                    {
                    _last = (CommonTree)input.LT(1);
                    HEX5=(CommonTree)match(input,HEX,FOLLOW_HEX_in_block_child100); if (state.failed) return retval;
                     
                    if ( state.backtracking==0 )
                    if ( _first_0==null ) _first_0 = HEX5;

                    if ( state.backtracking==0 ) {
                    retval.tree = (CommonTree)_first_0;
                    if ( adaptor.getParent(retval.tree)!=null && adaptor.isNil( adaptor.getParent(retval.tree) ) )
                        retval.tree = (CommonTree)adaptor.getParent(retval.tree);}
                    }
                    break;
                case 2 :
                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmGenerativeWalker.g:134:4: GEN
                    {
                    _last = (CommonTree)input.LT(1);
                    GEN6=(CommonTree)match(input,GEN,FOLLOW_GEN_in_block_child105); if (state.failed) return retval; 
                    if ( state.backtracking==0 ) stream_GEN.add(GEN6);



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
                    // 134:8: -> ^()
                    {
                        // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmGenerativeWalker.g:134:11: ^()
                        {
                        CommonTree root_1 = (CommonTree)adaptor.nil();
                        root_1 = (CommonTree)adaptor.becomeRoot(expandGenerative(GEN6), root_1);

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
                case 3 :
                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmGenerativeWalker.g:135:4: block
                    {
                    _last = (CommonTree)input.LT(1);
                    pushFollow(FOLLOW_block_in_block_child116);
                    block7=block();

                    state._fsp--;
                    if (state.failed) return retval;
                    if ( state.backtracking==0 ) 
                     
                    if ( _first_0==null ) _first_0 = block7.tree;

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


 

    public static final BitSet FOLLOW_ROOT_in_root65 = new BitSet(new long[]{0x0000000000000004L});
    public static final BitSet FOLLOW_block_in_root67 = new BitSet(new long[]{0x0000000000000008L});
    public static final BitSet FOLLOW_BLOCK_in_block83 = new BitSet(new long[]{0x0000000000000004L});
    public static final BitSet FOLLOW_block_child_in_block85 = new BitSet(new long[]{0x0000000020000148L});
    public static final BitSet FOLLOW_HEX_in_block_child100 = new BitSet(new long[]{0x0000000000000002L});
    public static final BitSet FOLLOW_GEN_in_block_child105 = new BitSet(new long[]{0x0000000000000002L});
    public static final BitSet FOLLOW_block_in_block_child116 = new BitSet(new long[]{0x0000000000000002L});

}