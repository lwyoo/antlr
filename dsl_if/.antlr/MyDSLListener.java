// Generated from /home/ldg/tmp/antlr/example/dsl_if/MyDSL.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link MyDSLParser}.
 */
public interface MyDSLListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link MyDSLParser#prog}.
	 * @param ctx the parse tree
	 */
	void enterProg(MyDSLParser.ProgContext ctx);
	/**
	 * Exit a parse tree produced by {@link MyDSLParser#prog}.
	 * @param ctx the parse tree
	 */
	void exitProg(MyDSLParser.ProgContext ctx);
	/**
	 * Enter a parse tree produced by the {@code VariableAssign}
	 * labeled alternative in {@link MyDSLParser#stmt}.
	 * @param ctx the parse tree
	 */
	void enterVariableAssign(MyDSLParser.VariableAssignContext ctx);
	/**
	 * Exit a parse tree produced by the {@code VariableAssign}
	 * labeled alternative in {@link MyDSLParser#stmt}.
	 * @param ctx the parse tree
	 */
	void exitVariableAssign(MyDSLParser.VariableAssignContext ctx);
	/**
	 * Enter a parse tree produced by the {@code IfElse}
	 * labeled alternative in {@link MyDSLParser#stmt}.
	 * @param ctx the parse tree
	 */
	void enterIfElse(MyDSLParser.IfElseContext ctx);
	/**
	 * Exit a parse tree produced by the {@code IfElse}
	 * labeled alternative in {@link MyDSLParser#stmt}.
	 * @param ctx the parse tree
	 */
	void exitIfElse(MyDSLParser.IfElseContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Print}
	 * labeled alternative in {@link MyDSLParser#stmt}.
	 * @param ctx the parse tree
	 */
	void enterPrint(MyDSLParser.PrintContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Print}
	 * labeled alternative in {@link MyDSLParser#stmt}.
	 * @param ctx the parse tree
	 */
	void exitPrint(MyDSLParser.PrintContext ctx);
	/**
	 * Enter a parse tree produced by {@link MyDSLParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(MyDSLParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link MyDSLParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(MyDSLParser.ExprContext ctx);
}