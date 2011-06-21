public interface IErrorReporter {
	void reportError (RecognitionException e);
	void displayRecognitionError (String[] tokenNames, RecognitionException e);
	String getErrorMessage (RecognitionException e, String[] tokenNames);
	String getTokenErrorDisplay(Token t);
}