// Generated from /home/ldg/tmp/antlr/example/dsl_match/MyDSLParser.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class MyDSLParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		MATCH=1, UNDERSCORE=2, EQUAL=3, ARROW=4, LPAREN=5, RPAREN=6, LBRACE=7, 
		RBRACE=8, COMMA=9, SEMICOLON=10, ID=11, NUMBER=12, WS=13;
	public static final int
		RULE_prog = 0, RULE_stmt = 1, RULE_assignment = 2, RULE_matchExpr = 3, 
		RULE_matchCaseList = 4, RULE_matchCase = 5, RULE_defaultCase = 6;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "stmt", "assignment", "matchExpr", "matchCaseList", "matchCase", 
			"defaultCase"
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

	@Override
	public String getGrammarFileName() { return "MyDSLParser.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public MyDSLParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(MyDSLParser.EOF, 0); }
		public List<StmtContext> stmt() {
			return getRuleContexts(StmtContext.class);
		}
		public StmtContext stmt(int i) {
			return getRuleContext(StmtContext.class,i);
		}
		public ProgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog; }
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_prog);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(15); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(14);
				stmt();
				}
				}
				setState(17); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==ID );
			setState(19);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StmtContext extends ParserRuleContext {
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public StmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stmt; }
	}

	public final StmtContext stmt() throws RecognitionException {
		StmtContext _localctx = new StmtContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(21);
			assignment();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignmentContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(MyDSLParser.ID, 0); }
		public TerminalNode EQUAL() { return getToken(MyDSLParser.EQUAL, 0); }
		public MatchExprContext matchExpr() {
			return getRuleContext(MatchExprContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(MyDSLParser.SEMICOLON, 0); }
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_assignment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(23);
			match(ID);
			setState(24);
			match(EQUAL);
			setState(25);
			matchExpr();
			setState(26);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MatchExprContext extends ParserRuleContext {
		public TerminalNode MATCH() { return getToken(MyDSLParser.MATCH, 0); }
		public TerminalNode LPAREN() { return getToken(MyDSLParser.LPAREN, 0); }
		public TerminalNode ID() { return getToken(MyDSLParser.ID, 0); }
		public TerminalNode RPAREN() { return getToken(MyDSLParser.RPAREN, 0); }
		public TerminalNode LBRACE() { return getToken(MyDSLParser.LBRACE, 0); }
		public MatchCaseListContext matchCaseList() {
			return getRuleContext(MatchCaseListContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(MyDSLParser.RBRACE, 0); }
		public MatchExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_matchExpr; }
	}

	public final MatchExprContext matchExpr() throws RecognitionException {
		MatchExprContext _localctx = new MatchExprContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_matchExpr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(28);
			match(MATCH);
			setState(29);
			match(LPAREN);
			setState(30);
			match(ID);
			setState(31);
			match(RPAREN);
			setState(32);
			match(LBRACE);
			setState(33);
			matchCaseList();
			setState(34);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MatchCaseListContext extends ParserRuleContext {
		public List<MatchCaseContext> matchCase() {
			return getRuleContexts(MatchCaseContext.class);
		}
		public MatchCaseContext matchCase(int i) {
			return getRuleContext(MatchCaseContext.class,i);
		}
		public DefaultCaseContext defaultCase() {
			return getRuleContext(DefaultCaseContext.class,0);
		}
		public List<TerminalNode> COMMA() { return getTokens(MyDSLParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(MyDSLParser.COMMA, i);
		}
		public MatchCaseListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_matchCaseList; }
	}

	public final MatchCaseListContext matchCaseList() throws RecognitionException {
		MatchCaseListContext _localctx = new MatchCaseListContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_matchCaseList);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(36);
			matchCase();
			setState(41);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,1,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(37);
					match(COMMA);
					setState(38);
					matchCase();
					}
					} 
				}
				setState(43);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,1,_ctx);
			}
			setState(45);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(44);
				match(COMMA);
				}
			}

			setState(47);
			defaultCase();
			setState(49);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(48);
				match(COMMA);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MatchCaseContext extends ParserRuleContext {
		public TerminalNode LPAREN() { return getToken(MyDSLParser.LPAREN, 0); }
		public TerminalNode NUMBER() { return getToken(MyDSLParser.NUMBER, 0); }
		public TerminalNode RPAREN() { return getToken(MyDSLParser.RPAREN, 0); }
		public TerminalNode ARROW() { return getToken(MyDSLParser.ARROW, 0); }
		public TerminalNode ID() { return getToken(MyDSLParser.ID, 0); }
		public MatchCaseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_matchCase; }
	}

	public final MatchCaseContext matchCase() throws RecognitionException {
		MatchCaseContext _localctx = new MatchCaseContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_matchCase);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(51);
			match(LPAREN);
			setState(52);
			match(NUMBER);
			setState(53);
			match(RPAREN);
			setState(54);
			match(ARROW);
			setState(55);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DefaultCaseContext extends ParserRuleContext {
		public TerminalNode LPAREN() { return getToken(MyDSLParser.LPAREN, 0); }
		public TerminalNode UNDERSCORE() { return getToken(MyDSLParser.UNDERSCORE, 0); }
		public TerminalNode RPAREN() { return getToken(MyDSLParser.RPAREN, 0); }
		public TerminalNode ARROW() { return getToken(MyDSLParser.ARROW, 0); }
		public TerminalNode ID() { return getToken(MyDSLParser.ID, 0); }
		public DefaultCaseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_defaultCase; }
	}

	public final DefaultCaseContext defaultCase() throws RecognitionException {
		DefaultCaseContext _localctx = new DefaultCaseContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_defaultCase);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(57);
			match(LPAREN);
			setState(58);
			match(UNDERSCORE);
			setState(59);
			match(RPAREN);
			setState(60);
			match(ARROW);
			setState(61);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\r@\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0001\u0000\u0004\u0000\u0010"+
		"\b\u0000\u000b\u0000\f\u0000\u0011\u0001\u0000\u0001\u0000\u0001\u0001"+
		"\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0005\u0004"+
		"(\b\u0004\n\u0004\f\u0004+\t\u0004\u0001\u0004\u0003\u0004.\b\u0004\u0001"+
		"\u0004\u0001\u0004\u0003\u00042\b\u0004\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0000\u0000\u0007"+
		"\u0000\u0002\u0004\u0006\b\n\f\u0000\u0000<\u0000\u000f\u0001\u0000\u0000"+
		"\u0000\u0002\u0015\u0001\u0000\u0000\u0000\u0004\u0017\u0001\u0000\u0000"+
		"\u0000\u0006\u001c\u0001\u0000\u0000\u0000\b$\u0001\u0000\u0000\u0000"+
		"\n3\u0001\u0000\u0000\u0000\f9\u0001\u0000\u0000\u0000\u000e\u0010\u0003"+
		"\u0002\u0001\u0000\u000f\u000e\u0001\u0000\u0000\u0000\u0010\u0011\u0001"+
		"\u0000\u0000\u0000\u0011\u000f\u0001\u0000\u0000\u0000\u0011\u0012\u0001"+
		"\u0000\u0000\u0000\u0012\u0013\u0001\u0000\u0000\u0000\u0013\u0014\u0005"+
		"\u0000\u0000\u0001\u0014\u0001\u0001\u0000\u0000\u0000\u0015\u0016\u0003"+
		"\u0004\u0002\u0000\u0016\u0003\u0001\u0000\u0000\u0000\u0017\u0018\u0005"+
		"\u000b\u0000\u0000\u0018\u0019\u0005\u0003\u0000\u0000\u0019\u001a\u0003"+
		"\u0006\u0003\u0000\u001a\u001b\u0005\n\u0000\u0000\u001b\u0005\u0001\u0000"+
		"\u0000\u0000\u001c\u001d\u0005\u0001\u0000\u0000\u001d\u001e\u0005\u0005"+
		"\u0000\u0000\u001e\u001f\u0005\u000b\u0000\u0000\u001f \u0005\u0006\u0000"+
		"\u0000 !\u0005\u0007\u0000\u0000!\"\u0003\b\u0004\u0000\"#\u0005\b\u0000"+
		"\u0000#\u0007\u0001\u0000\u0000\u0000$)\u0003\n\u0005\u0000%&\u0005\t"+
		"\u0000\u0000&(\u0003\n\u0005\u0000\'%\u0001\u0000\u0000\u0000(+\u0001"+
		"\u0000\u0000\u0000)\'\u0001\u0000\u0000\u0000)*\u0001\u0000\u0000\u0000"+
		"*-\u0001\u0000\u0000\u0000+)\u0001\u0000\u0000\u0000,.\u0005\t\u0000\u0000"+
		"-,\u0001\u0000\u0000\u0000-.\u0001\u0000\u0000\u0000./\u0001\u0000\u0000"+
		"\u0000/1\u0003\f\u0006\u000002\u0005\t\u0000\u000010\u0001\u0000\u0000"+
		"\u000012\u0001\u0000\u0000\u00002\t\u0001\u0000\u0000\u000034\u0005\u0005"+
		"\u0000\u000045\u0005\f\u0000\u000056\u0005\u0006\u0000\u000067\u0005\u0004"+
		"\u0000\u000078\u0005\u000b\u0000\u00008\u000b\u0001\u0000\u0000\u0000"+
		"9:\u0005\u0005\u0000\u0000:;\u0005\u0002\u0000\u0000;<\u0005\u0006\u0000"+
		"\u0000<=\u0005\u0004\u0000\u0000=>\u0005\u000b\u0000\u0000>\r\u0001\u0000"+
		"\u0000\u0000\u0004\u0011)-1";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}