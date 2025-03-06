from antlr4 import *
from py.MyDSLLexer import MyDSLLexer
from py.MyDSLParser import MyDSLParser
from py.MyDSLParserVisitor import MyDSLParserVisitor

class CodeGenerator(MyDSLParserVisitor):
    def visitProg(self, ctx):
        return "\n".join(self.visit(stmt) for stmt in ctx.stmt())

    def visitAssignment(self, ctx):
        var_name = ctx.ID().getText()
        match_expr = self.visit(ctx.matchExpr())
        return f"{match_expr}".replace("THIS_VAR", var_name)

    def visitMatchExpr(self, ctx):
        var_name = ctx.parentCtx.ID().getText()
        args = [arg.getText() for arg in ctx.paramList().ID()]
        cases = self.visit(ctx.matchCaseList())

        for i, arg in enumerate(args):
            cases = cases.replace(f"ARGS_{i}", arg)

        return cases.replace("THIS_VAR", var_name)

    def visitMatchCaseList(self, ctx):
        cases = [self.visit(case) for case in ctx.matchCase()]
        default_case = None

        if ctx.defaultCase():
            default_case = self.visit(ctx.defaultCase())

        cpp_code = ""

        if cases:
            first_condition, first_result = cases[0]
            if first_condition != "true":
                cpp_code += f"if ({first_condition}) {{\n  THIS_VAR = {first_result};\n}}"
            else:
                cpp_code += f"THIS_VAR = {first_result};"

        for condition, result in cases[1:]:
            if condition != "true":
                cpp_code += f" else if ({condition}) {{\n  THIS_VAR = {result};\n}}"
            else:
                default_case = result

        if default_case:
            cpp_code += f" else {{\n  THIS_VAR = {default_case};\n}}"

        return cpp_code

    def visitMatchCase(self, ctx):
        values = [self.visit(param) for param in ctx.paramValues().paramValue()]
        
        conditions = []
        for i, value in enumerate(values):
            if value and value.strip():  # ✅ `None` 체크 추가
                conditions.append(f"ARGS_{i} == {value}")

        condition = " && ".join(conditions) if conditions else "true"
        result = self.visit(ctx.expression() or ctx.value())

        return (condition, result)






    def visitDefaultCase(self, ctx):
        return self.visit(ctx.expression() or ctx.value())

    def visitExpression(self, ctx):
        terms = [self.visit(term) for term in ctx.term()]
        operators = [op.getText() for op in ctx.getTokens(MyDSLParser.PLUS) + ctx.getTokens(MyDSLParser.MINUS)]

        expr = terms[0]
        for i in range(len(operators)):
            expr += f" {operators[i]} {terms[i + 1]}"

        return expr

    def visitTerm(self, ctx):
        factors = [self.visit(factor) for factor in ctx.factor()]
        operators = [op.getText() for op in ctx.getTokens(MyDSLParser.MUL) + ctx.getTokens(MyDSLParser.DIV)]

        expr = factors[0]
        for i in range(len(operators)):
            expr += f" {operators[i]} {factors[i + 1]}"

        return expr

    def visitFactor(self, ctx):
        if ctx.FLOAT():
            return ctx.FLOAT().getText()  # ✅ 부동소수점 처리
        elif ctx.NUMBER():
            return ctx.NUMBER().getText()
        elif ctx.ID():
            return ctx.ID().getText()
        elif ctx.expression():
            return f"({self.visit(ctx.expression())})"

    def visitValue(self, ctx):
        if ctx.NUMBER():
            return ctx.NUMBER().getText()
        elif ctx.ID():
            return ctx.ID().getText()
        elif ctx.UNDERSCORE():
            return ""  # `_`를 유지하여 비교에서 제거 가능


def generate_cpp_code(input_text):
    lexer = MyDSLLexer(InputStream(input_text))
    tokens = CommonTokenStream(lexer)
    parser = MyDSLParser(tokens)
    tree = parser.prog()

    visitor = CodeGenerator()
    cpp_code = visitor.visit(tree)

    with open("output.cpp", "w") as f:
        f.write(f"#include <iostream>\nint main() {{\n{cpp_code}\nreturn 0;\n}}")
    print("C++ 코드가 생성되었습니다: output.cpp")

    return cpp_code


# ✅ DSL 코드 예제
# dsl_code = """
# this = match(arg1, arg2, arg3) {
#   (0x1, 0x2, 0x3) => this,
#   (x, y, _) => OFF,
#   (_, y, _) => OFF,
#   (_, _, 0x3) => this + (arg1 * 0.00001)
# };
# """
dsl_code = """
this = match(arg1, arg2, arg3) {
  (0x1, 0x2, 0x3) => ON,
  (x, y, _) => OFF,
  (_, _, 0x3) => this + arg1 * 0.00001
};
"""

# ✅ 실행
cpp_code = generate_cpp_code(dsl_code)
if cpp_code:
    print("#include <iostream>\nint main() {\n" + cpp_code + "\nreturn 0;\n}")
else:
    print("C++ 코드 변환 실패")
