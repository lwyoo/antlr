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
        arg_name = ctx.ID().getText()
        cases = self.visit(ctx.matchCaseList())

        return f"{cases}".replace("THIS_VAR", var_name).replace("ARG_VAR", arg_name)

    def visitMatchCaseList(self, ctx):
        cases = [self.visit(case) for case in ctx.matchCase()]
        default_case = self.visit(ctx.defaultCase())
        
        # 🔹 첫 번째 `if` 문 생성
        cpp_code = f"if (ARG_VAR == {cases[0][0]}) {{\n  THIS_VAR = {cases[0][1]};\n}}"
        
        # 🔹 나머지 `else if` 추가
        for case in cases[1:]:
            cpp_code += f" else if (ARG_VAR == {case[0]}) {{\n  THIS_VAR = {case[1]};\n}}"

        # 🔹 `else` 블록 추가
        cpp_code += f" else {{\n  THIS_VAR = {default_case};\n}}"

        return cpp_code

    def visitMatchCase(self, ctx):
        value = ctx.NUMBER().getText()
        result = ctx.ID().getText()
        return (value, result)

    def visitDefaultCase(self, ctx):
        return ctx.ID().getText()

def generate_cpp_code(input_text):
    lexer = MyDSLLexer(InputStream(input_text))
    tokens = CommonTokenStream(lexer)
    parser = MyDSLParser(tokens)
    tree = parser.prog()

    visitor = CodeGenerator()
    return visitor.visit(tree)

# ✅ DSL 코드 예제
dsl_code = """
this = match(arg1) {
  (0x1) => ON,
  (0x2) => OFF,
  (_) => DISPLAY_OFF,
};
"""

# ✅ C++ 코드 변환 실행
cpp_code = generate_cpp_code(dsl_code)
print("#include <iostream>\nint main() {\n" + cpp_code + "\nreturn 0;\n}")
