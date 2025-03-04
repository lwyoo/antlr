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
        4,1,13,40,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,5,2,27,8,2,10,
        2,12,2,30,9,2,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,0,0,5,0,2,4,6,
        8,0,1,1,0,10,11,35,0,10,1,0,0,0,2,13,1,0,0,0,4,23,1,0,0,0,6,31,1,
        0,0,0,8,37,1,0,0,0,10,11,3,2,1,0,11,12,5,0,0,1,12,1,1,0,0,0,13,14,
        5,1,0,0,14,15,5,2,0,0,15,16,5,3,0,0,16,17,5,4,0,0,17,18,5,12,0,0,
        18,19,5,5,0,0,19,20,5,6,0,0,20,21,3,4,2,0,21,22,5,7,0,0,22,3,1,0,
        0,0,23,28,3,6,3,0,24,25,5,8,0,0,25,27,3,6,3,0,26,24,1,0,0,0,27,30,
        1,0,0,0,28,26,1,0,0,0,28,29,1,0,0,0,29,5,1,0,0,0,30,28,1,0,0,0,31,
        32,5,4,0,0,32,33,3,8,4,0,33,34,5,5,0,0,34,35,5,9,0,0,35,36,5,12,
        0,0,36,7,1,0,0,0,37,38,7,0,0,0,38,9,1,0,0,0,1,28
    ]

class MyDSLParser ( Parser ):

    grammarFileName = "MyDSL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'this'", "'='", "'match'", "'('", "')'", 
                     "'{'", "'}'", "','", "'=>'", "'_'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "HEX", "IDENT", 
                      "WS" ]

    RULE_prog = 0
    RULE_assign = 1
    RULE_cases = 2
    RULE_case = 3
    RULE_pattern = 4

    ruleNames =  [ "prog", "assign", "cases", "case", "pattern" ]

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
    HEX=11
    IDENT=12
    WS=13

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

        def assign(self):
            return self.getTypedRuleContext(MyDSLParser.AssignContext,0)


        def EOF(self):
            return self.getToken(MyDSLParser.EOF, 0)

        def getRuleIndex(self):
            return MyDSLParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = MyDSLParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.assign()
            self.state = 11
            self.match(MyDSLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(MyDSLParser.IDENT, 0)

        def cases(self):
            return self.getTypedRuleContext(MyDSLParser.CasesContext,0)


        def getRuleIndex(self):
            return MyDSLParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = MyDSLParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self.match(MyDSLParser.T__0)
            self.state = 14
            self.match(MyDSLParser.T__1)
            self.state = 15
            self.match(MyDSLParser.T__2)
            self.state = 16
            self.match(MyDSLParser.T__3)
            self.state = 17
            self.match(MyDSLParser.IDENT)
            self.state = 18
            self.match(MyDSLParser.T__4)
            self.state = 19
            self.match(MyDSLParser.T__5)
            self.state = 20
            self.cases()
            self.state = 21
            self.match(MyDSLParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CasesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def case(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyDSLParser.CaseContext)
            else:
                return self.getTypedRuleContext(MyDSLParser.CaseContext,i)


        def getRuleIndex(self):
            return MyDSLParser.RULE_cases

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCases" ):
                listener.enterCases(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCases" ):
                listener.exitCases(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCases" ):
                return visitor.visitCases(self)
            else:
                return visitor.visitChildren(self)




    def cases(self):

        localctx = MyDSLParser.CasesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_cases)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.case()
            self.state = 28
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 24
                self.match(MyDSLParser.T__7)
                self.state = 25
                self.case()
                self.state = 30
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CaseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pattern(self):
            return self.getTypedRuleContext(MyDSLParser.PatternContext,0)


        def IDENT(self):
            return self.getToken(MyDSLParser.IDENT, 0)

        def getRuleIndex(self):
            return MyDSLParser.RULE_case

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCase" ):
                listener.enterCase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCase" ):
                listener.exitCase(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCase" ):
                return visitor.visitCase(self)
            else:
                return visitor.visitChildren(self)




    def case(self):

        localctx = MyDSLParser.CaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_case)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(MyDSLParser.T__3)
            self.state = 32
            self.pattern()
            self.state = 33
            self.match(MyDSLParser.T__4)
            self.state = 34
            self.match(MyDSLParser.T__8)
            self.state = 35
            self.match(MyDSLParser.IDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PatternContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HEX(self):
            return self.getToken(MyDSLParser.HEX, 0)

        def getRuleIndex(self):
            return MyDSLParser.RULE_pattern

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPattern" ):
                listener.enterPattern(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPattern" ):
                listener.exitPattern(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPattern" ):
                return visitor.visitPattern(self)
            else:
                return visitor.visitChildren(self)




    def pattern(self):

        localctx = MyDSLParser.PatternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_pattern)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            _la = self._input.LA(1)
            if not(_la==10 or _la==11):
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





