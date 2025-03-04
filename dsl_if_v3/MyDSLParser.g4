parser grammar MyDSLParser;

options { tokenVocab=MyDSLLexer; }  // 🔹 Lexer에서 생성된 토큰 사용

prog: stmt+ EOF ;  // 🔹 최소한 하나 이상의 stmt가 필요함

stmt: LET ID EQUAL expr SEMICOLON  # VariableAssign
    | IF expr LBRACE stmt* RBRACE (ELSE LBRACE stmt* RBRACE)?  # IfElse
    | IF LPAREN expr RPAREN LBRACE stmt* RBRACE (ELSE LBRACE stmt* RBRACE)?  # IfElse
    | PRINT LPAREN STRING RPAREN SEMICOLON  # Print
    ;

// expr: ID 
//     | NUMBER 
//     | expr OP expr 
//     | LPAREN expr RPAREN 
//     | expr COMPARE expr ;
expr: expr COMPARE expr  
    | expr OP1 expr 
    | expr OP2 expr 
    | LPAREN expr RPAREN 
    | ID  
    | NUMBER  
    ;

