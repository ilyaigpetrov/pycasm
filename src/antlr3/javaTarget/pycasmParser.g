parser grammar pycasmParser;

options
{
backtrack=true;
output=AST;
memoize=true;
tokenVocab=pycasmLexer;
}

tokens {
ROOT;
HEX;
SYM;
}

@header
{
package pycasm.parser;
import pycasm.sym.*;
import java.util.Arrays;
}

@members
{
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
}

@rulecatch {
catch (RecognitionException re) {
    reportError(re);
    recover(input,re);
}
}

root
	:
		(block| sp+)? EOF
		-> ^(ROOT block?)
	;

sp	:
		(WS|NEWLINE)+ ->
	;

block
	:
		(
		element_chain -> ^(BLOCK element_chain)
		| spaced_element+ element_chain? -> ^(BLOCK spaced_element+ element_chain?)
		)
		((spaced_element+|sp+) element_chain? -> ^($block spaced_element+ element_chain?))*

	;

element_chain
	:
		chain_element (sp+ chain_element)*
	;

chain_element:
		sym_name
	|	generative
	|	hex_code
	;

spaced_element
	:
		directive
	|	INDENT! block NEWLINE? DEDENT!?
	;

directive
	:
		{ input.LT(1).getCharPositionInLine() == 0 || input.LT(-1).getType() == NEWLINE }? => (directive_header
			(INDENT block NEWLINE? DEDENT
				(DOT_END WS+
					(NAME
						{
						String dh = $directive_header.tree.toString().substring(1);
						if (!dh.startsWith($NAME.text))
							reportError(".end directive must have argument of the same name as directive '"+dh+"', compare with '"+$NAME.text+"'.");
						}
					)
				)?
			)?
		)  -> ^({$directive_header.tree} block?)
	;

directive_header
	:	
		DOT_NAME (WS+ directive_args)*  WS* (NEWLINE|EOF) -> ^(DOT_NAME ^(ARGS directive_args*))
	;

directive_args
	:
		sym_name
	|	hex_code
	|	generative
	|	HEX_DIGIT
	|	NON_WS_SEQUENCE // something parseable like 2.5
	;

sym_name
	:
		NAME -> ^(SYM NAME)
	;

generative
	:
	(
		c=STRING
	|	c=TYPED_VALUE
	)	-> ^({adaptor.create(GEN, $c.text)})
	;

hex_code:
	(	h=HEX_PAIR
	|	h=HEX_QUAD
	|	h=HEX_DQUAD
	|	h=HEX_EIGHT
	) -> ^({adaptor.create(HEX, $h.text)})
	;