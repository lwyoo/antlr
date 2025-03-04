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

        # 🔹 ARGS_0, ARGS_1 등의 잘못된 명칭을 올바르게 `args[i]`로 대체
        for i, arg in enumerate(args):
            cases = cases.replace(f"ARGS_{i}", arg)

        return cases.replace("THIS_VAR", var_name)

    def visitParamList(self, ctx):
        return [ctx.ID(i).getText() for i in range(len(ctx.ID()))]

    def visitMatchCaseList(self, ctx):
        cases = [self.visit(case) for case in ctx.matchCase()]
        default_case = self.visit(ctx.defaultCase())

        # 🔹 첫 번째 `if` 문 생성
        cpp_code = f"if ({cases[0][0]}) {{\n  THIS_VAR = {cases[0][1]};\n}}"
        
        # 🔹 나머지 `else if` 추가
        for case in cases[1:]:
            cpp_code += f" else if ({case[0]}) {{\n  THIS_VAR = {case[1]};\n}}"

        # 🔹 `else` 블록 추가
        cpp_code += f" else {{\n  THIS_VAR = {default_case};\n}}"

        return cpp_code

    def visitMatchCase(self, ctx):
        values = [self.visit(value) for value in ctx.paramValues().value()]

        # 🔹 `_`(와일드카드) 처리: 해당 인자는 비교 조건에서 제외
        conditions = []
        for i, value in enumerate(values):
            if value != "true":  # `_`이면 무시
                conditions.append(f"ARGS_{i} == {value}")

        condition = " && ".join(conditions) if conditions else "true"  # 모든 `_`이면 항상 참
        result = ctx.ID().getText()
        return (condition, result)

    def visitDefaultCase(self, ctx):
        return ctx.ID().getText()

    def visitValue(self, ctx):
        if ctx.NUMBER():
            return ctx.NUMBER().getText()
        elif ctx.ID():
            return ctx.ID().getText()
        elif ctx.UNDERSCORE():
            return "true"  # `_`는 비교에서 제외됨

def generate_cpp_code(input_text):
    lexer = MyDSLLexer(InputStream(input_text))
    tokens = CommonTokenStream(lexer)
    parser = MyDSLParser(tokens)
    tree = parser.prog()

    visitor = CodeGenerator()
    return visitor.visit(tree)

# ✅ DSL 코드 예제
dsl_code = """
this = match(arg1, arg2) {
  (0x1, _) => ON,
  (x, y) => OFF,
  (_) => DISPLAY_OFF,
};
"""

# ✅ C++ 코드 변환 실행
cpp_code = generate_cpp_code(dsl_code)
print("#include <iostream>\nint main() {\n" + cpp_code + "\nreturn 0;\n}")
