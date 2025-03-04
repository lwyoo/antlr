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

        # ✅ 첫 번째 if 문 생성
        if cases:
            first_condition, first_result = cases[0]
            if first_condition != "true":
                cpp_code += f"if ({first_condition}) {{\n  THIS_VAR = {first_result};\n}}"
            else:
                cpp_code += f"THIS_VAR = {first_result};"

        # ✅ 나머지 `else if` 추가
        for condition, result in cases[1:]:
            if condition != "true":
                cpp_code += f" else if ({condition}) {{\n  THIS_VAR = {result};\n}}"
            else:
                default_case = result  # `true`는 `else`로 변환

        # ✅ `_`(와일드카드) 또는 기본 케이스가 있으면 `else` 추가
        if default_case:
            cpp_code += f" else {{\n  THIS_VAR = {default_case};\n}}"

        return cpp_code

    def visitMatchCase(self, ctx):
        values = [self.visit(value) for value in ctx.paramValues().value()]
        
        conditions = []
        for i, value in enumerate(values):
            if value != "_":  # `_`(와일드카드)는 비교하지 않음
                conditions.append(f"ARGS_{i} == {value}")

        condition = " && ".join(conditions) if conditions else "true"
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
            return "_"  # `_` 유지


def generate_cpp_code(input_text):
    try:
        lexer = MyDSLLexer(InputStream(input_text))
        tokens = CommonTokenStream(lexer)
        parser = MyDSLParser(tokens)
        tree = parser.prog()

        visitor = CodeGenerator()
        cpp_code = visitor.visit(tree)

        # 🔹 파일 생성
        with open("output.cpp", "w") as f:
            f.write(f"#include <iostream>\nint main() {{\n{cpp_code}\nreturn 0;\n}}")
        print("C++ 코드가 생성되었습니다: output.cpp")

        return cpp_code
    except Exception as e:
        print(f"오류 발생: {e}")
        return ""

# ✅ DSL 코드 예제
dsl_code = """
this = match(arg1, arg2, arg3) {
  (0x1, 0x2, 0x3) => ON,
  (x, y, _) => OFF,
  (_, y, _) => OFF,
  (_, _, _) => DISPLAY_OFF,
};
"""

# ✅ C++ 코드 변환 실행
cpp_code = generate_cpp_code(dsl_code)
if cpp_code:
    print("#include <iostream>\nint main() {\n" + cpp_code + "\nreturn 0;\n}")
else:
    print("C++ 코드 변환 실패")
