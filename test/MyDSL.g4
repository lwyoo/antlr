grammar MyDSL;

prog   : assign EOF ;  

assign : 'this' '=' 'match' '(' IDENT ')' '{' cases '}' ; 

cases  : case (',' case)* ;  // 여러 개의 패턴을 허용

case   : '(' pattern ')' '=>' IDENT ; 

pattern : HEX | '_' ; // 16진수 또는 와일드카드

HEX   : '0x' [0-9a-fA-F]+ ;  // 16진수 정규 표현식
IDENT : [a-zA-Z_][a-zA-Z0-9_]* ; // 변수 및 식별자

WS    : [ \t\r\n]+ -> skip ;  // 공백 무시
