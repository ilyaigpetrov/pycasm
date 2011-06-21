/*
 * This grammar describes the first pycasm transformation step.
 * 
 * Tree transformation steps:
 *
 * 0) on input we have a pycasm tree: directives, symnames, bcgen, hex code
 * 1) expand directives,
 *        bcgen on demand (for symnames defs, mutable), symnames on demand (for symnames defs, symnames are kept)
 *    result: symnames, partialy sub-d bcgen, hex code
 * 2) expand symnames
 *    result: hex code with bcgen
 * 3) expand bcgen
 *    result: indented `xxd -ps`-like hex
 * 4) expand hex codes
 *    result: compiled bytecode
 *
**/
tree grammar pycasmDirectiveWalker;

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
import pycasm.sym.PycasmRootScope;
}

@members
{
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
		directive
	|	^(SYM NAME)
	|	HEX
	|	GEN
	|	block
	;

directive
	:
		^(DOT_NAME ^(ARGS directive_args*)
			block?
		)
		-> ^({expandDirective($DOT_NAME.getText(), $ARGS.tree, $block.tree)})
		//-> ^(HEX {(CommonTree)adaptor.create(HEX, "b3f20d0a")})
	;

directive_args
	:
		^(SYM NAME)
	|	HEX
	|	GEN
	|	HEX_DIGIT
	|	NON_WS_SEQUENCE // something parseable like 2.5
	;