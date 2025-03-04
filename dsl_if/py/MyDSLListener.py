# Generated from MyDSL.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .MyDSLParser import MyDSLParser
else:
    from MyDSLParser import MyDSLParser

# This class defines a complete listener for a parse tree produced by MyDSLParser.
class MyDSLListener(ParseTreeListener):

    # Enter a parse tree produced by MyDSLParser#prog.
    def enterProg(self, ctx:MyDSLParser.ProgContext):
        pass

    # Exit a parse tree produced by MyDSLParser#prog.
    def exitProg(self, ctx:MyDSLParser.ProgContext):
        pass


    # Enter a parse tree produced by MyDSLParser#VariableAssign.
    def enterVariableAssign(self, ctx:MyDSLParser.VariableAssignContext):
        pass

    # Exit a parse tree produced by MyDSLParser#VariableAssign.
    def exitVariableAssign(self, ctx:MyDSLParser.VariableAssignContext):
        pass


    # Enter a parse tree produced by MyDSLParser#IfElse.
    def enterIfElse(self, ctx:MyDSLParser.IfElseContext):
        pass

    # Exit a parse tree produced by MyDSLParser#IfElse.
    def exitIfElse(self, ctx:MyDSLParser.IfElseContext):
        pass


    # Enter a parse tree produced by MyDSLParser#Print.
    def enterPrint(self, ctx:MyDSLParser.PrintContext):
        pass

    # Exit a parse tree produced by MyDSLParser#Print.
    def exitPrint(self, ctx:MyDSLParser.PrintContext):
        pass


    # Enter a parse tree produced by MyDSLParser#expr.
    def enterExpr(self, ctx:MyDSLParser.ExprContext):
        pass

    # Exit a parse tree produced by MyDSLParser#expr.
    def exitExpr(self, ctx:MyDSLParser.ExprContext):
        pass



del MyDSLParser