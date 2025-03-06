// Generated from /home/ldg/tmp/antlr/example/dsl_match/MyDSLLexer.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class MyDSLLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		MATCH=1, UNDERSCORE=2, EQUAL=3, ARROW=4, LPAREN=5, RPAREN=6, LBRACE=7, 
		RBRACE=8, COMMA=9, SEMICOLON=10, PLUS=11, MINUS=12, MUL=13, DIV=14, ID=15, 
		FLOAT=16, NUMBER=17, WS=18;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"MATCH", "UNDERSCORE", "EQUAL", "ARROW", "LPAREN", "RPAREN", "LBRACE", 
			"RBRACE", "COMMA", "SEMICOLON", "PLUS", "MINUS", "MUL", "DIV", "ID", 
			"FLOAT", "NUMBER", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'match'", "'_'", "'='", "'=>'", "'('", "')'", "'{'", "'}'", "','", 
			"';'", "'+'", "'-'", "'*'", "'/'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "MATCH", "UNDERSCORE", "EQUAL", "ARROW", "LPAREN", "RPAREN", "LBRACE", 
			"RBRACE", "COMMA", "SEMICOLON", "PLUS", "MINUS", "MUL", "DIV", "ID", 
			"FLOAT", "NUMBER", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public MyDSLLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "MyDSLLexer.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\u0012n\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002"+
		"\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0006\u0001"+
		"\u0006\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\t\u0001\t\u0001\n"+
		"\u0001\n\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001\r\u0001\r\u0001"+
		"\u000e\u0001\u000e\u0005\u000eI\b\u000e\n\u000e\f\u000eL\t\u000e\u0001"+
		"\u000f\u0004\u000fO\b\u000f\u000b\u000f\f\u000fP\u0001\u000f\u0001\u000f"+
		"\u0004\u000fU\b\u000f\u000b\u000f\f\u000fV\u0001\u0010\u0001\u0010\u0001"+
		"\u0010\u0001\u0010\u0004\u0010]\b\u0010\u000b\u0010\f\u0010^\u0001\u0010"+
		"\u0004\u0010b\b\u0010\u000b\u0010\f\u0010c\u0003\u0010f\b\u0010\u0001"+
		"\u0011\u0004\u0011i\b\u0011\u000b\u0011\f\u0011j\u0001\u0011\u0001\u0011"+
		"\u0000\u0000\u0012\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005"+
		"\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019"+
		"\r\u001b\u000e\u001d\u000f\u001f\u0010!\u0011#\u0012\u0001\u0000\u0005"+
		"\u0003\u0000AZ__az\u0004\u000009AZ__az\u0001\u000009\u0003\u000009AFa"+
		"f\u0003\u0000\t\n\r\r  t\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003"+
		"\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007"+
		"\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001"+
		"\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000"+
		"\u0000\u0000\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000"+
		"\u0000\u0000\u0000\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000"+
		"\u0000\u0000\u0000\u0019\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000"+
		"\u0000\u0000\u0000\u001d\u0001\u0000\u0000\u0000\u0000\u001f\u0001\u0000"+
		"\u0000\u0000\u0000!\u0001\u0000\u0000\u0000\u0000#\u0001\u0000\u0000\u0000"+
		"\u0001%\u0001\u0000\u0000\u0000\u0003+\u0001\u0000\u0000\u0000\u0005-"+
		"\u0001\u0000\u0000\u0000\u0007/\u0001\u0000\u0000\u0000\t2\u0001\u0000"+
		"\u0000\u0000\u000b4\u0001\u0000\u0000\u0000\r6\u0001\u0000\u0000\u0000"+
		"\u000f8\u0001\u0000\u0000\u0000\u0011:\u0001\u0000\u0000\u0000\u0013<"+
		"\u0001\u0000\u0000\u0000\u0015>\u0001\u0000\u0000\u0000\u0017@\u0001\u0000"+
		"\u0000\u0000\u0019B\u0001\u0000\u0000\u0000\u001bD\u0001\u0000\u0000\u0000"+
		"\u001dF\u0001\u0000\u0000\u0000\u001fN\u0001\u0000\u0000\u0000!e\u0001"+
		"\u0000\u0000\u0000#h\u0001\u0000\u0000\u0000%&\u0005m\u0000\u0000&\'\u0005"+
		"a\u0000\u0000\'(\u0005t\u0000\u0000()\u0005c\u0000\u0000)*\u0005h\u0000"+
		"\u0000*\u0002\u0001\u0000\u0000\u0000+,\u0005_\u0000\u0000,\u0004\u0001"+
		"\u0000\u0000\u0000-.\u0005=\u0000\u0000.\u0006\u0001\u0000\u0000\u0000"+
		"/0\u0005=\u0000\u000001\u0005>\u0000\u00001\b\u0001\u0000\u0000\u0000"+
		"23\u0005(\u0000\u00003\n\u0001\u0000\u0000\u000045\u0005)\u0000\u0000"+
		"5\f\u0001\u0000\u0000\u000067\u0005{\u0000\u00007\u000e\u0001\u0000\u0000"+
		"\u000089\u0005}\u0000\u00009\u0010\u0001\u0000\u0000\u0000:;\u0005,\u0000"+
		"\u0000;\u0012\u0001\u0000\u0000\u0000<=\u0005;\u0000\u0000=\u0014\u0001"+
		"\u0000\u0000\u0000>?\u0005+\u0000\u0000?\u0016\u0001\u0000\u0000\u0000"+
		"@A\u0005-\u0000\u0000A\u0018\u0001\u0000\u0000\u0000BC\u0005*\u0000\u0000"+
		"C\u001a\u0001\u0000\u0000\u0000DE\u0005/\u0000\u0000E\u001c\u0001\u0000"+
		"\u0000\u0000FJ\u0007\u0000\u0000\u0000GI\u0007\u0001\u0000\u0000HG\u0001"+
		"\u0000\u0000\u0000IL\u0001\u0000\u0000\u0000JH\u0001\u0000\u0000\u0000"+
		"JK\u0001\u0000\u0000\u0000K\u001e\u0001\u0000\u0000\u0000LJ\u0001\u0000"+
		"\u0000\u0000MO\u0007\u0002\u0000\u0000NM\u0001\u0000\u0000\u0000OP\u0001"+
		"\u0000\u0000\u0000PN\u0001\u0000\u0000\u0000PQ\u0001\u0000\u0000\u0000"+
		"QR\u0001\u0000\u0000\u0000RT\u0005.\u0000\u0000SU\u0007\u0002\u0000\u0000"+
		"TS\u0001\u0000\u0000\u0000UV\u0001\u0000\u0000\u0000VT\u0001\u0000\u0000"+
		"\u0000VW\u0001\u0000\u0000\u0000W \u0001\u0000\u0000\u0000XY\u00050\u0000"+
		"\u0000YZ\u0005x\u0000\u0000Z\\\u0001\u0000\u0000\u0000[]\u0007\u0003\u0000"+
		"\u0000\\[\u0001\u0000\u0000\u0000]^\u0001\u0000\u0000\u0000^\\\u0001\u0000"+
		"\u0000\u0000^_\u0001\u0000\u0000\u0000_f\u0001\u0000\u0000\u0000`b\u0007"+
		"\u0002\u0000\u0000a`\u0001\u0000\u0000\u0000bc\u0001\u0000\u0000\u0000"+
		"ca\u0001\u0000\u0000\u0000cd\u0001\u0000\u0000\u0000df\u0001\u0000\u0000"+
		"\u0000eX\u0001\u0000\u0000\u0000ea\u0001\u0000\u0000\u0000f\"\u0001\u0000"+
		"\u0000\u0000gi\u0007\u0004\u0000\u0000hg\u0001\u0000\u0000\u0000ij\u0001"+
		"\u0000\u0000\u0000jh\u0001\u0000\u0000\u0000jk\u0001\u0000\u0000\u0000"+
		"kl\u0001\u0000\u0000\u0000lm\u0006\u0011\u0000\u0000m$\u0001\u0000\u0000"+
		"\u0000\b\u0000JPV^cej\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}