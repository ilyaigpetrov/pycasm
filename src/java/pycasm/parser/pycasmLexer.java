// $ANTLR 3.1.3 Mar 17, 2009 19:23:44 G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g 2011-05-08 12:08:37

package pycasm.parser;
import java.util.ArrayList;


import org.antlr.runtime.*;
import java.util.Stack;
import java.util.List;
import java.util.ArrayList;

public class pycasmLexer extends Lexer {
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
    public static final int HexDigit=14;
    public static final int INDENT=5;
    public static final int NAME=21;
    public static final int HEX_EIGHT=11;
    public static final int WS=23;
    public static final int NEWLINE=22;
    public static final int BLOCK=6;
    public static final int NON_WS_SEQUENCE=25;
    public static final int ARGS=7;
    public static final int GEN=8;
    public static final int DOT_NAME=20;
    public static final int COMMENT=24;
    public static final int HEX_QUAD=12;
    public static final int HEX_PAIR=9;
    public static final int STRING=18;

    // INDENT-DEDENT generation.
    ArrayList<Integer> IndentStack = new ArrayList<Integer>();
    int spaces = 0;

    int getColumn(RecognizerSharedState st)
    {
    	return st.tokenStartCharPositionInLine;
    }
    // Emit multiple tokens at once.
    List tokens = new ArrayList();
    @Override
    public void emit(Token token) {
    	state.token = token;
    	tokens.add(token);
    }
    @Override
    public Token nextToken() {
    	super.nextToken();
    	if ( tokens.size()==0 ) {
    		return Token.EOF_TOKEN;
    	}
    	return (Token)tokens.remove(0);
    }
    // Throw error, don't recover.
    public void reportError(String message) {
    	throw new IllegalArgumentException(message);
    }
    boolean isDebug = true;
    // Overriden lexers's methods for error decoration.
    public String getErrorMessage(RecognitionException e,
                                  String[] tokenNames) {
        String msg = "";
        String debugMsg = "";
        List stack = getRuleInvocationStack(e, this.getClass().getName());
        if ( e instanceof NoViableAltException ) {
          NoViableAltException nvae = (NoViableAltException)e;
          debugMsg = " no viable alt; token="+e.token+
             " (decision="+nvae.decisionNumber+
             " state "+nvae.stateNumber+")"+
             " decision=<<"+nvae.grammarDecisionDescription+">>";
        }
        else {
          debugMsg = super.getErrorMessage(e, tokenNames);
        }
        debugMsg = stack+" "+debugMsg;

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
    	return "LEXER ERROR: " + h + "\n";
    }
    // Don't recover, report and exit.
    @Override
    public void reportError(RecognitionException e) {
    	super.reportError(e);
    	System.out.println("OVER");
    }



    // delegates
    // delegators

    public pycasmLexer() {;} 
    public pycasmLexer(CharStream input) {
        this(input, new RecognizerSharedState());
    }
    public pycasmLexer(CharStream input, RecognizerSharedState state) {
        super(input,state);

    }
    public String getGrammarFileName() { return "G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g"; }

    // $ANTLR start "HEX_EIGHT"
    public final void mHEX_EIGHT() throws RecognitionException {
        try {
            int _type = HEX_EIGHT;
            int _channel = DEFAULT_TOKEN_CHANNEL;
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:98:2: ( HEX_PAIR HEX_DQUAD )
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:99:3: HEX_PAIR HEX_DQUAD
            {
            mHEX_PAIR(); 
            mHEX_DQUAD(); 

            }

            state.type = _type;
            state.channel = _channel;
        }
        finally {
        }
    }
    // $ANTLR end "HEX_EIGHT"

    // $ANTLR start "HEX_DQUAD"
    public final void mHEX_DQUAD() throws RecognitionException {
        try {
            int _type = HEX_DQUAD;
            int _channel = DEFAULT_TOKEN_CHANNEL;
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:103:2: ( HEX_QUAD HEX_QUAD )
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:104:3: HEX_QUAD HEX_QUAD
            {
            mHEX_QUAD(); 
            mHEX_QUAD(); 

            }

            state.type = _type;
            state.channel = _channel;
        }
        finally {
        }
    }
    // $ANTLR end "HEX_DQUAD"

    // $ANTLR start "HEX_QUAD"
    public final void mHEX_QUAD() throws RecognitionException {
        try {
            int _type = HEX_QUAD;
            int _channel = DEFAULT_TOKEN_CHANNEL;
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:108:2: ( HEX_PAIR HEX_PAIR )
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:109:3: HEX_PAIR HEX_PAIR
            {
            mHEX_PAIR(); 
            mHEX_PAIR(); 

            }

            state.type = _type;
            state.channel = _channel;
        }
        finally {
        }
    }
    // $ANTLR end "HEX_QUAD"

    // $ANTLR start "HEX_PAIR"
    public final void mHEX_PAIR() throws RecognitionException {
        try {
            int _type = HEX_PAIR;
            int _channel = DEFAULT_TOKEN_CHANNEL;
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:113:2: ( HEX_DIGIT HEX_DIGIT )
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:114:3: HEX_DIGIT HEX_DIGIT
            {
            mHEX_DIGIT(); 
            mHEX_DIGIT(); 

            }

            state.type = _type;
            state.channel = _channel;
        }
        finally {
        }
    }
    // $ANTLR end "HEX_PAIR"

    // $ANTLR start "HEX_DIGIT"
    public final void mHEX_DIGIT() throws RecognitionException {
        try {
            int _type = HEX_DIGIT;
            int _channel = DEFAULT_TOKEN_CHANNEL;
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:118:2: ( HexDigit )
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:119:3: HexDigit
            {
            mHexDigit(); 

            }

            state.type = _type;
            state.channel = _channel;
        }
        finally {
        }
    }
    // $ANTLR end "HEX_DIGIT"

    // $ANTLR start "DOT_END"
    public final void mDOT_END() throws RecognitionException {
        try {
            int _type = DOT_END;
            int _channel = DEFAULT_TOKEN_CHANNEL;
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:123:2: ( '.end' )
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:124:3: '.end'
            {
            match(".end"); 


            }

            state.type = _type;
            state.channel = _channel;
        }
        finally {
        }
    }
    // $ANTLR end "DOT_END"

    // $ANTLR start "TYPED_VALUE"
    public final void mTYPED_VALUE() throws RecognitionException {
        try {
            int _type = TYPED_VALUE;
            int _channel = DEFAULT_TOKEN_CHANNEL;
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:128:2: ( Type '\\'' (~ ( '\\'' ) )* '\\'' )
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:129:3: Type '\\'' (~ ( '\\'' ) )* '\\''
            {
            mType(); 
            match('\''); 
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:129:13: (~ ( '\\'' ) )*
            loop1:
            do {
                int alt1=2;
                int LA1_0 = input.LA(1);

                if ( ((LA1_0>='\u0000' && LA1_0<='&')||(LA1_0>='(' && LA1_0<='\uFFFF')) ) {
                    alt1=1;
                }


                switch (alt1) {
            	case 1 :
            	    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:129:13: ~ ( '\\'' )
            	    {
            	    if ( (input.LA(1)>='\u0000' && input.LA(1)<='&')||(input.LA(1)>='(' && input.LA(1)<='\uFFFF') ) {
            	        input.consume();

            	    }
            	    else {
            	        MismatchedSetException mse = new MismatchedSetException(null,input);
            	        recover(mse);
            	        throw mse;}


            	    }
            	    break;

            	default :
            	    break loop1;
                }
            } while (true);

            match('\''); 

            }

            state.type = _type;
            state.channel = _channel;
        }
        finally {
        }
    }
    // $ANTLR end "TYPED_VALUE"

    // $ANTLR start "STRING"
    public final void mSTRING() throws RecognitionException {
        try {
            int _type = STRING;
            int _channel = DEFAULT_TOKEN_CHANNEL;
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:133:2: ( '\\'' (~ ( '\\'' ) )+ '\\'' )
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:133:4: '\\'' (~ ( '\\'' ) )+ '\\''
            {
            match('\''); 
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:133:9: (~ ( '\\'' ) )+
            int cnt2=0;
            loop2:
            do {
                int alt2=2;
                int LA2_0 = input.LA(1);

                if ( ((LA2_0>='\u0000' && LA2_0<='&')||(LA2_0>='(' && LA2_0<='\uFFFF')) ) {
                    alt2=1;
                }


                switch (alt2) {
            	case 1 :
            	    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:133:9: ~ ( '\\'' )
            	    {
            	    if ( (input.LA(1)>='\u0000' && input.LA(1)<='&')||(input.LA(1)>='(' && input.LA(1)<='\uFFFF') ) {
            	        input.consume();

            	    }
            	    else {
            	        MismatchedSetException mse = new MismatchedSetException(null,input);
            	        recover(mse);
            	        throw mse;}


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

            match('\''); 

            }

            state.type = _type;
            state.channel = _channel;
        }
        finally {
        }
    }
    // $ANTLR end "STRING"

    // $ANTLR start "DOT_NAME"
    public final void mDOT_NAME() throws RecognitionException {
        try {
            int _type = DOT_NAME;
            int _channel = DEFAULT_TOKEN_CHANNEL;
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:137:2: ( '.' ( Alpha | '_' )+ )
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:138:3: '.' ( Alpha | '_' )+
            {
            match('.'); 
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:138:7: ( Alpha | '_' )+
            int cnt3=0;
            loop3:
            do {
                int alt3=2;
                int LA3_0 = input.LA(1);

                if ( ((LA3_0>='A' && LA3_0<='Z')||LA3_0=='_'||(LA3_0>='a' && LA3_0<='z')) ) {
                    alt3=1;
                }


                switch (alt3) {
            	case 1 :
            	    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:
            	    {
            	    if ( (input.LA(1)>='A' && input.LA(1)<='Z')||input.LA(1)=='_'||(input.LA(1)>='a' && input.LA(1)<='z') ) {
            	        input.consume();

            	    }
            	    else {
            	        MismatchedSetException mse = new MismatchedSetException(null,input);
            	        recover(mse);
            	        throw mse;}


            	    }
            	    break;

            	default :
            	    if ( cnt3 >= 1 ) break loop3;
                        EarlyExitException eee =
                            new EarlyExitException(3, input);
                        throw eee;
                }
                cnt3++;
            } while (true);


            }

            state.type = _type;
            state.channel = _channel;
        }
        finally {
        }
    }
    // $ANTLR end "DOT_NAME"

    // $ANTLR start "NAME"
    public final void mNAME() throws RecognitionException {
        try {
            int _type = NAME;
            int _channel = DEFAULT_TOKEN_CHANNEL;
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:141:6: ( ( Alpha | '_' )+ )
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:142:3: ( Alpha | '_' )+
            {
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:142:3: ( Alpha | '_' )+
            int cnt4=0;
            loop4:
            do {
                int alt4=2;
                int LA4_0 = input.LA(1);

                if ( ((LA4_0>='A' && LA4_0<='Z')||LA4_0=='_'||(LA4_0>='a' && LA4_0<='z')) ) {
                    alt4=1;
                }


                switch (alt4) {
            	case 1 :
            	    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:
            	    {
            	    if ( (input.LA(1)>='A' && input.LA(1)<='Z')||input.LA(1)=='_'||(input.LA(1)>='a' && input.LA(1)<='z') ) {
            	        input.consume();

            	    }
            	    else {
            	        MismatchedSetException mse = new MismatchedSetException(null,input);
            	        recover(mse);
            	        throw mse;}


            	    }
            	    break;

            	default :
            	    if ( cnt4 >= 1 ) break loop4;
                        EarlyExitException eee =
                            new EarlyExitException(4, input);
                        throw eee;
                }
                cnt4++;
            } while (true);


            }

            state.type = _type;
            state.channel = _channel;
        }
        finally {
        }
    }
    // $ANTLR end "NAME"

    // $ANTLR start "NEWLINE"
    public final void mNEWLINE() throws RecognitionException {
        try {
            int _type = NEWLINE;
            int _channel = DEFAULT_TOKEN_CHANNEL;
            int leading_space;


            int spaces = 0;

            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:149:5: ( ( ( ( '\\r' )? '\\n' ) | '\\t' | ' ' )* ( ( '\\r' )? '\\n' ) (leading_space= ( ' ' | '\\t' ) )* )
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:149:9: ( ( ( '\\r' )? '\\n' ) | '\\t' | ' ' )* ( ( '\\r' )? '\\n' ) (leading_space= ( ' ' | '\\t' ) )*
            {
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:149:9: ( ( ( '\\r' )? '\\n' ) | '\\t' | ' ' )*
            loop6:
            do {
                int alt6=4;
                alt6 = dfa6.predict(input);
                switch (alt6) {
            	case 1 :
            	    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:150:7: ( ( '\\r' )? '\\n' )
            	    {
            	    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:150:7: ( ( '\\r' )? '\\n' )
            	    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:150:9: ( '\\r' )? '\\n'
            	    {
            	    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:150:9: ( '\\r' )?
            	    int alt5=2;
            	    int LA5_0 = input.LA(1);

            	    if ( (LA5_0=='\r') ) {
            	        alt5=1;
            	    }
            	    switch (alt5) {
            	        case 1 :
            	            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:150:10: '\\r'
            	            {
            	            match('\r'); 

            	            }
            	            break;

            	    }

            	    match('\n'); 

            	    }


            	    }
            	    break;
            	case 2 :
            	    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:150:26: '\\t'
            	    {
            	    match('\t'); 

            	    }
            	    break;
            	case 3 :
            	    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:150:33: ' '
            	    {
            	    match(' '); 

            	    }
            	    break;

            	default :
            	    break loop6;
                }
            } while (true);

            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:151:7: ( ( '\\r' )? '\\n' )
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:151:9: ( '\\r' )? '\\n'
            {
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:151:9: ( '\\r' )?
            int alt7=2;
            int LA7_0 = input.LA(1);

            if ( (LA7_0=='\r') ) {
                alt7=1;
            }
            switch (alt7) {
                case 1 :
                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:151:10: '\\r'
                    {
                    match('\r'); 

                    }
                    break;

            }

            match('\n'); 

            }

            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:152:16: (leading_space= ( ' ' | '\\t' ) )*
            loop9:
            do {
                int alt9=2;
                int LA9_0 = input.LA(1);

                if ( (LA9_0=='\t'||LA9_0==' ') ) {
                    alt9=1;
                }


                switch (alt9) {
            	case 1 :
            	    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:152:16: leading_space= ( ' ' | '\\t' )
            	    {
            	    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:152:17: ( ' ' | '\\t' )
            	    int alt8=2;
            	    int LA8_0 = input.LA(1);

            	    if ( (LA8_0==' ') ) {
            	        alt8=1;
            	    }
            	    else if ( (LA8_0=='\t') ) {
            	        alt8=2;
            	    }
            	    else {
            	        NoViableAltException nvae =
            	            new NoViableAltException("", 8, 0, input);

            	        throw nvae;
            	    }
            	    switch (alt8) {
            	        case 1 :
            	            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:152:19: ' '
            	            {
            	            match(' '); 
            	             spaces += 1; 

            	            }
            	            break;
            	        case 2 :
            	            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:153:5: '\\t'
            	            {
            	            match('\t'); 
            	             spaces += 8; spaces -= (spaces % 8); 

            	            }
            	            break;

            	    }


            	    }
            	    break;

            	default :
            	    break loop9;
                }
            } while (true);


            		emit(new ClassicToken(NEWLINE, "\n"));
            		
            		if ( spaces!=0 && (IndentStack.size()==0 || spaces > IndentStack.get(IndentStack.size() - 1)) ) {
            			IndentStack.add(spaces);
            			emit(new ClassicToken(INDENT, ">"));
            		}
            		else {
            			while ( IndentStack.size()!=0 && spaces < IndentStack.get(IndentStack.size() - 1) ) {
            				IndentStack.remove(IndentStack.size() - 1);
            				emit(new ClassicToken(DEDENT, "<"));
            			}
            			int ss = IndentStack.size()!=0 ? IndentStack.get(IndentStack.size() - 1) : 0;
            			if( spaces != ss )
            				reportError("Uneven indent.");
            		}

                    

            }

            state.type = _type;
            state.channel = _channel;
        }
        finally {
        }
    }
    // $ANTLR end "NEWLINE"

    // $ANTLR start "WS"
    public final void mWS() throws RecognitionException {
        try {
            int _type = WS;
            int _channel = DEFAULT_TOKEN_CHANNEL;
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:175:5: ({...}? => ( ' ' | '\\t' )+ )
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:175:10: {...}? => ( ' ' | '\\t' )+
            {
            if ( !((getColumn(state) > 0)) ) {
                throw new FailedPredicateException(input, "WS", "getColumn(state) > 0");
            }
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:175:37: ( ' ' | '\\t' )+
            int cnt10=0;
            loop10:
            do {
                int alt10=2;
                int LA10_0 = input.LA(1);

                if ( (LA10_0=='\t'||LA10_0==' ') ) {
                    alt10=1;
                }


                switch (alt10) {
            	case 1 :
            	    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:
            	    {
            	    if ( input.LA(1)=='\t'||input.LA(1)==' ' ) {
            	        input.consume();

            	    }
            	    else {
            	        MismatchedSetException mse = new MismatchedSetException(null,input);
            	        recover(mse);
            	        throw mse;}


            	    }
            	    break;

            	default :
            	    if ( cnt10 >= 1 ) break loop10;
                        EarlyExitException eee =
                            new EarlyExitException(10, input);
                        throw eee;
                }
                cnt10++;
            } while (true);


            }

            state.type = _type;
            state.channel = _channel;
        }
        finally {
        }
    }
    // $ANTLR end "WS"

    // $ANTLR start "COMMENT"
    public final void mCOMMENT() throws RecognitionException {
        try {
            int _type = COMMENT;
            int _channel = DEFAULT_TOKEN_CHANNEL;

            _channel=HIDDEN;

            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:182:5: ({...}? => ( ' ' | '\\t' )* ';' (~ '\\n' )* ( '\\n' )+ | {...}? => ';' (~ '\\n' )* )
            int alt15=2;
            alt15 = dfa15.predict(input);
            switch (alt15) {
                case 1 :
                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:182:10: {...}? => ( ' ' | '\\t' )* ';' (~ '\\n' )* ( '\\n' )+
                    {
                    if ( !((getColumn(state) == 0)) ) {
                        throw new FailedPredicateException(input, "COMMENT", "getColumn(state) == 0");
                    }
                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:182:38: ( ' ' | '\\t' )*
                    loop11:
                    do {
                        int alt11=2;
                        int LA11_0 = input.LA(1);

                        if ( (LA11_0=='\t'||LA11_0==' ') ) {
                            alt11=1;
                        }


                        switch (alt11) {
                    	case 1 :
                    	    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:
                    	    {
                    	    if ( input.LA(1)=='\t'||input.LA(1)==' ' ) {
                    	        input.consume();

                    	    }
                    	    else {
                    	        MismatchedSetException mse = new MismatchedSetException(null,input);
                    	        recover(mse);
                    	        throw mse;}


                    	    }
                    	    break;

                    	default :
                    	    break loop11;
                        }
                    } while (true);

                    match(';'); 
                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:182:54: (~ '\\n' )*
                    loop12:
                    do {
                        int alt12=2;
                        int LA12_0 = input.LA(1);

                        if ( ((LA12_0>='\u0000' && LA12_0<='\t')||(LA12_0>='\u000B' && LA12_0<='\uFFFF')) ) {
                            alt12=1;
                        }


                        switch (alt12) {
                    	case 1 :
                    	    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:182:55: ~ '\\n'
                    	    {
                    	    if ( (input.LA(1)>='\u0000' && input.LA(1)<='\t')||(input.LA(1)>='\u000B' && input.LA(1)<='\uFFFF') ) {
                    	        input.consume();

                    	    }
                    	    else {
                    	        MismatchedSetException mse = new MismatchedSetException(null,input);
                    	        recover(mse);
                    	        throw mse;}


                    	    }
                    	    break;

                    	default :
                    	    break loop12;
                        }
                    } while (true);

                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:182:63: ( '\\n' )+
                    int cnt13=0;
                    loop13:
                    do {
                        int alt13=2;
                        int LA13_0 = input.LA(1);

                        if ( (LA13_0=='\n') ) {
                            alt13=1;
                        }


                        switch (alt13) {
                    	case 1 :
                    	    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:182:63: '\\n'
                    	    {
                    	    match('\n'); 

                    	    }
                    	    break;

                    	default :
                    	    if ( cnt13 >= 1 ) break loop13;
                                EarlyExitException eee =
                                    new EarlyExitException(13, input);
                                throw eee;
                        }
                        cnt13++;
                    } while (true);


                    }
                    break;
                case 2 :
                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:183:10: {...}? => ';' (~ '\\n' )*
                    {
                    if ( !((getColumn(state) > 0 )) ) {
                        throw new FailedPredicateException(input, "COMMENT", "getColumn(state) > 0 ");
                    }
                    match(';'); 
                    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:183:42: (~ '\\n' )*
                    loop14:
                    do {
                        int alt14=2;
                        int LA14_0 = input.LA(1);

                        if ( ((LA14_0>='\u0000' && LA14_0<='\t')||(LA14_0>='\u000B' && LA14_0<='\uFFFF')) ) {
                            alt14=1;
                        }


                        switch (alt14) {
                    	case 1 :
                    	    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:183:43: ~ '\\n'
                    	    {
                    	    if ( (input.LA(1)>='\u0000' && input.LA(1)<='\t')||(input.LA(1)>='\u000B' && input.LA(1)<='\uFFFF') ) {
                    	        input.consume();

                    	    }
                    	    else {
                    	        MismatchedSetException mse = new MismatchedSetException(null,input);
                    	        recover(mse);
                    	        throw mse;}


                    	    }
                    	    break;

                    	default :
                    	    break loop14;
                        }
                    } while (true);


                    }
                    break;

            }
            state.type = _type;
            state.channel = _channel;
        }
        finally {
        }
    }
    // $ANTLR end "COMMENT"

    // $ANTLR start "NON_WS_SEQUENCE"
    public final void mNON_WS_SEQUENCE() throws RecognitionException {
        try {
            int _type = NON_WS_SEQUENCE;
            int _channel = DEFAULT_TOKEN_CHANNEL;
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:187:5: ( (~ ( ' ' | '\\t' | '\\r' | '\\n' ) )+ )
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:188:6: (~ ( ' ' | '\\t' | '\\r' | '\\n' ) )+
            {
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:188:6: (~ ( ' ' | '\\t' | '\\r' | '\\n' ) )+
            int cnt16=0;
            loop16:
            do {
                int alt16=2;
                int LA16_0 = input.LA(1);

                if ( ((LA16_0>='\u0000' && LA16_0<='\b')||(LA16_0>='\u000B' && LA16_0<='\f')||(LA16_0>='\u000E' && LA16_0<='\u001F')||(LA16_0>='!' && LA16_0<='\uFFFF')) ) {
                    alt16=1;
                }


                switch (alt16) {
            	case 1 :
            	    // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:188:6: ~ ( ' ' | '\\t' | '\\r' | '\\n' )
            	    {
            	    if ( (input.LA(1)>='\u0000' && input.LA(1)<='\b')||(input.LA(1)>='\u000B' && input.LA(1)<='\f')||(input.LA(1)>='\u000E' && input.LA(1)<='\u001F')||(input.LA(1)>='!' && input.LA(1)<='\uFFFF') ) {
            	        input.consume();

            	    }
            	    else {
            	        MismatchedSetException mse = new MismatchedSetException(null,input);
            	        recover(mse);
            	        throw mse;}


            	    }
            	    break;

            	default :
            	    if ( cnt16 >= 1 ) break loop16;
                        EarlyExitException eee =
                            new EarlyExitException(16, input);
                        throw eee;
                }
                cnt16++;
            } while (true);


            }

            state.type = _type;
            state.channel = _channel;
        }
        finally {
        }
    }
    // $ANTLR end "NON_WS_SEQUENCE"

    // $ANTLR start "Type"
    public final void mType() throws RecognitionException {
        try {
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:199:6: ( 's' | 't' )
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:
            {
            if ( (input.LA(1)>='s' && input.LA(1)<='t') ) {
                input.consume();

            }
            else {
                MismatchedSetException mse = new MismatchedSetException(null,input);
                recover(mse);
                throw mse;}


            }

        }
        finally {
        }
    }
    // $ANTLR end "Type"

    // $ANTLR start "Alpha"
    public final void mAlpha() throws RecognitionException {
        try {
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:205:2: ( ( 'a' .. 'z' | 'A' .. 'Z' ) )
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:206:3: ( 'a' .. 'z' | 'A' .. 'Z' )
            {
            if ( (input.LA(1)>='A' && input.LA(1)<='Z')||(input.LA(1)>='a' && input.LA(1)<='z') ) {
                input.consume();

            }
            else {
                MismatchedSetException mse = new MismatchedSetException(null,input);
                recover(mse);
                throw mse;}


            }

        }
        finally {
        }
    }
    // $ANTLR end "Alpha"

    // $ANTLR start "HexAlpha"
    public final void mHexAlpha() throws RecognitionException {
        try {
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:211:2: ( ( 'a' .. 'f' | 'A' .. 'F' ) )
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:212:3: ( 'a' .. 'f' | 'A' .. 'F' )
            {
            if ( (input.LA(1)>='A' && input.LA(1)<='F')||(input.LA(1)>='a' && input.LA(1)<='f') ) {
                input.consume();

            }
            else {
                MismatchedSetException mse = new MismatchedSetException(null,input);
                recover(mse);
                throw mse;}


            }

        }
        finally {
        }
    }
    // $ANTLR end "HexAlpha"

    // $ANTLR start "HexDigit"
    public final void mHexDigit() throws RecognitionException {
        try {
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:217:2: ( ( HexAlpha | Digit ) )
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:218:3: ( HexAlpha | Digit )
            {
            if ( (input.LA(1)>='0' && input.LA(1)<='9')||(input.LA(1)>='A' && input.LA(1)<='F')||(input.LA(1)>='a' && input.LA(1)<='f') ) {
                input.consume();

            }
            else {
                MismatchedSetException mse = new MismatchedSetException(null,input);
                recover(mse);
                throw mse;}


            }

        }
        finally {
        }
    }
    // $ANTLR end "HexDigit"

    // $ANTLR start "Digit"
    public final void mDigit() throws RecognitionException {
        try {
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:222:7: ( '0' .. '9' )
            // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:223:3: '0' .. '9'
            {
            matchRange('0','9'); 

            }

        }
        finally {
        }
    }
    // $ANTLR end "Digit"

    public void mTokens() throws RecognitionException {
        // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:1:8: ( HEX_EIGHT | HEX_DQUAD | HEX_QUAD | HEX_PAIR | HEX_DIGIT | DOT_END | TYPED_VALUE | STRING | DOT_NAME | NAME | NEWLINE | WS | COMMENT | NON_WS_SEQUENCE )
        int alt17=14;
        alt17 = dfa17.predict(input);
        switch (alt17) {
            case 1 :
                // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:1:10: HEX_EIGHT
                {
                mHEX_EIGHT(); 

                }
                break;
            case 2 :
                // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:1:20: HEX_DQUAD
                {
                mHEX_DQUAD(); 

                }
                break;
            case 3 :
                // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:1:30: HEX_QUAD
                {
                mHEX_QUAD(); 

                }
                break;
            case 4 :
                // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:1:39: HEX_PAIR
                {
                mHEX_PAIR(); 

                }
                break;
            case 5 :
                // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:1:48: HEX_DIGIT
                {
                mHEX_DIGIT(); 

                }
                break;
            case 6 :
                // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:1:58: DOT_END
                {
                mDOT_END(); 

                }
                break;
            case 7 :
                // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:1:66: TYPED_VALUE
                {
                mTYPED_VALUE(); 

                }
                break;
            case 8 :
                // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:1:78: STRING
                {
                mSTRING(); 

                }
                break;
            case 9 :
                // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:1:85: DOT_NAME
                {
                mDOT_NAME(); 

                }
                break;
            case 10 :
                // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:1:94: NAME
                {
                mNAME(); 

                }
                break;
            case 11 :
                // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:1:99: NEWLINE
                {
                mNEWLINE(); 

                }
                break;
            case 12 :
                // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:1:107: WS
                {
                mWS(); 

                }
                break;
            case 13 :
                // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:1:110: COMMENT
                {
                mCOMMENT(); 

                }
                break;
            case 14 :
                // G:\\Storage\\workspace\\unpyc\\pycasm_first_release\\\\src\\antlr3\\javaTarget\\pycasmLexer.g:1:118: NON_WS_SEQUENCE
                {
                mNON_WS_SEQUENCE(); 

                }
                break;

        }

    }


    protected DFA6 dfa6 = new DFA6(this);
    protected DFA15 dfa15 = new DFA15(this);
    protected DFA17 dfa17 = new DFA17(this);
    static final String DFA6_eotS =
        "\2\uffff\1\7\2\uffff\2\7\2\uffff";
    static final String DFA6_eofS =
        "\11\uffff";
    static final String DFA6_minS =
        "\1\11\1\12\1\11\2\uffff\2\11\2\uffff";
    static final String DFA6_maxS =
        "\1\40\1\12\1\40\2\uffff\2\40\2\uffff";
    static final String DFA6_acceptS =
        "\3\uffff\1\2\1\3\2\uffff\1\4\1\1";
    static final String DFA6_specialS =
        "\11\uffff}>";
    static final String[] DFA6_transitionS = {
            "\1\3\1\2\2\uffff\1\1\22\uffff\1\4",
            "\1\2",
            "\1\6\1\10\2\uffff\1\10\22\uffff\1\5",
            "",
            "",
            "\1\6\1\10\2\uffff\1\10\22\uffff\1\5",
            "\1\6\1\10\2\uffff\1\10\22\uffff\1\5",
            "",
            ""
    };

    static final short[] DFA6_eot = DFA.unpackEncodedString(DFA6_eotS);
    static final short[] DFA6_eof = DFA.unpackEncodedString(DFA6_eofS);
    static final char[] DFA6_min = DFA.unpackEncodedStringToUnsignedChars(DFA6_minS);
    static final char[] DFA6_max = DFA.unpackEncodedStringToUnsignedChars(DFA6_maxS);
    static final short[] DFA6_accept = DFA.unpackEncodedString(DFA6_acceptS);
    static final short[] DFA6_special = DFA.unpackEncodedString(DFA6_specialS);
    static final short[][] DFA6_transition;

    static {
        int numStates = DFA6_transitionS.length;
        DFA6_transition = new short[numStates][];
        for (int i=0; i<numStates; i++) {
            DFA6_transition[i] = DFA.unpackEncodedString(DFA6_transitionS[i]);
        }
    }

    class DFA6 extends DFA {

        public DFA6(BaseRecognizer recognizer) {
            this.recognizer = recognizer;
            this.decisionNumber = 6;
            this.eot = DFA6_eot;
            this.eof = DFA6_eof;
            this.min = DFA6_min;
            this.max = DFA6_max;
            this.accept = DFA6_accept;
            this.special = DFA6_special;
            this.transition = DFA6_transition;
        }
        public String getDescription() {
            return "()* loopback of 149:9: ( ( ( '\\r' )? '\\n' ) | '\\t' | ' ' )*";
        }
    }
    static final String DFA15_eotS =
        "\2\uffff\2\4\1\uffff";
    static final String DFA15_eofS =
        "\5\uffff";
    static final String DFA15_minS =
        "\1\11\1\uffff\2\0\1\uffff";
    static final String DFA15_maxS =
        "\1\73\1\uffff\2\uffff\1\uffff";
    static final String DFA15_acceptS =
        "\1\uffff\1\1\2\uffff\1\2";
    static final String DFA15_specialS =
        "\1\0\1\uffff\1\1\1\2\1\uffff}>";
    static final String[] DFA15_transitionS = {
            "\1\1\26\uffff\1\1\32\uffff\1\2",
            "",
            "\12\3\1\1\ufff5\3",
            "\12\3\1\1\ufff5\3",
            ""
    };

    static final short[] DFA15_eot = DFA.unpackEncodedString(DFA15_eotS);
    static final short[] DFA15_eof = DFA.unpackEncodedString(DFA15_eofS);
    static final char[] DFA15_min = DFA.unpackEncodedStringToUnsignedChars(DFA15_minS);
    static final char[] DFA15_max = DFA.unpackEncodedStringToUnsignedChars(DFA15_maxS);
    static final short[] DFA15_accept = DFA.unpackEncodedString(DFA15_acceptS);
    static final short[] DFA15_special = DFA.unpackEncodedString(DFA15_specialS);
    static final short[][] DFA15_transition;

    static {
        int numStates = DFA15_transitionS.length;
        DFA15_transition = new short[numStates][];
        for (int i=0; i<numStates; i++) {
            DFA15_transition[i] = DFA.unpackEncodedString(DFA15_transitionS[i]);
        }
    }

    class DFA15 extends DFA {

        public DFA15(BaseRecognizer recognizer) {
            this.recognizer = recognizer;
            this.decisionNumber = 15;
            this.eot = DFA15_eot;
            this.eof = DFA15_eof;
            this.min = DFA15_min;
            this.max = DFA15_max;
            this.accept = DFA15_accept;
            this.special = DFA15_special;
            this.transition = DFA15_transition;
        }
        public String getDescription() {
            return "178:1: COMMENT : ({...}? => ( ' ' | '\\t' )* ';' (~ '\\n' )* ( '\\n' )+ | {...}? => ';' (~ '\\n' )* );";
        }
        public int specialStateTransition(int s, IntStream _input) throws NoViableAltException {
            IntStream input = _input;
        	int _s = s;
            switch ( s ) {
                    case 0 : 
                        int LA15_0 = input.LA(1);

                         
                        int index15_0 = input.index();
                        input.rewind();
                        s = -1;
                        if ( (LA15_0=='\t'||LA15_0==' ') && ((getColumn(state) == 0))) {s = 1;}

                        else if ( (LA15_0==';') && (((getColumn(state) > 0 )||(getColumn(state) == 0)))) {s = 2;}

                         
                        input.seek(index15_0);
                        if ( s>=0 ) return s;
                        break;
                    case 1 : 
                        int LA15_2 = input.LA(1);

                         
                        int index15_2 = input.index();
                        input.rewind();
                        s = -1;
                        if ( ((LA15_2>='\u0000' && LA15_2<='\t')||(LA15_2>='\u000B' && LA15_2<='\uFFFF')) && (((getColumn(state) > 0 )||(getColumn(state) == 0)))) {s = 3;}

                        else if ( (LA15_2=='\n') && ((getColumn(state) == 0))) {s = 1;}

                        else s = 4;

                         
                        input.seek(index15_2);
                        if ( s>=0 ) return s;
                        break;
                    case 2 : 
                        int LA15_3 = input.LA(1);

                         
                        int index15_3 = input.index();
                        input.rewind();
                        s = -1;
                        if ( (LA15_3=='\n') && ((getColumn(state) == 0))) {s = 1;}

                        else if ( ((LA15_3>='\u0000' && LA15_3<='\t')||(LA15_3>='\u000B' && LA15_3<='\uFFFF')) && (((getColumn(state) > 0 )||(getColumn(state) == 0)))) {s = 3;}

                        else s = 4;

                         
                        input.seek(index15_3);
                        if ( s>=0 ) return s;
                        break;
            }
            NoViableAltException nvae =
                new NoViableAltException(getDescription(), 15, _s, input);
            error(nvae);
            throw nvae;
        }
    }
    static final String DFA17_eotS =
        "\1\uffff\1\14\1\13\1\21\1\13\1\14\1\21\1\uffff\2\26\1\27\2\uffff"+
        "\2\33\2\37\1\uffff\2\13\4\uffff\1\27\3\uffff\1\21\1\13\1\37\1\uffff"+
        "\1\13\1\42\1\uffff\1\24\2\47\1\52\1\uffff\1\21\1\13\1\uffff\1\21"+
        "\1\13\1\21\1\13\2\61\1\uffff\1\21\1\13\2\66\1\uffff";
    static final String DFA17_eofS =
        "\67\uffff";
    static final String DFA17_minS =
        "\2\0\1\101\4\0\1\uffff\2\11\1\0\2\uffff\4\0\1\uffff\2\0\3\uffff"+
        "\2\0\3\uffff\1\0\1\60\1\0\1\uffff\2\0\1\uffff\4\0\1\uffff\1\0\1"+
        "\60\1\uffff\1\0\1\60\1\0\1\60\2\0\1\uffff\1\0\1\60\2\0\1\uffff";
    static final String DFA17_maxS =
        "\2\uffff\1\172\4\uffff\1\uffff\2\73\1\uffff\2\uffff\4\uffff\1\uffff"+
        "\2\uffff\3\uffff\1\0\1\uffff\3\uffff\1\uffff\1\146\1\uffff\1\uffff"+
        "\2\uffff\1\uffff\4\uffff\1\uffff\1\uffff\1\146\1\uffff\1\uffff\1"+
        "\146\1\uffff\1\146\2\uffff\1\uffff\1\uffff\1\146\2\uffff\1\uffff";
    static final String DFA17_acceptS =
        "\7\uffff\1\13\3\uffff\1\16\1\5\4\uffff\1\12\2\uffff\1\10\1\15\1"+
        "\14\2\uffff\2\15\1\4\3\uffff\1\11\2\uffff\1\7\4\uffff\1\3\2\uffff"+
        "\1\6\6\uffff\1\2\4\uffff\1\1";
    static final String DFA17_specialS =
        "\1\2\1\0\1\uffff\1\40\1\6\1\4\1\11\1\uffff\1\15\1\14\1\36\2\uffff"+
        "\1\31\1\23\1\5\1\34\1\uffff\1\13\1\10\3\uffff\1\37\1\24\3\uffff"+
        "\1\7\1\uffff\1\1\1\uffff\1\25\1\32\1\uffff\1\3\1\16\1\30\1\20\1"+
        "\uffff\1\26\2\uffff\1\33\1\uffff\1\27\1\uffff\1\22\1\35\1\uffff"+
        "\1\21\1\uffff\1\17\1\12\1\uffff}>";
    static final String[] DFA17_transitionS = {
            "\11\13\1\10\1\7\2\13\1\7\22\13\1\11\6\13\1\4\6\13\1\2\1\13"+
            "\12\5\1\13\1\12\5\13\6\1\24\6\4\13\1\6\1\13\6\1\14\6\2\3\6\6"+
            "\uff85\13",
            "\11\13\2\uffff\2\13\1\uffff\22\13\1\uffff\17\13\12\16\7\13"+
            "\6\15\24\6\4\13\1\6\1\13\6\15\24\6\uff85\13",
            "\32\20\4\uffff\1\20\1\uffff\4\20\1\17\25\20",
            "\11\13\2\uffff\2\13\1\uffff\22\13\1\uffff\6\13\1\22\31\13"+
            "\32\6\4\13\1\6\1\13\32\6\uff85\13",
            "\11\23\2\24\2\23\1\24\22\23\1\24\6\23\1\uffff\uffd8\23",
            "\11\13\2\uffff\2\13\1\uffff\22\13\1\uffff\17\13\12\16\7\13"+
            "\6\16\32\13\6\16\uff99\13",
            "\11\13\2\uffff\2\13\1\uffff\22\13\1\uffff\40\13\32\6\4\13"+
            "\1\6\1\13\32\6\uff85\13",
            "",
            "\1\10\1\7\2\uffff\1\7\22\uffff\1\11\32\uffff\1\25",
            "\1\10\1\7\2\uffff\1\7\22\uffff\1\11\32\uffff\1\25",
            "\11\30\1\31\1\32\2\30\1\31\22\30\1\31\uffdf\30",
            "",
            "",
            "\11\13\2\uffff\2\13\1\uffff\22\13\1\uffff\17\13\12\35\7\13"+
            "\6\34\24\6\4\13\1\6\1\13\6\34\24\6\uff85\13",
            "\11\13\2\uffff\2\13\1\uffff\22\13\1\uffff\17\13\12\35\7\13"+
            "\6\35\32\13\6\35\uff99\13",
            "\11\13\2\uffff\2\13\1\uffff\22\13\1\uffff\40\13\32\20\4\13"+
            "\1\20\1\13\15\20\1\36\14\20\uff85\13",
            "\11\13\2\uffff\2\13\1\uffff\22\13\1\uffff\40\13\32\20\4\13"+
            "\1\20\1\13\32\20\uff85\13",
            "",
            "\11\40\2\42\2\40\1\42\22\40\1\42\6\40\1\41\uffd8\40",
            "\11\23\2\24\2\23\1\24\22\23\1\24\6\23\1\43\uffd8\23",
            "",
            "",
            "",
            "\1\uffff",
            "\11\30\1\31\1\32\2\30\1\31\22\30\1\31\uffdf\30",
            "",
            "",
            "",
            "\11\13\2\uffff\2\13\1\uffff\22\13\1\uffff\17\13\12\45\7\13"+
            "\6\44\24\6\4\13\1\6\1\13\6\44\24\6\uff85\13",
            "\12\45\7\uffff\6\45\32\uffff\6\45",
            "\11\13\2\uffff\2\13\1\uffff\22\13\1\uffff\40\13\32\20\4\13"+
            "\1\20\1\13\3\20\1\46\26\20\uff85\13",
            "",
            "\11\40\2\42\2\40\1\42\22\40\1\42\6\40\1\41\uffd8\40",
            "\11\13\2\uffff\2\13\1\uffff\22\13\1\uffff\uffdf\13",
            "",
            "\11\13\2\uffff\2\13\1\uffff\22\13\1\uffff\uffdf\13",
            "\11\13\2\uffff\2\13\1\uffff\22\13\1\uffff\17\13\12\51\7\13"+
            "\6\50\24\6\4\13\1\6\1\13\6\50\24\6\uff85\13",
            "\11\13\2\uffff\2\13\1\uffff\22\13\1\uffff\17\13\12\51\7\13"+
            "\6\51\32\13\6\51\uff99\13",
            "\11\13\2\uffff\2\13\1\uffff\22\13\1\uffff\40\13\32\20\4\13"+
            "\1\20\1\13\32\20\uff85\13",
            "",
            "\11\13\2\uffff\2\13\1\uffff\22\13\1\uffff\17\13\12\54\7\13"+
            "\6\53\24\6\4\13\1\6\1\13\6\53\24\6\uff85\13",
            "\12\54\7\uffff\6\54\32\uffff\6\54",
            "",
            "\11\13\2\uffff\2\13\1\uffff\22\13\1\uffff\17\13\12\56\7\13"+
            "\6\55\24\6\4\13\1\6\1\13\6\55\24\6\uff85\13",
            "\12\56\7\uffff\6\56\32\uffff\6\56",
            "\11\13\2\uffff\2\13\1\uffff\22\13\1\uffff\17\13\12\60\7\13"+
            "\6\57\24\6\4\13\1\6\1\13\6\57\24\6\uff85\13",
            "\12\60\7\uffff\6\60\32\uffff\6\60",
            "\11\13\2\uffff\2\13\1\uffff\22\13\1\uffff\17\13\12\63\7\13"+
            "\6\62\24\6\4\13\1\6\1\13\6\62\24\6\uff85\13",
            "\11\13\2\uffff\2\13\1\uffff\22\13\1\uffff\17\13\12\63\7\13"+
            "\6\63\32\13\6\63\uff99\13",
            "",
            "\11\13\2\uffff\2\13\1\uffff\22\13\1\uffff\17\13\12\65\7\13"+
            "\6\64\24\6\4\13\1\6\1\13\6\64\24\6\uff85\13",
            "\12\65\7\uffff\6\65\32\uffff\6\65",
            "\11\13\2\uffff\2\13\1\uffff\22\13\1\uffff\40\13\32\6\4\13"+
            "\1\6\1\13\32\6\uff85\13",
            "\11\13\2\uffff\2\13\1\uffff\22\13\1\uffff\uffdf\13",
            ""
    };

    static final short[] DFA17_eot = DFA.unpackEncodedString(DFA17_eotS);
    static final short[] DFA17_eof = DFA.unpackEncodedString(DFA17_eofS);
    static final char[] DFA17_min = DFA.unpackEncodedStringToUnsignedChars(DFA17_minS);
    static final char[] DFA17_max = DFA.unpackEncodedStringToUnsignedChars(DFA17_maxS);
    static final short[] DFA17_accept = DFA.unpackEncodedString(DFA17_acceptS);
    static final short[] DFA17_special = DFA.unpackEncodedString(DFA17_specialS);
    static final short[][] DFA17_transition;

    static {
        int numStates = DFA17_transitionS.length;
        DFA17_transition = new short[numStates][];
        for (int i=0; i<numStates; i++) {
            DFA17_transition[i] = DFA.unpackEncodedString(DFA17_transitionS[i]);
        }
    }

    class DFA17 extends DFA {

        public DFA17(BaseRecognizer recognizer) {
            this.recognizer = recognizer;
            this.decisionNumber = 17;
            this.eot = DFA17_eot;
            this.eof = DFA17_eof;
            this.min = DFA17_min;
            this.max = DFA17_max;
            this.accept = DFA17_accept;
            this.special = DFA17_special;
            this.transition = DFA17_transition;
        }
        public String getDescription() {
            return "1:1: Tokens : ( HEX_EIGHT | HEX_DQUAD | HEX_QUAD | HEX_PAIR | HEX_DIGIT | DOT_END | TYPED_VALUE | STRING | DOT_NAME | NAME | NEWLINE | WS | COMMENT | NON_WS_SEQUENCE );";
        }
        public int specialStateTransition(int s, IntStream _input) throws NoViableAltException {
            IntStream input = _input;
        	int _s = s;
            switch ( s ) {
                    case 0 : 
                        int LA17_1 = input.LA(1);

                        s = -1;
                        if ( ((LA17_1>='A' && LA17_1<='F')||(LA17_1>='a' && LA17_1<='f')) ) {s = 13;}

                        else if ( ((LA17_1>='G' && LA17_1<='Z')||LA17_1=='_'||(LA17_1>='g' && LA17_1<='z')) ) {s = 6;}

                        else if ( ((LA17_1>='0' && LA17_1<='9')) ) {s = 14;}

                        else if ( ((LA17_1>='\u0000' && LA17_1<='\b')||(LA17_1>='\u000B' && LA17_1<='\f')||(LA17_1>='\u000E' && LA17_1<='\u001F')||(LA17_1>='!' && LA17_1<='/')||(LA17_1>=':' && LA17_1<='@')||(LA17_1>='[' && LA17_1<='^')||LA17_1=='`'||(LA17_1>='{' && LA17_1<='\uFFFF')) ) {s = 11;}

                        else s = 12;

                        if ( s>=0 ) return s;
                        break;
                    case 1 : 
                        int LA17_30 = input.LA(1);

                        s = -1;
                        if ( (LA17_30=='d') ) {s = 38;}

                        else if ( ((LA17_30>='A' && LA17_30<='Z')||LA17_30=='_'||(LA17_30>='a' && LA17_30<='c')||(LA17_30>='e' && LA17_30<='z')) ) {s = 16;}

                        else if ( ((LA17_30>='\u0000' && LA17_30<='\b')||(LA17_30>='\u000B' && LA17_30<='\f')||(LA17_30>='\u000E' && LA17_30<='\u001F')||(LA17_30>='!' && LA17_30<='@')||(LA17_30>='[' && LA17_30<='^')||LA17_30=='`'||(LA17_30>='{' && LA17_30<='\uFFFF')) ) {s = 11;}

                        else s = 31;

                        if ( s>=0 ) return s;
                        break;
                    case 2 : 
                        int LA17_0 = input.LA(1);

                        s = -1;
                        if ( ((LA17_0>='A' && LA17_0<='F')||(LA17_0>='a' && LA17_0<='f')) ) {s = 1;}

                        else if ( (LA17_0=='.') ) {s = 2;}

                        else if ( ((LA17_0>='s' && LA17_0<='t')) ) {s = 3;}

                        else if ( (LA17_0=='\'') ) {s = 4;}

                        else if ( ((LA17_0>='0' && LA17_0<='9')) ) {s = 5;}

                        else if ( ((LA17_0>='G' && LA17_0<='Z')||LA17_0=='_'||(LA17_0>='g' && LA17_0<='r')||(LA17_0>='u' && LA17_0<='z')) ) {s = 6;}

                        else if ( (LA17_0=='\n'||LA17_0=='\r') ) {s = 7;}

                        else if ( (LA17_0=='\t') ) {s = 8;}

                        else if ( (LA17_0==' ') ) {s = 9;}

                        else if ( (LA17_0==';') ) {s = 10;}

                        else if ( ((LA17_0>='\u0000' && LA17_0<='\b')||(LA17_0>='\u000B' && LA17_0<='\f')||(LA17_0>='\u000E' && LA17_0<='\u001F')||(LA17_0>='!' && LA17_0<='&')||(LA17_0>='(' && LA17_0<='-')||LA17_0=='/'||LA17_0==':'||(LA17_0>='<' && LA17_0<='@')||(LA17_0>='[' && LA17_0<='^')||LA17_0=='`'||(LA17_0>='{' && LA17_0<='\uFFFF')) ) {s = 11;}

                        if ( s>=0 ) return s;
                        break;
                    case 3 : 
                        int LA17_35 = input.LA(1);

                        s = -1;
                        if ( ((LA17_35>='\u0000' && LA17_35<='\b')||(LA17_35>='\u000B' && LA17_35<='\f')||(LA17_35>='\u000E' && LA17_35<='\u001F')||(LA17_35>='!' && LA17_35<='\uFFFF')) ) {s = 11;}

                        else s = 20;

                        if ( s>=0 ) return s;
                        break;
                    case 4 : 
                        int LA17_5 = input.LA(1);

                        s = -1;
                        if ( ((LA17_5>='0' && LA17_5<='9')||(LA17_5>='A' && LA17_5<='F')||(LA17_5>='a' && LA17_5<='f')) ) {s = 14;}

                        else if ( ((LA17_5>='\u0000' && LA17_5<='\b')||(LA17_5>='\u000B' && LA17_5<='\f')||(LA17_5>='\u000E' && LA17_5<='\u001F')||(LA17_5>='!' && LA17_5<='/')||(LA17_5>=':' && LA17_5<='@')||(LA17_5>='G' && LA17_5<='`')||(LA17_5>='g' && LA17_5<='\uFFFF')) ) {s = 11;}

                        else s = 12;

                        if ( s>=0 ) return s;
                        break;
                    case 5 : 
                        int LA17_15 = input.LA(1);

                        s = -1;
                        if ( (LA17_15=='n') ) {s = 30;}

                        else if ( ((LA17_15>='A' && LA17_15<='Z')||LA17_15=='_'||(LA17_15>='a' && LA17_15<='m')||(LA17_15>='o' && LA17_15<='z')) ) {s = 16;}

                        else if ( ((LA17_15>='\u0000' && LA17_15<='\b')||(LA17_15>='\u000B' && LA17_15<='\f')||(LA17_15>='\u000E' && LA17_15<='\u001F')||(LA17_15>='!' && LA17_15<='@')||(LA17_15>='[' && LA17_15<='^')||LA17_15=='`'||(LA17_15>='{' && LA17_15<='\uFFFF')) ) {s = 11;}

                        else s = 31;

                        if ( s>=0 ) return s;
                        break;
                    case 6 : 
                        int LA17_4 = input.LA(1);

                        s = -1;
                        if ( ((LA17_4>='\u0000' && LA17_4<='\b')||(LA17_4>='\u000B' && LA17_4<='\f')||(LA17_4>='\u000E' && LA17_4<='\u001F')||(LA17_4>='!' && LA17_4<='&')||(LA17_4>='(' && LA17_4<='\uFFFF')) ) {s = 19;}

                        else if ( ((LA17_4>='\t' && LA17_4<='\n')||LA17_4=='\r'||LA17_4==' ') ) {s = 20;}

                        else s = 11;

                        if ( s>=0 ) return s;
                        break;
                    case 7 : 
                        int LA17_28 = input.LA(1);

                        s = -1;
                        if ( ((LA17_28>='A' && LA17_28<='F')||(LA17_28>='a' && LA17_28<='f')) ) {s = 36;}

                        else if ( ((LA17_28>='G' && LA17_28<='Z')||LA17_28=='_'||(LA17_28>='g' && LA17_28<='z')) ) {s = 6;}

                        else if ( ((LA17_28>='0' && LA17_28<='9')) ) {s = 37;}

                        else if ( ((LA17_28>='\u0000' && LA17_28<='\b')||(LA17_28>='\u000B' && LA17_28<='\f')||(LA17_28>='\u000E' && LA17_28<='\u001F')||(LA17_28>='!' && LA17_28<='/')||(LA17_28>=':' && LA17_28<='@')||(LA17_28>='[' && LA17_28<='^')||LA17_28=='`'||(LA17_28>='{' && LA17_28<='\uFFFF')) ) {s = 11;}

                        else s = 17;

                        if ( s>=0 ) return s;
                        break;
                    case 8 : 
                        int LA17_19 = input.LA(1);

                        s = -1;
                        if ( (LA17_19=='\'') ) {s = 35;}

                        else if ( ((LA17_19>='\u0000' && LA17_19<='\b')||(LA17_19>='\u000B' && LA17_19<='\f')||(LA17_19>='\u000E' && LA17_19<='\u001F')||(LA17_19>='!' && LA17_19<='&')||(LA17_19>='(' && LA17_19<='\uFFFF')) ) {s = 19;}

                        else if ( ((LA17_19>='\t' && LA17_19<='\n')||LA17_19=='\r'||LA17_19==' ') ) {s = 20;}

                        else s = 11;

                        if ( s>=0 ) return s;
                        break;
                    case 9 : 
                        int LA17_6 = input.LA(1);

                        s = -1;
                        if ( ((LA17_6>='A' && LA17_6<='Z')||LA17_6=='_'||(LA17_6>='a' && LA17_6<='z')) ) {s = 6;}

                        else if ( ((LA17_6>='\u0000' && LA17_6<='\b')||(LA17_6>='\u000B' && LA17_6<='\f')||(LA17_6>='\u000E' && LA17_6<='\u001F')||(LA17_6>='!' && LA17_6<='@')||(LA17_6>='[' && LA17_6<='^')||LA17_6=='`'||(LA17_6>='{' && LA17_6<='\uFFFF')) ) {s = 11;}

                        else s = 17;

                        if ( s>=0 ) return s;
                        break;
                    case 10 : 
                        int LA17_53 = input.LA(1);

                        s = -1;
                        if ( ((LA17_53>='\u0000' && LA17_53<='\b')||(LA17_53>='\u000B' && LA17_53<='\f')||(LA17_53>='\u000E' && LA17_53<='\u001F')||(LA17_53>='!' && LA17_53<='\uFFFF')) ) {s = 11;}

                        else s = 54;

                        if ( s>=0 ) return s;
                        break;
                    case 11 : 
                        int LA17_18 = input.LA(1);

                        s = -1;
                        if ( ((LA17_18>='\u0000' && LA17_18<='\b')||(LA17_18>='\u000B' && LA17_18<='\f')||(LA17_18>='\u000E' && LA17_18<='\u001F')||(LA17_18>='!' && LA17_18<='&')||(LA17_18>='(' && LA17_18<='\uFFFF')) ) {s = 32;}

                        else if ( (LA17_18=='\'') ) {s = 33;}

                        else if ( ((LA17_18>='\t' && LA17_18<='\n')||LA17_18=='\r'||LA17_18==' ') ) {s = 34;}

                        else s = 11;

                        if ( s>=0 ) return s;
                        break;
                    case 12 : 
                        int LA17_9 = input.LA(1);

                         
                        int index17_9 = input.index();
                        input.rewind();
                        s = -1;
                        if ( (LA17_9==';') && ((getColumn(state) == 0))) {s = 21;}

                        else if ( (LA17_9=='\t') ) {s = 8;}

                        else if ( (LA17_9=='\n'||LA17_9=='\r') ) {s = 7;}

                        else if ( (LA17_9==' ') ) {s = 9;}

                        else s = 22;

                         
                        input.seek(index17_9);
                        if ( s>=0 ) return s;
                        break;
                    case 13 : 
                        int LA17_8 = input.LA(1);

                         
                        int index17_8 = input.index();
                        input.rewind();
                        s = -1;
                        if ( (LA17_8==';') && ((getColumn(state) == 0))) {s = 21;}

                        else if ( (LA17_8=='\t') ) {s = 8;}

                        else if ( (LA17_8=='\n'||LA17_8=='\r') ) {s = 7;}

                        else if ( (LA17_8==' ') ) {s = 9;}

                        else s = 22;

                         
                        input.seek(index17_8);
                        if ( s>=0 ) return s;
                        break;
                    case 14 : 
                        int LA17_36 = input.LA(1);

                        s = -1;
                        if ( ((LA17_36>='A' && LA17_36<='F')||(LA17_36>='a' && LA17_36<='f')) ) {s = 40;}

                        else if ( ((LA17_36>='G' && LA17_36<='Z')||LA17_36=='_'||(LA17_36>='g' && LA17_36<='z')) ) {s = 6;}

                        else if ( ((LA17_36>='0' && LA17_36<='9')) ) {s = 41;}

                        else if ( ((LA17_36>='\u0000' && LA17_36<='\b')||(LA17_36>='\u000B' && LA17_36<='\f')||(LA17_36>='\u000E' && LA17_36<='\u001F')||(LA17_36>='!' && LA17_36<='/')||(LA17_36>=':' && LA17_36<='@')||(LA17_36>='[' && LA17_36<='^')||LA17_36=='`'||(LA17_36>='{' && LA17_36<='\uFFFF')) ) {s = 11;}

                        else s = 39;

                        if ( s>=0 ) return s;
                        break;
                    case 15 : 
                        int LA17_52 = input.LA(1);

                        s = -1;
                        if ( ((LA17_52>='A' && LA17_52<='Z')||LA17_52=='_'||(LA17_52>='a' && LA17_52<='z')) ) {s = 6;}

                        else if ( ((LA17_52>='\u0000' && LA17_52<='\b')||(LA17_52>='\u000B' && LA17_52<='\f')||(LA17_52>='\u000E' && LA17_52<='\u001F')||(LA17_52>='!' && LA17_52<='@')||(LA17_52>='[' && LA17_52<='^')||LA17_52=='`'||(LA17_52>='{' && LA17_52<='\uFFFF')) ) {s = 11;}

                        else s = 54;

                        if ( s>=0 ) return s;
                        break;
                    case 16 : 
                        int LA17_38 = input.LA(1);

                        s = -1;
                        if ( ((LA17_38>='A' && LA17_38<='Z')||LA17_38=='_'||(LA17_38>='a' && LA17_38<='z')) ) {s = 16;}

                        else if ( ((LA17_38>='\u0000' && LA17_38<='\b')||(LA17_38>='\u000B' && LA17_38<='\f')||(LA17_38>='\u000E' && LA17_38<='\u001F')||(LA17_38>='!' && LA17_38<='@')||(LA17_38>='[' && LA17_38<='^')||LA17_38=='`'||(LA17_38>='{' && LA17_38<='\uFFFF')) ) {s = 11;}

                        else s = 42;

                        if ( s>=0 ) return s;
                        break;
                    case 17 : 
                        int LA17_50 = input.LA(1);

                        s = -1;
                        if ( ((LA17_50>='A' && LA17_50<='F')||(LA17_50>='a' && LA17_50<='f')) ) {s = 52;}

                        else if ( ((LA17_50>='G' && LA17_50<='Z')||LA17_50=='_'||(LA17_50>='g' && LA17_50<='z')) ) {s = 6;}

                        else if ( ((LA17_50>='0' && LA17_50<='9')) ) {s = 53;}

                        else if ( ((LA17_50>='\u0000' && LA17_50<='\b')||(LA17_50>='\u000B' && LA17_50<='\f')||(LA17_50>='\u000E' && LA17_50<='\u001F')||(LA17_50>='!' && LA17_50<='/')||(LA17_50>=':' && LA17_50<='@')||(LA17_50>='[' && LA17_50<='^')||LA17_50=='`'||(LA17_50>='{' && LA17_50<='\uFFFF')) ) {s = 11;}

                        else s = 17;

                        if ( s>=0 ) return s;
                        break;
                    case 18 : 
                        int LA17_47 = input.LA(1);

                        s = -1;
                        if ( ((LA17_47>='A' && LA17_47<='F')||(LA17_47>='a' && LA17_47<='f')) ) {s = 50;}

                        else if ( ((LA17_47>='G' && LA17_47<='Z')||LA17_47=='_'||(LA17_47>='g' && LA17_47<='z')) ) {s = 6;}

                        else if ( ((LA17_47>='0' && LA17_47<='9')) ) {s = 51;}

                        else if ( ((LA17_47>='\u0000' && LA17_47<='\b')||(LA17_47>='\u000B' && LA17_47<='\f')||(LA17_47>='\u000E' && LA17_47<='\u001F')||(LA17_47>='!' && LA17_47<='/')||(LA17_47>=':' && LA17_47<='@')||(LA17_47>='[' && LA17_47<='^')||LA17_47=='`'||(LA17_47>='{' && LA17_47<='\uFFFF')) ) {s = 11;}

                        else s = 49;

                        if ( s>=0 ) return s;
                        break;
                    case 19 : 
                        int LA17_14 = input.LA(1);

                        s = -1;
                        if ( ((LA17_14>='0' && LA17_14<='9')||(LA17_14>='A' && LA17_14<='F')||(LA17_14>='a' && LA17_14<='f')) ) {s = 29;}

                        else if ( ((LA17_14>='\u0000' && LA17_14<='\b')||(LA17_14>='\u000B' && LA17_14<='\f')||(LA17_14>='\u000E' && LA17_14<='\u001F')||(LA17_14>='!' && LA17_14<='/')||(LA17_14>=':' && LA17_14<='@')||(LA17_14>='G' && LA17_14<='`')||(LA17_14>='g' && LA17_14<='\uFFFF')) ) {s = 11;}

                        else s = 27;

                        if ( s>=0 ) return s;
                        break;
                    case 20 : 
                        int LA17_24 = input.LA(1);

                         
                        int index17_24 = input.index();
                        input.rewind();
                        s = -1;
                        if ( (LA17_24=='\n') && ((getColumn(state) == 0))) {s = 26;}

                        else if ( ((LA17_24>='\u0000' && LA17_24<='\b')||(LA17_24>='\u000B' && LA17_24<='\f')||(LA17_24>='\u000E' && LA17_24<='\u001F')||(LA17_24>='!' && LA17_24<='\uFFFF')) ) {s = 24;}

                        else if ( (LA17_24=='\t'||LA17_24=='\r'||LA17_24==' ') && (((getColumn(state) > 0 )||(getColumn(state) == 0)))) {s = 25;}

                        else s = 23;

                         
                        input.seek(index17_24);
                        if ( s>=0 ) return s;
                        break;
                    case 21 : 
                        int LA17_32 = input.LA(1);

                        s = -1;
                        if ( (LA17_32=='\'') ) {s = 33;}

                        else if ( ((LA17_32>='\u0000' && LA17_32<='\b')||(LA17_32>='\u000B' && LA17_32<='\f')||(LA17_32>='\u000E' && LA17_32<='\u001F')||(LA17_32>='!' && LA17_32<='&')||(LA17_32>='(' && LA17_32<='\uFFFF')) ) {s = 32;}

                        else if ( ((LA17_32>='\t' && LA17_32<='\n')||LA17_32=='\r'||LA17_32==' ') ) {s = 34;}

                        else s = 11;

                        if ( s>=0 ) return s;
                        break;
                    case 22 : 
                        int LA17_40 = input.LA(1);

                        s = -1;
                        if ( ((LA17_40>='A' && LA17_40<='F')||(LA17_40>='a' && LA17_40<='f')) ) {s = 43;}

                        else if ( ((LA17_40>='G' && LA17_40<='Z')||LA17_40=='_'||(LA17_40>='g' && LA17_40<='z')) ) {s = 6;}

                        else if ( ((LA17_40>='0' && LA17_40<='9')) ) {s = 44;}

                        else if ( ((LA17_40>='\u0000' && LA17_40<='\b')||(LA17_40>='\u000B' && LA17_40<='\f')||(LA17_40>='\u000E' && LA17_40<='\u001F')||(LA17_40>='!' && LA17_40<='/')||(LA17_40>=':' && LA17_40<='@')||(LA17_40>='[' && LA17_40<='^')||LA17_40=='`'||(LA17_40>='{' && LA17_40<='\uFFFF')) ) {s = 11;}

                        else s = 17;

                        if ( s>=0 ) return s;
                        break;
                    case 23 : 
                        int LA17_45 = input.LA(1);

                        s = -1;
                        if ( ((LA17_45>='A' && LA17_45<='F')||(LA17_45>='a' && LA17_45<='f')) ) {s = 47;}

                        else if ( ((LA17_45>='G' && LA17_45<='Z')||LA17_45=='_'||(LA17_45>='g' && LA17_45<='z')) ) {s = 6;}

                        else if ( ((LA17_45>='0' && LA17_45<='9')) ) {s = 48;}

                        else if ( ((LA17_45>='\u0000' && LA17_45<='\b')||(LA17_45>='\u000B' && LA17_45<='\f')||(LA17_45>='\u000E' && LA17_45<='\u001F')||(LA17_45>='!' && LA17_45<='/')||(LA17_45>=':' && LA17_45<='@')||(LA17_45>='[' && LA17_45<='^')||LA17_45=='`'||(LA17_45>='{' && LA17_45<='\uFFFF')) ) {s = 11;}

                        else s = 17;

                        if ( s>=0 ) return s;
                        break;
                    case 24 : 
                        int LA17_37 = input.LA(1);

                        s = -1;
                        if ( ((LA17_37>='0' && LA17_37<='9')||(LA17_37>='A' && LA17_37<='F')||(LA17_37>='a' && LA17_37<='f')) ) {s = 41;}

                        else if ( ((LA17_37>='\u0000' && LA17_37<='\b')||(LA17_37>='\u000B' && LA17_37<='\f')||(LA17_37>='\u000E' && LA17_37<='\u001F')||(LA17_37>='!' && LA17_37<='/')||(LA17_37>=':' && LA17_37<='@')||(LA17_37>='G' && LA17_37<='`')||(LA17_37>='g' && LA17_37<='\uFFFF')) ) {s = 11;}

                        else s = 39;

                        if ( s>=0 ) return s;
                        break;
                    case 25 : 
                        int LA17_13 = input.LA(1);

                        s = -1;
                        if ( ((LA17_13>='A' && LA17_13<='F')||(LA17_13>='a' && LA17_13<='f')) ) {s = 28;}

                        else if ( ((LA17_13>='G' && LA17_13<='Z')||LA17_13=='_'||(LA17_13>='g' && LA17_13<='z')) ) {s = 6;}

                        else if ( ((LA17_13>='0' && LA17_13<='9')) ) {s = 29;}

                        else if ( ((LA17_13>='\u0000' && LA17_13<='\b')||(LA17_13>='\u000B' && LA17_13<='\f')||(LA17_13>='\u000E' && LA17_13<='\u001F')||(LA17_13>='!' && LA17_13<='/')||(LA17_13>=':' && LA17_13<='@')||(LA17_13>='[' && LA17_13<='^')||LA17_13=='`'||(LA17_13>='{' && LA17_13<='\uFFFF')) ) {s = 11;}

                        else s = 27;

                        if ( s>=0 ) return s;
                        break;
                    case 26 : 
                        int LA17_33 = input.LA(1);

                        s = -1;
                        if ( ((LA17_33>='\u0000' && LA17_33<='\b')||(LA17_33>='\u000B' && LA17_33<='\f')||(LA17_33>='\u000E' && LA17_33<='\u001F')||(LA17_33>='!' && LA17_33<='\uFFFF')) ) {s = 11;}

                        else s = 34;

                        if ( s>=0 ) return s;
                        break;
                    case 27 : 
                        int LA17_43 = input.LA(1);

                        s = -1;
                        if ( ((LA17_43>='A' && LA17_43<='F')||(LA17_43>='a' && LA17_43<='f')) ) {s = 45;}

                        else if ( ((LA17_43>='G' && LA17_43<='Z')||LA17_43=='_'||(LA17_43>='g' && LA17_43<='z')) ) {s = 6;}

                        else if ( ((LA17_43>='0' && LA17_43<='9')) ) {s = 46;}

                        else if ( ((LA17_43>='\u0000' && LA17_43<='\b')||(LA17_43>='\u000B' && LA17_43<='\f')||(LA17_43>='\u000E' && LA17_43<='\u001F')||(LA17_43>='!' && LA17_43<='/')||(LA17_43>=':' && LA17_43<='@')||(LA17_43>='[' && LA17_43<='^')||LA17_43=='`'||(LA17_43>='{' && LA17_43<='\uFFFF')) ) {s = 11;}

                        else s = 17;

                        if ( s>=0 ) return s;
                        break;
                    case 28 : 
                        int LA17_16 = input.LA(1);

                        s = -1;
                        if ( ((LA17_16>='A' && LA17_16<='Z')||LA17_16=='_'||(LA17_16>='a' && LA17_16<='z')) ) {s = 16;}

                        else if ( ((LA17_16>='\u0000' && LA17_16<='\b')||(LA17_16>='\u000B' && LA17_16<='\f')||(LA17_16>='\u000E' && LA17_16<='\u001F')||(LA17_16>='!' && LA17_16<='@')||(LA17_16>='[' && LA17_16<='^')||LA17_16=='`'||(LA17_16>='{' && LA17_16<='\uFFFF')) ) {s = 11;}

                        else s = 31;

                        if ( s>=0 ) return s;
                        break;
                    case 29 : 
                        int LA17_48 = input.LA(1);

                        s = -1;
                        if ( ((LA17_48>='0' && LA17_48<='9')||(LA17_48>='A' && LA17_48<='F')||(LA17_48>='a' && LA17_48<='f')) ) {s = 51;}

                        else if ( ((LA17_48>='\u0000' && LA17_48<='\b')||(LA17_48>='\u000B' && LA17_48<='\f')||(LA17_48>='\u000E' && LA17_48<='\u001F')||(LA17_48>='!' && LA17_48<='/')||(LA17_48>=':' && LA17_48<='@')||(LA17_48>='G' && LA17_48<='`')||(LA17_48>='g' && LA17_48<='\uFFFF')) ) {s = 11;}

                        else s = 49;

                        if ( s>=0 ) return s;
                        break;
                    case 30 : 
                        int LA17_10 = input.LA(1);

                         
                        int index17_10 = input.index();
                        input.rewind();
                        s = -1;
                        if ( ((LA17_10>='\u0000' && LA17_10<='\b')||(LA17_10>='\u000B' && LA17_10<='\f')||(LA17_10>='\u000E' && LA17_10<='\u001F')||(LA17_10>='!' && LA17_10<='\uFFFF')) ) {s = 24;}

                        else if ( (LA17_10=='\t'||LA17_10=='\r'||LA17_10==' ') && (((getColumn(state) > 0 )||(getColumn(state) == 0)))) {s = 25;}

                        else if ( (LA17_10=='\n') && ((getColumn(state) == 0))) {s = 26;}

                        else s = 23;

                         
                        input.seek(index17_10);
                        if ( s>=0 ) return s;
                        break;
                    case 31 : 
                        int LA17_23 = input.LA(1);

                         
                        int index17_23 = input.index();
                        input.rewind();
                        s = -1;
                        if ( ((getColumn(state) > 0 )) ) {s = 26;}

                        else if ( (true) ) {s = 11;}

                         
                        input.seek(index17_23);
                        if ( s>=0 ) return s;
                        break;
                    case 32 : 
                        int LA17_3 = input.LA(1);

                        s = -1;
                        if ( (LA17_3=='\'') ) {s = 18;}

                        else if ( ((LA17_3>='A' && LA17_3<='Z')||LA17_3=='_'||(LA17_3>='a' && LA17_3<='z')) ) {s = 6;}

                        else if ( ((LA17_3>='\u0000' && LA17_3<='\b')||(LA17_3>='\u000B' && LA17_3<='\f')||(LA17_3>='\u000E' && LA17_3<='\u001F')||(LA17_3>='!' && LA17_3<='&')||(LA17_3>='(' && LA17_3<='@')||(LA17_3>='[' && LA17_3<='^')||LA17_3=='`'||(LA17_3>='{' && LA17_3<='\uFFFF')) ) {s = 11;}

                        else s = 17;

                        if ( s>=0 ) return s;
                        break;
            }
            NoViableAltException nvae =
                new NoViableAltException(getDescription(), 17, _s, input);
            error(nvae);
            throw nvae;
        }
    }
 

}