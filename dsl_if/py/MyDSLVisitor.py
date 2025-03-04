# Generated from MyDSL.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .MyDSLParser import MyDSLParser
else:
    from MyDSLParser import MyDSLParser

# This class defines a complete generic visitor for a parse tree produced by MyDSLParser.

class MyDSLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MyDSLParser#prog.
    def visitProg(self, ctx:MyDSLParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyDSLParser#VariableAssign.
    def visitVariableAssign(self, ctx:MyDSLParser.VariableAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyDSLParser#IfElse.
    def visitIfElse(self, ctx:MyDSLParser.IfElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyDSLParser#Print.
    def visitPrint(self, ctx:MyDSLParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyDSLParser#expr.
    def visitExpr(self, ctx:MyDSLParser.ExprContext):
        return self.visitChildren(ctx)



del MyDSLParser