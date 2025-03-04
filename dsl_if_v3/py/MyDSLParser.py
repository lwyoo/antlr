# Generated from MyDSLParser.g4 by ANTLR 4.13.2
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
        4,1,17,94,2,0,7,0,2,1,7,1,2,2,7,2,1,0,4,0,8,8,0,11,0,12,0,9,1,0,
        1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,24,8,1,10,1,12,1,
        27,9,1,1,1,1,1,1,1,1,1,5,1,33,8,1,10,1,12,1,36,9,1,1,1,3,1,39,8,
        1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,47,8,1,10,1,12,1,50,9,1,1,1,1,1,1,
        1,1,1,5,1,56,8,1,10,1,12,1,59,9,1,1,1,3,1,62,8,1,1,1,1,1,1,1,1,1,
        1,1,3,1,69,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,78,8,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,89,8,2,10,2,12,2,92,9,2,1,2,0,1,4,
        3,0,2,4,0,0,105,0,7,1,0,0,0,2,68,1,0,0,0,4,77,1,0,0,0,6,8,3,2,1,
        0,7,6,1,0,0,0,8,9,1,0,0,0,9,7,1,0,0,0,9,10,1,0,0,0,10,11,1,0,0,0,
        11,12,5,0,0,1,12,1,1,0,0,0,13,14,5,1,0,0,14,15,5,5,0,0,15,16,5,9,
        0,0,16,17,3,4,2,0,17,18,5,10,0,0,18,69,1,0,0,0,19,20,5,2,0,0,20,
        21,3,4,2,0,21,25,5,13,0,0,22,24,3,2,1,0,23,22,1,0,0,0,24,27,1,0,
        0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,28,1,0,0,0,27,25,1,0,0,0,28,38,
        5,14,0,0,29,30,5,3,0,0,30,34,5,13,0,0,31,33,3,2,1,0,32,31,1,0,0,
        0,33,36,1,0,0,0,34,32,1,0,0,0,34,35,1,0,0,0,35,37,1,0,0,0,36,34,
        1,0,0,0,37,39,5,14,0,0,38,29,1,0,0,0,38,39,1,0,0,0,39,69,1,0,0,0,
        40,41,5,2,0,0,41,42,5,11,0,0,42,43,3,4,2,0,43,44,5,12,0,0,44,48,
        5,13,0,0,45,47,3,2,1,0,46,45,1,0,0,0,47,50,1,0,0,0,48,46,1,0,0,0,
        48,49,1,0,0,0,49,51,1,0,0,0,50,48,1,0,0,0,51,61,5,14,0,0,52,53,5,
        3,0,0,53,57,5,13,0,0,54,56,3,2,1,0,55,54,1,0,0,0,56,59,1,0,0,0,57,
        55,1,0,0,0,57,58,1,0,0,0,58,60,1,0,0,0,59,57,1,0,0,0,60,62,5,14,
        0,0,61,52,1,0,0,0,61,62,1,0,0,0,62,69,1,0,0,0,63,64,5,4,0,0,64,65,
        5,11,0,0,65,66,5,7,0,0,66,67,5,12,0,0,67,69,5,10,0,0,68,13,1,0,0,
        0,68,19,1,0,0,0,68,40,1,0,0,0,68,63,1,0,0,0,69,3,1,0,0,0,70,71,6,
        2,-1,0,71,72,5,11,0,0,72,73,3,4,2,0,73,74,5,12,0,0,74,78,1,0,0,0,
        75,78,5,5,0,0,76,78,5,6,0,0,77,70,1,0,0,0,77,75,1,0,0,0,77,76,1,
        0,0,0,78,90,1,0,0,0,79,80,10,6,0,0,80,81,5,17,0,0,81,89,3,4,2,7,
        82,83,10,5,0,0,83,84,5,15,0,0,84,89,3,4,2,6,85,86,10,4,0,0,86,87,
        5,16,0,0,87,89,3,4,2,5,88,79,1,0,0,0,88,82,1,0,0,0,88,85,1,0,0,0,
        89,92,1,0,0,0,90,88,1,0,0,0,90,91,1,0,0,0,91,5,1,0,0,0,92,90,1,0,
        0,0,11,9,25,34,38,48,57,61,68,77,88,90
    ]

class MyDSLParser ( Parser ):

    grammarFileName = "MyDSLParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'let'", "'if'", "'else'", "'print'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'='", "';'", "'('", "')'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "LET", "IF", "ELSE", "PRINT", "ID", "NUMBER", 
                      "STRING", "WS", "EQUAL", "SEMICOLON", "LPAREN", "RPAREN", 
                      "LBRACE", "RBRACE", "OP1", "OP2", "COMPARE" ]

    RULE_prog = 0
    RULE_stmt = 1
    RULE_expr = 2

    ruleNames =  [ "prog", "stmt", "expr" ]

    EOF = Token.EOF
    LET=1
    IF=2
    ELSE=3
    PRINT=4
    ID=5
    NUMBER=6
    STRING=7
    WS=8
    EQUAL=9
    SEMICOLON=10
    LPAREN=11
    RPAREN=12
    LBRACE=13
    RBRACE=14
    OP1=15
    OP2=16
    COMPARE=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MyDSLParser.EOF, 0)

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
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.stmt()
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 22) != 0)):
                    break

            self.state = 11
            self.match(MyDSLParser.EOF)
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

        def PRINT(self):
            return self.getToken(MyDSLParser.PRINT, 0)
        def LPAREN(self):
            return self.getToken(MyDSLParser.LPAREN, 0)
        def STRING(self):
            return self.getToken(MyDSLParser.STRING, 0)
        def RPAREN(self):
            return self.getToken(MyDSLParser.RPAREN, 0)
        def SEMICOLON(self):
            return self.getToken(MyDSLParser.SEMICOLON, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)


    class IfElseContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyDSLParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(MyDSLParser.IF, 0)
        def expr(self):
            return self.getTypedRuleContext(MyDSLParser.ExprContext,0)

        def LBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(MyDSLParser.LBRACE)
            else:
                return self.getToken(MyDSLParser.LBRACE, i)
        def RBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(MyDSLParser.RBRACE)
            else:
                return self.getToken(MyDSLParser.RBRACE, i)
        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyDSLParser.StmtContext)
            else:
                return self.getTypedRuleContext(MyDSLParser.StmtContext,i)

        def ELSE(self):
            return self.getToken(MyDSLParser.ELSE, 0)
        def LPAREN(self):
            return self.getToken(MyDSLParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(MyDSLParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfElse" ):
                return visitor.visitIfElse(self)
            else:
                return visitor.visitChildren(self)


    class VariableAssignContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyDSLParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LET(self):
            return self.getToken(MyDSLParser.LET, 0)
        def ID(self):
            return self.getToken(MyDSLParser.ID, 0)
        def EQUAL(self):
            return self.getToken(MyDSLParser.EQUAL, 0)
        def expr(self):
            return self.getTypedRuleContext(MyDSLParser.ExprContext,0)

        def SEMICOLON(self):
            return self.getToken(MyDSLParser.SEMICOLON, 0)

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
            self.state = 68
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = MyDSLParser.VariableAssignContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.match(MyDSLParser.LET)
                self.state = 14
                self.match(MyDSLParser.ID)
                self.state = 15
                self.match(MyDSLParser.EQUAL)
                self.state = 16
                self.expr(0)
                self.state = 17
                self.match(MyDSLParser.SEMICOLON)
                pass

            elif la_ == 2:
                localctx = MyDSLParser.IfElseContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self.match(MyDSLParser.IF)
                self.state = 20
                self.expr(0)
                self.state = 21
                self.match(MyDSLParser.LBRACE)
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 22) != 0):
                    self.state = 22
                    self.stmt()
                    self.state = 27
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 28
                self.match(MyDSLParser.RBRACE)
                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==3:
                    self.state = 29
                    self.match(MyDSLParser.ELSE)
                    self.state = 30
                    self.match(MyDSLParser.LBRACE)
                    self.state = 34
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 22) != 0):
                        self.state = 31
                        self.stmt()
                        self.state = 36
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 37
                    self.match(MyDSLParser.RBRACE)


                pass

            elif la_ == 3:
                localctx = MyDSLParser.IfElseContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 40
                self.match(MyDSLParser.IF)
                self.state = 41
                self.match(MyDSLParser.LPAREN)
                self.state = 42
                self.expr(0)
                self.state = 43
                self.match(MyDSLParser.RPAREN)
                self.state = 44
                self.match(MyDSLParser.LBRACE)
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 22) != 0):
                    self.state = 45
                    self.stmt()
                    self.state = 50
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 51
                self.match(MyDSLParser.RBRACE)
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==3:
                    self.state = 52
                    self.match(MyDSLParser.ELSE)
                    self.state = 53
                    self.match(MyDSLParser.LBRACE)
                    self.state = 57
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 22) != 0):
                        self.state = 54
                        self.stmt()
                        self.state = 59
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 60
                    self.match(MyDSLParser.RBRACE)


                pass

            elif la_ == 4:
                localctx = MyDSLParser.PrintContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 63
                self.match(MyDSLParser.PRINT)
                self.state = 64
                self.match(MyDSLParser.LPAREN)
                self.state = 65
                self.match(MyDSLParser.STRING)
                self.state = 66
                self.match(MyDSLParser.RPAREN)
                self.state = 67
                self.match(MyDSLParser.SEMICOLON)
                pass


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

        def LPAREN(self):
            return self.getToken(MyDSLParser.LPAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyDSLParser.ExprContext)
            else:
                return self.getTypedRuleContext(MyDSLParser.ExprContext,i)


        def RPAREN(self):
            return self.getToken(MyDSLParser.RPAREN, 0)

        def ID(self):
            return self.getToken(MyDSLParser.ID, 0)

        def NUMBER(self):
            return self.getToken(MyDSLParser.NUMBER, 0)

        def COMPARE(self):
            return self.getToken(MyDSLParser.COMPARE, 0)

        def OP1(self):
            return self.getToken(MyDSLParser.OP1, 0)

        def OP2(self):
            return self.getToken(MyDSLParser.OP2, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.state = 71
                self.match(MyDSLParser.LPAREN)
                self.state = 72
                self.expr(0)
                self.state = 73
                self.match(MyDSLParser.RPAREN)
                pass
            elif token in [5]:
                self.state = 75
                self.match(MyDSLParser.ID)
                pass
            elif token in [6]:
                self.state = 76
                self.match(MyDSLParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 90
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 88
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = MyDSLParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 79
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 80
                        self.match(MyDSLParser.COMPARE)
                        self.state = 81
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = MyDSLParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 82
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 83
                        self.match(MyDSLParser.OP1)
                        self.state = 84
                        self.expr(6)
                        pass

                    elif la_ == 3:
                        localctx = MyDSLParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 85
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 86
                        self.match(MyDSLParser.OP2)
                        self.state = 87
                        self.expr(5)
                        pass

             
                self.state = 92
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

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
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         




