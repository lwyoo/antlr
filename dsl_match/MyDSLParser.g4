parser grammar MyDSLParser;

options { tokenVocab=MyDSLLexer; }

prog: stmt+ EOF ;

stmt: assignment ;

assignment: ID EQUAL matchExpr SEMICOLON;

matchExpr: MATCH LPAREN paramList RPAREN LBRACE matchCaseList RBRACE ;

paramList: ID (COMMA ID)* ;

matchCaseList: matchCase (COMMA matchCase)* (COMMA defaultCase)? ;

matchCase: LPAREN paramValues RPAREN ARROW expression;
defaultCase: LPAREN UNDERSCORE RPAREN ARROW expression;

paramValues: paramValue (COMMA paramValue)* ;
paramValue: value | UNDERSCORE ;  // ✅ `_`을 와일드카드로 처리
value: NUMBER | ID ;

expression: term ((PLUS | MINUS) term)* ;  // ✅ 연산자 지원
term: factor ((MUL | DIV) factor)* ;
factor: NUMBER | ID | LPAREN expression RPAREN ;
