import sys
from antlr4 import *
from ExpressionLexer import ExpressionLexer
from ExpressionParser import ExpressionParser

def main():
    # 수식 입력 (예: "3 + 5 * (2 - 8)")
    input_stream = InputStream(input("Enter expression: "))

    # 렉서(Lexer) 생성 → 토큰화: 입력을 토큰 단위로 나누는 역할
    lexer = ExpressionLexer(input_stream)
	# 생성된 토큰들을 모아서 토큰 스트림을 생성
    token_stream = CommonTokenStream(lexer)

    # 파서(Parser) 생성 → 구문 분석
    parser = ExpressionParser(token_stream) # 토큰을 읽는다
    tree = parser.expr()  # expr 규칙 시작

    # 파싱 트리 출력
    print(tree.toStringTree(recog=parser))

if __name__ == "__main__":
    main()

