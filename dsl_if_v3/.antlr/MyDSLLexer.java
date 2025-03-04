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
		SEMICOLON=10, LPAREN=11, RPAREN=12, LBRACE=13, RBRACE=14, OP1=15, OP2=16, 
		COMPARE=17;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"LET", "IF", "ELSE", "PRINT", "ID", "NUMBER", "STRING", "WS", "EQUAL", 
			"SEMICOLON", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "OP1", "OP2", "COMPARE"
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
			"SEMICOLON", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "OP1", "OP2", "COMPARE"
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
		"\u0004\u0000\u0011l\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002"+
		"\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0005"+
		"\u00048\b\u0004\n\u0004\f\u0004;\t\u0004\u0001\u0005\u0004\u0005>\b\u0005"+
		"\u000b\u0005\f\u0005?\u0001\u0006\u0001\u0006\u0005\u0006D\b\u0006\n\u0006"+
		"\f\u0006G\t\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0004\u0007L\b\u0007"+
		"\u000b\u0007\f\u0007M\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\t"+
		"\u0001\t\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001"+
		"\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0003\u0010k\b\u0010\u0000\u0000\u0011\u0001"+
		"\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007"+
		"\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019\r\u001b\u000e\u001d"+
		"\u000f\u001f\u0010!\u0011\u0001\u0000\b\u0003\u0000AZ__az\u0004\u0000"+
		"09AZ__az\u0001\u000009\u0001\u0000\"\"\u0003\u0000\t\n\r\r  \u0002\u0000"+
		"**//\u0002\u0000++--\u0002\u0000<<>>s\u0000\u0001\u0001\u0000\u0000\u0000"+
		"\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000"+
		"\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000"+
		"\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f"+
		"\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013"+
		"\u0001\u0000\u0000\u0000\u0000\u0015\u0001\u0000\u0000\u0000\u0000\u0017"+
		"\u0001\u0000\u0000\u0000\u0000\u0019\u0001\u0000\u0000\u0000\u0000\u001b"+
		"\u0001\u0000\u0000\u0000\u0000\u001d\u0001\u0000\u0000\u0000\u0000\u001f"+
		"\u0001\u0000\u0000\u0000\u0000!\u0001\u0000\u0000\u0000\u0001#\u0001\u0000"+
		"\u0000\u0000\u0003\'\u0001\u0000\u0000\u0000\u0005*\u0001\u0000\u0000"+
		"\u0000\u0007/\u0001\u0000\u0000\u0000\t5\u0001\u0000\u0000\u0000\u000b"+
		"=\u0001\u0000\u0000\u0000\rA\u0001\u0000\u0000\u0000\u000fK\u0001\u0000"+
		"\u0000\u0000\u0011Q\u0001\u0000\u0000\u0000\u0013S\u0001\u0000\u0000\u0000"+
		"\u0015U\u0001\u0000\u0000\u0000\u0017W\u0001\u0000\u0000\u0000\u0019Y"+
		"\u0001\u0000\u0000\u0000\u001b[\u0001\u0000\u0000\u0000\u001d]\u0001\u0000"+
		"\u0000\u0000\u001f_\u0001\u0000\u0000\u0000!j\u0001\u0000\u0000\u0000"+
		"#$\u0005l\u0000\u0000$%\u0005e\u0000\u0000%&\u0005t\u0000\u0000&\u0002"+
		"\u0001\u0000\u0000\u0000\'(\u0005i\u0000\u0000()\u0005f\u0000\u0000)\u0004"+
		"\u0001\u0000\u0000\u0000*+\u0005e\u0000\u0000+,\u0005l\u0000\u0000,-\u0005"+
		"s\u0000\u0000-.\u0005e\u0000\u0000.\u0006\u0001\u0000\u0000\u0000/0\u0005"+
		"p\u0000\u000001\u0005r\u0000\u000012\u0005i\u0000\u000023\u0005n\u0000"+
		"\u000034\u0005t\u0000\u00004\b\u0001\u0000\u0000\u000059\u0007\u0000\u0000"+
		"\u000068\u0007\u0001\u0000\u000076\u0001\u0000\u0000\u00008;\u0001\u0000"+
		"\u0000\u000097\u0001\u0000\u0000\u00009:\u0001\u0000\u0000\u0000:\n\u0001"+
		"\u0000\u0000\u0000;9\u0001\u0000\u0000\u0000<>\u0007\u0002\u0000\u0000"+
		"=<\u0001\u0000\u0000\u0000>?\u0001\u0000\u0000\u0000?=\u0001\u0000\u0000"+
		"\u0000?@\u0001\u0000\u0000\u0000@\f\u0001\u0000\u0000\u0000AE\u0005\""+
		"\u0000\u0000BD\b\u0003\u0000\u0000CB\u0001\u0000\u0000\u0000DG\u0001\u0000"+
		"\u0000\u0000EC\u0001\u0000\u0000\u0000EF\u0001\u0000\u0000\u0000FH\u0001"+
		"\u0000\u0000\u0000GE\u0001\u0000\u0000\u0000HI\u0005\"\u0000\u0000I\u000e"+
		"\u0001\u0000\u0000\u0000JL\u0007\u0004\u0000\u0000KJ\u0001\u0000\u0000"+
		"\u0000LM\u0001\u0000\u0000\u0000MK\u0001\u0000\u0000\u0000MN\u0001\u0000"+
		"\u0000\u0000NO\u0001\u0000\u0000\u0000OP\u0006\u0007\u0000\u0000P\u0010"+
		"\u0001\u0000\u0000\u0000QR\u0005=\u0000\u0000R\u0012\u0001\u0000\u0000"+
		"\u0000ST\u0005;\u0000\u0000T\u0014\u0001\u0000\u0000\u0000UV\u0005(\u0000"+
		"\u0000V\u0016\u0001\u0000\u0000\u0000WX\u0005)\u0000\u0000X\u0018\u0001"+
		"\u0000\u0000\u0000YZ\u0005{\u0000\u0000Z\u001a\u0001\u0000\u0000\u0000"+
		"[\\\u0005}\u0000\u0000\\\u001c\u0001\u0000\u0000\u0000]^\u0007\u0005\u0000"+
		"\u0000^\u001e\u0001\u0000\u0000\u0000_`\u0007\u0006\u0000\u0000` \u0001"+
		"\u0000\u0000\u0000ak\u0007\u0007\u0000\u0000bc\u0005=\u0000\u0000ck\u0005"+
		"=\u0000\u0000de\u0005!\u0000\u0000ek\u0005=\u0000\u0000fg\u0005>\u0000"+
		"\u0000gk\u0005=\u0000\u0000hi\u0005<\u0000\u0000ik\u0005=\u0000\u0000"+
		"ja\u0001\u0000\u0000\u0000jb\u0001\u0000\u0000\u0000jd\u0001\u0000\u0000"+
		"\u0000jf\u0001\u0000\u0000\u0000jh\u0001\u0000\u0000\u0000k\"\u0001\u0000"+
		"\u0000\u0000\u0006\u00009?EMj\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}