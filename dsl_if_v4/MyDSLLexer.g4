lexer grammar MyDSLLexer;

LET: 'let';
IF: 'if';
ELSE: 'else';
ELSEIF: 'else if';  // 🔹 `else if`를 하나의 토큰으로 정의
PRINT: 'print';

ID: [a-zA-Z_][a-zA-Z_0-9]* ;  // 예약어보다 나중에 정의해야 함!

NUMBER: [0-9]+ ;
STRING: '"' ~["]* '"' ;
WS: [ \t\r\n]+ -> skip;

EQUAL: '=';
SEMICOLON: ';';
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';

OP1: ('*'|'/');
OP2: ('+'|'-');
COMPARE: ('>'|'<'|'=='|'!='|'>='|'<=');
