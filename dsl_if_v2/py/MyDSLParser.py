# Generated from MyDSLParser.g4 by ANTLR 4.13.0
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
        4,1,16,68,2,0,7,0,2,1,7,1,2,2,7,2,1,0,4,0,8,8,0,11,0,12,0,9,1,0,
        1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,24,8,1,10,1,12,1,
        27,9,1,1,1,1,1,1,1,1,1,5,1,33,8,1,10,1,12,1,36,9,1,1,1,3,1,39,8,
        1,1,1,1,1,1,1,1,1,1,1,3,1,46,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,
        55,8,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,63,8,2,10,2,12,2,66,9,2,1,2,0,
        1,4,3,0,2,4,0,0,74,0,7,1,0,0,0,2,45,1,0,0,0,4,54,1,0,0,0,6,8,3,2,
        1,0,7,6,1,0,0,0,8,9,1,0,0,0,9,7,1,0,0,0,9,10,1,0,0,0,10,11,1,0,0,
        0,11,12,5,0,0,1,12,1,1,0,0,0,13,14,5,1,0,0,14,15,5,5,0,0,15,16,5,
        9,0,0,16,17,3,4,2,0,17,18,5,10,0,0,18,46,1,0,0,0,19,20,5,2,0,0,20,
        21,3,4,2,0,21,25,5,13,0,0,22,24,3,2,1,0,23,22,1,0,0,0,24,27,1,0,
        0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,28,1,0,0,0,27,25,1,0,0,0,28,38,
        5,14,0,0,29,30,5,3,0,0,30,34,5,13,0,0,31,33,3,2,1,0,32,31,1,0,0,
        0,33,36,1,0,0,0,34,32,1,0,0,0,34,35,1,0,0,0,35,37,1,0,0,0,36,34,
        1,0,0,0,37,39,5,14,0,0,38,29,1,0,0,0,38,39,1,0,0,0,39,46,1,0,0,0,
        40,41,5,4,0,0,41,42,5,11,0,0,42,43,5,7,0,0,43,44,5,12,0,0,44,46,
        5,10,0,0,45,13,1,0,0,0,45,19,1,0,0,0,45,40,1,0,0,0,46,3,1,0,0,0,
        47,48,6,2,-1,0,48,55,5,5,0,0,49,55,5,6,0,0,50,51,5,11,0,0,51,52,
        3,4,2,0,52,53,5,12,0,0,53,55,1,0,0,0,54,47,1,0,0,0,54,49,1,0,0,0,
        54,50,1,0,0,0,55,64,1,0,0,0,56,57,10,3,0,0,57,58,5,15,0,0,58,63,
        3,4,2,4,59,60,10,1,0,0,60,61,5,16,0,0,61,63,3,4,2,2,62,56,1,0,0,
        0,62,59,1,0,0,0,63,66,1,0,0,0,64,62,1,0,0,0,64,65,1,0,0,0,65,5,1,
        0,0,0,66,64,1,0,0,0,8,9,25,34,38,45,54,62,64
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
                      "LBRACE", "RBRACE", "OP", "COMPARE" ]

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
    OP=15
    COMPARE=16

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
            self.state = 45
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
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
            elif token in [2]:
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
            elif token in [4]:
                localctx = MyDSLParser.PrintContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 40
                self.match(MyDSLParser.PRINT)
                self.state = 41
                self.match(MyDSLParser.LPAREN)
                self.state = 42
                self.match(MyDSLParser.STRING)
                self.state = 43
                self.match(MyDSLParser.RPAREN)
                self.state = 44
                self.match(MyDSLParser.SEMICOLON)
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

        def LPAREN(self):
            return self.getToken(MyDSLParser.LPAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyDSLParser.ExprContext)
            else:
                return self.getTypedRuleContext(MyDSLParser.ExprContext,i)


        def RPAREN(self):
            return self.getToken(MyDSLParser.RPAREN, 0)

        def OP(self):
            return self.getToken(MyDSLParser.OP, 0)

        def COMPARE(self):
            return self.getToken(MyDSLParser.COMPARE, 0)

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
            self.state = 54
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.state = 48
                self.match(MyDSLParser.ID)
                pass
            elif token in [6]:
                self.state = 49
                self.match(MyDSLParser.NUMBER)
                pass
            elif token in [11]:
                self.state = 50
                self.match(MyDSLParser.LPAREN)
                self.state = 51
                self.expr(0)
                self.state = 52
                self.match(MyDSLParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 64
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 62
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = MyDSLParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 56
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 57
                        self.match(MyDSLParser.OP)
                        self.state = 58
                        self.expr(4)
                        pass

                    elif la_ == 2:
                        localctx = MyDSLParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 59
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 60
                        self.match(MyDSLParser.COMPARE)
                        self.state = 61
                        self.expr(2)
                        pass

             
                self.state = 66
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
         




