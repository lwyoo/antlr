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


    # Enter a parse tree produced by MyDSLParser#assign.
    def enterAssign(self, ctx:MyDSLParser.AssignContext):
        pass

    # Exit a parse tree produced by MyDSLParser#assign.
    def exitAssign(self, ctx:MyDSLParser.AssignContext):
        pass


    # Enter a parse tree produced by MyDSLParser#cases.
    def enterCases(self, ctx:MyDSLParser.CasesContext):
        pass

    # Exit a parse tree produced by MyDSLParser#cases.
    def exitCases(self, ctx:MyDSLParser.CasesContext):
        pass


    # Enter a parse tree produced by MyDSLParser#case.
    def enterCase(self, ctx:MyDSLParser.CaseContext):
        pass

    # Exit a parse tree produced by MyDSLParser#case.
    def exitCase(self, ctx:MyDSLParser.CaseContext):
        pass


    # Enter a parse tree produced by MyDSLParser#pattern.
    def enterPattern(self, ctx:MyDSLParser.PatternContext):
        pass

    # Exit a parse tree produced by MyDSLParser#pattern.
    def exitPattern(self, ctx:MyDSLParser.PatternContext):
        pass



del MyDSLParser