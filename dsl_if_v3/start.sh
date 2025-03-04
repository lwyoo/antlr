PYTHONPATH=$(pwd)/py
antlr4 -Dlanguage=Python3 MyDSLLexer.g4 -o py;
antlr4 -Dlanguage=Python3 MyDSLParser.g4 -visitor -no-listener -o py;
python main.py

cat output.cpp
