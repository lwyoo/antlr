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


    # Visit a parse tree produced by MyDSLParser#assign.
    def visitAssign(self, ctx:MyDSLParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyDSLParser#cases.
    def visitCases(self, ctx:MyDSLParser.CasesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyDSLParser#case.
    def visitCase(self, ctx:MyDSLParser.CaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyDSLParser#pattern.
    def visitPattern(self, ctx:MyDSLParser.PatternContext):
        return self.visitChildren(ctx)



del MyDSLParser