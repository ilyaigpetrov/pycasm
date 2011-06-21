tree grammar pycasmBytecodeGenerator;

options {
tokenVocab=pycasmParser;
ASTLabelType=CommonTree;
}

@header
{
package pycasm.parser;
import java.io.*;
}

@members {
public static byte[] hexStringToByteArray(String s) {
	int len = s.length();
	byte[] data = new byte[len / 2];
	for (int i = 0; i < len; i += 2) {
		data[i / 2] = (byte) ((Character.digit(s.charAt(i), 16) << 4)
							 + Character.digit(s.charAt(i+1), 16));
	}
	return data;
}

StringBuilder result;
FileOutputStream out;
}

@rulecatch {
catch (RecognitionException e) {
	this.reportError(e);
	throw e;
}
}

root returns [byte[\] bytecode]
@init {
	result = new StringBuilder();
}
@after {
	bytecode = hexStringToByteArray(result.toString());
}
	:
		^(ROOT block?)
	;

block
	:
		^(BLOCK block_child+)
	;

block_child
	:
		HEX {result.append( $HEX.text );}
	|	block
	;
