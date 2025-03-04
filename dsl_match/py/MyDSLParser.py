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
        4,1,13,64,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,4,0,16,8,0,11,0,12,0,17,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,2,1,
        2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,5,4,40,8,4,10,4,12,
        4,43,9,4,1,4,3,4,46,8,4,1,4,1,4,3,4,50,8,4,1,5,1,5,1,5,1,5,1,5,1,
        5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,0,0,7,0,2,4,6,8,10,12,0,0,60,0,15,
        1,0,0,0,2,21,1,0,0,0,4,23,1,0,0,0,6,28,1,0,0,0,8,36,1,0,0,0,10,51,
        1,0,0,0,12,57,1,0,0,0,14,16,3,2,1,0,15,14,1,0,0,0,16,17,1,0,0,0,
        17,15,1,0,0,0,17,18,1,0,0,0,18,19,1,0,0,0,19,20,5,0,0,1,20,1,1,0,
        0,0,21,22,3,4,2,0,22,3,1,0,0,0,23,24,5,11,0,0,24,25,5,3,0,0,25,26,
        3,6,3,0,26,27,5,10,0,0,27,5,1,0,0,0,28,29,5,1,0,0,29,30,5,5,0,0,
        30,31,5,11,0,0,31,32,5,6,0,0,32,33,5,7,0,0,33,34,3,8,4,0,34,35,5,
        8,0,0,35,7,1,0,0,0,36,41,3,10,5,0,37,38,5,9,0,0,38,40,3,10,5,0,39,
        37,1,0,0,0,40,43,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,45,1,0,0,
        0,43,41,1,0,0,0,44,46,5,9,0,0,45,44,1,0,0,0,45,46,1,0,0,0,46,47,
        1,0,0,0,47,49,3,12,6,0,48,50,5,9,0,0,49,48,1,0,0,0,49,50,1,0,0,0,
        50,9,1,0,0,0,51,52,5,5,0,0,52,53,5,12,0,0,53,54,5,6,0,0,54,55,5,
        4,0,0,55,56,5,11,0,0,56,11,1,0,0,0,57,58,5,5,0,0,58,59,5,2,0,0,59,
        60,5,6,0,0,60,61,5,4,0,0,61,62,5,11,0,0,62,13,1,0,0,0,4,17,41,45,
        49
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
    RULE_matchCaseList = 4
    RULE_matchCase = 5
    RULE_defaultCase = 6

    ruleNames =  [ "prog", "stmt", "assignment", "matchExpr", "matchCaseList", 
                   "matchCase", "defaultCase" ]

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
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.stmt()
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==11):
                    break

            self.state = 19
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
            self.state = 21
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
            self.state = 23
            self.match(MyDSLParser.ID)
            self.state = 24
            self.match(MyDSLParser.EQUAL)
            self.state = 25
            self.matchExpr()
            self.state = 26
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

        def ID(self):
            return self.getToken(MyDSLParser.ID, 0)

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
            self.state = 28
            self.match(MyDSLParser.MATCH)
            self.state = 29
            self.match(MyDSLParser.LPAREN)
            self.state = 30
            self.match(MyDSLParser.ID)
            self.state = 31
            self.match(MyDSLParser.RPAREN)
            self.state = 32
            self.match(MyDSLParser.LBRACE)
            self.state = 33
            self.matchCaseList()
            self.state = 34
            self.match(MyDSLParser.RBRACE)
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


        def defaultCase(self):
            return self.getTypedRuleContext(MyDSLParser.DefaultCaseContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MyDSLParser.COMMA)
            else:
                return self.getToken(MyDSLParser.COMMA, i)

        def getRuleIndex(self):
            return MyDSLParser.RULE_matchCaseList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatchCaseList" ):
                return visitor.visitMatchCaseList(self)
            else:
                return visitor.visitChildren(self)




    def matchCaseList(self):

        localctx = MyDSLParser.MatchCaseListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_matchCaseList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.matchCase()
            self.state = 41
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 37
                    self.match(MyDSLParser.COMMA)
                    self.state = 38
                    self.matchCase() 
                self.state = 43
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 44
                self.match(MyDSLParser.COMMA)


            self.state = 47
            self.defaultCase()
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 48
                self.match(MyDSLParser.COMMA)


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

        def NUMBER(self):
            return self.getToken(MyDSLParser.NUMBER, 0)

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
        self.enterRule(localctx, 10, self.RULE_matchCase)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(MyDSLParser.LPAREN)
            self.state = 52
            self.match(MyDSLParser.NUMBER)
            self.state = 53
            self.match(MyDSLParser.RPAREN)
            self.state = 54
            self.match(MyDSLParser.ARROW)
            self.state = 55
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
        self.enterRule(localctx, 12, self.RULE_defaultCase)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(MyDSLParser.LPAREN)
            self.state = 58
            self.match(MyDSLParser.UNDERSCORE)
            self.state = 59
            self.match(MyDSLParser.RPAREN)
            self.state = 60
            self.match(MyDSLParser.ARROW)
            self.state = 61
            self.match(MyDSLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





