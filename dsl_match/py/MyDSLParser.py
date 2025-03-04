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
        4,1,13,85,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,4,0,22,8,0,11,0,12,0,23,1,0,1,0,1,
        1,1,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,
        4,1,4,5,4,46,8,4,10,4,12,4,49,9,4,1,5,1,5,1,5,5,5,54,8,5,10,5,12,
        5,57,9,5,1,5,1,5,3,5,61,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,
        1,7,1,7,1,7,1,8,1,8,1,8,5,8,78,8,8,10,8,12,8,81,9,8,1,9,1,9,1,9,
        0,0,10,0,2,4,6,8,10,12,14,16,18,0,1,2,0,2,2,11,12,79,0,21,1,0,0,
        0,2,27,1,0,0,0,4,29,1,0,0,0,6,34,1,0,0,0,8,42,1,0,0,0,10,50,1,0,
        0,0,12,62,1,0,0,0,14,68,1,0,0,0,16,74,1,0,0,0,18,82,1,0,0,0,20,22,
        3,2,1,0,21,20,1,0,0,0,22,23,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,
        24,25,1,0,0,0,25,26,5,0,0,1,26,1,1,0,0,0,27,28,3,4,2,0,28,3,1,0,
        0,0,29,30,5,11,0,0,30,31,5,3,0,0,31,32,3,6,3,0,32,33,5,10,0,0,33,
        5,1,0,0,0,34,35,5,1,0,0,35,36,5,5,0,0,36,37,3,8,4,0,37,38,5,6,0,
        0,38,39,5,7,0,0,39,40,3,10,5,0,40,41,5,8,0,0,41,7,1,0,0,0,42,47,
        5,11,0,0,43,44,5,9,0,0,44,46,5,11,0,0,45,43,1,0,0,0,46,49,1,0,0,
        0,47,45,1,0,0,0,47,48,1,0,0,0,48,9,1,0,0,0,49,47,1,0,0,0,50,55,3,
        12,6,0,51,52,5,9,0,0,52,54,3,12,6,0,53,51,1,0,0,0,54,57,1,0,0,0,
        55,53,1,0,0,0,55,56,1,0,0,0,56,60,1,0,0,0,57,55,1,0,0,0,58,59,5,
        9,0,0,59,61,3,14,7,0,60,58,1,0,0,0,60,61,1,0,0,0,61,11,1,0,0,0,62,
        63,5,5,0,0,63,64,3,16,8,0,64,65,5,6,0,0,65,66,5,4,0,0,66,67,5,11,
        0,0,67,13,1,0,0,0,68,69,5,5,0,0,69,70,5,2,0,0,70,71,5,6,0,0,71,72,
        5,4,0,0,72,73,5,11,0,0,73,15,1,0,0,0,74,79,3,18,9,0,75,76,5,9,0,
        0,76,78,3,18,9,0,77,75,1,0,0,0,78,81,1,0,0,0,79,77,1,0,0,0,79,80,
        1,0,0,0,80,17,1,0,0,0,81,79,1,0,0,0,82,83,7,0,0,0,83,19,1,0,0,0,
        5,23,47,55,60,79
    ]

class MyDSLParser ( Parser ):

    grammarFileName = "MyDSLParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'match'", "'_'", "'='", "'=>'", "'('", 
                     "')'", "'{'", "'}'", "','", "';'" ]

    symbolicNames = [ "<INVALID>", "MATCH", "UNDERSCORE", "EQUAL", "ARROW", 
                      "LPAREN", "RPAREN", "LBRACE", "RBRACE", "COMMA", "SEMICOLON", 
                      "ID", "NUMBER", "WS" ]

    RULE_prog = 0
    RULE_stmt = 1
    RULE_assignment = 2
    RULE_matchExpr = 3
    RULE_paramList = 4
    RULE_matchCaseList = 5
    RULE_matchCase = 6
    RULE_defaultCase = 7
    RULE_paramValues = 8
    RULE_value = 9

    ruleNames =  [ "prog", "stmt", "assignment", "matchExpr", "paramList", 
                   "matchCaseList", "matchCase", "defaultCase", "paramValues", 
                   "value" ]

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
    ID=11
    NUMBER=12
    WS=13

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
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self.stmt()
                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==11):
                    break

            self.state = 25
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
            self.state = 27
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
            self.state = 29
            self.match(MyDSLParser.ID)
            self.state = 30
            self.match(MyDSLParser.EQUAL)
            self.state = 31
            self.matchExpr()
            self.state = 32
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
            self.state = 34
            self.match(MyDSLParser.MATCH)
            self.state = 35
            self.match(MyDSLParser.LPAREN)
            self.state = 36
            self.paramList()
            self.state = 37
            self.match(MyDSLParser.RPAREN)
            self.state = 38
            self.match(MyDSLParser.LBRACE)
            self.state = 39
            self.matchCaseList()
            self.state = 40
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
            self.state = 42
            self.match(MyDSLParser.ID)
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 43
                self.match(MyDSLParser.COMMA)
                self.state = 44
                self.match(MyDSLParser.ID)
                self.state = 49
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
            self.state = 50
            self.matchCase()
            self.state = 55
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 51
                    self.match(MyDSLParser.COMMA)
                    self.state = 52
                    self.matchCase() 
                self.state = 57
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 58
                self.match(MyDSLParser.COMMA)
                self.state = 59
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

        def ID(self):
            return self.getToken(MyDSLParser.ID, 0)

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
            self.state = 62
            self.match(MyDSLParser.LPAREN)
            self.state = 63
            self.paramValues()
            self.state = 64
            self.match(MyDSLParser.RPAREN)
            self.state = 65
            self.match(MyDSLParser.ARROW)
            self.state = 66
            self.match(MyDSLParser.ID)
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

        def ID(self):
            return self.getToken(MyDSLParser.ID, 0)

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
            self.state = 68
            self.match(MyDSLParser.LPAREN)
            self.state = 69
            self.match(MyDSLParser.UNDERSCORE)
            self.state = 70
            self.match(MyDSLParser.RPAREN)
            self.state = 71
            self.match(MyDSLParser.ARROW)
            self.state = 72
            self.match(MyDSLParser.ID)
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

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyDSLParser.ValueContext)
            else:
                return self.getTypedRuleContext(MyDSLParser.ValueContext,i)


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
            self.state = 74
            self.value()
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 75
                self.match(MyDSLParser.COMMA)
                self.state = 76
                self.value()
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def UNDERSCORE(self):
            return self.getToken(MyDSLParser.UNDERSCORE, 0)

        def getRuleIndex(self):
            return MyDSLParser.RULE_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = MyDSLParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 6148) != 0)):
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





