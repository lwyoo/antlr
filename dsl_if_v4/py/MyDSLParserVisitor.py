# Generated from MyDSLParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MyDSLParser import MyDSLParser
else:
    from MyDSLParser import MyDSLParser

# This class defines a complete generic visitor for a parse tree produced by MyDSLParser.

class MyDSLParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MyDSLParser#prog.
    def visitProg(self, ctx:MyDSLParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyDSLParser#ifElseOrIfElseIfElse.
    def visitIfElseOrIfElseIfElse(self, ctx:MyDSLParser.IfElseOrIfElseIfElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyDSLParser#VariableAssign.
    def visitVariableAssign(self, ctx:MyDSLParser.VariableAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyDSLParser#Print.
    def visitPrint(self, ctx:MyDSLParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyDSLParser#IfElse.
    def visitIfElse(self, ctx:MyDSLParser.IfElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyDSLParser#IfElseIfElse.
    def visitIfElseIfElse(self, ctx:MyDSLParser.IfElseIfElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyDSLParser#elifBlock.
    def visitElifBlock(self, ctx:MyDSLParser.ElifBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyDSLParser#elseBlock.
    def visitElseBlock(self, ctx:MyDSLParser.ElseBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyDSLParser#expr.
    def visitExpr(self, ctx:MyDSLParser.ExprContext):
        return self.visitChildren(ctx)



del MyDSLParser