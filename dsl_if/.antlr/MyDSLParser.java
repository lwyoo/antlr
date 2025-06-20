// Generated from /home/ldg/tmp/antlr/example/dsl_if/MyDSL.g4 by ANTLR 4.13.1
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
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, ID=21, NUMBER=22, STRING=23, WS=24;
	public static final int
		RULE_prog = 0, RULE_stmt = 1, RULE_expr = 2;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "stmt", "expr"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'let'", "'='", "';'", "'if'", "'{'", "'}'", "'else'", "'print'", 
			"'('", "')'", "'+'", "'-'", "'*'", "'/'", "'>'", "'<'", "'=='", "'!='", 
			"'>='", "'<='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, "ID", "NUMBER", 
			"STRING", "WS"
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
	public String getGrammarFileName() { return "MyDSL.g4"; }

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
			setState(9);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 274L) != 0)) {
				{
				{
				setState(6);
				stmt();
				}
				}
				setState(11);
				_errHandler.sync(this);
				_la = _input.LA(1);
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
	public static class StmtContext extends ParserRuleContext {
		public StmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stmt; }
	 
		public StmtContext() { }
		public void copyFrom(StmtContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class PrintContext extends StmtContext {
		public TerminalNode STRING() { return getToken(MyDSLParser.STRING, 0); }
		public PrintContext(StmtContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class IfElseContext extends StmtContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public List<StmtContext> stmt() {
			return getRuleContexts(StmtContext.class);
		}
		public StmtContext stmt(int i) {
			return getRuleContext(StmtContext.class,i);
		}
		public IfElseContext(StmtContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class VariableAssignContext extends StmtContext {
		public TerminalNode ID() { return getToken(MyDSLParser.ID, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public VariableAssignContext(StmtContext ctx) { copyFrom(ctx); }
	}

	public final StmtContext stmt() throws RecognitionException {
		StmtContext _localctx = new StmtContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_stmt);
		int _la;
		try {
			setState(44);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
				_localctx = new VariableAssignContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(12);
				match(T__0);
				setState(13);
				match(ID);
				setState(14);
				match(T__1);
				setState(15);
				expr(0);
				setState(16);
				match(T__2);
				}
				break;
			case T__3:
				_localctx = new IfElseContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(18);
				match(T__3);
				setState(19);
				expr(0);
				setState(20);
				match(T__4);
				setState(24);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 274L) != 0)) {
					{
					{
					setState(21);
					stmt();
					}
					}
					setState(26);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(27);
				match(T__5);
				setState(37);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__6) {
					{
					setState(28);
					match(T__6);
					setState(29);
					match(T__4);
					setState(33);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 274L) != 0)) {
						{
						{
						setState(30);
						stmt();
						}
						}
						setState(35);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					setState(36);
					match(T__5);
					}
				}

				}
				break;
			case T__7:
				_localctx = new PrintContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(39);
				match(T__7);
				setState(40);
				match(T__8);
				setState(41);
				match(STRING);
				setState(42);
				match(T__9);
				setState(43);
				match(T__2);
				}
				break;
			default:
				throw new NoViableAltException(this);
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
	public static class ExprContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(MyDSLParser.ID, 0); }
		public TerminalNode NUMBER() { return getToken(MyDSLParser.NUMBER, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 4;
		enterRecursionRule(_localctx, 4, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(53);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				{
				setState(47);
				match(ID);
				}
				break;
			case NUMBER:
				{
				setState(48);
				match(NUMBER);
				}
				break;
			case T__8:
				{
				setState(49);
				match(T__8);
				setState(50);
				expr(0);
				setState(51);
				match(T__9);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(63);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(61);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
					case 1:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(55);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(56);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 30720L) != 0)) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(57);
						expr(4);
						}
						break;
					case 2:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(58);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(59);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 2064384L) != 0)) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(60);
						expr(2);
						}
						break;
					}
					} 
				}
				setState(65);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 2:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 3);
		case 1:
			return precpred(_ctx, 1);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u0018C\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0001\u0000\u0005\u0000\b\b\u0000\n\u0000\f\u0000\u000b"+
		"\t\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0005\u0001\u0017"+
		"\b\u0001\n\u0001\f\u0001\u001a\t\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0005\u0001 \b\u0001\n\u0001\f\u0001#\t\u0001\u0001\u0001"+
		"\u0003\u0001&\b\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0003\u0001-\b\u0001\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0003\u00026\b\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0005\u0002>\b\u0002\n\u0002\f\u0002A\t\u0002\u0001\u0002\u0000\u0001"+
		"\u0004\u0003\u0000\u0002\u0004\u0000\u0002\u0001\u0000\u000b\u000e\u0001"+
		"\u0000\u000f\u0014I\u0000\t\u0001\u0000\u0000\u0000\u0002,\u0001\u0000"+
		"\u0000\u0000\u00045\u0001\u0000\u0000\u0000\u0006\b\u0003\u0002\u0001"+
		"\u0000\u0007\u0006\u0001\u0000\u0000\u0000\b\u000b\u0001\u0000\u0000\u0000"+
		"\t\u0007\u0001\u0000\u0000\u0000\t\n\u0001\u0000\u0000\u0000\n\u0001\u0001"+
		"\u0000\u0000\u0000\u000b\t\u0001\u0000\u0000\u0000\f\r\u0005\u0001\u0000"+
		"\u0000\r\u000e\u0005\u0015\u0000\u0000\u000e\u000f\u0005\u0002\u0000\u0000"+
		"\u000f\u0010\u0003\u0004\u0002\u0000\u0010\u0011\u0005\u0003\u0000\u0000"+
		"\u0011-\u0001\u0000\u0000\u0000\u0012\u0013\u0005\u0004\u0000\u0000\u0013"+
		"\u0014\u0003\u0004\u0002\u0000\u0014\u0018\u0005\u0005\u0000\u0000\u0015"+
		"\u0017\u0003\u0002\u0001\u0000\u0016\u0015\u0001\u0000\u0000\u0000\u0017"+
		"\u001a\u0001\u0000\u0000\u0000\u0018\u0016\u0001\u0000\u0000\u0000\u0018"+
		"\u0019\u0001\u0000\u0000\u0000\u0019\u001b\u0001\u0000\u0000\u0000\u001a"+
		"\u0018\u0001\u0000\u0000\u0000\u001b%\u0005\u0006\u0000\u0000\u001c\u001d"+
		"\u0005\u0007\u0000\u0000\u001d!\u0005\u0005\u0000\u0000\u001e \u0003\u0002"+
		"\u0001\u0000\u001f\u001e\u0001\u0000\u0000\u0000 #\u0001\u0000\u0000\u0000"+
		"!\u001f\u0001\u0000\u0000\u0000!\"\u0001\u0000\u0000\u0000\"$\u0001\u0000"+
		"\u0000\u0000#!\u0001\u0000\u0000\u0000$&\u0005\u0006\u0000\u0000%\u001c"+
		"\u0001\u0000\u0000\u0000%&\u0001\u0000\u0000\u0000&-\u0001\u0000\u0000"+
		"\u0000\'(\u0005\b\u0000\u0000()\u0005\t\u0000\u0000)*\u0005\u0017\u0000"+
		"\u0000*+\u0005\n\u0000\u0000+-\u0005\u0003\u0000\u0000,\f\u0001\u0000"+
		"\u0000\u0000,\u0012\u0001\u0000\u0000\u0000,\'\u0001\u0000\u0000\u0000"+
		"-\u0003\u0001\u0000\u0000\u0000./\u0006\u0002\uffff\uffff\u0000/6\u0005"+
		"\u0015\u0000\u000006\u0005\u0016\u0000\u000012\u0005\t\u0000\u000023\u0003"+
		"\u0004\u0002\u000034\u0005\n\u0000\u000046\u0001\u0000\u0000\u00005.\u0001"+
		"\u0000\u0000\u000050\u0001\u0000\u0000\u000051\u0001\u0000\u0000\u0000"+
		"6?\u0001\u0000\u0000\u000078\n\u0003\u0000\u000089\u0007\u0000\u0000\u0000"+
		"9>\u0003\u0004\u0002\u0004:;\n\u0001\u0000\u0000;<\u0007\u0001\u0000\u0000"+
		"<>\u0003\u0004\u0002\u0002=7\u0001\u0000\u0000\u0000=:\u0001\u0000\u0000"+
		"\u0000>A\u0001\u0000\u0000\u0000?=\u0001\u0000\u0000\u0000?@\u0001\u0000"+
		"\u0000\u0000@\u0005\u0001\u0000\u0000\u0000A?\u0001\u0000\u0000\u0000"+
		"\b\t\u0018!%,5=?";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}