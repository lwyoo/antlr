from antlr4 import *
from MyDSLLexer import MyDSLLexer
from MyDSLParser import MyDSLParser
from MyDSLVisitor import MyDSLVisitor

class CppGenerator(MyDSLVisitor):
    def __init__(self):
        self.match_var = ""

    def visitAssign(self, ctx):
        self.match_var = ctx.IDENT().getText()  # match(arg1)에서 arg1 가져오기
        cases = self.visit(ctx.cases())  # case 변환
        return cases if cases else ""  # 반환 값이 없을 경우 빈 문자열 반환

    def visitCases(self, ctx):
        cases = [self.visit(case) for case in ctx.case()]
        default_case = None
        conditions = []

        for c in cases:
            if c.startswith("else"):
                default_case = c
            else:
                conditions.append(c)

        # if-else 조합 생성
        cpp_code = ""
        if conditions:
            cpp_code = "if " + " else ".join(conditions)
        if default_case:
            cpp_code += " " + default_case

        return cpp_code if cpp_code else ""  # 반환 값이 없으면 빈 문자열 반환

    def visitCase(self, ctx):
        pattern = self.visit(ctx.pattern())  # 0x1 또는 _
        result = ctx.IDENT().getText()  # ON, OFF 등

        if pattern == "_":  # 와일드카드 처리
            return f"else {{ this = \"{result}\"; }}"
        else:
            return f"if ({self.match_var} == {pattern}) {{ this = \"{result}\"; }}"

    def visitPattern(self, ctx):
        if ctx.HEX():
            return ctx.HEX().getText()  # 0x1 같은 값을 그대로 반환
        return "_"  # 와일드카드

def generate_cpp(input_str):
    lexer = MyDSLLexer(InputStream(input_str))
    stream = CommonTokenStream(lexer)
    parser = MyDSLParser(stream)
    tree = parser.prog()

    generator = CppGenerator()
    cpp_code = generator.visit(tree)  # 반환값을 변수에 저장
    return cpp_code if cpp_code else "/* Error: No code generated */"

if __name__ == "__main__":
    input_str = """this = match(arg1) {
      (0x1) => ON,
      (_) => OFF
    }"""
    
    cpp_code = generate_cpp(input_str)
    print("Generated C++ Code:\n", cpp_code)
