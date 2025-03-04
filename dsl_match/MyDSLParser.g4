parser grammar MyDSLParser;

options { tokenVocab=MyDSLLexer; }

prog: stmt+ EOF ;

stmt: assignment ;

assignment: ID EQUAL matchExpr SEMICOLON;

matchExpr: MATCH LPAREN paramList RPAREN LBRACE matchCaseList RBRACE ;

paramList: ID (COMMA ID)* ;

matchCaseList: matchCase (COMMA matchCase)* (COMMA defaultCase)? ;  // 🔹 마지막 `,` 허용

matchCase: LPAREN paramValues RPAREN ARROW ID;
defaultCase: LPAREN UNDERSCORE RPAREN ARROW ID;

paramValues: value (COMMA value)* ;

value: NUMBER | ID | UNDERSCORE ;