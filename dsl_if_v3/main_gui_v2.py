#pip3 install graphviz
from graphviz import Digraph
from antlr4 import *
from py.MyDSLLexer import MyDSLLexer
from py.MyDSLParser import MyDSLParser
from py.MyDSLParserVisitor import MyDSLParserVisitor

class CodeGenerator(MyDSLParserVisitor):
    def visitProg(self, ctx):
        # print("visitProg() 실행됨!")  # 🔹 디버깅 출력 추가

        # for stmt in ctx.stmt():
        #     print(f"🔹 stmt 타입: {type(stmt)}")  # 🔹 stmt의 실제 타입 출력
        #     result = self.visit(stmt)  # 🔹 stmt를 방문
        #     print(f"🔹 visit({stmt}) 결과: {result}")  # 🔹 반환값 출력

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

def build_ast_graphviz(node, dot, parent=None):
    """ANTLR AST를 Graphviz 트리로 변환"""
    node_id = str(id(node))
    label = node.getText() if hasattr(node, 'getText') else node.__class__.__name__

    dot.node(node_id, label)  # 노드 추가
    if parent:
        dot.edge(parent, node_id)  # 부모-자식 간선 추가

    for i in range(node.getChildCount()):
        child = node.getChild(i)
        build_ast_graphviz(child, dot, node_id)

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
    # 🔹 Graphviz 트리 생성
    dot = Digraph(format='png')
    build_ast_graphviz(tree, dot)

    # 🔹 AST 트리 출력
    dot.render("ast_output")  # ast_output.png 파일 생성
    print("✅ AST 그래프가 ast_output.png로 저장되었습니다!")

    visitor = CodeGenerator()
    return visitor.visit(tree)

# DSL 코드 입력
dsl_code = """
let x = 10;
let y = 20;
if x > y {
    print("x is greater");
} else {
    print("y is greater");
}
"""

# C++ 코드 생성
cpp_code = generate_cpp_code(dsl_code)

# 결과 저장
with open("output.cpp", "w") as f:
    f.write(f"#include <iostream>\nint main() {{\n{cpp_code}\nreturn 0;\n}}")

print("C++ 코드가 생성되었습니다: output.cpp")
