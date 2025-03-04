# pip install matplotlib
import matplotlib.pyplot as plt
#pip install networkx
import networkx as nx
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


# 🔹 트리를 트리 형태로 그리도록 노드 배치하는 함수
def hierarchy_pos(G, root=None, width=2., vert_gap=0.6, xcenter=0.5):
    pos = _hierarchy_pos(G, root, width, vert_gap, xcenter, depth=0)
    return pos

def _hierarchy_pos(G, root, width, vert_gap, xcenter, depth=0, pos=None, parent=None, parsed=[]):
    if pos is None:
        pos = {root: (xcenter, 1 - depth * vert_gap)}
    else:
        pos[root] = (xcenter, 1 - depth * vert_gap)

    children = list(G.neighbors(root))
    if not isinstance(G, nx.DiGraph):
        children = [node for node in children if node not in parsed]
    if children:
        dx = width / len(children) 
        nextx = xcenter - width / 2 - dx / 2
        for child in children:
            nextx += dx
            pos = _hierarchy_pos(G, child, width=dx, vert_gap=vert_gap,
                                 xcenter=nextx, depth=depth+1, pos=pos,
                                 parent=root, parsed=parsed+[root])
    return pos

# 🔹 트리를 그래프 형태로 변환하는 함수
def build_ast_graph(node, graph, parent=None):
    node_id = str(id(node))
    label = node.getText() if hasattr(node, 'getText') else node.__class__.__name__

    graph.add_node(node_id, label=label)
    if parent:
        graph.add_edge(parent, node_id)

    for i in range(node.getChildCount()):
        child = node.getChild(i)
        build_ast_graph(child, graph, node_id)


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
    # 🔹 AST 그래프 생성
    graph = nx.DiGraph()
    build_ast_graph(tree, graph)

    # 🔹 트리 형태로 레이아웃 조정
    pos = hierarchy_pos(graph, root=str(id(tree)))

    # 🔹 그래프 그리기
    plt.figure(figsize=(10, 6))
    labels = nx.get_node_attributes(graph, 'label')
    nx.draw(graph, pos, with_labels=True, labels=labels, node_size=3000, node_color='lightblue', font_size=10, font_weight="bold", edge_color="gray")
    plt.title("ANTLR AST Visualization", fontsize=14)
    plt.show()
    print("\n생성된 AST 파싱 트리:\n%s\n" % tree.toStringTree(recog=parser))  # ✅ 파싱 트리 출력

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
