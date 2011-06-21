import java.io.*;
import org.antlr.runtime.*;
import org.antlr.runtime.tree.*;
import org.junit.*;
import pycasm.parser.*;
import static org.junit.Assert.*;

public class TestPycasm {

	// Basic common tests.

    @Test
    public void testEmpty() throws Exception {
        runPycasm("");
    }

    @Test
    public void testNewlines() throws Exception {
		runPycasm("\r\n\n\n\r\n");
    }

	// Bytecode generation tests.

    @Test
    public void testHex() throws Exception {
		runPycasm("5f 67");
		runPycasm("2a6f aabb cc");
		runPycasm("01abcdef a0");
    }

    @Test
    public void testQuotedString() throws Exception {
        runPycasm("'generate_me'");
    }

    @Test
    public void testTypedValue() throws Exception {
        runPycasm("s'generate_me' t'another type'");
    }

	// Symnames' tests.

    @Test
    public void testSymnames() throws Exception {
        runParser("this_is_A_SymName");
    }

	// Directives' tests.

    @Test
    public void testOneLinerDirective() throws Exception {
		runParser(".oneLinerDirective 0 1 2");
    }

    @Test
    public void testNoArgsOneLinerDirective() throws Exception {
        runParser(".oneLinerDirective");
    }

    @Test
    public void testFollowedDirective() throws Exception {
        runParser(".stamp now\n'string'");
    }

    @Test
    public void testPythonDirective() throws Exception {
		runPycasm(".python 2.5");
    }
	
    @Test(expected=IllegalArgumentException.class)
    public void testUndefinedPythonDirective() throws Exception {
		runPycasm(".undefinedDirective 2.5");
    }

	// Methods used by tests.

    private pycasmLexer runLexer(String testString) throws Exception {
		try {
			CharStream stream = new ANTLRStringStream(testString);
			pycasmLexer lexer = new pycasmLexer(stream);
			return lexer;
		} catch(Exception e) {
			System.out.println("Lexer failed on input: "+testString+".");
			throw e;
		}
    }

	private pycasmParser.root_return chainParser(pycasmLexer lexer) throws Exception  {
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

	private pycasmDirectiveWalker.root_return chainDirectiveWalker(pycasmParser.root_return root) throws Exception  {
		return chainDirectiveWalker((Tree)root.getTree());
	}

	private pycasmDirectiveWalker.root_return chainDirectiveWalker(Tree root) throws Exception  {
		try {
			BufferedTreeNodeStream nodes = new BufferedTreeNodeStream(root);
			pycasmDirectiveWalker walker = new pycasmDirectiveWalker(nodes);
			return walker.root();
		} catch(Exception e) {
			System.out.println("DirectiveWalker failed on input: "+ root.toStringTree()+".");
			throw e;
		}
	}

	private pycasmSymnameWalker.root_return chainSymnameWalker(pycasmDirectiveWalker.root_return root) throws Exception {
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

	private pycasmGenerativeWalker.root_return chainGenerativeWalker(pycasmSymnameWalker.root_return root) throws Exception {
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

	private void chainBytecodeGenerator(pycasmGenerativeWalker.root_return root) throws Exception {
		Tree rootTree = (Tree)root.getTree();
		try {
			BufferedTreeNodeStream nodes = new BufferedTreeNodeStream(rootTree);
			pycasmBytecodeGenerator walker = new pycasmBytecodeGenerator(nodes);
			walker.root();
		} catch(Exception e) {
			System.out.println("BytecodeGenerator failed on input: "+ rootTree.toStringTree()+".");
			throw e;
		}		
	}
	
	private void runPycasm(String testString) throws Exception {
		chainBytecodeGenerator(
			chainGenerativeWalker(
				chainSymnameWalker(
					chainDirectiveWalker(chainParser(runLexer(testString)))
				)
			)
		)
		;
	}

	private void runParser(String testString) throws Exception {
		chainParser(runLexer(testString));
	}
}