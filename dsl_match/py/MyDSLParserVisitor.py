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


    # Visit a parse tree produced by MyDSLParser#stmt.
    def visitStmt(self, ctx:MyDSLParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyDSLParser#assignment.
    def visitAssignment(self, ctx:MyDSLParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyDSLParser#matchExpr.
    def visitMatchExpr(self, ctx:MyDSLParser.MatchExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyDSLParser#matchCaseList.
    def visitMatchCaseList(self, ctx:MyDSLParser.MatchCaseListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyDSLParser#matchCase.
    def visitMatchCase(self, ctx:MyDSLParser.MatchCaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyDSLParser#defaultCase.
    def visitDefaultCase(self, ctx:MyDSLParser.DefaultCaseContext):
        return self.visitChildren(ctx)



del MyDSLParser