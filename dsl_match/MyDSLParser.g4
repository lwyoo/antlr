parser grammar MyDSLParser;

options { tokenVocab=MyDSLLexer; }

prog: stmt+ EOF ;

stmt: assignment ;

assignment: ID EQUAL matchExpr SEMICOLON;

matchExpr: MATCH LPAREN paramList RPAREN LBRACE matchCaseList RBRACE ;

paramList: ID (COMMA ID)* ;  // 여러 개의 변수 허용

matchCaseList: matchCase (COMMA matchCase)* COMMA? defaultCase COMMA?;

matchCase: LPAREN paramValues RPAREN ARROW ID;
defaultCase: LPAREN UNDERSCORE RPAREN ARROW ID;

paramValues: value (COMMA value)* ;

value: NUMBER | ID | UNDERSCORE ;
