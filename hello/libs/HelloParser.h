
// Generated from Hello.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"




class  HelloParser : public antlr4::Parser {
public:
  enum {
    T__0 = 1, T__1 = 2, ID = 3, WS = 4
  };

  enum {
    RuleR = 0
  };

  explicit HelloParser(antlr4::TokenStream *input);

  HelloParser(antlr4::TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options);

  ~HelloParser() override;

  std::string getGrammarFileName() const override;

  const antlr4::atn::ATN& getATN() const override;

  const std::vector<std::string>& getRuleNames() const override;

  const antlr4::dfa::Vocabulary& getVocabulary() const override;

  antlr4::atn::SerializedATNView getSerializedATN() const override;


  class RContext; 

  class  RContext : public antlr4::ParserRuleContext {
  public:
    RContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *ID();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  RContext* r();


  // By default the static state used to implement the parser is lazily initialized during the first
  // call to the constructor. You can call this function if you wish to initialize the static state
  // ahead of time.
  static void initialize();

private:
};

