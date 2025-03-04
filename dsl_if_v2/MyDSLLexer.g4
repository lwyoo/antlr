// 실패
// // ID=1
// // NUMBER=2
// // STRING=3
// // WS=4
// // LET=5
// // IF=6
// // ELSE=7
// // PRINT=8
// // EQUAL=9
// // SEMICOLON=10
// // LPAREN=11
// // RPAREN=12
// // LBRACE=13
// // RBRACE=14
// // OP=15
// // COMPARE=16
// lexer grammar MyDSLLexer;

// ID: [a-zA-Z_][a-zA-Z_0-9]* ; // ❌ 예약어보다 먼저 정의됨!, ID 정의 이후 예약어도 모두 ID 로 간주함
// NUMBER: [0-9]+ ;
// STRING: '"' ~["]* '"' ;
// WS: [ \t\r\n]+ -> skip;

// // 키워드 (예약어)
// LET: 'let';
// IF: 'if';
// ELSE: 'else';
// PRINT: 'print';

// // 연산자 및 기호
// EQUAL: '=';
// SEMICOLON: ';';
// LPAREN: '(';
// RPAREN: ')';
// LBRACE: '{';
// RBRACE: '}';
// OP: ('+'|'-'|'*'|'/');
// COMPARE: ('>'|'<'|'=='|'!='|'>='|'<=');


lexer grammar MyDSLLexer;

LET: 'let';
IF: 'if';
ELSE: 'else';
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
OP: ('+'|'-'|'*'|'/');
COMPARE: ('>'|'<'|'=='|'!='|'>='|'<=');

