// Hello.g4 - 예시 ANTLR 문법 파일
grammar Hello;

r   : 'hello' ID ;   // 예: "hello John" 과 같이 인식
ID  : [a-zA-Z]+ ;        // 하나 이상의 알파벳 문자
WS  : [ \t\r\n]+ -> skip ;  // 공백, 탭, 개행은 무시

