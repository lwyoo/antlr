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
        4,1,17,121,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,4,0,30,8,0,11,0,12,0,31,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,2,1,2,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,5,4,54,8,4,10,4,12,4,
        57,9,4,1,5,1,5,1,5,5,5,62,8,5,10,5,12,5,65,9,5,1,5,1,5,3,5,69,8,
        5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,5,
        8,86,8,8,10,8,12,8,89,9,8,1,9,1,9,3,9,93,8,9,1,10,1,10,1,11,1,11,
        1,11,5,11,100,8,11,10,11,12,11,103,9,11,1,12,1,12,1,12,5,12,108,
        8,12,10,12,12,12,111,9,12,1,13,1,13,1,13,1,13,1,13,1,13,3,13,119,
        8,13,1,13,0,0,14,0,2,4,6,8,10,12,14,16,18,20,22,24,26,0,3,1,0,15,
        16,1,0,11,12,1,0,13,14,116,0,29,1,0,0,0,2,35,1,0,0,0,4,37,1,0,0,
        0,6,42,1,0,0,0,8,50,1,0,0,0,10,58,1,0,0,0,12,70,1,0,0,0,14,76,1,
        0,0,0,16,82,1,0,0,0,18,92,1,0,0,0,20,94,1,0,0,0,22,96,1,0,0,0,24,
        104,1,0,0,0,26,118,1,0,0,0,28,30,3,2,1,0,29,28,1,0,0,0,30,31,1,0,
        0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,33,1,0,0,0,33,34,5,0,0,1,34,1,
        1,0,0,0,35,36,3,4,2,0,36,3,1,0,0,0,37,38,5,15,0,0,38,39,5,3,0,0,
        39,40,3,6,3,0,40,41,5,10,0,0,41,5,1,0,0,0,42,43,5,1,0,0,43,44,5,
        5,0,0,44,45,3,8,4,0,45,46,5,6,0,0,46,47,5,7,0,0,47,48,3,10,5,0,48,
        49,5,8,0,0,49,7,1,0,0,0,50,55,5,15,0,0,51,52,5,9,0,0,52,54,5,15,
        0,0,53,51,1,0,0,0,54,57,1,0,0,0,55,53,1,0,0,0,55,56,1,0,0,0,56,9,
        1,0,0,0,57,55,1,0,0,0,58,63,3,12,6,0,59,60,5,9,0,0,60,62,3,12,6,
        0,61,59,1,0,0,0,62,65,1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,68,
        1,0,0,0,65,63,1,0,0,0,66,67,5,9,0,0,67,69,3,14,7,0,68,66,1,0,0,0,
        68,69,1,0,0,0,69,11,1,0,0,0,70,71,5,5,0,0,71,72,3,16,8,0,72,73,5,
        6,0,0,73,74,5,4,0,0,74,75,3,22,11,0,75,13,1,0,0,0,76,77,5,5,0,0,
        77,78,5,2,0,0,78,79,5,6,0,0,79,80,5,4,0,0,80,81,3,22,11,0,81,15,
        1,0,0,0,82,87,3,18,9,0,83,84,5,9,0,0,84,86,3,18,9,0,85,83,1,0,0,
        0,86,89,1,0,0,0,87,85,1,0,0,0,87,88,1,0,0,0,88,17,1,0,0,0,89,87,
        1,0,0,0,90,93,3,20,10,0,91,93,5,2,0,0,92,90,1,0,0,0,92,91,1,0,0,
        0,93,19,1,0,0,0,94,95,7,0,0,0,95,21,1,0,0,0,96,101,3,24,12,0,97,
        98,7,1,0,0,98,100,3,24,12,0,99,97,1,0,0,0,100,103,1,0,0,0,101,99,
        1,0,0,0,101,102,1,0,0,0,102,23,1,0,0,0,103,101,1,0,0,0,104,109,3,
        26,13,0,105,106,7,2,0,0,106,108,3,26,13,0,107,105,1,0,0,0,108,111,
        1,0,0,0,109,107,1,0,0,0,109,110,1,0,0,0,110,25,1,0,0,0,111,109,1,
        0,0,0,112,119,5,16,0,0,113,119,5,15,0,0,114,115,5,5,0,0,115,116,
        3,22,11,0,116,117,5,6,0,0,117,119,1,0,0,0,118,112,1,0,0,0,118,113,
        1,0,0,0,118,114,1,0,0,0,119,27,1,0,0,0,9,31,55,63,68,87,92,101,109,
        118
    ]

class MyDSLParser ( Parser ):

    grammarFileName = "MyDSLParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'match'", "'_'", "'='", "'=>'", "'('", 
                     "')'", "'{'", "'}'", "','", "';'", "'+'", "'-'", "'*'", 
                     "'/'" ]

    symbolicNames = [ "<INVALID>", "MATCH", "UNDERSCORE", "EQUAL", "ARROW", 
                      "LPAREN", "RPAREN", "LBRACE", "RBRACE", "COMMA", "SEMICOLON", 
                      "PLUS", "MINUS", "MUL", "DIV", "ID", "NUMBER", "WS" ]

    RULE_prog = 0
    RULE_stmt = 1
    RULE_assignment = 2
    RULE_matchExpr = 3
    RULE_paramList = 4
    RULE_matchCaseList = 5
    RULE_matchCase = 6
    RULE_defaultCase = 7
    RULE_paramValues = 8
    RULE_paramValue = 9
    RULE_value = 10
    RULE_expression = 11
    RULE_term = 12
    RULE_factor = 13

    ruleNames =  [ "prog", "stmt", "assignment", "matchExpr", "paramList", 
                   "matchCaseList", "matchCase", "defaultCase", "paramValues", 
                   "paramValue", "value", "expression", "term", "factor" ]

    EOF = Token.EOF
    MATCH=1
    UNDERSCORE=2
    EQUAL=3
    ARROW=4
    LPAREN=5
    RPAREN=6
    LBRACE=7
    RBRACE=8
    COMMA=9
    SEMICOLON=10
    PLUS=11
    MINUS=12
    MUL=13
    DIV=14
    ID=15
    NUMBER=16
    WS=17

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
            self.state = 29 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 28
                self.stmt()
                self.state = 31 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==15):
                    break

            self.state = 33
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

        def assignment(self):
            return self.getTypedRuleContext(MyDSLParser.AssignmentContext,0)


        def getRuleIndex(self):
            return MyDSLParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MyDSLParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.assignment()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MyDSLParser.ID, 0)

        def EQUAL(self):
            return self.getToken(MyDSLParser.EQUAL, 0)

        def matchExpr(self):
            return self.getTypedRuleContext(MyDSLParser.MatchExprContext,0)


        def SEMICOLON(self):
            return self.getToken(MyDSLParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MyDSLParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = MyDSLParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(MyDSLParser.ID)
            self.state = 38
            self.match(MyDSLParser.EQUAL)
            self.state = 39
            self.matchExpr()
            self.state = 40
            self.match(MyDSLParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatchExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MATCH(self):
            return self.getToken(MyDSLParser.MATCH, 0)

        def LPAREN(self):
            return self.getToken(MyDSLParser.LPAREN, 0)

        def paramList(self):
            return self.getTypedRuleContext(MyDSLParser.ParamListContext,0)


        def RPAREN(self):
            return self.getToken(MyDSLParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(MyDSLParser.LBRACE, 0)

        def matchCaseList(self):
            return self.getTypedRuleContext(MyDSLParser.MatchCaseListContext,0)


        def RBRACE(self):
            return self.getToken(MyDSLParser.RBRACE, 0)

        def getRuleIndex(self):
            return MyDSLParser.RULE_matchExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatchExpr" ):
                return visitor.visitMatchExpr(self)
            else:
                return visitor.visitChildren(self)




    def matchExpr(self):

        localctx = MyDSLParser.MatchExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_matchExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(MyDSLParser.MATCH)
            self.state = 43
            self.match(MyDSLParser.LPAREN)
            self.state = 44
            self.paramList()
            self.state = 45
            self.match(MyDSLParser.RPAREN)
            self.state = 46
            self.match(MyDSLParser.LBRACE)
            self.state = 47
            self.matchCaseList()
            self.state = 48
            self.match(MyDSLParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MyDSLParser.ID)
            else:
                return self.getToken(MyDSLParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MyDSLParser.COMMA)
            else:
                return self.getToken(MyDSLParser.COMMA, i)

        def getRuleIndex(self):
            return MyDSLParser.RULE_paramList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = MyDSLParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(MyDSLParser.ID)
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 51
                self.match(MyDSLParser.COMMA)
                self.state = 52
                self.match(MyDSLParser.ID)
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatchCaseListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def matchCase(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyDSLParser.MatchCaseContext)
            else:
                return self.getTypedRuleContext(MyDSLParser.MatchCaseContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MyDSLParser.COMMA)
            else:
                return self.getToken(MyDSLParser.COMMA, i)

        def defaultCase(self):
            return self.getTypedRuleContext(MyDSLParser.DefaultCaseContext,0)


        def getRuleIndex(self):
            return MyDSLParser.RULE_matchCaseList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatchCaseList" ):
                return visitor.visitMatchCaseList(self)
            else:
                return visitor.visitChildren(self)




    def matchCaseList(self):

        localctx = MyDSLParser.MatchCaseListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_matchCaseList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.matchCase()
            self.state = 63
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 59
                    self.match(MyDSLParser.COMMA)
                    self.state = 60
                    self.matchCase() 
                self.state = 65
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 66
                self.match(MyDSLParser.COMMA)
                self.state = 67
                self.defaultCase()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatchCaseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(MyDSLParser.LPAREN, 0)

        def paramValues(self):
            return self.getTypedRuleContext(MyDSLParser.ParamValuesContext,0)


        def RPAREN(self):
            return self.getToken(MyDSLParser.RPAREN, 0)

        def ARROW(self):
            return self.getToken(MyDSLParser.ARROW, 0)

        def expression(self):
            return self.getTypedRuleContext(MyDSLParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MyDSLParser.RULE_matchCase

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatchCase" ):
                return visitor.visitMatchCase(self)
            else:
                return visitor.visitChildren(self)




    def matchCase(self):

        localctx = MyDSLParser.MatchCaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_matchCase)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(MyDSLParser.LPAREN)
            self.state = 71
            self.paramValues()
            self.state = 72
            self.match(MyDSLParser.RPAREN)
            self.state = 73
            self.match(MyDSLParser.ARROW)
            self.state = 74
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefaultCaseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(MyDSLParser.LPAREN, 0)

        def UNDERSCORE(self):
            return self.getToken(MyDSLParser.UNDERSCORE, 0)

        def RPAREN(self):
            return self.getToken(MyDSLParser.RPAREN, 0)

        def ARROW(self):
            return self.getToken(MyDSLParser.ARROW, 0)

        def expression(self):
            return self.getTypedRuleContext(MyDSLParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MyDSLParser.RULE_defaultCase

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefaultCase" ):
                return visitor.visitDefaultCase(self)
            else:
                return visitor.visitChildren(self)




    def defaultCase(self):

        localctx = MyDSLParser.DefaultCaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_defaultCase)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(MyDSLParser.LPAREN)
            self.state = 77
            self.match(MyDSLParser.UNDERSCORE)
            self.state = 78
            self.match(MyDSLParser.RPAREN)
            self.state = 79
            self.match(MyDSLParser.ARROW)
            self.state = 80
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamValuesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyDSLParser.ParamValueContext)
            else:
                return self.getTypedRuleContext(MyDSLParser.ParamValueContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MyDSLParser.COMMA)
            else:
                return self.getToken(MyDSLParser.COMMA, i)

        def getRuleIndex(self):
            return MyDSLParser.RULE_paramValues

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamValues" ):
                return visitor.visitParamValues(self)
            else:
                return visitor.visitChildren(self)




    def paramValues(self):

        localctx = MyDSLParser.ParamValuesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_paramValues)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.paramValue()
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 83
                self.match(MyDSLParser.COMMA)
                self.state = 84
                self.paramValue()
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(MyDSLParser.ValueContext,0)


        def UNDERSCORE(self):
            return self.getToken(MyDSLParser.UNDERSCORE, 0)

        def getRuleIndex(self):
            return MyDSLParser.RULE_paramValue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamValue" ):
                return visitor.visitParamValue(self)
            else:
                return visitor.visitChildren(self)




    def paramValue(self):

        localctx = MyDSLParser.ParamValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_paramValue)
        try:
            self.state = 92
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15, 16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 90
                self.value()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 91
                self.match(MyDSLParser.UNDERSCORE)
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


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(MyDSLParser.NUMBER, 0)

        def ID(self):
            return self.getToken(MyDSLParser.ID, 0)

        def getRuleIndex(self):
            return MyDSLParser.RULE_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = MyDSLParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            _la = self._input.LA(1)
            if not(_la==15 or _la==16):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyDSLParser.TermContext)
            else:
                return self.getTypedRuleContext(MyDSLParser.TermContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(MyDSLParser.PLUS)
            else:
                return self.getToken(MyDSLParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(MyDSLParser.MINUS)
            else:
                return self.getToken(MyDSLParser.MINUS, i)

        def getRuleIndex(self):
            return MyDSLParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = MyDSLParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.term()
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11 or _la==12:
                self.state = 97
                _la = self._input.LA(1)
                if not(_la==11 or _la==12):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 98
                self.term()
                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyDSLParser.FactorContext)
            else:
                return self.getTypedRuleContext(MyDSLParser.FactorContext,i)


        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(MyDSLParser.MUL)
            else:
                return self.getToken(MyDSLParser.MUL, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(MyDSLParser.DIV)
            else:
                return self.getToken(MyDSLParser.DIV, i)

        def getRuleIndex(self):
            return MyDSLParser.RULE_term

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = MyDSLParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.factor()
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13 or _la==14:
                self.state = 105
                _la = self._input.LA(1)
                if not(_la==13 or _la==14):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 106
                self.factor()
                self.state = 111
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(MyDSLParser.NUMBER, 0)

        def ID(self):
            return self.getToken(MyDSLParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MyDSLParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MyDSLParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MyDSLParser.RPAREN, 0)

        def getRuleIndex(self):
            return MyDSLParser.RULE_factor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = MyDSLParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_factor)
        try:
            self.state = 118
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 112
                self.match(MyDSLParser.NUMBER)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 113
                self.match(MyDSLParser.ID)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 114
                self.match(MyDSLParser.LPAREN)
                self.state = 115
                self.expression()
                self.state = 116
                self.match(MyDSLParser.RPAREN)
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





