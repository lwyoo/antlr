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
		NUMBER=16, WS=17;
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
			"NUMBER", "WS"
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
			"NUMBER", "WS"
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
		"\u0004\u0000\u0011a\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002"+
		"\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001"+
		"\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001"+
		"\u0004\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0007\u0001"+
		"\u0007\u0001\b\u0001\b\u0001\t\u0001\t\u0001\n\u0001\n\u0001\u000b\u0001"+
		"\u000b\u0001\f\u0001\f\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0005\u000e"+
		"G\b\u000e\n\u000e\f\u000eJ\t\u000e\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0004\u000fP\b\u000f\u000b\u000f\f\u000fQ\u0001\u000f\u0004"+
		"\u000fU\b\u000f\u000b\u000f\f\u000fV\u0003\u000fY\b\u000f\u0001\u0010"+
		"\u0004\u0010\\\b\u0010\u000b\u0010\f\u0010]\u0001\u0010\u0001\u0010\u0000"+
		"\u0000\u0011\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b"+
		"\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019\r\u001b"+
		"\u000e\u001d\u000f\u001f\u0010!\u0011\u0001\u0000\u0005\u0003\u0000AZ"+
		"__az\u0004\u000009AZ__az\u0003\u000009AFaf\u0001\u000009\u0003\u0000\t"+
		"\n\r\r  e\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000"+
		"\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000"+
		"\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000"+
		"\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000"+
		"\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000"+
		"\u0000\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000"+
		"\u0000\u0019\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000\u0000\u0000"+
		"\u0000\u001d\u0001\u0000\u0000\u0000\u0000\u001f\u0001\u0000\u0000\u0000"+
		"\u0000!\u0001\u0000\u0000\u0000\u0001#\u0001\u0000\u0000\u0000\u0003)"+
		"\u0001\u0000\u0000\u0000\u0005+\u0001\u0000\u0000\u0000\u0007-\u0001\u0000"+
		"\u0000\u0000\t0\u0001\u0000\u0000\u0000\u000b2\u0001\u0000\u0000\u0000"+
		"\r4\u0001\u0000\u0000\u0000\u000f6\u0001\u0000\u0000\u0000\u00118\u0001"+
		"\u0000\u0000\u0000\u0013:\u0001\u0000\u0000\u0000\u0015<\u0001\u0000\u0000"+
		"\u0000\u0017>\u0001\u0000\u0000\u0000\u0019@\u0001\u0000\u0000\u0000\u001b"+
		"B\u0001\u0000\u0000\u0000\u001dD\u0001\u0000\u0000\u0000\u001fX\u0001"+
		"\u0000\u0000\u0000![\u0001\u0000\u0000\u0000#$\u0005m\u0000\u0000$%\u0005"+
		"a\u0000\u0000%&\u0005t\u0000\u0000&\'\u0005c\u0000\u0000\'(\u0005h\u0000"+
		"\u0000(\u0002\u0001\u0000\u0000\u0000)*\u0005_\u0000\u0000*\u0004\u0001"+
		"\u0000\u0000\u0000+,\u0005=\u0000\u0000,\u0006\u0001\u0000\u0000\u0000"+
		"-.\u0005=\u0000\u0000./\u0005>\u0000\u0000/\b\u0001\u0000\u0000\u0000"+
		"01\u0005(\u0000\u00001\n\u0001\u0000\u0000\u000023\u0005)\u0000\u0000"+
		"3\f\u0001\u0000\u0000\u000045\u0005{\u0000\u00005\u000e\u0001\u0000\u0000"+
		"\u000067\u0005}\u0000\u00007\u0010\u0001\u0000\u0000\u000089\u0005,\u0000"+
		"\u00009\u0012\u0001\u0000\u0000\u0000:;\u0005;\u0000\u0000;\u0014\u0001"+
		"\u0000\u0000\u0000<=\u0005+\u0000\u0000=\u0016\u0001\u0000\u0000\u0000"+
		">?\u0005-\u0000\u0000?\u0018\u0001\u0000\u0000\u0000@A\u0005*\u0000\u0000"+
		"A\u001a\u0001\u0000\u0000\u0000BC\u0005/\u0000\u0000C\u001c\u0001\u0000"+
		"\u0000\u0000DH\u0007\u0000\u0000\u0000EG\u0007\u0001\u0000\u0000FE\u0001"+
		"\u0000\u0000\u0000GJ\u0001\u0000\u0000\u0000HF\u0001\u0000\u0000\u0000"+
		"HI\u0001\u0000\u0000\u0000I\u001e\u0001\u0000\u0000\u0000JH\u0001\u0000"+
		"\u0000\u0000KL\u00050\u0000\u0000LM\u0005x\u0000\u0000MO\u0001\u0000\u0000"+
		"\u0000NP\u0007\u0002\u0000\u0000ON\u0001\u0000\u0000\u0000PQ\u0001\u0000"+
		"\u0000\u0000QO\u0001\u0000\u0000\u0000QR\u0001\u0000\u0000\u0000RY\u0001"+
		"\u0000\u0000\u0000SU\u0007\u0003\u0000\u0000TS\u0001\u0000\u0000\u0000"+
		"UV\u0001\u0000\u0000\u0000VT\u0001\u0000\u0000\u0000VW\u0001\u0000\u0000"+
		"\u0000WY\u0001\u0000\u0000\u0000XK\u0001\u0000\u0000\u0000XT\u0001\u0000"+
		"\u0000\u0000Y \u0001\u0000\u0000\u0000Z\\\u0007\u0004\u0000\u0000[Z\u0001"+
		"\u0000\u0000\u0000\\]\u0001\u0000\u0000\u0000][\u0001\u0000\u0000\u0000"+
		"]^\u0001\u0000\u0000\u0000^_\u0001\u0000\u0000\u0000_`\u0006\u0010\u0000"+
		"\u0000`\"\u0001\u0000\u0000\u0000\u0006\u0000HQVX]\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}