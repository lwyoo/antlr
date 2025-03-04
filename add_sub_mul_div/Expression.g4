grammar Expression;  // 문법의 이름을 정의

expr: expr ('+'|'-') term  # AddSub
    | term                 # TermExpr
    ;

term: term ('*'|'/') factor  # MulDiv
    | factor                 # FactorTerm
    ;

factor: NUMBER            # Number
      | '(' expr ')'      # Parens
      ;

NUMBER: [0-9]+;  // 숫자 정의
WS: [ \t\r\n]+ -> skip;  // 공백 및 개행 문자 무시

