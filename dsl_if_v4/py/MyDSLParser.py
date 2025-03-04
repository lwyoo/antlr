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
        4,1,18,111,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,4,
        0,14,8,0,11,0,12,0,15,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,3,1,32,8,1,1,2,1,2,1,2,1,2,5,2,38,8,2,10,2,12,2,41,
        9,2,1,2,1,2,3,2,45,8,2,1,2,1,2,1,2,1,2,5,2,51,8,2,10,2,12,2,54,9,
        2,1,2,1,2,4,2,58,8,2,11,2,12,2,59,1,2,3,2,63,8,2,3,2,65,8,2,1,3,
        1,3,1,3,1,3,5,3,71,8,3,10,3,12,3,74,9,3,1,3,1,3,1,4,1,4,1,4,5,4,
        81,8,4,10,4,12,4,84,9,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,
        95,8,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,106,8,5,10,5,12,5,
        109,9,5,1,5,0,1,10,6,0,2,4,6,8,10,0,0,120,0,13,1,0,0,0,2,31,1,0,
        0,0,4,64,1,0,0,0,6,66,1,0,0,0,8,77,1,0,0,0,10,94,1,0,0,0,12,14,3,
        2,1,0,13,12,1,0,0,0,14,15,1,0,0,0,15,13,1,0,0,0,15,16,1,0,0,0,16,
        17,1,0,0,0,17,18,5,0,0,1,18,1,1,0,0,0,19,32,3,4,2,0,20,21,5,1,0,
        0,21,22,5,6,0,0,22,23,5,10,0,0,23,24,3,10,5,0,24,25,5,11,0,0,25,
        32,1,0,0,0,26,27,5,5,0,0,27,28,5,12,0,0,28,29,5,8,0,0,29,30,5,13,
        0,0,30,32,5,11,0,0,31,19,1,0,0,0,31,20,1,0,0,0,31,26,1,0,0,0,32,
        3,1,0,0,0,33,34,5,2,0,0,34,35,3,10,5,0,35,39,5,14,0,0,36,38,3,2,
        1,0,37,36,1,0,0,0,38,41,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,42,
        1,0,0,0,41,39,1,0,0,0,42,44,5,15,0,0,43,45,3,8,4,0,44,43,1,0,0,0,
        44,45,1,0,0,0,45,65,1,0,0,0,46,47,5,2,0,0,47,48,3,10,5,0,48,52,5,
        14,0,0,49,51,3,2,1,0,50,49,1,0,0,0,51,54,1,0,0,0,52,50,1,0,0,0,52,
        53,1,0,0,0,53,55,1,0,0,0,54,52,1,0,0,0,55,57,5,15,0,0,56,58,3,6,
        3,0,57,56,1,0,0,0,58,59,1,0,0,0,59,57,1,0,0,0,59,60,1,0,0,0,60,62,
        1,0,0,0,61,63,3,8,4,0,62,61,1,0,0,0,62,63,1,0,0,0,63,65,1,0,0,0,
        64,33,1,0,0,0,64,46,1,0,0,0,65,5,1,0,0,0,66,67,5,4,0,0,67,68,3,10,
        5,0,68,72,5,14,0,0,69,71,3,2,1,0,70,69,1,0,0,0,71,74,1,0,0,0,72,
        70,1,0,0,0,72,73,1,0,0,0,73,75,1,0,0,0,74,72,1,0,0,0,75,76,5,15,
        0,0,76,7,1,0,0,0,77,78,5,3,0,0,78,82,5,14,0,0,79,81,3,2,1,0,80,79,
        1,0,0,0,81,84,1,0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,85,1,0,0,0,
        84,82,1,0,0,0,85,86,5,15,0,0,86,9,1,0,0,0,87,88,6,5,-1,0,88,89,5,
        12,0,0,89,90,3,10,5,0,90,91,5,13,0,0,91,95,1,0,0,0,92,95,5,6,0,0,
        93,95,5,7,0,0,94,87,1,0,0,0,94,92,1,0,0,0,94,93,1,0,0,0,95,107,1,
        0,0,0,96,97,10,6,0,0,97,98,5,18,0,0,98,106,3,10,5,7,99,100,10,5,
        0,0,100,101,5,16,0,0,101,106,3,10,5,6,102,103,10,4,0,0,103,104,5,
        17,0,0,104,106,3,10,5,5,105,96,1,0,0,0,105,99,1,0,0,0,105,102,1,
        0,0,0,106,109,1,0,0,0,107,105,1,0,0,0,107,108,1,0,0,0,108,11,1,0,
        0,0,109,107,1,0,0,0,13,15,31,39,44,52,59,62,64,72,82,94,105,107
    ]

class MyDSLParser ( Parser ):

    grammarFileName = "MyDSLParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'let'", "'if'", "'else'", "'else if'", 
                     "'print'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'='", "';'", "'('", "')'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "LET", "IF", "ELSE", "ELSEIF", "PRINT", 
                      "ID", "NUMBER", "STRING", "WS", "EQUAL", "SEMICOLON", 
                      "LPAREN", "RPAREN", "LBRACE", "RBRACE", "OP1", "OP2", 
                      "COMPARE" ]

    RULE_prog = 0
    RULE_stmt = 1
    RULE_ifElseStmt = 2
    RULE_elifBlock = 3
    RULE_elseBlock = 4
    RULE_expr = 5

    ruleNames =  [ "prog", "stmt", "ifElseStmt", "elifBlock", "elseBlock", 
                   "expr" ]

    EOF = Token.EOF
    LET=1
    IF=2
    ELSE=3
    ELSEIF=4
    PRINT=5
    ID=6
    NUMBER=7
    STRING=8
    WS=9
    EQUAL=10
    SEMICOLON=11
    LPAREN=12
    RPAREN=13
    LBRACE=14
    RBRACE=15
    OP1=16
    OP2=17
    COMPARE=18

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
            self.state = 13 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 12
                self.stmt()
                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 38) != 0)):
                    break

            self.state = 17
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


    class IfElseOrIfElseIfElseContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyDSLParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ifElseStmt(self):
            return self.getTypedRuleContext(MyDSLParser.IfElseStmtContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfElseOrIfElseIfElse" ):
                return visitor.visitIfElseOrIfElseIfElse(self)
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
        try:
            self.state = 31
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                localctx = MyDSLParser.IfElseOrIfElseIfElseContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self.ifElseStmt()
                pass
            elif token in [1]:
                localctx = MyDSLParser.VariableAssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.match(MyDSLParser.LET)
                self.state = 21
                self.match(MyDSLParser.ID)
                self.state = 22
                self.match(MyDSLParser.EQUAL)
                self.state = 23
                self.expr(0)
                self.state = 24
                self.match(MyDSLParser.SEMICOLON)
                pass
            elif token in [5]:
                localctx = MyDSLParser.PrintContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 26
                self.match(MyDSLParser.PRINT)
                self.state = 27
                self.match(MyDSLParser.LPAREN)
                self.state = 28
                self.match(MyDSLParser.STRING)
                self.state = 29
                self.match(MyDSLParser.RPAREN)
                self.state = 30
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


    class IfElseStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MyDSLParser.RULE_ifElseStmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IfElseIfElseContext(IfElseStmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyDSLParser.IfElseStmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(MyDSLParser.IF, 0)
        def expr(self):
            return self.getTypedRuleContext(MyDSLParser.ExprContext,0)

        def LBRACE(self):
            return self.getToken(MyDSLParser.LBRACE, 0)
        def RBRACE(self):
            return self.getToken(MyDSLParser.RBRACE, 0)
        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyDSLParser.StmtContext)
            else:
                return self.getTypedRuleContext(MyDSLParser.StmtContext,i)

        def elifBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyDSLParser.ElifBlockContext)
            else:
                return self.getTypedRuleContext(MyDSLParser.ElifBlockContext,i)

        def elseBlock(self):
            return self.getTypedRuleContext(MyDSLParser.ElseBlockContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfElseIfElse" ):
                return visitor.visitIfElseIfElse(self)
            else:
                return visitor.visitChildren(self)


    class IfElseContext(IfElseStmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyDSLParser.IfElseStmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(MyDSLParser.IF, 0)
        def expr(self):
            return self.getTypedRuleContext(MyDSLParser.ExprContext,0)

        def LBRACE(self):
            return self.getToken(MyDSLParser.LBRACE, 0)
        def RBRACE(self):
            return self.getToken(MyDSLParser.RBRACE, 0)
        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyDSLParser.StmtContext)
            else:
                return self.getTypedRuleContext(MyDSLParser.StmtContext,i)

        def elseBlock(self):
            return self.getTypedRuleContext(MyDSLParser.ElseBlockContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfElse" ):
                return visitor.visitIfElse(self)
            else:
                return visitor.visitChildren(self)



    def ifElseStmt(self):

        localctx = MyDSLParser.IfElseStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_ifElseStmt)
        self._la = 0 # Token type
        try:
            self.state = 64
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = MyDSLParser.IfElseContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.match(MyDSLParser.IF)
                self.state = 34
                self.expr(0)
                self.state = 35
                self.match(MyDSLParser.LBRACE)
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 38) != 0):
                    self.state = 36
                    self.stmt()
                    self.state = 41
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 42
                self.match(MyDSLParser.RBRACE)
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==3:
                    self.state = 43
                    self.elseBlock()


                pass

            elif la_ == 2:
                localctx = MyDSLParser.IfElseIfElseContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                self.match(MyDSLParser.IF)
                self.state = 47
                self.expr(0)
                self.state = 48
                self.match(MyDSLParser.LBRACE)
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 38) != 0):
                    self.state = 49
                    self.stmt()
                    self.state = 54
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 55
                self.match(MyDSLParser.RBRACE)
                self.state = 57 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 56
                    self.elifBlock()
                    self.state = 59 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==4):
                        break

                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==3:
                    self.state = 61
                    self.elseBlock()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(MyDSLParser.ELSEIF, 0)

        def expr(self):
            return self.getTypedRuleContext(MyDSLParser.ExprContext,0)


        def LBRACE(self):
            return self.getToken(MyDSLParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MyDSLParser.RBRACE, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyDSLParser.StmtContext)
            else:
                return self.getTypedRuleContext(MyDSLParser.StmtContext,i)


        def getRuleIndex(self):
            return MyDSLParser.RULE_elifBlock

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElifBlock" ):
                return visitor.visitElifBlock(self)
            else:
                return visitor.visitChildren(self)




    def elifBlock(self):

        localctx = MyDSLParser.ElifBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_elifBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(MyDSLParser.ELSEIF)
            self.state = 67
            self.expr(0)
            self.state = 68
            self.match(MyDSLParser.LBRACE)
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 38) != 0):
                self.state = 69
                self.stmt()
                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 75
            self.match(MyDSLParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MyDSLParser.ELSE, 0)

        def LBRACE(self):
            return self.getToken(MyDSLParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MyDSLParser.RBRACE, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyDSLParser.StmtContext)
            else:
                return self.getTypedRuleContext(MyDSLParser.StmtContext,i)


        def getRuleIndex(self):
            return MyDSLParser.RULE_elseBlock

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseBlock" ):
                return visitor.visitElseBlock(self)
            else:
                return visitor.visitChildren(self)




    def elseBlock(self):

        localctx = MyDSLParser.ElseBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_elseBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(MyDSLParser.ELSE)
            self.state = 78
            self.match(MyDSLParser.LBRACE)
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 38) != 0):
                self.state = 79
                self.stmt()
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 85
            self.match(MyDSLParser.RBRACE)
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
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.state = 88
                self.match(MyDSLParser.LPAREN)
                self.state = 89
                self.expr(0)
                self.state = 90
                self.match(MyDSLParser.RPAREN)
                pass
            elif token in [6]:
                self.state = 92
                self.match(MyDSLParser.ID)
                pass
            elif token in [7]:
                self.state = 93
                self.match(MyDSLParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 107
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 105
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = MyDSLParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 96
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 97
                        self.match(MyDSLParser.COMPARE)
                        self.state = 98
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = MyDSLParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 99
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 100
                        self.match(MyDSLParser.OP1)
                        self.state = 101
                        self.expr(6)
                        pass

                    elif la_ == 3:
                        localctx = MyDSLParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 102
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 103
                        self.match(MyDSLParser.OP2)
                        self.state = 104
                        self.expr(5)
                        pass

             
                self.state = 109
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

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
        self._predicates[5] = self.expr_sempred
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
         




