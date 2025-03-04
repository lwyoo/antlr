parser grammar MyDSLParser;

options { tokenVocab=MyDSLLexer; }  // 🔹 Lexer에서 생성된 토큰 사용

prog: stmt+ EOF ;  // 🔹 최소한 하나 이상의 stmt가 필요함

stmt: ifElseStmt  # ifElseOrIfElseIfElse // `if-else` 또는 `if-else if-else`
    | LET ID EQUAL expr SEMICOLON  # VariableAssign
    | PRINT LPAREN STRING RPAREN SEMICOLON  # Print
    ;

ifElseStmt: IF expr LBRACE stmt* RBRACE (elseBlock)? # IfElse
          | IF expr LBRACE stmt* RBRACE elifBlock+ elseBlock? # IfElseIfElse
          ;  

elifBlock: ELSEIF expr LBRACE stmt* RBRACE;
elseBlock: ELSE LBRACE stmt* RBRACE;

expr: expr COMPARE expr  
    | expr OP1 expr 
    | expr OP2 expr 
    | LPAREN expr RPAREN 
    | ID  
    | NUMBER  
    ;
