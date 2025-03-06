lexer grammar MyDSLLexer;

MATCH: 'match';
UNDERSCORE: '_';
EQUAL: '=';
ARROW: '=>';
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
COMMA: ',';
SEMICOLON: ';';

PLUS: '+';
MINUS: '-';
MUL: '*';
DIV: '/';

ID: [a-zA-Z_][a-zA-Z_0-9]*;  // 변수 이름, 키워드
NUMBER: '0x'[0-9a-fA-F]+ | [0-9]+;  // 16진수 또는 10진수 숫자
WS: [ \t\r\n]+ -> skip;  // 공백 및 개행 무시
