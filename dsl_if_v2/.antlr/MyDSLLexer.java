// Generated from /home/ldg/tmp/antlr/example/dsl_if_v2/MyDSLLexer.g4 by ANTLR 4.13.1
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
		LET=1, IF=2, ELSE=3, PRINT=4, ID=5, NUMBER=6, STRING=7, WS=8, EQUAL=9, 
		SEMICOLON=10, LPAREN=11, RPAREN=12, LBRACE=13, RBRACE=14, OP=15, COMPARE=16;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"LET", "IF", "ELSE", "PRINT", "ID", "NUMBER", "STRING", "WS", "EQUAL", 
			"SEMICOLON", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "OP", "COMPARE"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'let'", "'if'", "'else'", "'print'", null, null, null, null, "'='", 
			"';'", "'('", "')'", "'{'", "'}'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "LET", "IF", "ELSE", "PRINT", "ID", "NUMBER", "STRING", "WS", "EQUAL", 
			"SEMICOLON", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "OP", "COMPARE"
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
		"\u0004\u0000\u0010h\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002"+
		"\u000f\u0007\u000f\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0005\u00046\b\u0004\n\u0004"+
		"\f\u00049\t\u0004\u0001\u0005\u0004\u0005<\b\u0005\u000b\u0005\f\u0005"+
		"=\u0001\u0006\u0001\u0006\u0005\u0006B\b\u0006\n\u0006\f\u0006E\t\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0007\u0004\u0007J\b\u0007\u000b\u0007"+
		"\f\u0007K\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\t\u0001\t\u0001"+
		"\n\u0001\n\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001\r\u0001\r\u0001"+
		"\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001"+
		"\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0003\u000fg\b"+
		"\u000f\u0000\u0000\u0010\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004"+
		"\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017"+
		"\f\u0019\r\u001b\u000e\u001d\u000f\u001f\u0010\u0001\u0000\u0007\u0003"+
		"\u0000AZ__az\u0004\u000009AZ__az\u0001\u000009\u0001\u0000\"\"\u0003\u0000"+
		"\t\n\r\r  \u0003\u0000*+--//\u0002\u0000<<>>o\u0000\u0001\u0001\u0000"+
		"\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000"+
		"\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000"+
		"\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000"+
		"\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000\u0000"+
		"\u0000\u0013\u0001\u0000\u0000\u0000\u0000\u0015\u0001\u0000\u0000\u0000"+
		"\u0000\u0017\u0001\u0000\u0000\u0000\u0000\u0019\u0001\u0000\u0000\u0000"+
		"\u0000\u001b\u0001\u0000\u0000\u0000\u0000\u001d\u0001\u0000\u0000\u0000"+
		"\u0000\u001f\u0001\u0000\u0000\u0000\u0001!\u0001\u0000\u0000\u0000\u0003"+
		"%\u0001\u0000\u0000\u0000\u0005(\u0001\u0000\u0000\u0000\u0007-\u0001"+
		"\u0000\u0000\u0000\t3\u0001\u0000\u0000\u0000\u000b;\u0001\u0000\u0000"+
		"\u0000\r?\u0001\u0000\u0000\u0000\u000fI\u0001\u0000\u0000\u0000\u0011"+
		"O\u0001\u0000\u0000\u0000\u0013Q\u0001\u0000\u0000\u0000\u0015S\u0001"+
		"\u0000\u0000\u0000\u0017U\u0001\u0000\u0000\u0000\u0019W\u0001\u0000\u0000"+
		"\u0000\u001bY\u0001\u0000\u0000\u0000\u001d[\u0001\u0000\u0000\u0000\u001f"+
		"f\u0001\u0000\u0000\u0000!\"\u0005l\u0000\u0000\"#\u0005e\u0000\u0000"+
		"#$\u0005t\u0000\u0000$\u0002\u0001\u0000\u0000\u0000%&\u0005i\u0000\u0000"+
		"&\'\u0005f\u0000\u0000\'\u0004\u0001\u0000\u0000\u0000()\u0005e\u0000"+
		"\u0000)*\u0005l\u0000\u0000*+\u0005s\u0000\u0000+,\u0005e\u0000\u0000"+
		",\u0006\u0001\u0000\u0000\u0000-.\u0005p\u0000\u0000./\u0005r\u0000\u0000"+
		"/0\u0005i\u0000\u000001\u0005n\u0000\u000012\u0005t\u0000\u00002\b\u0001"+
		"\u0000\u0000\u000037\u0007\u0000\u0000\u000046\u0007\u0001\u0000\u0000"+
		"54\u0001\u0000\u0000\u000069\u0001\u0000\u0000\u000075\u0001\u0000\u0000"+
		"\u000078\u0001\u0000\u0000\u00008\n\u0001\u0000\u0000\u000097\u0001\u0000"+
		"\u0000\u0000:<\u0007\u0002\u0000\u0000;:\u0001\u0000\u0000\u0000<=\u0001"+
		"\u0000\u0000\u0000=;\u0001\u0000\u0000\u0000=>\u0001\u0000\u0000\u0000"+
		">\f\u0001\u0000\u0000\u0000?C\u0005\"\u0000\u0000@B\b\u0003\u0000\u0000"+
		"A@\u0001\u0000\u0000\u0000BE\u0001\u0000\u0000\u0000CA\u0001\u0000\u0000"+
		"\u0000CD\u0001\u0000\u0000\u0000DF\u0001\u0000\u0000\u0000EC\u0001\u0000"+
		"\u0000\u0000FG\u0005\"\u0000\u0000G\u000e\u0001\u0000\u0000\u0000HJ\u0007"+
		"\u0004\u0000\u0000IH\u0001\u0000\u0000\u0000JK\u0001\u0000\u0000\u0000"+
		"KI\u0001\u0000\u0000\u0000KL\u0001\u0000\u0000\u0000LM\u0001\u0000\u0000"+
		"\u0000MN\u0006\u0007\u0000\u0000N\u0010\u0001\u0000\u0000\u0000OP\u0005"+
		"=\u0000\u0000P\u0012\u0001\u0000\u0000\u0000QR\u0005;\u0000\u0000R\u0014"+
		"\u0001\u0000\u0000\u0000ST\u0005(\u0000\u0000T\u0016\u0001\u0000\u0000"+
		"\u0000UV\u0005)\u0000\u0000V\u0018\u0001\u0000\u0000\u0000WX\u0005{\u0000"+
		"\u0000X\u001a\u0001\u0000\u0000\u0000YZ\u0005}\u0000\u0000Z\u001c\u0001"+
		"\u0000\u0000\u0000[\\\u0007\u0005\u0000\u0000\\\u001e\u0001\u0000\u0000"+
		"\u0000]g\u0007\u0006\u0000\u0000^_\u0005=\u0000\u0000_g\u0005=\u0000\u0000"+
		"`a\u0005!\u0000\u0000ag\u0005=\u0000\u0000bc\u0005>\u0000\u0000cg\u0005"+
		"=\u0000\u0000de\u0005<\u0000\u0000eg\u0005=\u0000\u0000f]\u0001\u0000"+
		"\u0000\u0000f^\u0001\u0000\u0000\u0000f`\u0001\u0000\u0000\u0000fb\u0001"+
		"\u0000\u0000\u0000fd\u0001\u0000\u0000\u0000g \u0001\u0000\u0000\u0000"+
		"\u0006\u00007=CKf\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}