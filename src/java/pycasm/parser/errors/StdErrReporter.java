public class StdErrReporter implements IErrorReporter {
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

	public String getTokenErrorDisplay(Token t) {
		return t.toString();
	}
}
