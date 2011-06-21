/*
 * This grammar describes pycasm assembler language.
 * Pycasm is, like Python, indent-sensetive.
 *
**/
lexer grammar pycasmLexer;

tokens {
DEDENT;
INDENT;
BLOCK;
ARGS;
GEN;
}

@header
{
package pycasm.parser;
import java.util.ArrayList;
}

@members
{
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

}

@rulecatch {
	System.out.println("wow");
}

HEX_EIGHT
	:
		HEX_PAIR HEX_DQUAD
	;

HEX_DQUAD
	:
		HEX_QUAD HEX_QUAD
	;

HEX_QUAD
	:
		HEX_PAIR HEX_PAIR
	;

HEX_PAIR
	:
		HEX_DIGIT HEX_DIGIT
	;

HEX_DIGIT
	:
		HexDigit
	;

DOT_END
	:		
		'.end'
	;

TYPED_VALUE
	:
		Type '\'' ~('\'')* '\''
	;

STRING
	:	'\'' ~('\'')+ '\''
	;

DOT_NAME
	:
		'.' (Alpha|'_')+
	;

NAME	:
		(Alpha|'_')+
	;

NEWLINE
@init {
int spaces = 0;
}
    :   (
    		( ('\r')? '\n' ) | '\t' | ' ' )*
    		( ('\r')? '\n' )
  leading_space=( ' '  { spaces += 1; }
		| '\t' { spaces += 8; spaces -= (spaces \% 8); }
		)*
        {
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
    ;

WS  :    {getColumn(state) > 0}? => (' '|'\t')+
    ;

COMMENT
@init {
$channel=HIDDEN;
}
    :    {getColumn(state) == 0}? => (' '|'\t')* ';' (~'\n')* '\n'+
    |    {getColumn(state) > 0 }? => ';' (~'\n')*
    ;

NON_WS_SEQUENCE
    :
    	~(' '|'\t'|'\r'|'\n')+
    ;
/*
UNPREDICTED_TOKEN
    :
    	~'\n'	
    ;
*/
// Fragments

fragment
Type	:	
		's'|'t'
	;

fragment
Alpha
	:
		('a'..'z'|'A'..'Z')
	;

fragment
HexAlpha
	:
		('a'..'f'|'A'..'F')
	;

fragment
HexDigit
	:
		(HexAlpha|Digit)
	;

fragment
Digit	:
		'0'..'9'
	;