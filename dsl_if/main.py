from antlr4 import *    # antlr 관련 기능 가져오기

# ANTLR이 자동 생성한 파일들
from MyDSLLexer import MyDSLLexer       # 입력을 토큰으로 변환
from MyDSLParser import MyDSLParser     # 토큰을 구문 분석하여 트리 생성
from MyDSLVisitor import MyDSLVisitor   # 트리를 탐색하며 C++ 코드 생성

# ANTLR의 MyDSLVisitor를 상속받아, DSL 문법을 방문(visit)할 때마다 C++ 코드를 생성
# visitXXX() 메서드들은 MyDSL.g4에 정의된 문법을 기반으로 동작
class CodeGenerator(MyDSLVisitor):
    # 프로그램 시작
    # prog (프로그램 전체)를 방문할 때 실행됨.
    # 여러 개의 stmt(문장)를 \n으로 연결하여 C++ 코드로 변환.
    def visitProg(self, ctx):
        # ctx.stmt(): prog 아래에 있는 모든 문장(stmt)을 리스트로 반환
        # prog
        # ├── stmt (let x = 10)
        # ├── stmt (let y = 20)
        # ├── stmt (if x > y)
        # │    ├── expr (x > y)
        # │    ├── stmt (print("x is greater"))
        # │    ├── stmt (else)
        # │        ├── stmt (print("y is greater"))
        return "\n".join([self.visit(stmt) for stmt in ctx.stmt()])

    def visitVariableAssign(self, ctx):
        return f"int {ctx.ID().getText()} = {self.visit(ctx.expr())};"

    def visitPrint(self, ctx):
        return f'std::cout << {ctx.STRING().getText()} << std::endl;'

    def visitIfElse(self, ctx):
        cond = self.visit(ctx.expr())

        # if-body 처리
        if ctx.stmt(0):  # if 블록이 비어있지 않은 경우
            if isinstance(ctx.stmt(0), list):  
                if_body = "\n".join([self.visit(stmt) for stmt in ctx.stmt(0)])
            else:  
                if_body = self.visit(ctx.stmt(0))  # 하나의 stmt만 있는 경우 직접 방문
        else:
            if_body = ""

        # else-body 처리
        if ctx.stmt(1):  # else 블록이 있을 때만
            if isinstance(ctx.stmt(1), list):
                else_body = "\n".join([self.visit(stmt) for stmt in ctx.stmt(1)])
            else:
                else_body = self.visit(ctx.stmt(1))
        else:
            else_body = ""

        return f"if ({cond}) {{\n{if_body}\n}} else {{\n{else_body}\n}}"



    def visitExpr(self, ctx):
        if ctx.NUMBER():
            return ctx.NUMBER().getText()
        elif ctx.ID():
            return ctx.ID().getText()
        else:
            left = self.visit(ctx.expr(0))
            op = ctx.getChild(1).getText()
            right = self.visit(ctx.expr(1))
            return f"({left} {op} {right})"

def generate_cpp_code(input_text):
    lexer = MyDSLLexer(InputStream(input_text))  # 토큰화
    tokens = CommonTokenStream(lexer)  # 토큰 스트림 생성
    parser = MyDSLParser(tokens)  # 파서 생성
    tree = parser.prog()  # 트리 생성
    print("🔹 생성된 파싱 트리:\n", tree.toStringTree(recog=parser))  # ✅ 파싱 트리 출력
        # prog  ← visitor.visit(tree)에서 visitProg() 호출
        # ├── stmt (let x = 10)
        # ├── stmt (let y = 20)
        # ├── stmt (if x > y)
        # │    ├── expr (x > y)
        # │    ├── stmt (print("x is greater"))
        # │    ├── stmt (else)
        # │        ├── stmt (print("y is greater"))

    visitor = CodeGenerator()  # C++ 코드 생성기

    # 내부적으로 visitProg() 호출함
    return visitor.visit(tree)  # 트리 방문 및 변환 실행

dsl_code = """
let x = 10;
let y = 20;
if x > y {
    print("x is greater");
} else {
    print("y is greater");
}
"""

cpp_code = generate_cpp_code(dsl_code)
print("cpp_code\n", cpp_code)

with open("output.cpp", "w") as f:
    f.write(f"#include <iostream>\nint main() {{\n{cpp_code}\nreturn 0;\n}}")

print("C++ 코드가 생성되었습니다: output.cpp")

