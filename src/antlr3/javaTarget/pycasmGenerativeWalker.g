tree grammar pycasmGenerativeWalker;

options
{
backtrack=true;
output=AST;
tokenVocab=pycasmParser;
ASTLabelType=CommonTree;
rewrite=true;
}

@header
{
package pycasm.parser;
import java.text.*;
}

@members
{
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
}

// Don't recover from error, report and rethrow.
@rulecatch {
catch (RecognitionException e) {
  this.reportError(e);
  throw e;
}
}

root
	:
		^(ROOT block?)
	;

block
	:
		^(BLOCK block_child+)
	;

block_child
	:
		HEX
	|	GEN -> ^({expandGenerative($GEN)})
	|	block
	;
