// $ANTLR 3.1.3 Mar 17, 2009 19:23:44 G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmDirectiveWalker.g 2011-05-08 12:08:40

package pycasm.parser;
import pycasm.sym.PycasmRootScope;


import org.antlr.runtime.*;
import org.antlr.runtime.tree.*;import java.util.Stack;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;

public class pycasmDirectiveWalker extends TreeParser {
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


        public pycasmDirectiveWalker(TreeNodeStream input) {
            this(input, new RecognizerSharedState());
        }
        public pycasmDirectiveWalker(TreeNodeStream input, RecognizerSharedState state) {
            super(input, state);
             
        }
        
    protected TreeAdaptor adaptor = new CommonTreeAdaptor();

    public void setTreeAdaptor(TreeAdaptor adaptor) {
        this.adaptor = adaptor;
    }
    public TreeAdaptor getTreeAdaptor() {
        return adaptor;
    }

    public String[] getTokenNames() { return pycasmDirectiveWalker.tokenNames; }
    public String getGrammarFileName() { return "G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmDirectiveWalker.g"; }


    public PycasmRootScope rootScope = new PycasmRootScope();

    public CommonTree expandDirective(String dotName, CommonTree args, CommonTree body) throws IllegalArgumentException {
    	String name = dotName.substring(1);
    	
    	if (name.equals("python")) {
    		return (CommonTree)adaptor.create(HEX, "b3f20d0a");
    	}
    	else if (name.equals("stamp"))
    		return (CommonTree)adaptor.create(HEX,"00000000");
    	else throw new IllegalArgumentException("Unknown directive named "+name+".");
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
    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmDirectiveWalker.g:132:1: root : ^( ROOT ( block )? ) ;
    public final pycasmDirectiveWalker.root_return root() throws RecognitionException {
        pycasmDirectiveWalker.root_return retval = new pycasmDirectiveWalker.root_return();
        retval.start = input.LT(1);

        CommonTree root_0 = null;

        CommonTree _first_0 = null;
        CommonTree _last = null;

        CommonTree ROOT1=null;
        pycasmDirectiveWalker.block_return block2 = null;


        CommonTree ROOT1_tree=null;

        try {
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmDirectiveWalker.g:133:2: ( ^( ROOT ( block )? ) )
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmDirectiveWalker.g:134:3: ^( ROOT ( block )? )
            {
            _last = (CommonTree)input.LT(1);
            {
            CommonTree _save_last_1 = _last;
            CommonTree _first_1 = null;
            _last = (CommonTree)input.LT(1);
            ROOT1=(CommonTree)match(input,ROOT,FOLLOW_ROOT_in_root67); if (state.failed) return retval;


            if ( state.backtracking==0 )
            if ( _first_0==null ) _first_0 = ROOT1;
            if ( input.LA(1)==Token.DOWN ) {
                match(input, Token.DOWN, null); if (state.failed) return retval;
                // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmDirectiveWalker.g:134:10: ( block )?
                int alt1=2;
                int LA1_0 = input.LA(1);

                if ( (LA1_0==BLOCK) ) {
                    alt1=1;
                }
                switch (alt1) {
                    case 1 :
                        // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmDirectiveWalker.g:0:0: block
                        {
                        _last = (CommonTree)input.LT(1);
                        pushFollow(FOLLOW_block_in_root69);
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
    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmDirectiveWalker.g:137:1: block : ^( BLOCK ( block_child )+ ) ;
    public final pycasmDirectiveWalker.block_return block() throws RecognitionException {
        pycasmDirectiveWalker.block_return retval = new pycasmDirectiveWalker.block_return();
        retval.start = input.LT(1);

        CommonTree root_0 = null;

        CommonTree _first_0 = null;
        CommonTree _last = null;

        CommonTree BLOCK3=null;
        pycasmDirectiveWalker.block_child_return block_child4 = null;


        CommonTree BLOCK3_tree=null;

        try {
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmDirectiveWalker.g:138:2: ( ^( BLOCK ( block_child )+ ) )
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmDirectiveWalker.g:139:3: ^( BLOCK ( block_child )+ )
            {
            _last = (CommonTree)input.LT(1);
            {
            CommonTree _save_last_1 = _last;
            CommonTree _first_1 = null;
            _last = (CommonTree)input.LT(1);
            BLOCK3=(CommonTree)match(input,BLOCK,FOLLOW_BLOCK_in_block85); if (state.failed) return retval;


            if ( state.backtracking==0 )
            if ( _first_0==null ) _first_0 = BLOCK3;
            match(input, Token.DOWN, null); if (state.failed) return retval;
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmDirectiveWalker.g:139:11: ( block_child )+
            int cnt2=0;
            loop2:
            do {
                int alt2=2;
                int LA2_0 = input.LA(1);

                if ( (LA2_0==BLOCK||LA2_0==GEN||LA2_0==DOT_NAME||(LA2_0>=HEX && LA2_0<=SYM)) ) {
                    alt2=1;
                }


                switch (alt2) {
            	case 1 :
            	    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmDirectiveWalker.g:0:0: block_child
            	    {
            	    _last = (CommonTree)input.LT(1);
            	    pushFollow(FOLLOW_block_child_in_block87);
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
    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmDirectiveWalker.g:142:1: block_child : ( directive | ^( SYM NAME ) | HEX | GEN | block );
    public final pycasmDirectiveWalker.block_child_return block_child() throws RecognitionException {
        pycasmDirectiveWalker.block_child_return retval = new pycasmDirectiveWalker.block_child_return();
        retval.start = input.LT(1);

        CommonTree root_0 = null;

        CommonTree _first_0 = null;
        CommonTree _last = null;

        CommonTree SYM6=null;
        CommonTree NAME7=null;
        CommonTree HEX8=null;
        CommonTree GEN9=null;
        pycasmDirectiveWalker.directive_return directive5 = null;

        pycasmDirectiveWalker.block_return block10 = null;


        CommonTree SYM6_tree=null;
        CommonTree NAME7_tree=null;
        CommonTree HEX8_tree=null;
        CommonTree GEN9_tree=null;

        try {
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmDirectiveWalker.g:143:2: ( directive | ^( SYM NAME ) | HEX | GEN | block )
            int alt3=5;
            switch ( input.LA(1) ) {
            case DOT_NAME:
                {
                alt3=1;
                }
                break;
            case SYM:
                {
                alt3=2;
                }
                break;
            case HEX:
                {
                alt3=3;
                }
                break;
            case GEN:
                {
                alt3=4;
                }
                break;
            case BLOCK:
                {
                alt3=5;
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
                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmDirectiveWalker.g:144:3: directive
                    {
                    _last = (CommonTree)input.LT(1);
                    pushFollow(FOLLOW_directive_in_block_child103);
                    directive5=directive();

                    state._fsp--;
                    if (state.failed) return retval;
                    if ( state.backtracking==0 ) 
                     
                    if ( _first_0==null ) _first_0 = directive5.tree;

                    if ( state.backtracking==0 ) {
                    retval.tree = (CommonTree)_first_0;
                    if ( adaptor.getParent(retval.tree)!=null && adaptor.isNil( adaptor.getParent(retval.tree) ) )
                        retval.tree = (CommonTree)adaptor.getParent(retval.tree);}
                    }
                    break;
                case 2 :
                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmDirectiveWalker.g:145:4: ^( SYM NAME )
                    {
                    _last = (CommonTree)input.LT(1);
                    {
                    CommonTree _save_last_1 = _last;
                    CommonTree _first_1 = null;
                    _last = (CommonTree)input.LT(1);
                    SYM6=(CommonTree)match(input,SYM,FOLLOW_SYM_in_block_child109); if (state.failed) return retval;


                    if ( state.backtracking==0 )
                    if ( _first_0==null ) _first_0 = SYM6;
                    match(input, Token.DOWN, null); if (state.failed) return retval;
                    _last = (CommonTree)input.LT(1);
                    NAME7=(CommonTree)match(input,NAME,FOLLOW_NAME_in_block_child111); if (state.failed) return retval;
                     
                    if ( state.backtracking==0 )
                    if ( _first_1==null ) _first_1 = NAME7;

                    match(input, Token.UP, null); if (state.failed) return retval;_last = _save_last_1;
                    }


                    if ( state.backtracking==0 ) {
                    retval.tree = (CommonTree)_first_0;
                    if ( adaptor.getParent(retval.tree)!=null && adaptor.isNil( adaptor.getParent(retval.tree) ) )
                        retval.tree = (CommonTree)adaptor.getParent(retval.tree);}
                    }
                    break;
                case 3 :
                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmDirectiveWalker.g:146:4: HEX
                    {
                    _last = (CommonTree)input.LT(1);
                    HEX8=(CommonTree)match(input,HEX,FOLLOW_HEX_in_block_child117); if (state.failed) return retval;
                     
                    if ( state.backtracking==0 )
                    if ( _first_0==null ) _first_0 = HEX8;

                    if ( state.backtracking==0 ) {
                    retval.tree = (CommonTree)_first_0;
                    if ( adaptor.getParent(retval.tree)!=null && adaptor.isNil( adaptor.getParent(retval.tree) ) )
                        retval.tree = (CommonTree)adaptor.getParent(retval.tree);}
                    }
                    break;
                case 4 :
                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmDirectiveWalker.g:147:4: GEN
                    {
                    _last = (CommonTree)input.LT(1);
                    GEN9=(CommonTree)match(input,GEN,FOLLOW_GEN_in_block_child122); if (state.failed) return retval;
                     
                    if ( state.backtracking==0 )
                    if ( _first_0==null ) _first_0 = GEN9;

                    if ( state.backtracking==0 ) {
                    retval.tree = (CommonTree)_first_0;
                    if ( adaptor.getParent(retval.tree)!=null && adaptor.isNil( adaptor.getParent(retval.tree) ) )
                        retval.tree = (CommonTree)adaptor.getParent(retval.tree);}
                    }
                    break;
                case 5 :
                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmDirectiveWalker.g:148:4: block
                    {
                    _last = (CommonTree)input.LT(1);
                    pushFollow(FOLLOW_block_in_block_child127);
                    block10=block();

                    state._fsp--;
                    if (state.failed) return retval;
                    if ( state.backtracking==0 ) 
                     
                    if ( _first_0==null ) _first_0 = block10.tree;

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

    public static class directive_return extends TreeRuleReturnScope {
        CommonTree tree;
        public Object getTree() { return tree; }
    };

    // $ANTLR start "directive"
    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmDirectiveWalker.g:151:1: directive : ^( DOT_NAME ^( ARGS ( directive_args )* ) ( block )? ) -> ^() ;
    public final pycasmDirectiveWalker.directive_return directive() throws RecognitionException {
        pycasmDirectiveWalker.directive_return retval = new pycasmDirectiveWalker.directive_return();
        retval.start = input.LT(1);

        CommonTree root_0 = null;

        CommonTree _first_0 = null;
        CommonTree _last = null;

        CommonTree DOT_NAME11=null;
        CommonTree ARGS12=null;
        pycasmDirectiveWalker.directive_args_return directive_args13 = null;

        pycasmDirectiveWalker.block_return block14 = null;


        CommonTree DOT_NAME11_tree=null;
        CommonTree ARGS12_tree=null;
        RewriteRuleNodeStream stream_ARGS=new RewriteRuleNodeStream(adaptor,"token ARGS");
        RewriteRuleNodeStream stream_DOT_NAME=new RewriteRuleNodeStream(adaptor,"token DOT_NAME");
        RewriteRuleSubtreeStream stream_directive_args=new RewriteRuleSubtreeStream(adaptor,"rule directive_args");
        RewriteRuleSubtreeStream stream_block=new RewriteRuleSubtreeStream(adaptor,"rule block");
        try {
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmDirectiveWalker.g:152:2: ( ^( DOT_NAME ^( ARGS ( directive_args )* ) ( block )? ) -> ^() )
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmDirectiveWalker.g:153:3: ^( DOT_NAME ^( ARGS ( directive_args )* ) ( block )? )
            {
            _last = (CommonTree)input.LT(1);
            {
            CommonTree _save_last_1 = _last;
            CommonTree _first_1 = null;
            _last = (CommonTree)input.LT(1);
            DOT_NAME11=(CommonTree)match(input,DOT_NAME,FOLLOW_DOT_NAME_in_directive141); if (state.failed) return retval; 
            if ( state.backtracking==0 ) stream_DOT_NAME.add(DOT_NAME11);


            if ( state.backtracking==0 )
            if ( _first_0==null ) _first_0 = DOT_NAME11;
            match(input, Token.DOWN, null); if (state.failed) return retval;
            _last = (CommonTree)input.LT(1);
            {
            CommonTree _save_last_2 = _last;
            CommonTree _first_2 = null;
            _last = (CommonTree)input.LT(1);
            ARGS12=(CommonTree)match(input,ARGS,FOLLOW_ARGS_in_directive144); if (state.failed) return retval; 
            if ( state.backtracking==0 ) stream_ARGS.add(ARGS12);


            if ( state.backtracking==0 )
            if ( _first_1==null ) _first_1 = ARGS12;
            if ( input.LA(1)==Token.DOWN ) {
                match(input, Token.DOWN, null); if (state.failed) return retval;
                // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmDirectiveWalker.g:153:21: ( directive_args )*
                loop4:
                do {
                    int alt4=2;
                    int LA4_0 = input.LA(1);

                    if ( (LA4_0==GEN||LA4_0==HEX_DIGIT||LA4_0==NON_WS_SEQUENCE||(LA4_0>=HEX && LA4_0<=SYM)) ) {
                        alt4=1;
                    }


                    switch (alt4) {
                	case 1 :
                	    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmDirectiveWalker.g:0:0: directive_args
                	    {
                	    _last = (CommonTree)input.LT(1);
                	    pushFollow(FOLLOW_directive_args_in_directive146);
                	    directive_args13=directive_args();

                	    state._fsp--;
                	    if (state.failed) return retval;
                	    if ( state.backtracking==0 ) stream_directive_args.add(directive_args13.getTree());

                	    if ( state.backtracking==0 ) {
                	    retval.tree = (CommonTree)_first_0;
                	    if ( adaptor.getParent(retval.tree)!=null && adaptor.isNil( adaptor.getParent(retval.tree) ) )
                	        retval.tree = (CommonTree)adaptor.getParent(retval.tree);}
                	    }
                	    break;

                	default :
                	    break loop4;
                    }
                } while (true);


                match(input, Token.UP, null); if (state.failed) return retval;
            }_last = _save_last_2;
            }

            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmDirectiveWalker.g:154:4: ( block )?
            int alt5=2;
            int LA5_0 = input.LA(1);

            if ( (LA5_0==BLOCK) ) {
                alt5=1;
            }
            switch (alt5) {
                case 1 :
                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmDirectiveWalker.g:0:0: block
                    {
                    _last = (CommonTree)input.LT(1);
                    pushFollow(FOLLOW_block_in_directive153);
                    block14=block();

                    state._fsp--;
                    if (state.failed) return retval;
                    if ( state.backtracking==0 ) stream_block.add(block14.getTree());

                    if ( state.backtracking==0 ) {
                    retval.tree = (CommonTree)_first_0;
                    if ( adaptor.getParent(retval.tree)!=null && adaptor.isNil( adaptor.getParent(retval.tree) ) )
                        retval.tree = (CommonTree)adaptor.getParent(retval.tree);}
                    }
                    break;

            }


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
            // 156:3: -> ^()
            {
                // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmDirectiveWalker.g:156:6: ^()
                {
                CommonTree root_1 = (CommonTree)adaptor.nil();
                root_1 = (CommonTree)adaptor.becomeRoot(expandDirective(DOT_NAME11.getText(), ARGS12_tree, (block14!=null?((CommonTree)block14.tree):null)), root_1);

                adaptor.addChild(root_0, root_1);
                }

            }

            retval.tree = (CommonTree)adaptor.rulePostProcessing(root_0);
            input.replaceChildren(adaptor.getParent(retval.start),
                                  adaptor.getChildIndex(retval.start),
                                  adaptor.getChildIndex(_last),
                                  retval.tree);}
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
    // $ANTLR end "directive"

    public static class directive_args_return extends TreeRuleReturnScope {
        CommonTree tree;
        public Object getTree() { return tree; }
    };

    // $ANTLR start "directive_args"
    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmDirectiveWalker.g:160:1: directive_args : ( ^( SYM NAME ) | HEX | GEN | HEX_DIGIT | NON_WS_SEQUENCE );
    public final pycasmDirectiveWalker.directive_args_return directive_args() throws RecognitionException {
        pycasmDirectiveWalker.directive_args_return retval = new pycasmDirectiveWalker.directive_args_return();
        retval.start = input.LT(1);

        CommonTree root_0 = null;

        CommonTree _first_0 = null;
        CommonTree _last = null;

        CommonTree SYM15=null;
        CommonTree NAME16=null;
        CommonTree HEX17=null;
        CommonTree GEN18=null;
        CommonTree HEX_DIGIT19=null;
        CommonTree NON_WS_SEQUENCE20=null;

        CommonTree SYM15_tree=null;
        CommonTree NAME16_tree=null;
        CommonTree HEX17_tree=null;
        CommonTree GEN18_tree=null;
        CommonTree HEX_DIGIT19_tree=null;
        CommonTree NON_WS_SEQUENCE20_tree=null;

        try {
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmDirectiveWalker.g:161:2: ( ^( SYM NAME ) | HEX | GEN | HEX_DIGIT | NON_WS_SEQUENCE )
            int alt6=5;
            switch ( input.LA(1) ) {
            case SYM:
                {
                alt6=1;
                }
                break;
            case HEX:
                {
                alt6=2;
                }
                break;
            case GEN:
                {
                alt6=3;
                }
                break;
            case HEX_DIGIT:
                {
                alt6=4;
                }
                break;
            case NON_WS_SEQUENCE:
                {
                alt6=5;
                }
                break;
            default:
                if (state.backtracking>0) {state.failed=true; return retval;}
                NoViableAltException nvae =
                    new NoViableAltException("", 6, 0, input);

                throw nvae;
            }

            switch (alt6) {
                case 1 :
                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmDirectiveWalker.g:162:3: ^( SYM NAME )
                    {
                    _last = (CommonTree)input.LT(1);
                    {
                    CommonTree _save_last_1 = _last;
                    CommonTree _first_1 = null;
                    _last = (CommonTree)input.LT(1);
                    SYM15=(CommonTree)match(input,SYM,FOLLOW_SYM_in_directive_args183); if (state.failed) return retval;


                    if ( state.backtracking==0 )
                    if ( _first_0==null ) _first_0 = SYM15;
                    match(input, Token.DOWN, null); if (state.failed) return retval;
                    _last = (CommonTree)input.LT(1);
                    NAME16=(CommonTree)match(input,NAME,FOLLOW_NAME_in_directive_args185); if (state.failed) return retval;
                     
                    if ( state.backtracking==0 )
                    if ( _first_1==null ) _first_1 = NAME16;

                    match(input, Token.UP, null); if (state.failed) return retval;_last = _save_last_1;
                    }


                    if ( state.backtracking==0 ) {
                    retval.tree = (CommonTree)_first_0;
                    if ( adaptor.getParent(retval.tree)!=null && adaptor.isNil( adaptor.getParent(retval.tree) ) )
                        retval.tree = (CommonTree)adaptor.getParent(retval.tree);}
                    }
                    break;
                case 2 :
                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmDirectiveWalker.g:163:4: HEX
                    {
                    _last = (CommonTree)input.LT(1);
                    HEX17=(CommonTree)match(input,HEX,FOLLOW_HEX_in_directive_args191); if (state.failed) return retval;
                     
                    if ( state.backtracking==0 )
                    if ( _first_0==null ) _first_0 = HEX17;

                    if ( state.backtracking==0 ) {
                    retval.tree = (CommonTree)_first_0;
                    if ( adaptor.getParent(retval.tree)!=null && adaptor.isNil( adaptor.getParent(retval.tree) ) )
                        retval.tree = (CommonTree)adaptor.getParent(retval.tree);}
                    }
                    break;
                case 3 :
                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmDirectiveWalker.g:164:4: GEN
                    {
                    _last = (CommonTree)input.LT(1);
                    GEN18=(CommonTree)match(input,GEN,FOLLOW_GEN_in_directive_args196); if (state.failed) return retval;
                     
                    if ( state.backtracking==0 )
                    if ( _first_0==null ) _first_0 = GEN18;

                    if ( state.backtracking==0 ) {
                    retval.tree = (CommonTree)_first_0;
                    if ( adaptor.getParent(retval.tree)!=null && adaptor.isNil( adaptor.getParent(retval.tree) ) )
                        retval.tree = (CommonTree)adaptor.getParent(retval.tree);}
                    }
                    break;
                case 4 :
                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmDirectiveWalker.g:165:4: HEX_DIGIT
                    {
                    _last = (CommonTree)input.LT(1);
                    HEX_DIGIT19=(CommonTree)match(input,HEX_DIGIT,FOLLOW_HEX_DIGIT_in_directive_args201); if (state.failed) return retval;
                     
                    if ( state.backtracking==0 )
                    if ( _first_0==null ) _first_0 = HEX_DIGIT19;

                    if ( state.backtracking==0 ) {
                    retval.tree = (CommonTree)_first_0;
                    if ( adaptor.getParent(retval.tree)!=null && adaptor.isNil( adaptor.getParent(retval.tree) ) )
                        retval.tree = (CommonTree)adaptor.getParent(retval.tree);}
                    }
                    break;
                case 5 :
                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmDirectiveWalker.g:166:4: NON_WS_SEQUENCE
                    {
                    _last = (CommonTree)input.LT(1);
                    NON_WS_SEQUENCE20=(CommonTree)match(input,NON_WS_SEQUENCE,FOLLOW_NON_WS_SEQUENCE_in_directive_args206); if (state.failed) return retval;
                     
                    if ( state.backtracking==0 )
                    if ( _first_0==null ) _first_0 = NON_WS_SEQUENCE20;

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
    // $ANTLR end "directive_args"

    // Delegated rules


 

    public static final BitSet FOLLOW_ROOT_in_root67 = new BitSet(new long[]{0x0000000000000004L});
    public static final BitSet FOLLOW_block_in_root69 = new BitSet(new long[]{0x0000000000000008L});
    public static final BitSet FOLLOW_BLOCK_in_block85 = new BitSet(new long[]{0x0000000000000004L});
    public static final BitSet FOLLOW_block_child_in_block87 = new BitSet(new long[]{0x0000000060100148L});
    public static final BitSet FOLLOW_directive_in_block_child103 = new BitSet(new long[]{0x0000000000000002L});
    public static final BitSet FOLLOW_SYM_in_block_child109 = new BitSet(new long[]{0x0000000000000004L});
    public static final BitSet FOLLOW_NAME_in_block_child111 = new BitSet(new long[]{0x0000000000000008L});
    public static final BitSet FOLLOW_HEX_in_block_child117 = new BitSet(new long[]{0x0000000000000002L});
    public static final BitSet FOLLOW_GEN_in_block_child122 = new BitSet(new long[]{0x0000000000000002L});
    public static final BitSet FOLLOW_block_in_block_child127 = new BitSet(new long[]{0x0000000000000002L});
    public static final BitSet FOLLOW_DOT_NAME_in_directive141 = new BitSet(new long[]{0x0000000000000004L});
    public static final BitSet FOLLOW_ARGS_in_directive144 = new BitSet(new long[]{0x0000000000000004L});
    public static final BitSet FOLLOW_directive_args_in_directive146 = new BitSet(new long[]{0x0000000062002108L});
    public static final BitSet FOLLOW_block_in_directive153 = new BitSet(new long[]{0x0000000000000008L});
    public static final BitSet FOLLOW_SYM_in_directive_args183 = new BitSet(new long[]{0x0000000000000004L});
    public static final BitSet FOLLOW_NAME_in_directive_args185 = new BitSet(new long[]{0x0000000000000008L});
    public static final BitSet FOLLOW_HEX_in_directive_args191 = new BitSet(new long[]{0x0000000000000002L});
    public static final BitSet FOLLOW_GEN_in_directive_args196 = new BitSet(new long[]{0x0000000000000002L});
    public static final BitSet FOLLOW_HEX_DIGIT_in_directive_args201 = new BitSet(new long[]{0x0000000000000002L});
    public static final BitSet FOLLOW_NON_WS_SEQUENCE_in_directive_args206 = new BitSet(new long[]{0x0000000000000002L});

}