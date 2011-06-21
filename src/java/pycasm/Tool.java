/*
pycasm tool
pycasm in.file.asm
creates in.file with generated python bc
*/
import java.util.Scanner;
import java.io.*;
import pycasm.parser.*;

import org.antlr.runtime.*;
import org.antlr.runtime.tree.*;

public class Tool {

	public static void main(String[] args) throws Exception {
		String fileName = args[0];
		String fileContent = new Scanner(new File(fileName)).useDelimiter("\\Z").next();
		byte[] bytecode = runPycasm(fileContent);
		String pycFileName;
		if( fileName.endsWith(".asm") ) {
			pycFileName = fileName.substring(0,fileName.length()-4);
		} else {
			pycFileName = fileName+".pyc";
		}
		FileOutputStream out = new FileOutputStream( pycFileName );
		out.write(bytecode);
	}
	
    private static pycasmLexer runLexer(String testString) throws Exception {
		try {
			CharStream stream = new ANTLRStringStream(testString);
			pycasmLexer lexer = new pycasmLexer(stream);
			return lexer;
		} catch(Exception e) {
			System.out.println("Lexer failed on input: "+testString+".");
			throw e;
		}
    }

	private static pycasmParser.root_return chainParser(pycasmLexer lexer) throws Exception  {
		try {
			CommonTokenStream tokens = new CommonTokenStream(lexer);
			pycasmParser parser = new pycasmParser(tokens);
			return parser.root();
		} catch(Exception e) {
			String acc = "";
			Token token;
			lexer.reset();
			while ((token = lexer.nextToken())!=Token.EOF_TOKEN) {
				acc += "<"+ token.getText() +">";
			}
			System.out.println("Parser failed on input: "+acc+".");
			throw e;
		}
	}

	private static pycasmDirectiveWalker.root_return chainDirectiveWalker(pycasmParser.root_return root) throws Exception  {
		return chainDirectiveWalker((Tree)root.getTree());
	}

	private static pycasmDirectiveWalker.root_return chainDirectiveWalker(Tree root) throws Exception  {
		try {
			BufferedTreeNodeStream nodes = new BufferedTreeNodeStream(root);
			pycasmDirectiveWalker walker = new pycasmDirectiveWalker(nodes);
			return walker.root();
		} catch(Exception e) {
			System.out.println("DirectiveWalker failed on input: "+ root.toStringTree()+".");
			throw e;
		}
	}

	private static pycasmSymnameWalker.root_return chainSymnameWalker(pycasmDirectiveWalker.root_return root) throws Exception {
		Tree rootTree = (Tree)root.getTree();
		try {
			BufferedTreeNodeStream nodes = new BufferedTreeNodeStream(rootTree);
			pycasmSymnameWalker walker = new pycasmSymnameWalker(nodes);
			return walker.root();
		} catch(Exception e) {
			System.out.println("SymnameWalker failed on input: "+ rootTree.toStringTree()+".");
			throw e;
		}
	}

	private static pycasmGenerativeWalker.root_return chainGenerativeWalker(pycasmSymnameWalker.root_return root) throws Exception {
		Tree rootTree = (Tree)root.getTree();
		try {
			BufferedTreeNodeStream nodes = new BufferedTreeNodeStream(rootTree);
			pycasmGenerativeWalker walker = new pycasmGenerativeWalker(nodes);
			return walker.root();
		} catch(Exception e) {
			System.out.println("GenerativeWalker failed on input: "+ rootTree.toStringTree()+".");
			throw e;
		}
	}

	private static byte[] chainBytecodeGenerator(pycasmGenerativeWalker.root_return root) throws Exception {
		Tree rootTree = (Tree)root.getTree();
		try {
			BufferedTreeNodeStream nodes = new BufferedTreeNodeStream(rootTree);
			pycasmBytecodeGenerator walker = new pycasmBytecodeGenerator(nodes);
			byte[] bytecode = walker.root();
			return bytecode;
		} catch(Exception e) {
			System.out.println("BytecodeGenerator failed on input: "+ rootTree.toStringTree()+".");
			throw e;
		}		
	}

	private static byte[] runPycasm(String testString) throws Exception {
		return chainBytecodeGenerator(
			chainGenerativeWalker(
				chainSymnameWalker(
					chainDirectiveWalker(chainParser(runLexer(testString)))
				)
			)
		);
	}

	private static void runParser(String testString) throws Exception {
		chainParser(runLexer(testString));
	}

}