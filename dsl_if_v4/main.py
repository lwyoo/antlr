from antlr4 import *
from py.MyDSLLexer import MyDSLLexer
from py.MyDSLParser import MyDSLParser
from py.MyDSLParserVisitor import MyDSLParserVisitor

class CodeGenerator(MyDSLParserVisitor):
    def visitProg(self, ctx):
        result = []
        for index, stmt in enumerate(ctx.stmt()):  
            print(f"🔹 stmt[{index}] 처리 중: {stmt.getText()}")
            print(f"stmt[{index}] 타입: {type(stmt)}")
            print(f"stmt[{index}] 클래스 이름: {stmt.__class__.__name__}")  
            result.append(self.visit(stmt))  
            print("\n\n")
        return "\n".join(result)

    def visitVariableAssign(self, ctx):
        print("visitVariableAssign() [%s]" % ctx.getText())
        return f"int {ctx.ID().getText()} = {self.visit(ctx.expr())};"

    def visitPrint(self, ctx):
        print("visitPrint() - ", ctx.getText())
        return f'std::cout << {ctx.STRING().getText()} << std::endl;'

    def visitIfElse(self, ctx):
        print("visitIfElse() - ", ctx.getText())  
        cond = self.visit(ctx.expr())  
        print("cond: ", cond)

        # 🔹 IF 블록 처리
        open_brace_index = next(i for i, child in enumerate(ctx.children) if child.getText() == "{")
        close_brace_index = next(i for i, child in enumerate(ctx.children) if child.getText() == "}")

        if_block_stmts = ctx.children[open_brace_index + 1: close_brace_index]  

        # 🔹 ELSE 블록 확인 및 처리
        else_body = ""
        if ctx.elseBlock():
            else_open_brace_index = next(i for i, child in enumerate(ctx.elseBlock().children) if child.getText() == "{")
            else_close_brace_index = next(i for i, child in enumerate(ctx.elseBlock().children) if child.getText() == "}")
            else_stmts = ctx.elseBlock().children[else_open_brace_index + 1: else_close_brace_index]
            else_body = "\n".join(self.visit(stmt) for stmt in else_stmts)
            else_body = f"else {{\n{else_body}\n}}"

        # 🔹 최종 C++ 코드 변환
        if_body = "\n".join(self.visit(stmt) for stmt in if_block_stmts)
        return f"if ({cond}) {{\n{if_body}\n}}\n{else_body}"
        
    def visitIfElseIfElse(self, ctx):
        print("visitIfElseIfElse() - ", ctx.getText())  
        cond = self.visit(ctx.expr())  
        print("cond: ", cond)

        # 🔹 IF 블록 처리
        open_brace_index = next(i for i, child in enumerate(ctx.children) if child.getText() == "{")
        close_brace_index = next(i for i, child in enumerate(ctx.children) if child.getText() == "}")

        if_block_stmts = ctx.children[open_brace_index + 1: close_brace_index]  

        # 🔹 ELSE IF 블록 처리
        elif_blocks = []
        for elif_ctx in ctx.elifBlock():  
            elif_cond = self.visit(elif_ctx.expr())  
            elif_open_brace_index = next(i for i, child in enumerate(elif_ctx.children) if child.getText() == "{")
            elif_close_brace_index = next(i for i, child in enumerate(elif_ctx.children) if child.getText() == "}")
            elif_stmts = elif_ctx.children[elif_open_brace_index + 1: elif_close_brace_index]  
            elif_body = "\n".join(self.visit(stmt) for stmt in elif_stmts)
            elif_blocks.append(f"else if ({elif_cond}) {{\n{elif_body}\n}}")

        # 🔹 ELSE 블록 처리
        else_body = ""
        if ctx.elseBlock():
            else_open_brace_index = next(i for i, child in enumerate(ctx.elseBlock().children) if child.getText() == "{")
            else_close_brace_index = next(i for i, child in enumerate(ctx.elseBlock().children) if child.getText() == "}")
            else_stmts = ctx.elseBlock().children[else_open_brace_index + 1: else_close_brace_index]
            else_body = "\n".join(self.visit(stmt) for stmt in else_stmts)
            else_body = f"else {{\n{else_body}\n}}"

        # 🔹 최종 C++ 코드 변환
        if_body = "\n".join(self.visit(stmt) for stmt in if_block_stmts)
        return f"if ({cond}) {{\n{if_body}\n}}\n" + "\n".join(elif_blocks) + f"\n{else_body}"

    def visitExpr(self, ctx):
        print("visitExpr() - ", ctx.getText())
        if ctx.NUMBER():
            print("visitExpr() - NUMBER")
            return ctx.NUMBER().getText()
        elif ctx.ID():
            print("visitExpr() - ID")
            return ctx.ID().getText()
        elif ctx.getChildCount() == 3 and ctx.getChild(0).getText() == "(":
            print("visitExpr() - PAREN")
            inner_expr = self.visit(ctx.expr(0))
            return f"({inner_expr})"  
        else:
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
    print("\n생성된 AST 파싱 트리:\n%s\n" % tree.toStringTree(recog=parser))

    visitor = CodeGenerator()
    return visitor.visit(tree)

dsl_code = """
let x = 10;
let y = 20;
if x > y {
    print("x is greater");
    print("x is greater22222222222");
} else if x < y {
    print("x is greater");
    print("x is greater");
} else {
    print("y is greater");
    print("x is greater");
    print("x is greater22222222222");
}
"""

cpp_code = generate_cpp_code(dsl_code)

with open("output.cpp", "w") as f:
    f.write(f"#include <iostream>\nint main() {{\n{cpp_code}\nreturn 0;\n}}\n")

print("C++ 코드가 생성되었습니다: output.cpp")
