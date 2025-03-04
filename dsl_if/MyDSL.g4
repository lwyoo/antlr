grammar MyDSL;

prog: stmt* ;  // 프로그램은 여러 개의 stmt(문장)로 구성

stmt: 'let' ID '=' expr ';'  # VariableAssign
    | 'if' expr '{' stmt* '}' ('else' '{' stmt* '}')?  # IfElse
    | 'print' '(' STRING ')' ';'  # Print
    ;

expr: ID | NUMBER | expr ('+'|'-'|'*'|'/') expr | '(' expr ')' | expr ('>'|'<'|'=='|'!='|'>='|'<=') expr ;

ID: [a-zA-Z_][a-zA-Z_0-9]* ;
NUMBER: [0-9]+ ;
STRING: '"' ~["]* '"' ;
WS: [ \t\r\n]+ -> skip;
