import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;

public class Main {
    public static void main(String[] args) throws Exception {
        // 입력 받을 문자열 (예: "3 + 5 * (2 - 8)")
        String input = "3 + 5 * (2 - 8)";

        // 입력 스트림 생성
        CharStream charStream = CharStreams.fromString(input);

        // 렉서 생성 (토큰화)
        ExpressionLexer lexer = new ExpressionLexer(charStream);
        CommonTokenStream tokens = new CommonTokenStream(lexer);

        // 파서 생성
        ExpressionParser parser = new ExpressionParser(tokens);

        // 파싱 트리 생성 (expr 규칙 사용)
        ParseTree tree = parser.expr();

        // 트리 출력
        System.out.println(tree.toStringTree(parser));
    }
}

