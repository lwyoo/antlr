// 실패 
// parser grammar MyDSLParser;  // Parser 정의

// options { tokenVocab=MyDSLLexer; }  // 🔹 Lexer 파일 사용

// prog: stmt* ; // 문제 stmt*는 0개 이상의 문장을 허용하므로, ANTLR이 입력이 없을 때도 유효한 구문으로 간주할 수 있음.

// stmt: LET ID EQUAL expr SEMICOLON  # VariableAssign
//     | IF expr LBRACE stmt* RBRACE (ELSE LBRACE stmt* RBRACE)?  # IfElse
//     | PRINT LPAREN STRING RPAREN SEMICOLON  # Print
//     ;

// expr: ID 
//     | NUMBER 
//     | expr OP expr 
//     | LPAREN expr RPAREN 
//     | expr COMPARE expr ;

parser grammar MyDSLParser;

options { tokenVocab=MyDSLLexer; }  // 🔹 Lexer에서 생성된 토큰 사용

prog: stmt+ EOF ;  // 🔹 최소한 하나 이상의 stmt가 필요함

stmt: LET ID EQUAL expr SEMICOLON  # VariableAssign
    | IF expr LBRACE stmt* RBRACE (ELSE LBRACE stmt* RBRACE)?  # IfElse
    | PRINT LPAREN STRING RPAREN SEMICOLON  # Print
    ;

expr: ID 
    | NUMBER 
    | expr OP expr 
    | LPAREN expr RPAREN 
    | expr COMPARE expr ;
