// $ANTLR 3.1.3 Mar 17, 2009 19:23:44 G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g 2011-05-08 12:08:39

package pycasm.parser;
import pycasm.sym.*;
import java.util.Arrays;


import org.antlr.runtime.*;
import java.util.Stack;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;

import org.antlr.runtime.tree.*;

public class pycasmParser extends Parser {
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
    public static final int ARGS=7;
    public static final int NON_WS_SEQUENCE=25;
    public static final int GEN=8;
    public static final int DOT_NAME=20;
    public static final int COMMENT=24;
    public static final int HEX_QUAD=12;
    public static final int STRING=18;
    public static final int HEX_PAIR=9;

    // delegates
    // delegators


        public pycasmParser(TokenStream input) {
            this(input, new RecognizerSharedState());
        }
        public pycasmParser(TokenStream input, RecognizerSharedState state) {
            super(input, state);
            this.state.ruleMemo = new HashMap[48+1];
             
             
        }
        
    protected TreeAdaptor adaptor = new CommonTreeAdaptor();

    public void setTreeAdaptor(TreeAdaptor adaptor) {
        this.adaptor = adaptor;
    }
    public TreeAdaptor getTreeAdaptor() {
        return adaptor;
    }

    public String[] getTokenNames() { return pycasmParser.tokenNames; }
    public String getGrammarFileName() { return "G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g"; }


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
    	NoViableAltException nvae = (NoViableAltException)e;
    	debugMsg += "token:"+e.token+
             " (decision="+nvae.decisionNumber+
             " state "+nvae.stateNumber+")"+
             " decision=<<"+nvae.grammarDecisionDescription+">>\n";
        }
        else if ( e instanceof EarlyExitException ) {
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
        return t.toString()+"{"+tokenNames[t.getType()]+"}";
    }
    public String getErrorHeader(RecognitionException e) {
    	String h = super.getErrorHeader(e);
    	return "PARSER ERROR: " + h;
    }
    // Don't recover, report and exit.
    //@Override
    public void reportError(RecognitionException e) {
    	super.reportError(e);
    	throw new IllegalArgumentException();
    }
    // Throw error, don't recover.
    public void reportError(String message) {
    	throw new IllegalArgumentException(message);
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


    public static class root_return extends ParserRuleReturnScope {
        Object tree;
        public Object getTree() { return tree; }
    };

    // $ANTLR start "root"
    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:115:1: root : ( block | ( sp )+ )? EOF -> ^( ROOT ( block )? ) ;
    public final pycasmParser.root_return root() throws RecognitionException {
        pycasmParser.root_return retval = new pycasmParser.root_return();
        retval.start = input.LT(1);
        int root_StartIndex = input.index();
        Object root_0 = null;

        Token EOF3=null;
        pycasmParser.block_return block1 = null;

        pycasmParser.sp_return sp2 = null;


        Object EOF3_tree=null;
        RewriteRuleTokenStream stream_EOF=new RewriteRuleTokenStream(adaptor,"token EOF");
        RewriteRuleSubtreeStream stream_sp=new RewriteRuleSubtreeStream(adaptor,"rule sp");
        RewriteRuleSubtreeStream stream_block=new RewriteRuleSubtreeStream(adaptor,"rule block");
        try {
            if ( state.backtracking>0 && alreadyParsedRule(input, 1) ) { return retval; }
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:116:2: ( ( block | ( sp )+ )? EOF -> ^( ROOT ( block )? ) )
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:117:3: ( block | ( sp )+ )? EOF
            {
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:117:3: ( block | ( sp )+ )?
            int alt2=3;
            int LA2_0 = input.LA(1);

            if ( (LA2_0==INDENT||(LA2_0>=HEX_PAIR && LA2_0<=HEX_QUAD)||(LA2_0>=TYPED_VALUE && LA2_0<=STRING)||(LA2_0>=DOT_NAME && LA2_0<=NAME)) ) {
                alt2=1;
            }
            else if ( ((LA2_0>=NEWLINE && LA2_0<=WS)) ) {
                alt2=2;
            }
            switch (alt2) {
                case 1 :
                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:117:4: block
                    {
                    pushFollow(FOLLOW_block_in_root73);
                    block1=block();

                    state._fsp--;
                    if (state.failed) return retval;
                    if ( state.backtracking==0 ) stream_block.add(block1.getTree());

                    }
                    break;
                case 2 :
                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:117:11: ( sp )+
                    {
                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:117:11: ( sp )+
                    int cnt1=0;
                    loop1:
                    do {
                        int alt1=2;
                        int LA1_0 = input.LA(1);

                        if ( ((LA1_0>=NEWLINE && LA1_0<=WS)) ) {
                            alt1=1;
                        }


                        switch (alt1) {
                    	case 1 :
                    	    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:0:0: sp
                    	    {
                    	    pushFollow(FOLLOW_sp_in_root76);
                    	    sp2=sp();

                    	    state._fsp--;
                    	    if (state.failed) return retval;
                    	    if ( state.backtracking==0 ) stream_sp.add(sp2.getTree());

                    	    }
                    	    break;

                    	default :
                    	    if ( cnt1 >= 1 ) break loop1;
                    	    if (state.backtracking>0) {state.failed=true; return retval;}
                                EarlyExitException eee =
                                    new EarlyExitException(1, input);
                                throw eee;
                        }
                        cnt1++;
                    } while (true);


                    }
                    break;

            }

            EOF3=(Token)match(input,EOF,FOLLOW_EOF_in_root81); if (state.failed) return retval; 
            if ( state.backtracking==0 ) stream_EOF.add(EOF3);



            // AST REWRITE
            // elements: block
            // token labels: 
            // rule labels: retval
            // token list labels: 
            // rule list labels: 
            // wildcard labels: 
            if ( state.backtracking==0 ) {
            retval.tree = root_0;
            RewriteRuleSubtreeStream stream_retval=new RewriteRuleSubtreeStream(adaptor,"rule retval",retval!=null?retval.tree:null);

            root_0 = (Object)adaptor.nil();
            // 118:3: -> ^( ROOT ( block )? )
            {
                // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:118:6: ^( ROOT ( block )? )
                {
                Object root_1 = (Object)adaptor.nil();
                root_1 = (Object)adaptor.becomeRoot((Object)adaptor.create(ROOT, "ROOT"), root_1);

                // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:118:13: ( block )?
                if ( stream_block.hasNext() ) {
                    adaptor.addChild(root_1, stream_block.nextTree());

                }
                stream_block.reset();

                adaptor.addChild(root_0, root_1);
                }

            }

            retval.tree = root_0;}
            }

            retval.stop = input.LT(-1);

            if ( state.backtracking==0 ) {

            retval.tree = (Object)adaptor.rulePostProcessing(root_0);
            adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop);
            }
        }

        catch (RecognitionException re) {
            reportError(re);
            recover(input,re);
        }
        finally {
            if ( state.backtracking>0 ) { memoize(input, 1, root_StartIndex); }
        }
        return retval;
    }
    // $ANTLR end "root"

    public static class sp_return extends ParserRuleReturnScope {
        Object tree;
        public Object getTree() { return tree; }
    };

    // $ANTLR start "sp"
    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:121:1: sp : ( WS | NEWLINE )+ ->;
    public final pycasmParser.sp_return sp() throws RecognitionException {
        pycasmParser.sp_return retval = new pycasmParser.sp_return();
        retval.start = input.LT(1);
        int sp_StartIndex = input.index();
        Object root_0 = null;

        Token WS4=null;
        Token NEWLINE5=null;

        Object WS4_tree=null;
        Object NEWLINE5_tree=null;
        RewriteRuleTokenStream stream_WS=new RewriteRuleTokenStream(adaptor,"token WS");
        RewriteRuleTokenStream stream_NEWLINE=new RewriteRuleTokenStream(adaptor,"token NEWLINE");

        try {
            if ( state.backtracking>0 && alreadyParsedRule(input, 2) ) { return retval; }
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:121:4: ( ( WS | NEWLINE )+ ->)
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:122:3: ( WS | NEWLINE )+
            {
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:122:3: ( WS | NEWLINE )+
            int cnt3=0;
            loop3:
            do {
                int alt3=3;
                int LA3_0 = input.LA(1);

                if ( (LA3_0==WS) ) {
                    int LA3_2 = input.LA(2);

                    if ( (synpred4_pycasmParser()) ) {
                        alt3=1;
                    }


                }
                else if ( (LA3_0==NEWLINE) ) {
                    int LA3_3 = input.LA(2);

                    if ( (synpred5_pycasmParser()) ) {
                        alt3=2;
                    }


                }


                switch (alt3) {
            	case 1 :
            	    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:122:4: WS
            	    {
            	    WS4=(Token)match(input,WS,FOLLOW_WS_in_sp105); if (state.failed) return retval; 
            	    if ( state.backtracking==0 ) stream_WS.add(WS4);


            	    }
            	    break;
            	case 2 :
            	    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:122:7: NEWLINE
            	    {
            	    NEWLINE5=(Token)match(input,NEWLINE,FOLLOW_NEWLINE_in_sp107); if (state.failed) return retval; 
            	    if ( state.backtracking==0 ) stream_NEWLINE.add(NEWLINE5);


            	    }
            	    break;

            	default :
            	    if ( cnt3 >= 1 ) break loop3;
            	    if (state.backtracking>0) {state.failed=true; return retval;}
                        EarlyExitException eee =
                            new EarlyExitException(3, input);
                        throw eee;
                }
                cnt3++;
            } while (true);



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

            root_0 = (Object)adaptor.nil();
            // 122:17: ->
            {
                root_0 = null;
            }

            retval.tree = root_0;}
            }

            retval.stop = input.LT(-1);

            if ( state.backtracking==0 ) {

            retval.tree = (Object)adaptor.rulePostProcessing(root_0);
            adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop);
            }
        }

        catch (RecognitionException re) {
            reportError(re);
            recover(input,re);
        }
        finally {
            if ( state.backtracking>0 ) { memoize(input, 2, sp_StartIndex); }
        }
        return retval;
    }
    // $ANTLR end "sp"

    public static class block_return extends ParserRuleReturnScope {
        Object tree;
        public Object getTree() { return tree; }
    };

    // $ANTLR start "block"
    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:125:1: block : ( element_chain -> ^( BLOCK element_chain ) | ( spaced_element )+ ( element_chain )? -> ^( BLOCK ( spaced_element )+ ( element_chain )? ) ) ( ( ( spaced_element )+ | ( sp )+ ) ( element_chain )? -> ^( $block ( spaced_element )+ ( element_chain )? ) )* ;
    public final pycasmParser.block_return block() throws RecognitionException {
        pycasmParser.block_return retval = new pycasmParser.block_return();
        retval.start = input.LT(1);
        int block_StartIndex = input.index();
        Object root_0 = null;

        pycasmParser.element_chain_return element_chain6 = null;

        pycasmParser.spaced_element_return spaced_element7 = null;

        pycasmParser.element_chain_return element_chain8 = null;

        pycasmParser.spaced_element_return spaced_element9 = null;

        pycasmParser.sp_return sp10 = null;

        pycasmParser.element_chain_return element_chain11 = null;


        RewriteRuleSubtreeStream stream_sp=new RewriteRuleSubtreeStream(adaptor,"rule sp");
        RewriteRuleSubtreeStream stream_element_chain=new RewriteRuleSubtreeStream(adaptor,"rule element_chain");
        RewriteRuleSubtreeStream stream_spaced_element=new RewriteRuleSubtreeStream(adaptor,"rule spaced_element");
        try {
            if ( state.backtracking>0 && alreadyParsedRule(input, 3) ) { return retval; }
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:126:2: ( ( element_chain -> ^( BLOCK element_chain ) | ( spaced_element )+ ( element_chain )? -> ^( BLOCK ( spaced_element )+ ( element_chain )? ) ) ( ( ( spaced_element )+ | ( sp )+ ) ( element_chain )? -> ^( $block ( spaced_element )+ ( element_chain )? ) )* )
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:127:3: ( element_chain -> ^( BLOCK element_chain ) | ( spaced_element )+ ( element_chain )? -> ^( BLOCK ( spaced_element )+ ( element_chain )? ) ) ( ( ( spaced_element )+ | ( sp )+ ) ( element_chain )? -> ^( $block ( spaced_element )+ ( element_chain )? ) )*
            {
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:127:3: ( element_chain -> ^( BLOCK element_chain ) | ( spaced_element )+ ( element_chain )? -> ^( BLOCK ( spaced_element )+ ( element_chain )? ) )
            int alt6=2;
            int LA6_0 = input.LA(1);

            if ( ((LA6_0>=HEX_PAIR && LA6_0<=HEX_QUAD)||(LA6_0>=TYPED_VALUE && LA6_0<=STRING)||LA6_0==NAME) ) {
                alt6=1;
            }
            else if ( (LA6_0==DOT_NAME) && (( input.LT(1).getCharPositionInLine() == 0 || input.LT(-1).getType() == NEWLINE ))) {
                alt6=2;
            }
            else if ( (LA6_0==INDENT) ) {
                alt6=2;
            }
            else {
                if (state.backtracking>0) {state.failed=true; return retval;}
                NoViableAltException nvae =
                    new NoViableAltException("", 6, 0, input);

                throw nvae;
            }
            switch (alt6) {
                case 1 :
                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:128:3: element_chain
                    {
                    pushFollow(FOLLOW_element_chain_in_block128);
                    element_chain6=element_chain();

                    state._fsp--;
                    if (state.failed) return retval;
                    if ( state.backtracking==0 ) stream_element_chain.add(element_chain6.getTree());


                    // AST REWRITE
                    // elements: element_chain
                    // token labels: 
                    // rule labels: retval
                    // token list labels: 
                    // rule list labels: 
                    // wildcard labels: 
                    if ( state.backtracking==0 ) {
                    retval.tree = root_0;
                    RewriteRuleSubtreeStream stream_retval=new RewriteRuleSubtreeStream(adaptor,"rule retval",retval!=null?retval.tree:null);

                    root_0 = (Object)adaptor.nil();
                    // 128:17: -> ^( BLOCK element_chain )
                    {
                        // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:128:20: ^( BLOCK element_chain )
                        {
                        Object root_1 = (Object)adaptor.nil();
                        root_1 = (Object)adaptor.becomeRoot((Object)adaptor.create(BLOCK, "BLOCK"), root_1);

                        adaptor.addChild(root_1, stream_element_chain.nextTree());

                        adaptor.addChild(root_0, root_1);
                        }

                    }

                    retval.tree = root_0;}
                    }
                    break;
                case 2 :
                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:129:5: ( spaced_element )+ ( element_chain )?
                    {
                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:129:5: ( spaced_element )+
                    int cnt4=0;
                    loop4:
                    do {
                        int alt4=2;
                        alt4 = dfa4.predict(input);
                        switch (alt4) {
                    	case 1 :
                    	    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:0:0: spaced_element
                    	    {
                    	    pushFollow(FOLLOW_spaced_element_in_block142);
                    	    spaced_element7=spaced_element();

                    	    state._fsp--;
                    	    if (state.failed) return retval;
                    	    if ( state.backtracking==0 ) stream_spaced_element.add(spaced_element7.getTree());

                    	    }
                    	    break;

                    	default :
                    	    if ( cnt4 >= 1 ) break loop4;
                    	    if (state.backtracking>0) {state.failed=true; return retval;}
                                EarlyExitException eee =
                                    new EarlyExitException(4, input);
                                throw eee;
                        }
                        cnt4++;
                    } while (true);

                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:129:21: ( element_chain )?
                    int alt5=2;
                    alt5 = dfa5.predict(input);
                    switch (alt5) {
                        case 1 :
                            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:0:0: element_chain
                            {
                            pushFollow(FOLLOW_element_chain_in_block145);
                            element_chain8=element_chain();

                            state._fsp--;
                            if (state.failed) return retval;
                            if ( state.backtracking==0 ) stream_element_chain.add(element_chain8.getTree());

                            }
                            break;

                    }



                    // AST REWRITE
                    // elements: element_chain, spaced_element
                    // token labels: 
                    // rule labels: retval
                    // token list labels: 
                    // rule list labels: 
                    // wildcard labels: 
                    if ( state.backtracking==0 ) {
                    retval.tree = root_0;
                    RewriteRuleSubtreeStream stream_retval=new RewriteRuleSubtreeStream(adaptor,"rule retval",retval!=null?retval.tree:null);

                    root_0 = (Object)adaptor.nil();
                    // 129:36: -> ^( BLOCK ( spaced_element )+ ( element_chain )? )
                    {
                        // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:129:39: ^( BLOCK ( spaced_element )+ ( element_chain )? )
                        {
                        Object root_1 = (Object)adaptor.nil();
                        root_1 = (Object)adaptor.becomeRoot((Object)adaptor.create(BLOCK, "BLOCK"), root_1);

                        if ( !(stream_spaced_element.hasNext()) ) {
                            throw new RewriteEarlyExitException();
                        }
                        while ( stream_spaced_element.hasNext() ) {
                            adaptor.addChild(root_1, stream_spaced_element.nextTree());

                        }
                        stream_spaced_element.reset();
                        // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:129:63: ( element_chain )?
                        if ( stream_element_chain.hasNext() ) {
                            adaptor.addChild(root_1, stream_element_chain.nextTree());

                        }
                        stream_element_chain.reset();

                        adaptor.addChild(root_0, root_1);
                        }

                    }

                    retval.tree = root_0;}
                    }
                    break;

            }

            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:131:3: ( ( ( spaced_element )+ | ( sp )+ ) ( element_chain )? -> ^( $block ( spaced_element )+ ( element_chain )? ) )*
            loop11:
            do {
                int alt11=2;
                int LA11_0 = input.LA(1);

                if ( (LA11_0==NEWLINE) ) {
                    int LA11_2 = input.LA(2);

                    if ( (synpred13_pycasmParser()) ) {
                        alt11=1;
                    }


                }
                else if ( (LA11_0==DOT_NAME) && (( input.LT(1).getCharPositionInLine() == 0 || input.LT(-1).getType() == NEWLINE ))) {
                    int LA11_3 = input.LA(2);

                    if ( ((synpred13_pycasmParser()&&( input.LT(1).getCharPositionInLine() == 0 || input.LT(-1).getType() == NEWLINE ))) ) {
                        alt11=1;
                    }


                }
                else if ( (LA11_0==INDENT) ) {
                    int LA11_4 = input.LA(2);

                    if ( (synpred13_pycasmParser()) ) {
                        alt11=1;
                    }


                }
                else if ( (LA11_0==WS) ) {
                    int LA11_5 = input.LA(2);

                    if ( (synpred13_pycasmParser()) ) {
                        alt11=1;
                    }


                }


                switch (alt11) {
            	case 1 :
            	    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:131:4: ( ( spaced_element )+ | ( sp )+ ) ( element_chain )?
            	    {
            	    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:131:4: ( ( spaced_element )+ | ( sp )+ )
            	    int alt9=2;
            	    int LA9_0 = input.LA(1);

            	    if ( (LA9_0==DOT_NAME) && (( input.LT(1).getCharPositionInLine() == 0 || input.LT(-1).getType() == NEWLINE ))) {
            	        alt9=1;
            	    }
            	    else if ( (LA9_0==INDENT) ) {
            	        alt9=1;
            	    }
            	    else if ( ((LA9_0>=NEWLINE && LA9_0<=WS)) ) {
            	        alt9=2;
            	    }
            	    else {
            	        if (state.backtracking>0) {state.failed=true; return retval;}
            	        NoViableAltException nvae =
            	            new NoViableAltException("", 9, 0, input);

            	        throw nvae;
            	    }
            	    switch (alt9) {
            	        case 1 :
            	            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:131:5: ( spaced_element )+
            	            {
            	            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:131:5: ( spaced_element )+
            	            int cnt7=0;
            	            loop7:
            	            do {
            	                int alt7=2;
            	                int LA7_0 = input.LA(1);

            	                if ( (LA7_0==DOT_NAME) && (( input.LT(1).getCharPositionInLine() == 0 || input.LT(-1).getType() == NEWLINE ))) {
            	                    int LA7_2 = input.LA(2);

            	                    if ( ((synpred9_pycasmParser()&&( input.LT(1).getCharPositionInLine() == 0 || input.LT(-1).getType() == NEWLINE ))) ) {
            	                        alt7=1;
            	                    }


            	                }
            	                else if ( (LA7_0==INDENT) ) {
            	                    int LA7_3 = input.LA(2);

            	                    if ( (synpred9_pycasmParser()) ) {
            	                        alt7=1;
            	                    }


            	                }


            	                switch (alt7) {
            	            	case 1 :
            	            	    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:0:0: spaced_element
            	            	    {
            	            	    pushFollow(FOLLOW_spaced_element_in_block168);
            	            	    spaced_element9=spaced_element();

            	            	    state._fsp--;
            	            	    if (state.failed) return retval;
            	            	    if ( state.backtracking==0 ) stream_spaced_element.add(spaced_element9.getTree());

            	            	    }
            	            	    break;

            	            	default :
            	            	    if ( cnt7 >= 1 ) break loop7;
            	            	    if (state.backtracking>0) {state.failed=true; return retval;}
            	                        EarlyExitException eee =
            	                            new EarlyExitException(7, input);
            	                        throw eee;
            	                }
            	                cnt7++;
            	            } while (true);


            	            }
            	            break;
            	        case 2 :
            	            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:131:21: ( sp )+
            	            {
            	            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:131:21: ( sp )+
            	            int cnt8=0;
            	            loop8:
            	            do {
            	                int alt8=2;
            	                int LA8_0 = input.LA(1);

            	                if ( (LA8_0==NEWLINE) ) {
            	                    int LA8_2 = input.LA(2);

            	                    if ( (synpred11_pycasmParser()) ) {
            	                        alt8=1;
            	                    }


            	                }
            	                else if ( (LA8_0==WS) ) {
            	                    int LA8_5 = input.LA(2);

            	                    if ( (synpred11_pycasmParser()) ) {
            	                        alt8=1;
            	                    }


            	                }


            	                switch (alt8) {
            	            	case 1 :
            	            	    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:0:0: sp
            	            	    {
            	            	    pushFollow(FOLLOW_sp_in_block171);
            	            	    sp10=sp();

            	            	    state._fsp--;
            	            	    if (state.failed) return retval;
            	            	    if ( state.backtracking==0 ) stream_sp.add(sp10.getTree());

            	            	    }
            	            	    break;

            	            	default :
            	            	    if ( cnt8 >= 1 ) break loop8;
            	            	    if (state.backtracking>0) {state.failed=true; return retval;}
            	                        EarlyExitException eee =
            	                            new EarlyExitException(8, input);
            	                        throw eee;
            	                }
            	                cnt8++;
            	            } while (true);


            	            }
            	            break;

            	    }

            	    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:131:26: ( element_chain )?
            	    int alt10=2;
            	    alt10 = dfa10.predict(input);
            	    switch (alt10) {
            	        case 1 :
            	            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:0:0: element_chain
            	            {
            	            pushFollow(FOLLOW_element_chain_in_block175);
            	            element_chain11=element_chain();

            	            state._fsp--;
            	            if (state.failed) return retval;
            	            if ( state.backtracking==0 ) stream_element_chain.add(element_chain11.getTree());

            	            }
            	            break;

            	    }



            	    // AST REWRITE
            	    // elements: block, element_chain, spaced_element
            	    // token labels: 
            	    // rule labels: retval
            	    // token list labels: 
            	    // rule list labels: 
            	    // wildcard labels: 
            	    if ( state.backtracking==0 ) {
            	    retval.tree = root_0;
            	    RewriteRuleSubtreeStream stream_retval=new RewriteRuleSubtreeStream(adaptor,"rule retval",retval!=null?retval.tree:null);

            	    root_0 = (Object)adaptor.nil();
            	    // 131:41: -> ^( $block ( spaced_element )+ ( element_chain )? )
            	    {
            	        // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:131:44: ^( $block ( spaced_element )+ ( element_chain )? )
            	        {
            	        Object root_1 = (Object)adaptor.nil();
            	        root_1 = (Object)adaptor.becomeRoot(stream_retval.nextNode(), root_1);

            	        if ( !(stream_spaced_element.hasNext()) ) {
            	            throw new RewriteEarlyExitException();
            	        }
            	        while ( stream_spaced_element.hasNext() ) {
            	            adaptor.addChild(root_1, stream_spaced_element.nextTree());

            	        }
            	        stream_spaced_element.reset();
            	        // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:131:69: ( element_chain )?
            	        if ( stream_element_chain.hasNext() ) {
            	            adaptor.addChild(root_1, stream_element_chain.nextTree());

            	        }
            	        stream_element_chain.reset();

            	        adaptor.addChild(root_0, root_1);
            	        }

            	    }

            	    retval.tree = root_0;}
            	    }
            	    break;

            	default :
            	    break loop11;
                }
            } while (true);


            }

            retval.stop = input.LT(-1);

            if ( state.backtracking==0 ) {

            retval.tree = (Object)adaptor.rulePostProcessing(root_0);
            adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop);
            }
        }

        catch (RecognitionException re) {
            reportError(re);
            recover(input,re);
        }
        finally {
            if ( state.backtracking>0 ) { memoize(input, 3, block_StartIndex); }
        }
        return retval;
    }
    // $ANTLR end "block"

    public static class element_chain_return extends ParserRuleReturnScope {
        Object tree;
        public Object getTree() { return tree; }
    };

    // $ANTLR start "element_chain"
    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:135:1: element_chain : chain_element ( ( sp )+ chain_element )* ;
    public final pycasmParser.element_chain_return element_chain() throws RecognitionException {
        pycasmParser.element_chain_return retval = new pycasmParser.element_chain_return();
        retval.start = input.LT(1);
        int element_chain_StartIndex = input.index();
        Object root_0 = null;

        pycasmParser.chain_element_return chain_element12 = null;

        pycasmParser.sp_return sp13 = null;

        pycasmParser.chain_element_return chain_element14 = null;



        try {
            if ( state.backtracking>0 && alreadyParsedRule(input, 4) ) { return retval; }
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:136:2: ( chain_element ( ( sp )+ chain_element )* )
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:137:3: chain_element ( ( sp )+ chain_element )*
            {
            root_0 = (Object)adaptor.nil();

            pushFollow(FOLLOW_chain_element_in_element_chain205);
            chain_element12=chain_element();

            state._fsp--;
            if (state.failed) return retval;
            if ( state.backtracking==0 ) adaptor.addChild(root_0, chain_element12.getTree());
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:137:17: ( ( sp )+ chain_element )*
            loop13:
            do {
                int alt13=2;
                alt13 = dfa13.predict(input);
                switch (alt13) {
            	case 1 :
            	    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:137:18: ( sp )+ chain_element
            	    {
            	    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:137:18: ( sp )+
            	    int cnt12=0;
            	    loop12:
            	    do {
            	        int alt12=2;
            	        int LA12_0 = input.LA(1);

            	        if ( ((LA12_0>=NEWLINE && LA12_0<=WS)) ) {
            	            alt12=1;
            	        }


            	        switch (alt12) {
            	    	case 1 :
            	    	    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:0:0: sp
            	    	    {
            	    	    pushFollow(FOLLOW_sp_in_element_chain208);
            	    	    sp13=sp();

            	    	    state._fsp--;
            	    	    if (state.failed) return retval;
            	    	    if ( state.backtracking==0 ) adaptor.addChild(root_0, sp13.getTree());

            	    	    }
            	    	    break;

            	    	default :
            	    	    if ( cnt12 >= 1 ) break loop12;
            	    	    if (state.backtracking>0) {state.failed=true; return retval;}
            	                EarlyExitException eee =
            	                    new EarlyExitException(12, input);
            	                throw eee;
            	        }
            	        cnt12++;
            	    } while (true);

            	    pushFollow(FOLLOW_chain_element_in_element_chain211);
            	    chain_element14=chain_element();

            	    state._fsp--;
            	    if (state.failed) return retval;
            	    if ( state.backtracking==0 ) adaptor.addChild(root_0, chain_element14.getTree());

            	    }
            	    break;

            	default :
            	    break loop13;
                }
            } while (true);


            }

            retval.stop = input.LT(-1);

            if ( state.backtracking==0 ) {

            retval.tree = (Object)adaptor.rulePostProcessing(root_0);
            adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop);
            }
        }

        catch (RecognitionException re) {
            reportError(re);
            recover(input,re);
        }
        finally {
            if ( state.backtracking>0 ) { memoize(input, 4, element_chain_StartIndex); }
        }
        return retval;
    }
    // $ANTLR end "element_chain"

    public static class chain_element_return extends ParserRuleReturnScope {
        Object tree;
        public Object getTree() { return tree; }
    };

    // $ANTLR start "chain_element"
    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:140:1: chain_element : ( sym_name | generative | hex_code );
    public final pycasmParser.chain_element_return chain_element() throws RecognitionException {
        pycasmParser.chain_element_return retval = new pycasmParser.chain_element_return();
        retval.start = input.LT(1);
        int chain_element_StartIndex = input.index();
        Object root_0 = null;

        pycasmParser.sym_name_return sym_name15 = null;

        pycasmParser.generative_return generative16 = null;

        pycasmParser.hex_code_return hex_code17 = null;



        try {
            if ( state.backtracking>0 && alreadyParsedRule(input, 5) ) { return retval; }
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:140:14: ( sym_name | generative | hex_code )
            int alt14=3;
            switch ( input.LA(1) ) {
            case NAME:
                {
                alt14=1;
                }
                break;
            case TYPED_VALUE:
            case STRING:
                {
                alt14=2;
                }
                break;
            case HEX_PAIR:
            case HEX_DQUAD:
            case HEX_EIGHT:
            case HEX_QUAD:
                {
                alt14=3;
                }
                break;
            default:
                if (state.backtracking>0) {state.failed=true; return retval;}
                NoViableAltException nvae =
                    new NoViableAltException("", 14, 0, input);

                throw nvae;
            }

            switch (alt14) {
                case 1 :
                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:141:3: sym_name
                    {
                    root_0 = (Object)adaptor.nil();

                    pushFollow(FOLLOW_sym_name_in_chain_element224);
                    sym_name15=sym_name();

                    state._fsp--;
                    if (state.failed) return retval;
                    if ( state.backtracking==0 ) adaptor.addChild(root_0, sym_name15.getTree());

                    }
                    break;
                case 2 :
                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:142:4: generative
                    {
                    root_0 = (Object)adaptor.nil();

                    pushFollow(FOLLOW_generative_in_chain_element229);
                    generative16=generative();

                    state._fsp--;
                    if (state.failed) return retval;
                    if ( state.backtracking==0 ) adaptor.addChild(root_0, generative16.getTree());

                    }
                    break;
                case 3 :
                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:143:4: hex_code
                    {
                    root_0 = (Object)adaptor.nil();

                    pushFollow(FOLLOW_hex_code_in_chain_element234);
                    hex_code17=hex_code();

                    state._fsp--;
                    if (state.failed) return retval;
                    if ( state.backtracking==0 ) adaptor.addChild(root_0, hex_code17.getTree());

                    }
                    break;

            }
            retval.stop = input.LT(-1);

            if ( state.backtracking==0 ) {

            retval.tree = (Object)adaptor.rulePostProcessing(root_0);
            adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop);
            }
        }

        catch (RecognitionException re) {
            reportError(re);
            recover(input,re);
        }
        finally {
            if ( state.backtracking>0 ) { memoize(input, 5, chain_element_StartIndex); }
        }
        return retval;
    }
    // $ANTLR end "chain_element"

    public static class spaced_element_return extends ParserRuleReturnScope {
        Object tree;
        public Object getTree() { return tree; }
    };

    // $ANTLR start "spaced_element"
    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:146:1: spaced_element : ( directive | INDENT block ( NEWLINE )? ( DEDENT )? );
    public final pycasmParser.spaced_element_return spaced_element() throws RecognitionException {
        pycasmParser.spaced_element_return retval = new pycasmParser.spaced_element_return();
        retval.start = input.LT(1);
        int spaced_element_StartIndex = input.index();
        Object root_0 = null;

        Token INDENT19=null;
        Token NEWLINE21=null;
        Token DEDENT22=null;
        pycasmParser.directive_return directive18 = null;

        pycasmParser.block_return block20 = null;


        Object INDENT19_tree=null;
        Object NEWLINE21_tree=null;
        Object DEDENT22_tree=null;

        try {
            if ( state.backtracking>0 && alreadyParsedRule(input, 6) ) { return retval; }
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:147:2: ( directive | INDENT block ( NEWLINE )? ( DEDENT )? )
            int alt17=2;
            int LA17_0 = input.LA(1);

            if ( (LA17_0==DOT_NAME) && (( input.LT(1).getCharPositionInLine() == 0 || input.LT(-1).getType() == NEWLINE ))) {
                alt17=1;
            }
            else if ( (LA17_0==INDENT) ) {
                alt17=2;
            }
            else {
                if (state.backtracking>0) {state.failed=true; return retval;}
                NoViableAltException nvae =
                    new NoViableAltException("", 17, 0, input);

                throw nvae;
            }
            switch (alt17) {
                case 1 :
                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:148:3: directive
                    {
                    root_0 = (Object)adaptor.nil();

                    pushFollow(FOLLOW_directive_in_spaced_element247);
                    directive18=directive();

                    state._fsp--;
                    if (state.failed) return retval;
                    if ( state.backtracking==0 ) adaptor.addChild(root_0, directive18.getTree());

                    }
                    break;
                case 2 :
                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:149:4: INDENT block ( NEWLINE )? ( DEDENT )?
                    {
                    root_0 = (Object)adaptor.nil();

                    INDENT19=(Token)match(input,INDENT,FOLLOW_INDENT_in_spaced_element252); if (state.failed) return retval;
                    pushFollow(FOLLOW_block_in_spaced_element255);
                    block20=block();

                    state._fsp--;
                    if (state.failed) return retval;
                    if ( state.backtracking==0 ) adaptor.addChild(root_0, block20.getTree());
                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:149:18: ( NEWLINE )?
                    int alt15=2;
                    int LA15_0 = input.LA(1);

                    if ( (LA15_0==NEWLINE) ) {
                        int LA15_1 = input.LA(2);

                        if ( (synpred19_pycasmParser()) ) {
                            alt15=1;
                        }
                    }
                    switch (alt15) {
                        case 1 :
                            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:0:0: NEWLINE
                            {
                            NEWLINE21=(Token)match(input,NEWLINE,FOLLOW_NEWLINE_in_spaced_element257); if (state.failed) return retval;
                            if ( state.backtracking==0 ) {
                            NEWLINE21_tree = (Object)adaptor.create(NEWLINE21);
                            adaptor.addChild(root_0, NEWLINE21_tree);
                            }

                            }
                            break;

                    }

                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:149:33: ( DEDENT )?
                    int alt16=2;
                    int LA16_0 = input.LA(1);

                    if ( (LA16_0==DEDENT) ) {
                        int LA16_1 = input.LA(2);

                        if ( (synpred20_pycasmParser()) ) {
                            alt16=1;
                        }
                    }
                    switch (alt16) {
                        case 1 :
                            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:0:0: DEDENT
                            {
                            DEDENT22=(Token)match(input,DEDENT,FOLLOW_DEDENT_in_spaced_element260); if (state.failed) return retval;

                            }
                            break;

                    }


                    }
                    break;

            }
            retval.stop = input.LT(-1);

            if ( state.backtracking==0 ) {

            retval.tree = (Object)adaptor.rulePostProcessing(root_0);
            adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop);
            }
        }

        catch (RecognitionException re) {
            reportError(re);
            recover(input,re);
        }
        finally {
            if ( state.backtracking>0 ) { memoize(input, 6, spaced_element_StartIndex); }
        }
        return retval;
    }
    // $ANTLR end "spaced_element"

    public static class directive_return extends ParserRuleReturnScope {
        Object tree;
        public Object getTree() { return tree; }
    };

    // $ANTLR start "directive"
    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:152:1: directive : {...}? => ( directive_header ( INDENT block ( NEWLINE )? DEDENT ( DOT_END ( WS )+ ( NAME ) )? )? ) -> ^( ( block )? ) ;
    public final pycasmParser.directive_return directive() throws RecognitionException {
        pycasmParser.directive_return retval = new pycasmParser.directive_return();
        retval.start = input.LT(1);
        int directive_StartIndex = input.index();
        Object root_0 = null;

        Token INDENT24=null;
        Token NEWLINE26=null;
        Token DEDENT27=null;
        Token DOT_END28=null;
        Token WS29=null;
        Token NAME30=null;
        pycasmParser.directive_header_return directive_header23 = null;

        pycasmParser.block_return block25 = null;


        Object INDENT24_tree=null;
        Object NEWLINE26_tree=null;
        Object DEDENT27_tree=null;
        Object DOT_END28_tree=null;
        Object WS29_tree=null;
        Object NAME30_tree=null;
        RewriteRuleTokenStream stream_NAME=new RewriteRuleTokenStream(adaptor,"token NAME");
        RewriteRuleTokenStream stream_DEDENT=new RewriteRuleTokenStream(adaptor,"token DEDENT");
        RewriteRuleTokenStream stream_WS=new RewriteRuleTokenStream(adaptor,"token WS");
        RewriteRuleTokenStream stream_NEWLINE=new RewriteRuleTokenStream(adaptor,"token NEWLINE");
        RewriteRuleTokenStream stream_DOT_END=new RewriteRuleTokenStream(adaptor,"token DOT_END");
        RewriteRuleTokenStream stream_INDENT=new RewriteRuleTokenStream(adaptor,"token INDENT");
        RewriteRuleSubtreeStream stream_directive_header=new RewriteRuleSubtreeStream(adaptor,"rule directive_header");
        RewriteRuleSubtreeStream stream_block=new RewriteRuleSubtreeStream(adaptor,"rule block");
        try {
            if ( state.backtracking>0 && alreadyParsedRule(input, 7) ) { return retval; }
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:153:2: ({...}? => ( directive_header ( INDENT block ( NEWLINE )? DEDENT ( DOT_END ( WS )+ ( NAME ) )? )? ) -> ^( ( block )? ) )
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:154:3: {...}? => ( directive_header ( INDENT block ( NEWLINE )? DEDENT ( DOT_END ( WS )+ ( NAME ) )? )? )
            {
            if ( !(( input.LT(1).getCharPositionInLine() == 0 || input.LT(-1).getType() == NEWLINE )) ) {
                if (state.backtracking>0) {state.failed=true; return retval;}
                throw new FailedPredicateException(input, "directive", " input.LT(1).getCharPositionInLine() == 0 || input.LT(-1).getType() == NEWLINE ");
            }
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:154:89: ( directive_header ( INDENT block ( NEWLINE )? DEDENT ( DOT_END ( WS )+ ( NAME ) )? )? )
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:154:90: directive_header ( INDENT block ( NEWLINE )? DEDENT ( DOT_END ( WS )+ ( NAME ) )? )?
            {
            pushFollow(FOLLOW_directive_header_in_directive280);
            directive_header23=directive_header();

            state._fsp--;
            if (state.failed) return retval;
            if ( state.backtracking==0 ) stream_directive_header.add(directive_header23.getTree());
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:155:4: ( INDENT block ( NEWLINE )? DEDENT ( DOT_END ( WS )+ ( NAME ) )? )?
            int alt21=2;
            alt21 = dfa21.predict(input);
            switch (alt21) {
                case 1 :
                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:155:5: INDENT block ( NEWLINE )? DEDENT ( DOT_END ( WS )+ ( NAME ) )?
                    {
                    INDENT24=(Token)match(input,INDENT,FOLLOW_INDENT_in_directive286); if (state.failed) return retval; 
                    if ( state.backtracking==0 ) stream_INDENT.add(INDENT24);

                    pushFollow(FOLLOW_block_in_directive288);
                    block25=block();

                    state._fsp--;
                    if (state.failed) return retval;
                    if ( state.backtracking==0 ) stream_block.add(block25.getTree());
                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:155:18: ( NEWLINE )?
                    int alt18=2;
                    int LA18_0 = input.LA(1);

                    if ( (LA18_0==NEWLINE) ) {
                        alt18=1;
                    }
                    switch (alt18) {
                        case 1 :
                            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:0:0: NEWLINE
                            {
                            NEWLINE26=(Token)match(input,NEWLINE,FOLLOW_NEWLINE_in_directive290); if (state.failed) return retval; 
                            if ( state.backtracking==0 ) stream_NEWLINE.add(NEWLINE26);


                            }
                            break;

                    }

                    DEDENT27=(Token)match(input,DEDENT,FOLLOW_DEDENT_in_directive293); if (state.failed) return retval; 
                    if ( state.backtracking==0 ) stream_DEDENT.add(DEDENT27);

                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:156:5: ( DOT_END ( WS )+ ( NAME ) )?
                    int alt20=2;
                    int LA20_0 = input.LA(1);

                    if ( (LA20_0==DOT_END) ) {
                        alt20=1;
                    }
                    switch (alt20) {
                        case 1 :
                            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:156:6: DOT_END ( WS )+ ( NAME )
                            {
                            DOT_END28=(Token)match(input,DOT_END,FOLLOW_DOT_END_in_directive300); if (state.failed) return retval; 
                            if ( state.backtracking==0 ) stream_DOT_END.add(DOT_END28);

                            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:156:14: ( WS )+
                            int cnt19=0;
                            loop19:
                            do {
                                int alt19=2;
                                int LA19_0 = input.LA(1);

                                if ( (LA19_0==WS) ) {
                                    alt19=1;
                                }


                                switch (alt19) {
                            	case 1 :
                            	    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:0:0: WS
                            	    {
                            	    WS29=(Token)match(input,WS,FOLLOW_WS_in_directive302); if (state.failed) return retval; 
                            	    if ( state.backtracking==0 ) stream_WS.add(WS29);


                            	    }
                            	    break;

                            	default :
                            	    if ( cnt19 >= 1 ) break loop19;
                            	    if (state.backtracking>0) {state.failed=true; return retval;}
                                        EarlyExitException eee =
                                            new EarlyExitException(19, input);
                                        throw eee;
                                }
                                cnt19++;
                            } while (true);

                            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:157:6: ( NAME )
                            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:157:7: NAME
                            {
                            NAME30=(Token)match(input,NAME,FOLLOW_NAME_in_directive311); if (state.failed) return retval; 
                            if ( state.backtracking==0 ) stream_NAME.add(NAME30);

                            if ( state.backtracking==0 ) {

                              						String dh = (directive_header23!=null?((Object)directive_header23.tree):null).toString().substring(1);
                              						if (!dh.startsWith((NAME30!=null?NAME30.getText():null)))
                              							reportError(".end directive must have argument of the same name as directive '"+dh+"', compare with '"+(NAME30!=null?NAME30.getText():null)+"'.");
                              						
                            }

                            }


                            }
                            break;

                    }


                    }
                    break;

            }


            }



            // AST REWRITE
            // elements: block
            // token labels: 
            // rule labels: retval
            // token list labels: 
            // rule list labels: 
            // wildcard labels: 
            if ( state.backtracking==0 ) {
            retval.tree = root_0;
            RewriteRuleSubtreeStream stream_retval=new RewriteRuleSubtreeStream(adaptor,"rule retval",retval!=null?retval.tree:null);

            root_0 = (Object)adaptor.nil();
            // 166:6: -> ^( ( block )? )
            {
                // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:166:9: ^( ( block )? )
                {
                Object root_1 = (Object)adaptor.nil();
                root_1 = (Object)adaptor.becomeRoot((directive_header23!=null?((Object)directive_header23.tree):null), root_1);

                // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:166:36: ( block )?
                if ( stream_block.hasNext() ) {
                    adaptor.addChild(root_1, stream_block.nextTree());

                }
                stream_block.reset();

                adaptor.addChild(root_0, root_1);
                }

            }

            retval.tree = root_0;}
            }

            retval.stop = input.LT(-1);

            if ( state.backtracking==0 ) {

            retval.tree = (Object)adaptor.rulePostProcessing(root_0);
            adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop);
            }
        }

        catch (RecognitionException re) {
            reportError(re);
            recover(input,re);
        }
        finally {
            if ( state.backtracking>0 ) { memoize(input, 7, directive_StartIndex); }
        }
        return retval;
    }
    // $ANTLR end "directive"

    public static class directive_header_return extends ParserRuleReturnScope {
        Object tree;
        public Object getTree() { return tree; }
    };

    // $ANTLR start "directive_header"
    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:169:1: directive_header : DOT_NAME ( ( WS )+ directive_args )* ( WS )* ( NEWLINE | EOF ) -> ^( DOT_NAME ^( ARGS ( directive_args )* ) ) ;
    public final pycasmParser.directive_header_return directive_header() throws RecognitionException {
        pycasmParser.directive_header_return retval = new pycasmParser.directive_header_return();
        retval.start = input.LT(1);
        int directive_header_StartIndex = input.index();
        Object root_0 = null;

        Token DOT_NAME31=null;
        Token WS32=null;
        Token WS34=null;
        Token NEWLINE35=null;
        Token EOF36=null;
        pycasmParser.directive_args_return directive_args33 = null;


        Object DOT_NAME31_tree=null;
        Object WS32_tree=null;
        Object WS34_tree=null;
        Object NEWLINE35_tree=null;
        Object EOF36_tree=null;
        RewriteRuleTokenStream stream_WS=new RewriteRuleTokenStream(adaptor,"token WS");
        RewriteRuleTokenStream stream_DOT_NAME=new RewriteRuleTokenStream(adaptor,"token DOT_NAME");
        RewriteRuleTokenStream stream_NEWLINE=new RewriteRuleTokenStream(adaptor,"token NEWLINE");
        RewriteRuleTokenStream stream_EOF=new RewriteRuleTokenStream(adaptor,"token EOF");
        RewriteRuleSubtreeStream stream_directive_args=new RewriteRuleSubtreeStream(adaptor,"rule directive_args");
        try {
            if ( state.backtracking>0 && alreadyParsedRule(input, 8) ) { return retval; }
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:170:2: ( DOT_NAME ( ( WS )+ directive_args )* ( WS )* ( NEWLINE | EOF ) -> ^( DOT_NAME ^( ARGS ( directive_args )* ) ) )
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:171:3: DOT_NAME ( ( WS )+ directive_args )* ( WS )* ( NEWLINE | EOF )
            {
            DOT_NAME31=(Token)match(input,DOT_NAME,FOLLOW_DOT_NAME_in_directive_header367); if (state.failed) return retval; 
            if ( state.backtracking==0 ) stream_DOT_NAME.add(DOT_NAME31);

            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:171:12: ( ( WS )+ directive_args )*
            loop23:
            do {
                int alt23=2;
                alt23 = dfa23.predict(input);
                switch (alt23) {
            	case 1 :
            	    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:171:13: ( WS )+ directive_args
            	    {
            	    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:171:13: ( WS )+
            	    int cnt22=0;
            	    loop22:
            	    do {
            	        int alt22=2;
            	        int LA22_0 = input.LA(1);

            	        if ( (LA22_0==WS) ) {
            	            alt22=1;
            	        }


            	        switch (alt22) {
            	    	case 1 :
            	    	    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:0:0: WS
            	    	    {
            	    	    WS32=(Token)match(input,WS,FOLLOW_WS_in_directive_header370); if (state.failed) return retval; 
            	    	    if ( state.backtracking==0 ) stream_WS.add(WS32);


            	    	    }
            	    	    break;

            	    	default :
            	    	    if ( cnt22 >= 1 ) break loop22;
            	    	    if (state.backtracking>0) {state.failed=true; return retval;}
            	                EarlyExitException eee =
            	                    new EarlyExitException(22, input);
            	                throw eee;
            	        }
            	        cnt22++;
            	    } while (true);

            	    pushFollow(FOLLOW_directive_args_in_directive_header373);
            	    directive_args33=directive_args();

            	    state._fsp--;
            	    if (state.failed) return retval;
            	    if ( state.backtracking==0 ) stream_directive_args.add(directive_args33.getTree());

            	    }
            	    break;

            	default :
            	    break loop23;
                }
            } while (true);

            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:171:35: ( WS )*
            loop24:
            do {
                int alt24=2;
                int LA24_0 = input.LA(1);

                if ( (LA24_0==WS) ) {
                    alt24=1;
                }


                switch (alt24) {
            	case 1 :
            	    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:0:0: WS
            	    {
            	    WS34=(Token)match(input,WS,FOLLOW_WS_in_directive_header378); if (state.failed) return retval; 
            	    if ( state.backtracking==0 ) stream_WS.add(WS34);


            	    }
            	    break;

            	default :
            	    break loop24;
                }
            } while (true);

            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:171:39: ( NEWLINE | EOF )
            int alt25=2;
            int LA25_0 = input.LA(1);

            if ( (LA25_0==NEWLINE) ) {
                alt25=1;
            }
            else if ( (LA25_0==EOF) ) {
                alt25=2;
            }
            else {
                if (state.backtracking>0) {state.failed=true; return retval;}
                NoViableAltException nvae =
                    new NoViableAltException("", 25, 0, input);

                throw nvae;
            }
            switch (alt25) {
                case 1 :
                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:171:40: NEWLINE
                    {
                    NEWLINE35=(Token)match(input,NEWLINE,FOLLOW_NEWLINE_in_directive_header382); if (state.failed) return retval; 
                    if ( state.backtracking==0 ) stream_NEWLINE.add(NEWLINE35);


                    }
                    break;
                case 2 :
                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:171:48: EOF
                    {
                    EOF36=(Token)match(input,EOF,FOLLOW_EOF_in_directive_header384); if (state.failed) return retval; 
                    if ( state.backtracking==0 ) stream_EOF.add(EOF36);


                    }
                    break;

            }



            // AST REWRITE
            // elements: directive_args, DOT_NAME
            // token labels: 
            // rule labels: retval
            // token list labels: 
            // rule list labels: 
            // wildcard labels: 
            if ( state.backtracking==0 ) {
            retval.tree = root_0;
            RewriteRuleSubtreeStream stream_retval=new RewriteRuleSubtreeStream(adaptor,"rule retval",retval!=null?retval.tree:null);

            root_0 = (Object)adaptor.nil();
            // 171:53: -> ^( DOT_NAME ^( ARGS ( directive_args )* ) )
            {
                // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:171:56: ^( DOT_NAME ^( ARGS ( directive_args )* ) )
                {
                Object root_1 = (Object)adaptor.nil();
                root_1 = (Object)adaptor.becomeRoot(stream_DOT_NAME.nextNode(), root_1);

                // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:171:67: ^( ARGS ( directive_args )* )
                {
                Object root_2 = (Object)adaptor.nil();
                root_2 = (Object)adaptor.becomeRoot((Object)adaptor.create(ARGS, "ARGS"), root_2);

                // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:171:74: ( directive_args )*
                while ( stream_directive_args.hasNext() ) {
                    adaptor.addChild(root_2, stream_directive_args.nextTree());

                }
                stream_directive_args.reset();

                adaptor.addChild(root_1, root_2);
                }

                adaptor.addChild(root_0, root_1);
                }

            }

            retval.tree = root_0;}
            }

            retval.stop = input.LT(-1);

            if ( state.backtracking==0 ) {

            retval.tree = (Object)adaptor.rulePostProcessing(root_0);
            adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop);
            }
        }

        catch (RecognitionException re) {
            reportError(re);
            recover(input,re);
        }
        finally {
            if ( state.backtracking>0 ) { memoize(input, 8, directive_header_StartIndex); }
        }
        return retval;
    }
    // $ANTLR end "directive_header"

    public static class directive_args_return extends ParserRuleReturnScope {
        Object tree;
        public Object getTree() { return tree; }
    };

    // $ANTLR start "directive_args"
    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:174:1: directive_args : ( sym_name | hex_code | generative | HEX_DIGIT | NON_WS_SEQUENCE );
    public final pycasmParser.directive_args_return directive_args() throws RecognitionException {
        pycasmParser.directive_args_return retval = new pycasmParser.directive_args_return();
        retval.start = input.LT(1);
        int directive_args_StartIndex = input.index();
        Object root_0 = null;

        Token HEX_DIGIT40=null;
        Token NON_WS_SEQUENCE41=null;
        pycasmParser.sym_name_return sym_name37 = null;

        pycasmParser.hex_code_return hex_code38 = null;

        pycasmParser.generative_return generative39 = null;


        Object HEX_DIGIT40_tree=null;
        Object NON_WS_SEQUENCE41_tree=null;

        try {
            if ( state.backtracking>0 && alreadyParsedRule(input, 9) ) { return retval; }
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:175:2: ( sym_name | hex_code | generative | HEX_DIGIT | NON_WS_SEQUENCE )
            int alt26=5;
            switch ( input.LA(1) ) {
            case NAME:
                {
                alt26=1;
                }
                break;
            case HEX_PAIR:
            case HEX_DQUAD:
            case HEX_EIGHT:
            case HEX_QUAD:
                {
                alt26=2;
                }
                break;
            case TYPED_VALUE:
            case STRING:
                {
                alt26=3;
                }
                break;
            case HEX_DIGIT:
                {
                alt26=4;
                }
                break;
            case NON_WS_SEQUENCE:
                {
                alt26=5;
                }
                break;
            default:
                if (state.backtracking>0) {state.failed=true; return retval;}
                NoViableAltException nvae =
                    new NoViableAltException("", 26, 0, input);

                throw nvae;
            }

            switch (alt26) {
                case 1 :
                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:176:3: sym_name
                    {
                    root_0 = (Object)adaptor.nil();

                    pushFollow(FOLLOW_sym_name_in_directive_args411);
                    sym_name37=sym_name();

                    state._fsp--;
                    if (state.failed) return retval;
                    if ( state.backtracking==0 ) adaptor.addChild(root_0, sym_name37.getTree());

                    }
                    break;
                case 2 :
                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:177:4: hex_code
                    {
                    root_0 = (Object)adaptor.nil();

                    pushFollow(FOLLOW_hex_code_in_directive_args416);
                    hex_code38=hex_code();

                    state._fsp--;
                    if (state.failed) return retval;
                    if ( state.backtracking==0 ) adaptor.addChild(root_0, hex_code38.getTree());

                    }
                    break;
                case 3 :
                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:178:4: generative
                    {
                    root_0 = (Object)adaptor.nil();

                    pushFollow(FOLLOW_generative_in_directive_args421);
                    generative39=generative();

                    state._fsp--;
                    if (state.failed) return retval;
                    if ( state.backtracking==0 ) adaptor.addChild(root_0, generative39.getTree());

                    }
                    break;
                case 4 :
                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:179:4: HEX_DIGIT
                    {
                    root_0 = (Object)adaptor.nil();

                    HEX_DIGIT40=(Token)match(input,HEX_DIGIT,FOLLOW_HEX_DIGIT_in_directive_args426); if (state.failed) return retval;
                    if ( state.backtracking==0 ) {
                    HEX_DIGIT40_tree = (Object)adaptor.create(HEX_DIGIT40);
                    adaptor.addChild(root_0, HEX_DIGIT40_tree);
                    }

                    }
                    break;
                case 5 :
                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:180:4: NON_WS_SEQUENCE
                    {
                    root_0 = (Object)adaptor.nil();

                    NON_WS_SEQUENCE41=(Token)match(input,NON_WS_SEQUENCE,FOLLOW_NON_WS_SEQUENCE_in_directive_args431); if (state.failed) return retval;
                    if ( state.backtracking==0 ) {
                    NON_WS_SEQUENCE41_tree = (Object)adaptor.create(NON_WS_SEQUENCE41);
                    adaptor.addChild(root_0, NON_WS_SEQUENCE41_tree);
                    }

                    }
                    break;

            }
            retval.stop = input.LT(-1);

            if ( state.backtracking==0 ) {

            retval.tree = (Object)adaptor.rulePostProcessing(root_0);
            adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop);
            }
        }

        catch (RecognitionException re) {
            reportError(re);
            recover(input,re);
        }
        finally {
            if ( state.backtracking>0 ) { memoize(input, 9, directive_args_StartIndex); }
        }
        return retval;
    }
    // $ANTLR end "directive_args"

    public static class sym_name_return extends ParserRuleReturnScope {
        Object tree;
        public Object getTree() { return tree; }
    };

    // $ANTLR start "sym_name"
    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:183:1: sym_name : NAME -> ^( SYM NAME ) ;
    public final pycasmParser.sym_name_return sym_name() throws RecognitionException {
        pycasmParser.sym_name_return retval = new pycasmParser.sym_name_return();
        retval.start = input.LT(1);
        int sym_name_StartIndex = input.index();
        Object root_0 = null;

        Token NAME42=null;

        Object NAME42_tree=null;
        RewriteRuleTokenStream stream_NAME=new RewriteRuleTokenStream(adaptor,"token NAME");

        try {
            if ( state.backtracking>0 && alreadyParsedRule(input, 10) ) { return retval; }
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:184:2: ( NAME -> ^( SYM NAME ) )
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:185:3: NAME
            {
            NAME42=(Token)match(input,NAME,FOLLOW_NAME_in_sym_name445); if (state.failed) return retval; 
            if ( state.backtracking==0 ) stream_NAME.add(NAME42);



            // AST REWRITE
            // elements: NAME
            // token labels: 
            // rule labels: retval
            // token list labels: 
            // rule list labels: 
            // wildcard labels: 
            if ( state.backtracking==0 ) {
            retval.tree = root_0;
            RewriteRuleSubtreeStream stream_retval=new RewriteRuleSubtreeStream(adaptor,"rule retval",retval!=null?retval.tree:null);

            root_0 = (Object)adaptor.nil();
            // 185:8: -> ^( SYM NAME )
            {
                // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:185:11: ^( SYM NAME )
                {
                Object root_1 = (Object)adaptor.nil();
                root_1 = (Object)adaptor.becomeRoot((Object)adaptor.create(SYM, "SYM"), root_1);

                adaptor.addChild(root_1, stream_NAME.nextNode());

                adaptor.addChild(root_0, root_1);
                }

            }

            retval.tree = root_0;}
            }

            retval.stop = input.LT(-1);

            if ( state.backtracking==0 ) {

            retval.tree = (Object)adaptor.rulePostProcessing(root_0);
            adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop);
            }
        }

        catch (RecognitionException re) {
            reportError(re);
            recover(input,re);
        }
        finally {
            if ( state.backtracking>0 ) { memoize(input, 10, sym_name_StartIndex); }
        }
        return retval;
    }
    // $ANTLR end "sym_name"

    public static class generative_return extends ParserRuleReturnScope {
        Object tree;
        public Object getTree() { return tree; }
    };

    // $ANTLR start "generative"
    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:188:1: generative : (c= STRING | c= TYPED_VALUE ) -> ^() ;
    public final pycasmParser.generative_return generative() throws RecognitionException {
        pycasmParser.generative_return retval = new pycasmParser.generative_return();
        retval.start = input.LT(1);
        int generative_StartIndex = input.index();
        Object root_0 = null;

        Token c=null;

        Object c_tree=null;
        RewriteRuleTokenStream stream_TYPED_VALUE=new RewriteRuleTokenStream(adaptor,"token TYPED_VALUE");
        RewriteRuleTokenStream stream_STRING=new RewriteRuleTokenStream(adaptor,"token STRING");

        try {
            if ( state.backtracking>0 && alreadyParsedRule(input, 11) ) { return retval; }
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:189:2: ( (c= STRING | c= TYPED_VALUE ) -> ^() )
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:190:2: (c= STRING | c= TYPED_VALUE )
            {
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:190:2: (c= STRING | c= TYPED_VALUE )
            int alt27=2;
            int LA27_0 = input.LA(1);

            if ( (LA27_0==STRING) ) {
                alt27=1;
            }
            else if ( (LA27_0==TYPED_VALUE) ) {
                alt27=2;
            }
            else {
                if (state.backtracking>0) {state.failed=true; return retval;}
                NoViableAltException nvae =
                    new NoViableAltException("", 27, 0, input);

                throw nvae;
            }
            switch (alt27) {
                case 1 :
                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:191:3: c= STRING
                    {
                    c=(Token)match(input,STRING,FOLLOW_STRING_in_generative471); if (state.failed) return retval; 
                    if ( state.backtracking==0 ) stream_STRING.add(c);


                    }
                    break;
                case 2 :
                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:192:4: c= TYPED_VALUE
                    {
                    c=(Token)match(input,TYPED_VALUE,FOLLOW_TYPED_VALUE_in_generative478); if (state.failed) return retval; 
                    if ( state.backtracking==0 ) stream_TYPED_VALUE.add(c);


                    }
                    break;

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

            root_0 = (Object)adaptor.nil();
            // 193:4: -> ^()
            {
                // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:193:7: ^()
                {
                Object root_1 = (Object)adaptor.nil();
                root_1 = (Object)adaptor.becomeRoot(adaptor.create(GEN, (c!=null?c.getText():null)), root_1);

                adaptor.addChild(root_0, root_1);
                }

            }

            retval.tree = root_0;}
            }

            retval.stop = input.LT(-1);

            if ( state.backtracking==0 ) {

            retval.tree = (Object)adaptor.rulePostProcessing(root_0);
            adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop);
            }
        }

        catch (RecognitionException re) {
            reportError(re);
            recover(input,re);
        }
        finally {
            if ( state.backtracking>0 ) { memoize(input, 11, generative_StartIndex); }
        }
        return retval;
    }
    // $ANTLR end "generative"

    public static class hex_code_return extends ParserRuleReturnScope {
        Object tree;
        public Object getTree() { return tree; }
    };

    // $ANTLR start "hex_code"
    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:196:1: hex_code : (h= HEX_PAIR | h= HEX_QUAD | h= HEX_DQUAD | h= HEX_EIGHT ) -> ^() ;
    public final pycasmParser.hex_code_return hex_code() throws RecognitionException {
        pycasmParser.hex_code_return retval = new pycasmParser.hex_code_return();
        retval.start = input.LT(1);
        int hex_code_StartIndex = input.index();
        Object root_0 = null;

        Token h=null;

        Object h_tree=null;
        RewriteRuleTokenStream stream_HEX_EIGHT=new RewriteRuleTokenStream(adaptor,"token HEX_EIGHT");
        RewriteRuleTokenStream stream_HEX_DQUAD=new RewriteRuleTokenStream(adaptor,"token HEX_DQUAD");
        RewriteRuleTokenStream stream_HEX_QUAD=new RewriteRuleTokenStream(adaptor,"token HEX_QUAD");
        RewriteRuleTokenStream stream_HEX_PAIR=new RewriteRuleTokenStream(adaptor,"token HEX_PAIR");

        try {
            if ( state.backtracking>0 && alreadyParsedRule(input, 12) ) { return retval; }
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:196:9: ( (h= HEX_PAIR | h= HEX_QUAD | h= HEX_DQUAD | h= HEX_EIGHT ) -> ^() )
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:197:2: (h= HEX_PAIR | h= HEX_QUAD | h= HEX_DQUAD | h= HEX_EIGHT )
            {
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:197:2: (h= HEX_PAIR | h= HEX_QUAD | h= HEX_DQUAD | h= HEX_EIGHT )
            int alt28=4;
            switch ( input.LA(1) ) {
            case HEX_PAIR:
                {
                alt28=1;
                }
                break;
            case HEX_QUAD:
                {
                alt28=2;
                }
                break;
            case HEX_DQUAD:
                {
                alt28=3;
                }
                break;
            case HEX_EIGHT:
                {
                alt28=4;
                }
                break;
            default:
                if (state.backtracking>0) {state.failed=true; return retval;}
                NoViableAltException nvae =
                    new NoViableAltException("", 28, 0, input);

                throw nvae;
            }

            switch (alt28) {
                case 1 :
                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:197:4: h= HEX_PAIR
                    {
                    h=(Token)match(input,HEX_PAIR,FOLLOW_HEX_PAIR_in_hex_code501); if (state.failed) return retval; 
                    if ( state.backtracking==0 ) stream_HEX_PAIR.add(h);


                    }
                    break;
                case 2 :
                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:198:4: h= HEX_QUAD
                    {
                    h=(Token)match(input,HEX_QUAD,FOLLOW_HEX_QUAD_in_hex_code508); if (state.failed) return retval; 
                    if ( state.backtracking==0 ) stream_HEX_QUAD.add(h);


                    }
                    break;
                case 3 :
                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:199:4: h= HEX_DQUAD
                    {
                    h=(Token)match(input,HEX_DQUAD,FOLLOW_HEX_DQUAD_in_hex_code515); if (state.failed) return retval; 
                    if ( state.backtracking==0 ) stream_HEX_DQUAD.add(h);


                    }
                    break;
                case 4 :
                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:200:4: h= HEX_EIGHT
                    {
                    h=(Token)match(input,HEX_EIGHT,FOLLOW_HEX_EIGHT_in_hex_code522); if (state.failed) return retval; 
                    if ( state.backtracking==0 ) stream_HEX_EIGHT.add(h);


                    }
                    break;

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

            root_0 = (Object)adaptor.nil();
            // 201:4: -> ^()
            {
                // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:201:7: ^()
                {
                Object root_1 = (Object)adaptor.nil();
                root_1 = (Object)adaptor.becomeRoot(adaptor.create(HEX, (h!=null?h.getText():null)), root_1);

                adaptor.addChild(root_0, root_1);
                }

            }

            retval.tree = root_0;}
            }

            retval.stop = input.LT(-1);

            if ( state.backtracking==0 ) {

            retval.tree = (Object)adaptor.rulePostProcessing(root_0);
            adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop);
            }
        }

        catch (RecognitionException re) {
            reportError(re);
            recover(input,re);
        }
        finally {
            if ( state.backtracking>0 ) { memoize(input, 12, hex_code_StartIndex); }
        }
        return retval;
    }
    // $ANTLR end "hex_code"

    // $ANTLR start synpred4_pycasmParser
    public final void synpred4_pycasmParser_fragment() throws RecognitionException {   
        // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:122:4: ( WS )
        // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:122:4: WS
        {
        match(input,WS,FOLLOW_WS_in_synpred4_pycasmParser105); if (state.failed) return ;

        }
    }
    // $ANTLR end synpred4_pycasmParser

    // $ANTLR start synpred5_pycasmParser
    public final void synpred5_pycasmParser_fragment() throws RecognitionException {   
        // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:122:7: ( NEWLINE )
        // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:122:7: NEWLINE
        {
        match(input,NEWLINE,FOLLOW_NEWLINE_in_synpred5_pycasmParser107); if (state.failed) return ;

        }
    }
    // $ANTLR end synpred5_pycasmParser

    // $ANTLR start synpred7_pycasmParser
    public final void synpred7_pycasmParser_fragment() throws RecognitionException {   
        // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:129:5: ( spaced_element )
        // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:129:5: spaced_element
        {
        pushFollow(FOLLOW_spaced_element_in_synpred7_pycasmParser142);
        spaced_element();

        state._fsp--;
        if (state.failed) return ;

        }
    }
    // $ANTLR end synpred7_pycasmParser

    // $ANTLR start synpred8_pycasmParser
    public final void synpred8_pycasmParser_fragment() throws RecognitionException {   
        // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:129:21: ( element_chain )
        // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:129:21: element_chain
        {
        pushFollow(FOLLOW_element_chain_in_synpred8_pycasmParser145);
        element_chain();

        state._fsp--;
        if (state.failed) return ;

        }
    }
    // $ANTLR end synpred8_pycasmParser

    // $ANTLR start synpred9_pycasmParser
    public final void synpred9_pycasmParser_fragment() throws RecognitionException {   
        // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:131:5: ( spaced_element )
        // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:131:5: spaced_element
        {
        pushFollow(FOLLOW_spaced_element_in_synpred9_pycasmParser168);
        spaced_element();

        state._fsp--;
        if (state.failed) return ;

        }
    }
    // $ANTLR end synpred9_pycasmParser

    // $ANTLR start synpred11_pycasmParser
    public final void synpred11_pycasmParser_fragment() throws RecognitionException {   
        // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:131:21: ( sp )
        // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:131:21: sp
        {
        pushFollow(FOLLOW_sp_in_synpred11_pycasmParser171);
        sp();

        state._fsp--;
        if (state.failed) return ;

        }
    }
    // $ANTLR end synpred11_pycasmParser

    // $ANTLR start synpred12_pycasmParser
    public final void synpred12_pycasmParser_fragment() throws RecognitionException {   
        // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:131:26: ( element_chain )
        // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:131:26: element_chain
        {
        pushFollow(FOLLOW_element_chain_in_synpred12_pycasmParser175);
        element_chain();

        state._fsp--;
        if (state.failed) return ;

        }
    }
    // $ANTLR end synpred12_pycasmParser

    // $ANTLR start synpred13_pycasmParser
    public final void synpred13_pycasmParser_fragment() throws RecognitionException {   
        // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:131:4: ( ( ( spaced_element )+ | ( sp )+ ) ( element_chain )? )
        // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:131:4: ( ( spaced_element )+ | ( sp )+ ) ( element_chain )?
        {
        // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:131:4: ( ( spaced_element )+ | ( sp )+ )
        int alt33=2;
        int LA33_0 = input.LA(1);

        if ( (LA33_0==DOT_NAME) && (( input.LT(1).getCharPositionInLine() == 0 || input.LT(-1).getType() == NEWLINE ))) {
            alt33=1;
        }
        else if ( (LA33_0==INDENT) ) {
            alt33=1;
        }
        else if ( ((LA33_0>=NEWLINE && LA33_0<=WS)) ) {
            alt33=2;
        }
        else {
            if (state.backtracking>0) {state.failed=true; return ;}
            NoViableAltException nvae =
                new NoViableAltException("", 33, 0, input);

            throw nvae;
        }
        switch (alt33) {
            case 1 :
                // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:131:5: ( spaced_element )+
                {
                // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:131:5: ( spaced_element )+
                int cnt31=0;
                loop31:
                do {
                    int alt31=2;
                    int LA31_0 = input.LA(1);

                    if ( (LA31_0==DOT_NAME) && (( input.LT(1).getCharPositionInLine() == 0 || input.LT(-1).getType() == NEWLINE ))) {
                        alt31=1;
                    }
                    else if ( (LA31_0==INDENT) ) {
                        alt31=1;
                    }


                    switch (alt31) {
                	case 1 :
                	    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:0:0: spaced_element
                	    {
                	    pushFollow(FOLLOW_spaced_element_in_synpred13_pycasmParser168);
                	    spaced_element();

                	    state._fsp--;
                	    if (state.failed) return ;

                	    }
                	    break;

                	default :
                	    if ( cnt31 >= 1 ) break loop31;
                	    if (state.backtracking>0) {state.failed=true; return ;}
                            EarlyExitException eee =
                                new EarlyExitException(31, input);
                            throw eee;
                    }
                    cnt31++;
                } while (true);


                }
                break;
            case 2 :
                // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:131:21: ( sp )+
                {
                // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:131:21: ( sp )+
                int cnt32=0;
                loop32:
                do {
                    int alt32=2;
                    int LA32_0 = input.LA(1);

                    if ( ((LA32_0>=NEWLINE && LA32_0<=WS)) ) {
                        alt32=1;
                    }


                    switch (alt32) {
                	case 1 :
                	    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:0:0: sp
                	    {
                	    pushFollow(FOLLOW_sp_in_synpred13_pycasmParser171);
                	    sp();

                	    state._fsp--;
                	    if (state.failed) return ;

                	    }
                	    break;

                	default :
                	    if ( cnt32 >= 1 ) break loop32;
                	    if (state.backtracking>0) {state.failed=true; return ;}
                            EarlyExitException eee =
                                new EarlyExitException(32, input);
                            throw eee;
                    }
                    cnt32++;
                } while (true);


                }
                break;

        }

        // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:131:26: ( element_chain )?
        int alt34=2;
        int LA34_0 = input.LA(1);

        if ( ((LA34_0>=HEX_PAIR && LA34_0<=HEX_QUAD)||(LA34_0>=TYPED_VALUE && LA34_0<=STRING)||LA34_0==NAME) ) {
            alt34=1;
        }
        switch (alt34) {
            case 1 :
                // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:0:0: element_chain
                {
                pushFollow(FOLLOW_element_chain_in_synpred13_pycasmParser175);
                element_chain();

                state._fsp--;
                if (state.failed) return ;

                }
                break;

        }


        }
    }
    // $ANTLR end synpred13_pycasmParser

    // $ANTLR start synpred15_pycasmParser
    public final void synpred15_pycasmParser_fragment() throws RecognitionException {   
        // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:137:18: ( ( sp )+ chain_element )
        // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:137:18: ( sp )+ chain_element
        {
        // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:137:18: ( sp )+
        int cnt35=0;
        loop35:
        do {
            int alt35=2;
            int LA35_0 = input.LA(1);

            if ( ((LA35_0>=NEWLINE && LA35_0<=WS)) ) {
                alt35=1;
            }


            switch (alt35) {
        	case 1 :
        	    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:0:0: sp
        	    {
        	    pushFollow(FOLLOW_sp_in_synpred15_pycasmParser208);
        	    sp();

        	    state._fsp--;
        	    if (state.failed) return ;

        	    }
        	    break;

        	default :
        	    if ( cnt35 >= 1 ) break loop35;
        	    if (state.backtracking>0) {state.failed=true; return ;}
                    EarlyExitException eee =
                        new EarlyExitException(35, input);
                    throw eee;
            }
            cnt35++;
        } while (true);

        pushFollow(FOLLOW_chain_element_in_synpred15_pycasmParser211);
        chain_element();

        state._fsp--;
        if (state.failed) return ;

        }
    }
    // $ANTLR end synpred15_pycasmParser

    // $ANTLR start synpred18_pycasmParser
    public final void synpred18_pycasmParser_fragment() throws RecognitionException {   
        // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:148:3: ( directive )
        // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:148:3: directive
        {
        pushFollow(FOLLOW_directive_in_synpred18_pycasmParser247);
        directive();

        state._fsp--;
        if (state.failed) return ;

        }
    }
    // $ANTLR end synpred18_pycasmParser

    // $ANTLR start synpred19_pycasmParser
    public final void synpred19_pycasmParser_fragment() throws RecognitionException {   
        // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:149:18: ( NEWLINE )
        // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:149:18: NEWLINE
        {
        match(input,NEWLINE,FOLLOW_NEWLINE_in_synpred19_pycasmParser257); if (state.failed) return ;

        }
    }
    // $ANTLR end synpred19_pycasmParser

    // $ANTLR start synpred20_pycasmParser
    public final void synpred20_pycasmParser_fragment() throws RecognitionException {   
        // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:149:27: ( DEDENT )
        // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:149:27: DEDENT
        {
        match(input,DEDENT,FOLLOW_DEDENT_in_synpred20_pycasmParser260); if (state.failed) return ;

        }
    }
    // $ANTLR end synpred20_pycasmParser

    // $ANTLR start synpred24_pycasmParser
    public final void synpred24_pycasmParser_fragment() throws RecognitionException {   
        // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:155:5: ( INDENT block ( NEWLINE )? DEDENT ( DOT_END ( WS )+ ( NAME ) )? )
        // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:155:5: INDENT block ( NEWLINE )? DEDENT ( DOT_END ( WS )+ ( NAME ) )?
        {
        match(input,INDENT,FOLLOW_INDENT_in_synpred24_pycasmParser286); if (state.failed) return ;
        pushFollow(FOLLOW_block_in_synpred24_pycasmParser288);
        block();

        state._fsp--;
        if (state.failed) return ;
        // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:155:18: ( NEWLINE )?
        int alt37=2;
        int LA37_0 = input.LA(1);

        if ( (LA37_0==NEWLINE) ) {
            alt37=1;
        }
        switch (alt37) {
            case 1 :
                // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:0:0: NEWLINE
                {
                match(input,NEWLINE,FOLLOW_NEWLINE_in_synpred24_pycasmParser290); if (state.failed) return ;

                }
                break;

        }

        match(input,DEDENT,FOLLOW_DEDENT_in_synpred24_pycasmParser293); if (state.failed) return ;
        // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:156:5: ( DOT_END ( WS )+ ( NAME ) )?
        int alt39=2;
        int LA39_0 = input.LA(1);

        if ( (LA39_0==DOT_END) ) {
            alt39=1;
        }
        switch (alt39) {
            case 1 :
                // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:156:6: DOT_END ( WS )+ ( NAME )
                {
                match(input,DOT_END,FOLLOW_DOT_END_in_synpred24_pycasmParser300); if (state.failed) return ;
                // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:156:14: ( WS )+
                int cnt38=0;
                loop38:
                do {
                    int alt38=2;
                    int LA38_0 = input.LA(1);

                    if ( (LA38_0==WS) ) {
                        alt38=1;
                    }


                    switch (alt38) {
                	case 1 :
                	    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:0:0: WS
                	    {
                	    match(input,WS,FOLLOW_WS_in_synpred24_pycasmParser302); if (state.failed) return ;

                	    }
                	    break;

                	default :
                	    if ( cnt38 >= 1 ) break loop38;
                	    if (state.backtracking>0) {state.failed=true; return ;}
                            EarlyExitException eee =
                                new EarlyExitException(38, input);
                            throw eee;
                    }
                    cnt38++;
                } while (true);

                // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:157:6: ( NAME )
                // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmParser.g:157:7: NAME
                {
                match(input,NAME,FOLLOW_NAME_in_synpred24_pycasmParser311); if (state.failed) return ;

                }


                }
                break;

        }


        }
    }
    // $ANTLR end synpred24_pycasmParser

    // Delegated rules

    public final boolean synpred19_pycasmParser() {
        state.backtracking++;
        int start = input.mark();
        try {
            synpred19_pycasmParser_fragment(); // can never throw exception
        } catch (RecognitionException re) {
            System.err.println("impossible: "+re);
        }
        boolean success = !state.failed;
        input.rewind(start);
        state.backtracking--;
        state.failed=false;
        return success;
    }
    public final boolean synpred8_pycasmParser() {
        state.backtracking++;
        int start = input.mark();
        try {
            synpred8_pycasmParser_fragment(); // can never throw exception
        } catch (RecognitionException re) {
            System.err.println("impossible: "+re);
        }
        boolean success = !state.failed;
        input.rewind(start);
        state.backtracking--;
        state.failed=false;
        return success;
    }
    public final boolean synpred20_pycasmParser() {
        state.backtracking++;
        int start = input.mark();
        try {
            synpred20_pycasmParser_fragment(); // can never throw exception
        } catch (RecognitionException re) {
            System.err.println("impossible: "+re);
        }
        boolean success = !state.failed;
        input.rewind(start);
        state.backtracking--;
        state.failed=false;
        return success;
    }
    public final boolean synpred5_pycasmParser() {
        state.backtracking++;
        int start = input.mark();
        try {
            synpred5_pycasmParser_fragment(); // can never throw exception
        } catch (RecognitionException re) {
            System.err.println("impossible: "+re);
        }
        boolean success = !state.failed;
        input.rewind(start);
        state.backtracking--;
        state.failed=false;
        return success;
    }
    public final boolean synpred4_pycasmParser() {
        state.backtracking++;
        int start = input.mark();
        try {
            synpred4_pycasmParser_fragment(); // can never throw exception
        } catch (RecognitionException re) {
            System.err.println("impossible: "+re);
        }
        boolean success = !state.failed;
        input.rewind(start);
        state.backtracking--;
        state.failed=false;
        return success;
    }
    public final boolean synpred11_pycasmParser() {
        state.backtracking++;
        int start = input.mark();
        try {
            synpred11_pycasmParser_fragment(); // can never throw exception
        } catch (RecognitionException re) {
            System.err.println("impossible: "+re);
        }
        boolean success = !state.failed;
        input.rewind(start);
        state.backtracking--;
        state.failed=false;
        return success;
    }
    public final boolean synpred18_pycasmParser() {
        state.backtracking++;
        int start = input.mark();
        try {
            synpred18_pycasmParser_fragment(); // can never throw exception
        } catch (RecognitionException re) {
            System.err.println("impossible: "+re);
        }
        boolean success = !state.failed;
        input.rewind(start);
        state.backtracking--;
        state.failed=false;
        return success;
    }
    public final boolean synpred7_pycasmParser() {
        state.backtracking++;
        int start = input.mark();
        try {
            synpred7_pycasmParser_fragment(); // can never throw exception
        } catch (RecognitionException re) {
            System.err.println("impossible: "+re);
        }
        boolean success = !state.failed;
        input.rewind(start);
        state.backtracking--;
        state.failed=false;
        return success;
    }
    public final boolean synpred13_pycasmParser() {
        state.backtracking++;
        int start = input.mark();
        try {
            synpred13_pycasmParser_fragment(); // can never throw exception
        } catch (RecognitionException re) {
            System.err.println("impossible: "+re);
        }
        boolean success = !state.failed;
        input.rewind(start);
        state.backtracking--;
        state.failed=false;
        return success;
    }
    public final boolean synpred24_pycasmParser() {
        state.backtracking++;
        int start = input.mark();
        try {
            synpred24_pycasmParser_fragment(); // can never throw exception
        } catch (RecognitionException re) {
            System.err.println("impossible: "+re);
        }
        boolean success = !state.failed;
        input.rewind(start);
        state.backtracking--;
        state.failed=false;
        return success;
    }
    public final boolean synpred15_pycasmParser() {
        state.backtracking++;
        int start = input.mark();
        try {
            synpred15_pycasmParser_fragment(); // can never throw exception
        } catch (RecognitionException re) {
            System.err.println("impossible: "+re);
        }
        boolean success = !state.failed;
        input.rewind(start);
        state.backtracking--;
        state.failed=false;
        return success;
    }
    public final boolean synpred9_pycasmParser() {
        state.backtracking++;
        int start = input.mark();
        try {
            synpred9_pycasmParser_fragment(); // can never throw exception
        } catch (RecognitionException re) {
            System.err.println("impossible: "+re);
        }
        boolean success = !state.failed;
        input.rewind(start);
        state.backtracking--;
        state.failed=false;
        return success;
    }
    public final boolean synpred12_pycasmParser() {
        state.backtracking++;
        int start = input.mark();
        try {
            synpred12_pycasmParser_fragment(); // can never throw exception
        } catch (RecognitionException re) {
            System.err.println("impossible: "+re);
        }
        boolean success = !state.failed;
        input.rewind(start);
        state.backtracking--;
        state.failed=false;
        return success;
    }


    protected DFA4 dfa4 = new DFA4(this);
    protected DFA5 dfa5 = new DFA5(this);
    protected DFA10 dfa10 = new DFA10(this);
    protected DFA13 dfa13 = new DFA13(this);
    protected DFA21 dfa21 = new DFA21(this);
    protected DFA23 dfa23 = new DFA23(this);
    static final String DFA4_eotS =
        "\17\uffff";
    static final String DFA4_eofS =
        "\1\1\16\uffff";
    static final String DFA4_minS =
        "\1\4\7\uffff\2\0\5\uffff";
    static final String DFA4_maxS =
        "\1\27\7\uffff\2\0\5\uffff";
    static final String DFA4_acceptS =
        "\1\uffff\1\2\14\uffff\1\1";
    static final String DFA4_specialS =
        "\1\0\7\uffff\1\1\1\2\5\uffff}>";
    static final String[] DFA4_transitionS = {
            "\1\1\1\11\3\uffff\4\1\4\uffff\2\1\1\uffff\1\10\3\1",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "\1\uffff",
            "\1\uffff",
            "",
            "",
            "",
            "",
            ""
    };

    static final short[] DFA4_eot = DFA.unpackEncodedString(DFA4_eotS);
    static final short[] DFA4_eof = DFA.unpackEncodedString(DFA4_eofS);
    static final char[] DFA4_min = DFA.unpackEncodedStringToUnsignedChars(DFA4_minS);
    static final char[] DFA4_max = DFA.unpackEncodedStringToUnsignedChars(DFA4_maxS);
    static final short[] DFA4_accept = DFA.unpackEncodedString(DFA4_acceptS);
    static final short[] DFA4_special = DFA.unpackEncodedString(DFA4_specialS);
    static final short[][] DFA4_transition;

    static {
        int numStates = DFA4_transitionS.length;
        DFA4_transition = new short[numStates][];
        for (int i=0; i<numStates; i++) {
            DFA4_transition[i] = DFA.unpackEncodedString(DFA4_transitionS[i]);
        }
    }

    class DFA4 extends DFA {

        public DFA4(BaseRecognizer recognizer) {
            this.recognizer = recognizer;
            this.decisionNumber = 4;
            this.eot = DFA4_eot;
            this.eof = DFA4_eof;
            this.min = DFA4_min;
            this.max = DFA4_max;
            this.accept = DFA4_accept;
            this.special = DFA4_special;
            this.transition = DFA4_transition;
        }
        public String getDescription() {
            return "()+ loopback of 129:5: ( spaced_element )+";
        }
        public int specialStateTransition(int s, IntStream _input) throws NoViableAltException {
            TokenStream input = (TokenStream)_input;
        	int _s = s;
            switch ( s ) {
                    case 0 : 
                        int LA4_0 = input.LA(1);

                         
                        int index4_0 = input.index();
                        input.rewind();
                        s = -1;
                        if ( (LA4_0==EOF||LA4_0==DEDENT||(LA4_0>=HEX_PAIR && LA4_0<=HEX_QUAD)||(LA4_0>=TYPED_VALUE && LA4_0<=STRING)||(LA4_0>=NAME && LA4_0<=WS)) ) {s = 1;}

                        else if ( (LA4_0==DOT_NAME) && (( input.LT(1).getCharPositionInLine() == 0 || input.LT(-1).getType() == NEWLINE ))) {s = 8;}

                        else if ( (LA4_0==INDENT) ) {s = 9;}

                         
                        input.seek(index4_0);
                        if ( s>=0 ) return s;
                        break;
                    case 1 : 
                        int LA4_8 = input.LA(1);

                         
                        int index4_8 = input.index();
                        input.rewind();
                        s = -1;
                        if ( ((synpred7_pycasmParser()&&( input.LT(1).getCharPositionInLine() == 0 || input.LT(-1).getType() == NEWLINE ))) ) {s = 14;}

                        else if ( (( input.LT(1).getCharPositionInLine() == 0 || input.LT(-1).getType() == NEWLINE )) ) {s = 1;}

                         
                        input.seek(index4_8);
                        if ( s>=0 ) return s;
                        break;
                    case 2 : 
                        int LA4_9 = input.LA(1);

                         
                        int index4_9 = input.index();
                        input.rewind();
                        s = -1;
                        if ( (synpred7_pycasmParser()) ) {s = 14;}

                        else if ( (true) ) {s = 1;}

                         
                        input.seek(index4_9);
                        if ( s>=0 ) return s;
                        break;
            }
            if (state.backtracking>0) {state.failed=true; return -1;}
            NoViableAltException nvae =
                new NoViableAltException(getDescription(), 4, _s, input);
            error(nvae);
            throw nvae;
        }
    }
    static final String DFA5_eotS =
        "\13\uffff";
    static final String DFA5_eofS =
        "\1\11\12\uffff";
    static final String DFA5_minS =
        "\1\4\7\0\3\uffff";
    static final String DFA5_maxS =
        "\1\27\7\0\3\uffff";
    static final String DFA5_acceptS =
        "\10\uffff\2\2\1\1";
    static final String DFA5_specialS =
        "\1\4\1\7\1\6\1\3\1\1\1\2\1\0\1\5\3\uffff}>";
    static final String[] DFA5_transitionS = {
            "\2\11\3\uffff\1\4\1\6\1\7\1\5\4\uffff\1\3\1\2\1\uffff\1\10"+
            "\1\1\2\11",
            "\1\uffff",
            "\1\uffff",
            "\1\uffff",
            "\1\uffff",
            "\1\uffff",
            "\1\uffff",
            "\1\uffff",
            "",
            "",
            ""
    };

    static final short[] DFA5_eot = DFA.unpackEncodedString(DFA5_eotS);
    static final short[] DFA5_eof = DFA.unpackEncodedString(DFA5_eofS);
    static final char[] DFA5_min = DFA.unpackEncodedStringToUnsignedChars(DFA5_minS);
    static final char[] DFA5_max = DFA.unpackEncodedStringToUnsignedChars(DFA5_maxS);
    static final short[] DFA5_accept = DFA.unpackEncodedString(DFA5_acceptS);
    static final short[] DFA5_special = DFA.unpackEncodedString(DFA5_specialS);
    static final short[][] DFA5_transition;

    static {
        int numStates = DFA5_transitionS.length;
        DFA5_transition = new short[numStates][];
        for (int i=0; i<numStates; i++) {
            DFA5_transition[i] = DFA.unpackEncodedString(DFA5_transitionS[i]);
        }
    }

    class DFA5 extends DFA {

        public DFA5(BaseRecognizer recognizer) {
            this.recognizer = recognizer;
            this.decisionNumber = 5;
            this.eot = DFA5_eot;
            this.eof = DFA5_eof;
            this.min = DFA5_min;
            this.max = DFA5_max;
            this.accept = DFA5_accept;
            this.special = DFA5_special;
            this.transition = DFA5_transition;
        }
        public String getDescription() {
            return "129:21: ( element_chain )?";
        }
        public int specialStateTransition(int s, IntStream _input) throws NoViableAltException {
            TokenStream input = (TokenStream)_input;
        	int _s = s;
            switch ( s ) {
                    case 0 : 
                        int LA5_6 = input.LA(1);

                         
                        int index5_6 = input.index();
                        input.rewind();
                        s = -1;
                        if ( (synpred8_pycasmParser()) ) {s = 10;}

                        else if ( (true) ) {s = 9;}

                         
                        input.seek(index5_6);
                        if ( s>=0 ) return s;
                        break;
                    case 1 : 
                        int LA5_4 = input.LA(1);

                         
                        int index5_4 = input.index();
                        input.rewind();
                        s = -1;
                        if ( (synpred8_pycasmParser()) ) {s = 10;}

                        else if ( (true) ) {s = 9;}

                         
                        input.seek(index5_4);
                        if ( s>=0 ) return s;
                        break;
                    case 2 : 
                        int LA5_5 = input.LA(1);

                         
                        int index5_5 = input.index();
                        input.rewind();
                        s = -1;
                        if ( (synpred8_pycasmParser()) ) {s = 10;}

                        else if ( (true) ) {s = 9;}

                         
                        input.seek(index5_5);
                        if ( s>=0 ) return s;
                        break;
                    case 3 : 
                        int LA5_3 = input.LA(1);

                         
                        int index5_3 = input.index();
                        input.rewind();
                        s = -1;
                        if ( (synpred8_pycasmParser()) ) {s = 10;}

                        else if ( (true) ) {s = 9;}

                         
                        input.seek(index5_3);
                        if ( s>=0 ) return s;
                        break;
                    case 4 : 
                        int LA5_0 = input.LA(1);

                         
                        int index5_0 = input.index();
                        input.rewind();
                        s = -1;
                        if ( (LA5_0==NAME) ) {s = 1;}

                        else if ( (LA5_0==STRING) ) {s = 2;}

                        else if ( (LA5_0==TYPED_VALUE) ) {s = 3;}

                        else if ( (LA5_0==HEX_PAIR) ) {s = 4;}

                        else if ( (LA5_0==HEX_QUAD) ) {s = 5;}

                        else if ( (LA5_0==HEX_DQUAD) ) {s = 6;}

                        else if ( (LA5_0==HEX_EIGHT) ) {s = 7;}

                        else if ( (LA5_0==DOT_NAME) && (( input.LT(1).getCharPositionInLine() == 0 || input.LT(-1).getType() == NEWLINE ))) {s = 8;}

                        else if ( (LA5_0==EOF||(LA5_0>=DEDENT && LA5_0<=INDENT)||(LA5_0>=NEWLINE && LA5_0<=WS)) ) {s = 9;}

                         
                        input.seek(index5_0);
                        if ( s>=0 ) return s;
                        break;
                    case 5 : 
                        int LA5_7 = input.LA(1);

                         
                        int index5_7 = input.index();
                        input.rewind();
                        s = -1;
                        if ( (synpred8_pycasmParser()) ) {s = 10;}

                        else if ( (true) ) {s = 9;}

                         
                        input.seek(index5_7);
                        if ( s>=0 ) return s;
                        break;
                    case 6 : 
                        int LA5_2 = input.LA(1);

                         
                        int index5_2 = input.index();
                        input.rewind();
                        s = -1;
                        if ( (synpred8_pycasmParser()) ) {s = 10;}

                        else if ( (true) ) {s = 9;}

                         
                        input.seek(index5_2);
                        if ( s>=0 ) return s;
                        break;
                    case 7 : 
                        int LA5_1 = input.LA(1);

                         
                        int index5_1 = input.index();
                        input.rewind();
                        s = -1;
                        if ( (synpred8_pycasmParser()) ) {s = 10;}

                        else if ( (true) ) {s = 9;}

                         
                        input.seek(index5_1);
                        if ( s>=0 ) return s;
                        break;
            }
            if (state.backtracking>0) {state.failed=true; return -1;}
            NoViableAltException nvae =
                new NoViableAltException(getDescription(), 5, _s, input);
            error(nvae);
            throw nvae;
        }
    }
    static final String DFA10_eotS =
        "\14\uffff";
    static final String DFA10_eofS =
        "\1\10\13\uffff";
    static final String DFA10_minS =
        "\1\4\7\0\4\uffff";
    static final String DFA10_maxS =
        "\1\27\7\0\4\uffff";
    static final String DFA10_acceptS =
        "\10\uffff\3\2\1\1";
    static final String DFA10_specialS =
        "\1\0\1\7\1\6\1\4\1\1\1\2\1\3\1\5\4\uffff}>";
    static final String[] DFA10_transitionS = {
            "\1\10\1\12\3\uffff\1\4\1\6\1\7\1\5\4\uffff\1\3\1\2\1\uffff"+
            "\1\11\1\1\1\10\1\12",
            "\1\uffff",
            "\1\uffff",
            "\1\uffff",
            "\1\uffff",
            "\1\uffff",
            "\1\uffff",
            "\1\uffff",
            "",
            "",
            "",
            ""
    };

    static final short[] DFA10_eot = DFA.unpackEncodedString(DFA10_eotS);
    static final short[] DFA10_eof = DFA.unpackEncodedString(DFA10_eofS);
    static final char[] DFA10_min = DFA.unpackEncodedStringToUnsignedChars(DFA10_minS);
    static final char[] DFA10_max = DFA.unpackEncodedStringToUnsignedChars(DFA10_maxS);
    static final short[] DFA10_accept = DFA.unpackEncodedString(DFA10_acceptS);
    static final short[] DFA10_special = DFA.unpackEncodedString(DFA10_specialS);
    static final short[][] DFA10_transition;

    static {
        int numStates = DFA10_transitionS.length;
        DFA10_transition = new short[numStates][];
        for (int i=0; i<numStates; i++) {
            DFA10_transition[i] = DFA.unpackEncodedString(DFA10_transitionS[i]);
        }
    }

    class DFA10 extends DFA {

        public DFA10(BaseRecognizer recognizer) {
            this.recognizer = recognizer;
            this.decisionNumber = 10;
            this.eot = DFA10_eot;
            this.eof = DFA10_eof;
            this.min = DFA10_min;
            this.max = DFA10_max;
            this.accept = DFA10_accept;
            this.special = DFA10_special;
            this.transition = DFA10_transition;
        }
        public String getDescription() {
            return "131:26: ( element_chain )?";
        }
        public int specialStateTransition(int s, IntStream _input) throws NoViableAltException {
            TokenStream input = (TokenStream)_input;
        	int _s = s;
            switch ( s ) {
                    case 0 : 
                        int LA10_0 = input.LA(1);

                         
                        int index10_0 = input.index();
                        input.rewind();
                        s = -1;
                        if ( (LA10_0==NAME) ) {s = 1;}

                        else if ( (LA10_0==STRING) ) {s = 2;}

                        else if ( (LA10_0==TYPED_VALUE) ) {s = 3;}

                        else if ( (LA10_0==HEX_PAIR) ) {s = 4;}

                        else if ( (LA10_0==HEX_QUAD) ) {s = 5;}

                        else if ( (LA10_0==HEX_DQUAD) ) {s = 6;}

                        else if ( (LA10_0==HEX_EIGHT) ) {s = 7;}

                        else if ( (LA10_0==EOF||LA10_0==DEDENT||LA10_0==NEWLINE) ) {s = 8;}

                        else if ( (LA10_0==DOT_NAME) && (( input.LT(1).getCharPositionInLine() == 0 || input.LT(-1).getType() == NEWLINE ))) {s = 9;}

                        else if ( (LA10_0==INDENT||LA10_0==WS) ) {s = 10;}

                         
                        input.seek(index10_0);
                        if ( s>=0 ) return s;
                        break;
                    case 1 : 
                        int LA10_4 = input.LA(1);

                         
                        int index10_4 = input.index();
                        input.rewind();
                        s = -1;
                        if ( (synpred12_pycasmParser()) ) {s = 11;}

                        else if ( (true) ) {s = 10;}

                         
                        input.seek(index10_4);
                        if ( s>=0 ) return s;
                        break;
                    case 2 : 
                        int LA10_5 = input.LA(1);

                         
                        int index10_5 = input.index();
                        input.rewind();
                        s = -1;
                        if ( (synpred12_pycasmParser()) ) {s = 11;}

                        else if ( (true) ) {s = 10;}

                         
                        input.seek(index10_5);
                        if ( s>=0 ) return s;
                        break;
                    case 3 : 
                        int LA10_6 = input.LA(1);

                         
                        int index10_6 = input.index();
                        input.rewind();
                        s = -1;
                        if ( (synpred12_pycasmParser()) ) {s = 11;}

                        else if ( (true) ) {s = 10;}

                         
                        input.seek(index10_6);
                        if ( s>=0 ) return s;
                        break;
                    case 4 : 
                        int LA10_3 = input.LA(1);

                         
                        int index10_3 = input.index();
                        input.rewind();
                        s = -1;
                        if ( (synpred12_pycasmParser()) ) {s = 11;}

                        else if ( (true) ) {s = 10;}

                         
                        input.seek(index10_3);
                        if ( s>=0 ) return s;
                        break;
                    case 5 : 
                        int LA10_7 = input.LA(1);

                         
                        int index10_7 = input.index();
                        input.rewind();
                        s = -1;
                        if ( (synpred12_pycasmParser()) ) {s = 11;}

                        else if ( (true) ) {s = 10;}

                         
                        input.seek(index10_7);
                        if ( s>=0 ) return s;
                        break;
                    case 6 : 
                        int LA10_2 = input.LA(1);

                         
                        int index10_2 = input.index();
                        input.rewind();
                        s = -1;
                        if ( (synpred12_pycasmParser()) ) {s = 11;}

                        else if ( (true) ) {s = 10;}

                         
                        input.seek(index10_2);
                        if ( s>=0 ) return s;
                        break;
                    case 7 : 
                        int LA10_1 = input.LA(1);

                         
                        int index10_1 = input.index();
                        input.rewind();
                        s = -1;
                        if ( (synpred12_pycasmParser()) ) {s = 11;}

                        else if ( (true) ) {s = 10;}

                         
                        input.seek(index10_1);
                        if ( s>=0 ) return s;
                        break;
            }
            if (state.backtracking>0) {state.failed=true; return -1;}
            NoViableAltException nvae =
                new NoViableAltException(getDescription(), 10, _s, input);
            error(nvae);
            throw nvae;
        }
    }
    static final String DFA13_eotS =
        "\15\uffff";
    static final String DFA13_eofS =
        "\1\2\2\uffff\2\2\10\uffff";
    static final String DFA13_minS =
        "\1\4\2\uffff\2\4\7\0\1\uffff";
    static final String DFA13_maxS =
        "\1\27\2\uffff\2\27\7\0\1\uffff";
    static final String DFA13_acceptS =
        "\1\uffff\2\2\11\uffff\1\1";
    static final String DFA13_specialS =
        "\1\6\4\uffff\1\5\1\0\1\7\1\4\1\1\1\3\1\2\1\uffff}>";
    static final String[] DFA13_transitionS = {
            "\2\2\3\uffff\4\2\4\uffff\2\2\1\uffff\1\1\1\2\1\4\1\3",
            "",
            "",
            "\2\2\3\uffff\1\10\1\12\1\13\1\11\4\uffff\1\7\1\6\1\uffff\1"+
            "\2\1\5\1\4\1\3",
            "\2\2\3\uffff\1\10\1\12\1\13\1\11\4\uffff\1\7\1\6\1\uffff\1"+
            "\2\1\5\1\4\1\3",
            "\1\uffff",
            "\1\uffff",
            "\1\uffff",
            "\1\uffff",
            "\1\uffff",
            "\1\uffff",
            "\1\uffff",
            ""
    };

    static final short[] DFA13_eot = DFA.unpackEncodedString(DFA13_eotS);
    static final short[] DFA13_eof = DFA.unpackEncodedString(DFA13_eofS);
    static final char[] DFA13_min = DFA.unpackEncodedStringToUnsignedChars(DFA13_minS);
    static final char[] DFA13_max = DFA.unpackEncodedStringToUnsignedChars(DFA13_maxS);
    static final short[] DFA13_accept = DFA.unpackEncodedString(DFA13_acceptS);
    static final short[] DFA13_special = DFA.unpackEncodedString(DFA13_specialS);
    static final short[][] DFA13_transition;

    static {
        int numStates = DFA13_transitionS.length;
        DFA13_transition = new short[numStates][];
        for (int i=0; i<numStates; i++) {
            DFA13_transition[i] = DFA.unpackEncodedString(DFA13_transitionS[i]);
        }
    }

    class DFA13 extends DFA {

        public DFA13(BaseRecognizer recognizer) {
            this.recognizer = recognizer;
            this.decisionNumber = 13;
            this.eot = DFA13_eot;
            this.eof = DFA13_eof;
            this.min = DFA13_min;
            this.max = DFA13_max;
            this.accept = DFA13_accept;
            this.special = DFA13_special;
            this.transition = DFA13_transition;
        }
        public String getDescription() {
            return "()* loopback of 137:17: ( ( sp )+ chain_element )*";
        }
        public int specialStateTransition(int s, IntStream _input) throws NoViableAltException {
            TokenStream input = (TokenStream)_input;
        	int _s = s;
            switch ( s ) {
                    case 0 : 
                        int LA13_6 = input.LA(1);

                         
                        int index13_6 = input.index();
                        input.rewind();
                        s = -1;
                        if ( (synpred15_pycasmParser()) ) {s = 12;}

                        else if ( (true) ) {s = 2;}

                         
                        input.seek(index13_6);
                        if ( s>=0 ) return s;
                        break;
                    case 1 : 
                        int LA13_9 = input.LA(1);

                         
                        int index13_9 = input.index();
                        input.rewind();
                        s = -1;
                        if ( (synpred15_pycasmParser()) ) {s = 12;}

                        else if ( (true) ) {s = 2;}

                         
                        input.seek(index13_9);
                        if ( s>=0 ) return s;
                        break;
                    case 2 : 
                        int LA13_11 = input.LA(1);

                         
                        int index13_11 = input.index();
                        input.rewind();
                        s = -1;
                        if ( (synpred15_pycasmParser()) ) {s = 12;}

                        else if ( (true) ) {s = 2;}

                         
                        input.seek(index13_11);
                        if ( s>=0 ) return s;
                        break;
                    case 3 : 
                        int LA13_10 = input.LA(1);

                         
                        int index13_10 = input.index();
                        input.rewind();
                        s = -1;
                        if ( (synpred15_pycasmParser()) ) {s = 12;}

                        else if ( (true) ) {s = 2;}

                         
                        input.seek(index13_10);
                        if ( s>=0 ) return s;
                        break;
                    case 4 : 
                        int LA13_8 = input.LA(1);

                         
                        int index13_8 = input.index();
                        input.rewind();
                        s = -1;
                        if ( (synpred15_pycasmParser()) ) {s = 12;}

                        else if ( (true) ) {s = 2;}

                         
                        input.seek(index13_8);
                        if ( s>=0 ) return s;
                        break;
                    case 5 : 
                        int LA13_5 = input.LA(1);

                         
                        int index13_5 = input.index();
                        input.rewind();
                        s = -1;
                        if ( (synpred15_pycasmParser()) ) {s = 12;}

                        else if ( (true) ) {s = 2;}

                         
                        input.seek(index13_5);
                        if ( s>=0 ) return s;
                        break;
                    case 6 : 
                        int LA13_0 = input.LA(1);

                         
                        int index13_0 = input.index();
                        input.rewind();
                        s = -1;
                        if ( (LA13_0==DOT_NAME) && (( input.LT(1).getCharPositionInLine() == 0 || input.LT(-1).getType() == NEWLINE ))) {s = 1;}

                        else if ( (LA13_0==EOF||(LA13_0>=DEDENT && LA13_0<=INDENT)||(LA13_0>=HEX_PAIR && LA13_0<=HEX_QUAD)||(LA13_0>=TYPED_VALUE && LA13_0<=STRING)||LA13_0==NAME) ) {s = 2;}

                        else if ( (LA13_0==WS) ) {s = 3;}

                        else if ( (LA13_0==NEWLINE) ) {s = 4;}

                         
                        input.seek(index13_0);
                        if ( s>=0 ) return s;
                        break;
                    case 7 : 
                        int LA13_7 = input.LA(1);

                         
                        int index13_7 = input.index();
                        input.rewind();
                        s = -1;
                        if ( (synpred15_pycasmParser()) ) {s = 12;}

                        else if ( (true) ) {s = 2;}

                         
                        input.seek(index13_7);
                        if ( s>=0 ) return s;
                        break;
            }
            if (state.backtracking>0) {state.failed=true; return -1;}
            NoViableAltException nvae =
                new NoViableAltException(getDescription(), 13, _s, input);
            error(nvae);
            throw nvae;
        }
    }
    static final String DFA21_eotS =
        "\17\uffff";
    static final String DFA21_eofS =
        "\1\12\16\uffff";
    static final String DFA21_minS =
        "\1\4\1\0\15\uffff";
    static final String DFA21_maxS =
        "\1\27\1\0\15\uffff";
    static final String DFA21_acceptS =
        "\2\uffff\1\2\6\uffff\2\2\3\uffff\1\1";
    static final String DFA21_specialS =
        "\1\0\1\1\15\uffff}>";
    static final String[] DFA21_transitionS = {
            "\1\12\1\1\3\uffff\4\2\4\uffff\2\2\1\uffff\1\11\1\2\2\12",
            "\1\uffff",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
    };

    static final short[] DFA21_eot = DFA.unpackEncodedString(DFA21_eotS);
    static final short[] DFA21_eof = DFA.unpackEncodedString(DFA21_eofS);
    static final char[] DFA21_min = DFA.unpackEncodedStringToUnsignedChars(DFA21_minS);
    static final char[] DFA21_max = DFA.unpackEncodedStringToUnsignedChars(DFA21_maxS);
    static final short[] DFA21_accept = DFA.unpackEncodedString(DFA21_acceptS);
    static final short[] DFA21_special = DFA.unpackEncodedString(DFA21_specialS);
    static final short[][] DFA21_transition;

    static {
        int numStates = DFA21_transitionS.length;
        DFA21_transition = new short[numStates][];
        for (int i=0; i<numStates; i++) {
            DFA21_transition[i] = DFA.unpackEncodedString(DFA21_transitionS[i]);
        }
    }

    class DFA21 extends DFA {

        public DFA21(BaseRecognizer recognizer) {
            this.recognizer = recognizer;
            this.decisionNumber = 21;
            this.eot = DFA21_eot;
            this.eof = DFA21_eof;
            this.min = DFA21_min;
            this.max = DFA21_max;
            this.accept = DFA21_accept;
            this.special = DFA21_special;
            this.transition = DFA21_transition;
        }
        public String getDescription() {
            return "155:4: ( INDENT block ( NEWLINE )? DEDENT ( DOT_END ( WS )+ ( NAME ) )? )?";
        }
        public int specialStateTransition(int s, IntStream _input) throws NoViableAltException {
            TokenStream input = (TokenStream)_input;
        	int _s = s;
            switch ( s ) {
                    case 0 : 
                        int LA21_0 = input.LA(1);

                         
                        int index21_0 = input.index();
                        input.rewind();
                        s = -1;
                        if ( (LA21_0==INDENT) ) {s = 1;}

                        else if ( ((LA21_0>=HEX_PAIR && LA21_0<=HEX_QUAD)||(LA21_0>=TYPED_VALUE && LA21_0<=STRING)||LA21_0==NAME) ) {s = 2;}

                        else if ( (LA21_0==DOT_NAME) && (( input.LT(1).getCharPositionInLine() == 0 || input.LT(-1).getType() == NEWLINE ))) {s = 9;}

                        else if ( (LA21_0==EOF||LA21_0==DEDENT||(LA21_0>=NEWLINE && LA21_0<=WS)) ) {s = 10;}

                         
                        input.seek(index21_0);
                        if ( s>=0 ) return s;
                        break;
                    case 1 : 
                        int LA21_1 = input.LA(1);

                         
                        int index21_1 = input.index();
                        input.rewind();
                        s = -1;
                        if ( (synpred24_pycasmParser()) ) {s = 14;}

                        else if ( (true) ) {s = 10;}

                         
                        input.seek(index21_1);
                        if ( s>=0 ) return s;
                        break;
            }
            if (state.backtracking>0) {state.failed=true; return -1;}
            NoViableAltException nvae =
                new NoViableAltException(getDescription(), 21, _s, input);
            error(nvae);
            throw nvae;
        }
    }
    static final String DFA23_eotS =
        "\4\uffff";
    static final String DFA23_eofS =
        "\2\2\2\uffff";
    static final String DFA23_minS =
        "\1\26\1\11\2\uffff";
    static final String DFA23_maxS =
        "\1\27\1\31\2\uffff";
    static final String DFA23_acceptS =
        "\2\uffff\1\2\1\1";
    static final String DFA23_specialS =
        "\4\uffff}>";
    static final String[] DFA23_transitionS = {
            "\1\2\1\1",
            "\5\3\3\uffff\2\3\2\uffff\1\3\1\2\1\1\1\uffff\1\3",
            "",
            ""
    };

    static final short[] DFA23_eot = DFA.unpackEncodedString(DFA23_eotS);
    static final short[] DFA23_eof = DFA.unpackEncodedString(DFA23_eofS);
    static final char[] DFA23_min = DFA.unpackEncodedStringToUnsignedChars(DFA23_minS);
    static final char[] DFA23_max = DFA.unpackEncodedStringToUnsignedChars(DFA23_maxS);
    static final short[] DFA23_accept = DFA.unpackEncodedString(DFA23_acceptS);
    static final short[] DFA23_special = DFA.unpackEncodedString(DFA23_specialS);
    static final short[][] DFA23_transition;

    static {
        int numStates = DFA23_transitionS.length;
        DFA23_transition = new short[numStates][];
        for (int i=0; i<numStates; i++) {
            DFA23_transition[i] = DFA.unpackEncodedString(DFA23_transitionS[i]);
        }
    }

    class DFA23 extends DFA {

        public DFA23(BaseRecognizer recognizer) {
            this.recognizer = recognizer;
            this.decisionNumber = 23;
            this.eot = DFA23_eot;
            this.eof = DFA23_eof;
            this.min = DFA23_min;
            this.max = DFA23_max;
            this.accept = DFA23_accept;
            this.special = DFA23_special;
            this.transition = DFA23_transition;
        }
        public String getDescription() {
            return "()* loopback of 171:12: ( ( WS )+ directive_args )*";
        }
    }
 

    public static final BitSet FOLLOW_block_in_root73 = new BitSet(new long[]{0x0000000000000000L});
    public static final BitSet FOLLOW_sp_in_root76 = new BitSet(new long[]{0x0000000000C00000L});
    public static final BitSet FOLLOW_EOF_in_root81 = new BitSet(new long[]{0x0000000000000002L});
    public static final BitSet FOLLOW_WS_in_sp105 = new BitSet(new long[]{0x0000000000C00002L});
    public static final BitSet FOLLOW_NEWLINE_in_sp107 = new BitSet(new long[]{0x0000000000C00002L});
    public static final BitSet FOLLOW_element_chain_in_block128 = new BitSet(new long[]{0x0000000000D00022L});
    public static final BitSet FOLLOW_spaced_element_in_block142 = new BitSet(new long[]{0x0000000000F61E22L});
    public static final BitSet FOLLOW_element_chain_in_block145 = new BitSet(new long[]{0x0000000000D00022L});
    public static final BitSet FOLLOW_spaced_element_in_block168 = new BitSet(new long[]{0x0000000000F61E22L});
    public static final BitSet FOLLOW_sp_in_block171 = new BitSet(new long[]{0x0000000000F61E22L});
    public static final BitSet FOLLOW_element_chain_in_block175 = new BitSet(new long[]{0x0000000000D00022L});
    public static final BitSet FOLLOW_chain_element_in_element_chain205 = new BitSet(new long[]{0x0000000000C00002L});
    public static final BitSet FOLLOW_sp_in_element_chain208 = new BitSet(new long[]{0x0000000000E61E00L});
    public static final BitSet FOLLOW_chain_element_in_element_chain211 = new BitSet(new long[]{0x0000000000C00002L});
    public static final BitSet FOLLOW_sym_name_in_chain_element224 = new BitSet(new long[]{0x0000000000000002L});
    public static final BitSet FOLLOW_generative_in_chain_element229 = new BitSet(new long[]{0x0000000000000002L});
    public static final BitSet FOLLOW_hex_code_in_chain_element234 = new BitSet(new long[]{0x0000000000000002L});
    public static final BitSet FOLLOW_directive_in_spaced_element247 = new BitSet(new long[]{0x0000000000000002L});
    public static final BitSet FOLLOW_INDENT_in_spaced_element252 = new BitSet(new long[]{0x0000000000361E20L});
    public static final BitSet FOLLOW_block_in_spaced_element255 = new BitSet(new long[]{0x0000000000400012L});
    public static final BitSet FOLLOW_NEWLINE_in_spaced_element257 = new BitSet(new long[]{0x0000000000000012L});
    public static final BitSet FOLLOW_DEDENT_in_spaced_element260 = new BitSet(new long[]{0x0000000000000002L});
    public static final BitSet FOLLOW_directive_header_in_directive280 = new BitSet(new long[]{0x0000000000000022L});
    public static final BitSet FOLLOW_INDENT_in_directive286 = new BitSet(new long[]{0x0000000000361E20L});
    public static final BitSet FOLLOW_block_in_directive288 = new BitSet(new long[]{0x0000000000400010L});
    public static final BitSet FOLLOW_NEWLINE_in_directive290 = new BitSet(new long[]{0x0000000000000010L});
    public static final BitSet FOLLOW_DEDENT_in_directive293 = new BitSet(new long[]{0x0000000000008002L});
    public static final BitSet FOLLOW_DOT_END_in_directive300 = new BitSet(new long[]{0x0000000000800000L});
    public static final BitSet FOLLOW_WS_in_directive302 = new BitSet(new long[]{0x0000000000A00000L});
    public static final BitSet FOLLOW_NAME_in_directive311 = new BitSet(new long[]{0x0000000000000002L});
    public static final BitSet FOLLOW_DOT_NAME_in_directive_header367 = new BitSet(new long[]{0x0000000000C00000L});
    public static final BitSet FOLLOW_WS_in_directive_header370 = new BitSet(new long[]{0x0000000002A63E00L});
    public static final BitSet FOLLOW_directive_args_in_directive_header373 = new BitSet(new long[]{0x0000000000C00000L});
    public static final BitSet FOLLOW_WS_in_directive_header378 = new BitSet(new long[]{0x0000000000C00000L});
    public static final BitSet FOLLOW_NEWLINE_in_directive_header382 = new BitSet(new long[]{0x0000000000000002L});
    public static final BitSet FOLLOW_EOF_in_directive_header384 = new BitSet(new long[]{0x0000000000000002L});
    public static final BitSet FOLLOW_sym_name_in_directive_args411 = new BitSet(new long[]{0x0000000000000002L});
    public static final BitSet FOLLOW_hex_code_in_directive_args416 = new BitSet(new long[]{0x0000000000000002L});
    public static final BitSet FOLLOW_generative_in_directive_args421 = new BitSet(new long[]{0x0000000000000002L});
    public static final BitSet FOLLOW_HEX_DIGIT_in_directive_args426 = new BitSet(new long[]{0x0000000000000002L});
    public static final BitSet FOLLOW_NON_WS_SEQUENCE_in_directive_args431 = new BitSet(new long[]{0x0000000000000002L});
    public static final BitSet FOLLOW_NAME_in_sym_name445 = new BitSet(new long[]{0x0000000000000002L});
    public static final BitSet FOLLOW_STRING_in_generative471 = new BitSet(new long[]{0x0000000000000002L});
    public static final BitSet FOLLOW_TYPED_VALUE_in_generative478 = new BitSet(new long[]{0x0000000000000002L});
    public static final BitSet FOLLOW_HEX_PAIR_in_hex_code501 = new BitSet(new long[]{0x0000000000000002L});
    public static final BitSet FOLLOW_HEX_QUAD_in_hex_code508 = new BitSet(new long[]{0x0000000000000002L});
    public static final BitSet FOLLOW_HEX_DQUAD_in_hex_code515 = new BitSet(new long[]{0x0000000000000002L});
    public static final BitSet FOLLOW_HEX_EIGHT_in_hex_code522 = new BitSet(new long[]{0x0000000000000002L});
    public static final BitSet FOLLOW_WS_in_synpred4_pycasmParser105 = new BitSet(new long[]{0x0000000000000002L});
    public static final BitSet FOLLOW_NEWLINE_in_synpred5_pycasmParser107 = new BitSet(new long[]{0x0000000000000002L});
    public static final BitSet FOLLOW_spaced_element_in_synpred7_pycasmParser142 = new BitSet(new long[]{0x0000000000000002L});
    public static final BitSet FOLLOW_element_chain_in_synpred8_pycasmParser145 = new BitSet(new long[]{0x0000000000000002L});
    public static final BitSet FOLLOW_spaced_element_in_synpred9_pycasmParser168 = new BitSet(new long[]{0x0000000000000002L});
    public static final BitSet FOLLOW_sp_in_synpred11_pycasmParser171 = new BitSet(new long[]{0x0000000000000002L});
    public static final BitSet FOLLOW_element_chain_in_synpred12_pycasmParser175 = new BitSet(new long[]{0x0000000000000002L});
    public static final BitSet FOLLOW_spaced_element_in_synpred13_pycasmParser168 = new BitSet(new long[]{0x0000000000361E22L});
    public static final BitSet FOLLOW_sp_in_synpred13_pycasmParser171 = new BitSet(new long[]{0x0000000000E61E02L});
    public static final BitSet FOLLOW_element_chain_in_synpred13_pycasmParser175 = new BitSet(new long[]{0x0000000000000002L});
    public static final BitSet FOLLOW_sp_in_synpred15_pycasmParser208 = new BitSet(new long[]{0x0000000000E61E00L});
    public static final BitSet FOLLOW_chain_element_in_synpred15_pycasmParser211 = new BitSet(new long[]{0x0000000000000002L});
    public static final BitSet FOLLOW_directive_in_synpred18_pycasmParser247 = new BitSet(new long[]{0x0000000000000002L});
    public static final BitSet FOLLOW_NEWLINE_in_synpred19_pycasmParser257 = new BitSet(new long[]{0x0000000000000002L});
    public static final BitSet FOLLOW_DEDENT_in_synpred20_pycasmParser260 = new BitSet(new long[]{0x0000000000000002L});
    public static final BitSet FOLLOW_INDENT_in_synpred24_pycasmParser286 = new BitSet(new long[]{0x0000000000361E20L});
    public static final BitSet FOLLOW_block_in_synpred24_pycasmParser288 = new BitSet(new long[]{0x0000000000400010L});
    public static final BitSet FOLLOW_NEWLINE_in_synpred24_pycasmParser290 = new BitSet(new long[]{0x0000000000000010L});
    public static final BitSet FOLLOW_DEDENT_in_synpred24_pycasmParser293 = new BitSet(new long[]{0x0000000000008002L});
    public static final BitSet FOLLOW_DOT_END_in_synpred24_pycasmParser300 = new BitSet(new long[]{0x0000000000800000L});
    public static final BitSet FOLLOW_WS_in_synpred24_pycasmParser302 = new BitSet(new long[]{0x0000000000A00000L});
    public static final BitSet FOLLOW_NAME_in_synpred24_pycasmParser311 = new BitSet(new long[]{0x0000000000000002L});

}