from antlr4 import *
from py.MyDSLLexer import MyDSLLexer
from py.MyDSLParser import MyDSLParser
from py.MyDSLParserVisitor import MyDSLParserVisitor

class CodeGenerator(MyDSLParserVisitor):
    # def visitProg(self, ctx):

    #     for stmt in ctx.stmt():
    #         print("stmt (AST 트리):", stmt.getText())

    #     return "\n".join([self.visit(stmt) for stmt in ctx.stmt()])
    def visitProg(self, ctx):
        result = []
        for index, stmt in enumerate(ctx.stmt()):  # 🔹 enumerate()로 인덱스 추가
            print(f"🔹 stmt[{index}] 처리 중: {stmt.getText()}")  # 🔹 현재 문장의 인덱스 및 내용 출력
            print(f"stmt[{index}] 타입: {type(stmt)}")
            print(f"stmt[{index}] 클래스 이름: {stmt.__class__.__name__}")  # 🔹 클래스 이름 출력
            result.append(self.visit(stmt)) # visit(stmt)가 어떤 노드인지 자동으로 판별 & 그에 맞는 함수 호출 
            print("\n\n")
        return "\n".join(result)

    def visitVariableAssign(self, ctx):
        print("visitVariableAssign() [%s]" % ctx.getText())
        return f"int {ctx.ID().getText()} = {self.visit(ctx.expr())};"

    def visitPrint(self, ctx):
        print("visitPrint() - ", ctx.getText())
        return f'std::cout << {ctx.STRING().getText()} << std::endl;'

    def visitIfElse(self, ctx):
        print("visitIfElse() - ", ctx.getText())  # 🔹 전체 `if-else` 블록을 출력
        cond = self.visit(ctx.expr())  # 🔹 `if` 조건을 파싱
        print("cond: ", cond)

        # 🔹 전체 stmt 리스트 가져오기
        all_statements = ctx.stmt()
        print(f"🔹 전체 stmt 개수: {len(all_statements)}")

        # 🔹 `{`(LBRACE)와 `}`(RBRACE)의 위치 찾기
        open_brace_index = next(i for i, child in enumerate(ctx.children) if child.getText() == "{")
        close_brace_index = next(i for i, child in enumerate(ctx.children) if child.getText() == "}")
        print("open_brace_index: ", open_brace_index)
        print("close_brace_index: ", close_brace_index)

        # 🔹 ELSE 블록 존재 여부 확인
        if ctx.ELSE():
            # 🔹 ELSE가 있는 경우: `}` 이후부터 else 블록 시작
            if_block_stmts = all_statements[: (close_brace_index - open_brace_index - 1)]  # 🔹 `{}` 내부 stmt 개수 계산
            else_block_stmts = all_statements[(close_brace_index - open_brace_index - 1):]  # 🔹 ELSE 블록 stmt 가져오기
        else:
            # 🔹 ELSE가 없는 경우: 전체 stmt는 if 블록에 속함
            if_block_stmts = all_statements[: (close_brace_index - open_brace_index - 1)]
            else_block_stmts = []

        print(f"🔹 IF 블록 stmt 개수: {len(if_block_stmts)}")
        print(f"🔹 ELSE 블록 stmt 개수: {len(else_block_stmts)}")

        # 🔹 IF 블록 코드 변환
        if_body = "\n".join(self.visit(stmt) for stmt in if_block_stmts)

        # 🔹 ELSE 블록 코드 변환 (존재하는 경우만)
        if else_block_stmts:
            else_body = "\n".join(self.visit(stmt) for stmt in else_block_stmts)
            return f"if ({cond}) {{\n{if_body}\n}} else {{\n{else_body}\n}}"
        else:
            return f"if ({cond}) {{\n{if_body}\n}}"

    def visitExpr(self, ctx):
        print("visitExpr() - ", ctx.getText())
        if ctx.NUMBER():
            print("visitExpr() - NUMBER")
            return ctx.NUMBER().getText()
        elif ctx.ID():
            print("visitExpr() - ID")
            return ctx.ID().getText()
        elif ctx.getChildCount() == 3 and ctx.getChild(0).getText() == "(":
            # 🔹 괄호 처리: (expr)
            print("visitExpr() - PAREN")
            inner_expr = self.visit(ctx.expr(0))
            return f"({inner_expr})"  # 🔹 괄호 유지
        else:
            print("visitExpr() - ELSE")
            # print("ctx.expr(0): " , ctx.expr(0).getText())
            # print("ctx.getChild(0).getText(): " ,  ctx.getChild(0).getText())
            # print("ctx.getChild(1).getText(): " ,  ctx.getChild(1).getText())
            # print("ctx.getChild(2).getText(): " ,  ctx.getChild(2).getText())
            # print("ctx.getChildCount(): " ,  ctx.getChildCount())
            # print("ctx.expr 개수:", len(ctx.expr()))  # 🔹 ctx.expr()의 크기 출력

            # if 2 == len(ctx.expr()) and ctx.getChildCount() == 3:
            #     left = self.visit(ctx.expr(0))
            #     op = ctx.getChild(1).getText()
            #     right = self.visit(ctx.expr(1))
            #     return f"{left} {op} {right}"
            left = self.visit(ctx.expr(0))
            op = ctx.getChild(1).getText()
            right = self.visit(ctx.expr(1))
            return f"{left} {op} {right}"


def generate_cpp_code(input_text):
    lexer = MyDSLLexer(InputStream(input_text))
    tokens = CommonTokenStream(lexer)
    tokens.fill()
    print("생성된 토큰:")
    for token in tokens.tokens:
        print(f"TOKEN({token.type}): {token.text}")

    parser = MyDSLParser(tokens)
    tree = parser.prog()
    ##

    print("\n생성된 AST 파싱 트리:\n%s\n" % tree.toStringTree(recog=parser))  # ✅ 파싱 트리 출력

    visitor = CodeGenerator()
    return visitor.visit(tree)

# DSL 코드 입력
dsl_code = """
let x = 10;
let y = 20;
if x > y {
    print("x is greater");
    print("y~~ is greater");
    print("x is greater");
    print("y~~ is greater");
} else {
    print("y is greater");
    print("y is greater");
    print("y~~ is greater");
    print("y~~ is greater");
    print("y~~ is greater");
}
"""

# C++ 코드 생성
cpp_code = generate_cpp_code(dsl_code)

# 결과 저장
with open("output.cpp", "w") as f:
    f.write(f"#include <iostream>\nint main() {{\n{cpp_code}\nreturn 0;\n}}")

print("C++ 코드가 생성되었습니다: output.cpp")
