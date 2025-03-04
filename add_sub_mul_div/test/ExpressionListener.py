# Generated from Expression.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .ExpressionParser import ExpressionParser
else:
    from ExpressionParser import ExpressionParser

# This class defines a complete listener for a parse tree produced by ExpressionParser.
class ExpressionListener(ParseTreeListener):

    # Enter a parse tree produced by ExpressionParser#TermExpr.
    def enterTermExpr(self, ctx:ExpressionParser.TermExprContext):
        pass

    # Exit a parse tree produced by ExpressionParser#TermExpr.
    def exitTermExpr(self, ctx:ExpressionParser.TermExprContext):
        pass


    # Enter a parse tree produced by ExpressionParser#AddSub.
    def enterAddSub(self, ctx:ExpressionParser.AddSubContext):
        pass

    # Exit a parse tree produced by ExpressionParser#AddSub.
    def exitAddSub(self, ctx:ExpressionParser.AddSubContext):
        pass


    # Enter a parse tree produced by ExpressionParser#MulDiv.
    def enterMulDiv(self, ctx:ExpressionParser.MulDivContext):
        pass

    # Exit a parse tree produced by ExpressionParser#MulDiv.
    def exitMulDiv(self, ctx:ExpressionParser.MulDivContext):
        pass


    # Enter a parse tree produced by ExpressionParser#FactorTerm.
    def enterFactorTerm(self, ctx:ExpressionParser.FactorTermContext):
        pass

    # Exit a parse tree produced by ExpressionParser#FactorTerm.
    def exitFactorTerm(self, ctx:ExpressionParser.FactorTermContext):
        pass


    # Enter a parse tree produced by ExpressionParser#Number.
    def enterNumber(self, ctx:ExpressionParser.NumberContext):
        pass

    # Exit a parse tree produced by ExpressionParser#Number.
    def exitNumber(self, ctx:ExpressionParser.NumberContext):
        pass


    # Enter a parse tree produced by ExpressionParser#Parens.
    def enterParens(self, ctx:ExpressionParser.ParensContext):
        pass

    # Exit a parse tree produced by ExpressionParser#Parens.
    def exitParens(self, ctx:ExpressionParser.ParensContext):
        pass



del ExpressionParser