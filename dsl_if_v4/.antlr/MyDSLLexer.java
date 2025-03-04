// Generated from /home/ldg/tmp/antlr/example/dsl_if_v4/MyDSLLexer.g4 by ANTLR 4.13.1
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
		LET=1, IF=2, ELSE=3, ELSEIF=4, PRINT=5, ID=6, NUMBER=7, STRING=8, WS=9, 
		EQUAL=10, SEMICOLON=11, LPAREN=12, RPAREN=13, LBRACE=14, RBRACE=15, OP1=16, 
		OP2=17, COMPARE=18;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"LET", "IF", "ELSE", "ELSEIF", "PRINT", "ID", "NUMBER", "STRING", "WS", 
			"EQUAL", "SEMICOLON", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "OP1", 
			"OP2", "COMPARE"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'let'", "'if'", "'else'", "'else if'", "'print'", null, null, 
			null, null, "'='", "';'", "'('", "')'", "'{'", "'}'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "LET", "IF", "ELSE", "ELSEIF", "PRINT", "ID", "NUMBER", "STRING", 
			"WS", "EQUAL", "SEMICOLON", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "OP1", 
			"OP2", "COMPARE"
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
		"\u0004\u0000\u0012v\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002"+
		"\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0005\u0005B\b\u0005\n\u0005"+
		"\f\u0005E\t\u0005\u0001\u0006\u0004\u0006H\b\u0006\u000b\u0006\f\u0006"+
		"I\u0001\u0007\u0001\u0007\u0005\u0007N\b\u0007\n\u0007\f\u0007Q\t\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\b\u0004\bV\b\b\u000b\b\f\bW\u0001\b\u0001"+
		"\b\u0001\t\u0001\t\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\f\u0001"+
		"\f\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001"+
		"\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001"+
		"\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0003\u0011u\b"+
		"\u0011\u0000\u0000\u0012\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004"+
		"\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017"+
		"\f\u0019\r\u001b\u000e\u001d\u000f\u001f\u0010!\u0011#\u0012\u0001\u0000"+
		"\b\u0003\u0000AZ__az\u0004\u000009AZ__az\u0001\u000009\u0001\u0000\"\""+
		"\u0003\u0000\t\n\r\r  \u0002\u0000**//\u0002\u0000++--\u0002\u0000<<>"+
		">}\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000"+
		"\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000"+
		"\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000"+
		"\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011"+
		"\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000\u0000\u0015"+
		"\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000\u0000\u0019"+
		"\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000\u0000\u0000\u0000\u001d"+
		"\u0001\u0000\u0000\u0000\u0000\u001f\u0001\u0000\u0000\u0000\u0000!\u0001"+
		"\u0000\u0000\u0000\u0000#\u0001\u0000\u0000\u0000\u0001%\u0001\u0000\u0000"+
		"\u0000\u0003)\u0001\u0000\u0000\u0000\u0005,\u0001\u0000\u0000\u0000\u0007"+
		"1\u0001\u0000\u0000\u0000\t9\u0001\u0000\u0000\u0000\u000b?\u0001\u0000"+
		"\u0000\u0000\rG\u0001\u0000\u0000\u0000\u000fK\u0001\u0000\u0000\u0000"+
		"\u0011U\u0001\u0000\u0000\u0000\u0013[\u0001\u0000\u0000\u0000\u0015]"+
		"\u0001\u0000\u0000\u0000\u0017_\u0001\u0000\u0000\u0000\u0019a\u0001\u0000"+
		"\u0000\u0000\u001bc\u0001\u0000\u0000\u0000\u001de\u0001\u0000\u0000\u0000"+
		"\u001fg\u0001\u0000\u0000\u0000!i\u0001\u0000\u0000\u0000#t\u0001\u0000"+
		"\u0000\u0000%&\u0005l\u0000\u0000&\'\u0005e\u0000\u0000\'(\u0005t\u0000"+
		"\u0000(\u0002\u0001\u0000\u0000\u0000)*\u0005i\u0000\u0000*+\u0005f\u0000"+
		"\u0000+\u0004\u0001\u0000\u0000\u0000,-\u0005e\u0000\u0000-.\u0005l\u0000"+
		"\u0000./\u0005s\u0000\u0000/0\u0005e\u0000\u00000\u0006\u0001\u0000\u0000"+
		"\u000012\u0005e\u0000\u000023\u0005l\u0000\u000034\u0005s\u0000\u0000"+
		"45\u0005e\u0000\u000056\u0005 \u0000\u000067\u0005i\u0000\u000078\u0005"+
		"f\u0000\u00008\b\u0001\u0000\u0000\u00009:\u0005p\u0000\u0000:;\u0005"+
		"r\u0000\u0000;<\u0005i\u0000\u0000<=\u0005n\u0000\u0000=>\u0005t\u0000"+
		"\u0000>\n\u0001\u0000\u0000\u0000?C\u0007\u0000\u0000\u0000@B\u0007\u0001"+
		"\u0000\u0000A@\u0001\u0000\u0000\u0000BE\u0001\u0000\u0000\u0000CA\u0001"+
		"\u0000\u0000\u0000CD\u0001\u0000\u0000\u0000D\f\u0001\u0000\u0000\u0000"+
		"EC\u0001\u0000\u0000\u0000FH\u0007\u0002\u0000\u0000GF\u0001\u0000\u0000"+
		"\u0000HI\u0001\u0000\u0000\u0000IG\u0001\u0000\u0000\u0000IJ\u0001\u0000"+
		"\u0000\u0000J\u000e\u0001\u0000\u0000\u0000KO\u0005\"\u0000\u0000LN\b"+
		"\u0003\u0000\u0000ML\u0001\u0000\u0000\u0000NQ\u0001\u0000\u0000\u0000"+
		"OM\u0001\u0000\u0000\u0000OP\u0001\u0000\u0000\u0000PR\u0001\u0000\u0000"+
		"\u0000QO\u0001\u0000\u0000\u0000RS\u0005\"\u0000\u0000S\u0010\u0001\u0000"+
		"\u0000\u0000TV\u0007\u0004\u0000\u0000UT\u0001\u0000\u0000\u0000VW\u0001"+
		"\u0000\u0000\u0000WU\u0001\u0000\u0000\u0000WX\u0001\u0000\u0000\u0000"+
		"XY\u0001\u0000\u0000\u0000YZ\u0006\b\u0000\u0000Z\u0012\u0001\u0000\u0000"+
		"\u0000[\\\u0005=\u0000\u0000\\\u0014\u0001\u0000\u0000\u0000]^\u0005;"+
		"\u0000\u0000^\u0016\u0001\u0000\u0000\u0000_`\u0005(\u0000\u0000`\u0018"+
		"\u0001\u0000\u0000\u0000ab\u0005)\u0000\u0000b\u001a\u0001\u0000\u0000"+
		"\u0000cd\u0005{\u0000\u0000d\u001c\u0001\u0000\u0000\u0000ef\u0005}\u0000"+
		"\u0000f\u001e\u0001\u0000\u0000\u0000gh\u0007\u0005\u0000\u0000h \u0001"+
		"\u0000\u0000\u0000ij\u0007\u0006\u0000\u0000j\"\u0001\u0000\u0000\u0000"+
		"ku\u0007\u0007\u0000\u0000lm\u0005=\u0000\u0000mu\u0005=\u0000\u0000n"+
		"o\u0005!\u0000\u0000ou\u0005=\u0000\u0000pq\u0005>\u0000\u0000qu\u0005"+
		"=\u0000\u0000rs\u0005<\u0000\u0000su\u0005=\u0000\u0000tk\u0001\u0000"+
		"\u0000\u0000tl\u0001\u0000\u0000\u0000tn\u0001\u0000\u0000\u0000tp\u0001"+
		"\u0000\u0000\u0000tr\u0001\u0000\u0000\u0000u$\u0001\u0000\u0000\u0000"+
		"\u0006\u0000CIOWt\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}