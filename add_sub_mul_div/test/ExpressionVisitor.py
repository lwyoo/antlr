# Generated from Expression.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .ExpressionParser import ExpressionParser
else:
    from ExpressionParser import ExpressionParser

# This class defines a complete generic visitor for a parse tree produced by ExpressionParser.

class ExpressionVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExpressionParser#TermExpr.
    def visitTermExpr(self, ctx:ExpressionParser.TermExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#AddSub.
    def visitAddSub(self, ctx:ExpressionParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#MulDiv.
    def visitMulDiv(self, ctx:ExpressionParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#FactorTerm.
    def visitFactorTerm(self, ctx:ExpressionParser.FactorTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#Number.
    def visitNumber(self, ctx:ExpressionParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#Parens.
    def visitParens(self, ctx:ExpressionParser.ParensContext):
        return self.visitChildren(ctx)



del ExpressionParser