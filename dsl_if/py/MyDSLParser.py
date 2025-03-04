# Generated from MyDSL.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,24,67,2,0,7,0,2,1,7,1,2,2,7,2,1,0,5,0,8,8,0,10,0,12,0,11,9,0,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,23,8,1,10,1,12,1,26,
        9,1,1,1,1,1,1,1,1,1,5,1,32,8,1,10,1,12,1,35,9,1,1,1,3,1,38,8,1,1,
        1,1,1,1,1,1,1,1,1,3,1,45,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,54,
        8,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,62,8,2,10,2,12,2,65,9,2,1,2,0,1,
        4,3,0,2,4,0,2,1,0,11,14,1,0,15,20,73,0,9,1,0,0,0,2,44,1,0,0,0,4,
        53,1,0,0,0,6,8,3,2,1,0,7,6,1,0,0,0,8,11,1,0,0,0,9,7,1,0,0,0,9,10,
        1,0,0,0,10,1,1,0,0,0,11,9,1,0,0,0,12,13,5,1,0,0,13,14,5,21,0,0,14,
        15,5,2,0,0,15,16,3,4,2,0,16,17,5,3,0,0,17,45,1,0,0,0,18,19,5,4,0,
        0,19,20,3,4,2,0,20,24,5,5,0,0,21,23,3,2,1,0,22,21,1,0,0,0,23,26,
        1,0,0,0,24,22,1,0,0,0,24,25,1,0,0,0,25,27,1,0,0,0,26,24,1,0,0,0,
        27,37,5,6,0,0,28,29,5,7,0,0,29,33,5,5,0,0,30,32,3,2,1,0,31,30,1,
        0,0,0,32,35,1,0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,34,36,1,0,0,0,35,
        33,1,0,0,0,36,38,5,6,0,0,37,28,1,0,0,0,37,38,1,0,0,0,38,45,1,0,0,
        0,39,40,5,8,0,0,40,41,5,9,0,0,41,42,5,23,0,0,42,43,5,10,0,0,43,45,
        5,3,0,0,44,12,1,0,0,0,44,18,1,0,0,0,44,39,1,0,0,0,45,3,1,0,0,0,46,
        47,6,2,-1,0,47,54,5,21,0,0,48,54,5,22,0,0,49,50,5,9,0,0,50,51,3,
        4,2,0,51,52,5,10,0,0,52,54,1,0,0,0,53,46,1,0,0,0,53,48,1,0,0,0,53,
        49,1,0,0,0,54,63,1,0,0,0,55,56,10,3,0,0,56,57,7,0,0,0,57,62,3,4,
        2,4,58,59,10,1,0,0,59,60,7,1,0,0,60,62,3,4,2,2,61,55,1,0,0,0,61,
        58,1,0,0,0,62,65,1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,5,1,0,0,
        0,65,63,1,0,0,0,8,9,24,33,37,44,53,61,63
    ]

class MyDSLParser ( Parser ):

    grammarFileName = "MyDSL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'let'", "'='", "';'", "'if'", "'{'", 
                     "'}'", "'else'", "'print'", "'('", "')'", "'+'", "'-'", 
                     "'*'", "'/'", "'>'", "'<'", "'=='", "'!='", "'>='", 
                     "'<='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "NUMBER", "STRING", "WS" ]

    RULE_prog = 0
    RULE_stmt = 1
    RULE_expr = 2

    ruleNames =  [ "prog", "stmt", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    ID=21
    NUMBER=22
    STRING=23
    WS=24

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyDSLParser.StmtContext)
            else:
                return self.getTypedRuleContext(MyDSLParser.StmtContext,i)


        def getRuleIndex(self):
            return MyDSLParser.RULE_prog

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = MyDSLParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 274) != 0):
                self.state = 6
                self.stmt()
                self.state = 11
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MyDSLParser.RULE_stmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PrintContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyDSLParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(MyDSLParser.STRING, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)


    class IfElseContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyDSLParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MyDSLParser.ExprContext,0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyDSLParser.StmtContext)
            else:
                return self.getTypedRuleContext(MyDSLParser.StmtContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfElse" ):
                return visitor.visitIfElse(self)
            else:
                return visitor.visitChildren(self)


    class VariableAssignContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyDSLParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MyDSLParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(MyDSLParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableAssign" ):
                return visitor.visitVariableAssign(self)
            else:
                return visitor.visitChildren(self)



    def stmt(self):

        localctx = MyDSLParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        self._la = 0 # Token type
        try:
            self.state = 44
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = MyDSLParser.VariableAssignContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 12
                self.match(MyDSLParser.T__0)
                self.state = 13
                self.match(MyDSLParser.ID)
                self.state = 14
                self.match(MyDSLParser.T__1)
                self.state = 15
                self.expr(0)
                self.state = 16
                self.match(MyDSLParser.T__2)
                pass
            elif token in [4]:
                localctx = MyDSLParser.IfElseContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                self.match(MyDSLParser.T__3)
                self.state = 19
                self.expr(0)
                self.state = 20
                self.match(MyDSLParser.T__4)
                self.state = 24
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 274) != 0):
                    self.state = 21
                    self.stmt()
                    self.state = 26
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 27
                self.match(MyDSLParser.T__5)
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==7:
                    self.state = 28
                    self.match(MyDSLParser.T__6)
                    self.state = 29
                    self.match(MyDSLParser.T__4)
                    self.state = 33
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 274) != 0):
                        self.state = 30
                        self.stmt()
                        self.state = 35
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 36
                    self.match(MyDSLParser.T__5)


                pass
            elif token in [8]:
                localctx = MyDSLParser.PrintContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 39
                self.match(MyDSLParser.T__7)
                self.state = 40
                self.match(MyDSLParser.T__8)
                self.state = 41
                self.match(MyDSLParser.STRING)
                self.state = 42
                self.match(MyDSLParser.T__9)
                self.state = 43
                self.match(MyDSLParser.T__2)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MyDSLParser.ID, 0)

        def NUMBER(self):
            return self.getToken(MyDSLParser.NUMBER, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyDSLParser.ExprContext)
            else:
                return self.getTypedRuleContext(MyDSLParser.ExprContext,i)


        def getRuleIndex(self):
            return MyDSLParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MyDSLParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.state = 47
                self.match(MyDSLParser.ID)
                pass
            elif token in [22]:
                self.state = 48
                self.match(MyDSLParser.NUMBER)
                pass
            elif token in [9]:
                self.state = 49
                self.match(MyDSLParser.T__8)
                self.state = 50
                self.expr(0)
                self.state = 51
                self.match(MyDSLParser.T__9)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 63
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 61
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = MyDSLParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 55
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 56
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30720) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 57
                        self.expr(4)
                        pass

                    elif la_ == 2:
                        localctx = MyDSLParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 58
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 59
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2064384) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 60
                        self.expr(2)
                        pass

             
                self.state = 65
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         




