parser grammar MyDSLParser;

options { tokenVocab=MyDSLLexer; }

prog: stmt+ EOF ;

stmt: assignment ;

assignment: ID EQUAL matchExpr SEMICOLON;

matchExpr: MATCH LPAREN ID RPAREN LBRACE matchCaseList RBRACE ;

matchCaseList: matchCase (COMMA matchCase)* COMMA? defaultCase COMMA?;

matchCase: LPAREN NUMBER RPAREN ARROW ID;
defaultCase: LPAREN UNDERSCORE RPAREN ARROW ID;
