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
		RBRACE=8, COMMA=9, SEMICOLON=10, ID=11, NUMBER=12, WS=13;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"MATCH", "UNDERSCORE", "EQUAL", "ARROW", "LPAREN", "RPAREN", "LBRACE", 
			"RBRACE", "COMMA", "SEMICOLON", "ID", "NUMBER", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'match'", "'_'", "'='", "'=>'", "'('", "')'", "'{'", "'}'", "','", 
			"';'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "MATCH", "UNDERSCORE", "EQUAL", "ARROW", "LPAREN", "RPAREN", "LBRACE", 
			"RBRACE", "COMMA", "SEMICOLON", "ID", "NUMBER", "WS"
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
		"\u0004\u0000\rQ\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0002\u0001"+
		"\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001"+
		"\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001"+
		"\b\u0001\b\u0001\t\u0001\t\u0001\n\u0001\n\u0005\n7\b\n\n\n\f\n:\t\n\u0001"+
		"\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0004\u000b@\b\u000b\u000b"+
		"\u000b\f\u000bA\u0001\u000b\u0004\u000bE\b\u000b\u000b\u000b\f\u000bF"+
		"\u0003\u000bI\b\u000b\u0001\f\u0004\fL\b\f\u000b\f\f\fM\u0001\f\u0001"+
		"\f\u0000\u0000\r\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005"+
		"\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019"+
		"\r\u0001\u0000\u0005\u0003\u0000AZ__az\u0004\u000009AZ__az\u0003\u0000"+
		"09AFaf\u0001\u000009\u0003\u0000\t\n\r\r  U\u0000\u0001\u0001\u0000\u0000"+
		"\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000"+
		"\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000"+
		"\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000"+
		"\u000f\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000\u0000\u0000"+
		"\u0013\u0001\u0000\u0000\u0000\u0000\u0015\u0001\u0000\u0000\u0000\u0000"+
		"\u0017\u0001\u0000\u0000\u0000\u0000\u0019\u0001\u0000\u0000\u0000\u0001"+
		"\u001b\u0001\u0000\u0000\u0000\u0003!\u0001\u0000\u0000\u0000\u0005#\u0001"+
		"\u0000\u0000\u0000\u0007%\u0001\u0000\u0000\u0000\t(\u0001\u0000\u0000"+
		"\u0000\u000b*\u0001\u0000\u0000\u0000\r,\u0001\u0000\u0000\u0000\u000f"+
		".\u0001\u0000\u0000\u0000\u00110\u0001\u0000\u0000\u0000\u00132\u0001"+
		"\u0000\u0000\u0000\u00154\u0001\u0000\u0000\u0000\u0017H\u0001\u0000\u0000"+
		"\u0000\u0019K\u0001\u0000\u0000\u0000\u001b\u001c\u0005m\u0000\u0000\u001c"+
		"\u001d\u0005a\u0000\u0000\u001d\u001e\u0005t\u0000\u0000\u001e\u001f\u0005"+
		"c\u0000\u0000\u001f \u0005h\u0000\u0000 \u0002\u0001\u0000\u0000\u0000"+
		"!\"\u0005_\u0000\u0000\"\u0004\u0001\u0000\u0000\u0000#$\u0005=\u0000"+
		"\u0000$\u0006\u0001\u0000\u0000\u0000%&\u0005=\u0000\u0000&\'\u0005>\u0000"+
		"\u0000\'\b\u0001\u0000\u0000\u0000()\u0005(\u0000\u0000)\n\u0001\u0000"+
		"\u0000\u0000*+\u0005)\u0000\u0000+\f\u0001\u0000\u0000\u0000,-\u0005{"+
		"\u0000\u0000-\u000e\u0001\u0000\u0000\u0000./\u0005}\u0000\u0000/\u0010"+
		"\u0001\u0000\u0000\u000001\u0005,\u0000\u00001\u0012\u0001\u0000\u0000"+
		"\u000023\u0005;\u0000\u00003\u0014\u0001\u0000\u0000\u000048\u0007\u0000"+
		"\u0000\u000057\u0007\u0001\u0000\u000065\u0001\u0000\u0000\u00007:\u0001"+
		"\u0000\u0000\u000086\u0001\u0000\u0000\u000089\u0001\u0000\u0000\u0000"+
		"9\u0016\u0001\u0000\u0000\u0000:8\u0001\u0000\u0000\u0000;<\u00050\u0000"+
		"\u0000<=\u0005x\u0000\u0000=?\u0001\u0000\u0000\u0000>@\u0007\u0002\u0000"+
		"\u0000?>\u0001\u0000\u0000\u0000@A\u0001\u0000\u0000\u0000A?\u0001\u0000"+
		"\u0000\u0000AB\u0001\u0000\u0000\u0000BI\u0001\u0000\u0000\u0000CE\u0007"+
		"\u0003\u0000\u0000DC\u0001\u0000\u0000\u0000EF\u0001\u0000\u0000\u0000"+
		"FD\u0001\u0000\u0000\u0000FG\u0001\u0000\u0000\u0000GI\u0001\u0000\u0000"+
		"\u0000H;\u0001\u0000\u0000\u0000HD\u0001\u0000\u0000\u0000I\u0018\u0001"+
		"\u0000\u0000\u0000JL\u0007\u0004\u0000\u0000KJ\u0001\u0000\u0000\u0000"+
		"LM\u0001\u0000\u0000\u0000MK\u0001\u0000\u0000\u0000MN\u0001\u0000\u0000"+
		"\u0000NO\u0001\u0000\u0000\u0000OP\u0006\f\u0000\u0000P\u001a\u0001\u0000"+
		"\u0000\u0000\u0006\u00008AFHM\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}