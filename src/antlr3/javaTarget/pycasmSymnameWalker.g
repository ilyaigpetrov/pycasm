/*
 * This grammar describes the second pycasm transformation step.
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
tree grammar pycasmSymnameWalker;

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
}

@members
{
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
		^(SYM NAME) -> ^({expandSymname($NAME.text)})
	|	HEX
	|	GEN
	|	block
	;
