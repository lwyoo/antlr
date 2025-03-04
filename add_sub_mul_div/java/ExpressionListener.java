// Generated from Expression.g4 by ANTLR 4.13.0
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link ExpressionParser}.
 */
public interface ExpressionListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by the {@code TermExpr}
	 * labeled alternative in {@link ExpressionParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterTermExpr(ExpressionParser.TermExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code TermExpr}
	 * labeled alternative in {@link ExpressionParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitTermExpr(ExpressionParser.TermExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code AddSub}
	 * labeled alternative in {@link ExpressionParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterAddSub(ExpressionParser.AddSubContext ctx);
	/**
	 * Exit a parse tree produced by the {@code AddSub}
	 * labeled alternative in {@link ExpressionParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitAddSub(ExpressionParser.AddSubContext ctx);
	/**
	 * Enter a parse tree produced by the {@code MulDiv}
	 * labeled alternative in {@link ExpressionParser#term}.
	 * @param ctx the parse tree
	 */
	void enterMulDiv(ExpressionParser.MulDivContext ctx);
	/**
	 * Exit a parse tree produced by the {@code MulDiv}
	 * labeled alternative in {@link ExpressionParser#term}.
	 * @param ctx the parse tree
	 */
	void exitMulDiv(ExpressionParser.MulDivContext ctx);
	/**
	 * Enter a parse tree produced by the {@code FactorTerm}
	 * labeled alternative in {@link ExpressionParser#term}.
	 * @param ctx the parse tree
	 */
	void enterFactorTerm(ExpressionParser.FactorTermContext ctx);
	/**
	 * Exit a parse tree produced by the {@code FactorTerm}
	 * labeled alternative in {@link ExpressionParser#term}.
	 * @param ctx the parse tree
	 */
	void exitFactorTerm(ExpressionParser.FactorTermContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Number}
	 * labeled alternative in {@link ExpressionParser#factor}.
	 * @param ctx the parse tree
	 */
	void enterNumber(ExpressionParser.NumberContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Number}
	 * labeled alternative in {@link ExpressionParser#factor}.
	 * @param ctx the parse tree
	 */
	void exitNumber(ExpressionParser.NumberContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Parens}
	 * labeled alternative in {@link ExpressionParser#factor}.
	 * @param ctx the parse tree
	 */
	void enterParens(ExpressionParser.ParensContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Parens}
	 * labeled alternative in {@link ExpressionParser#factor}.
	 * @param ctx the parse tree
	 */
	void exitParens(ExpressionParser.ParensContext ctx);
}