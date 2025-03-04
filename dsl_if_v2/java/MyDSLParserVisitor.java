// Generated from MyDSLParser.g4 by ANTLR 4.13.0
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link MyDSLParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface MyDSLParserVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link MyDSLParser#prog}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProg(MyDSLParser.ProgContext ctx);
	/**
	 * Visit a parse tree produced by the {@code VariableAssign}
	 * labeled alternative in {@link MyDSLParser#stmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVariableAssign(MyDSLParser.VariableAssignContext ctx);
	/**
	 * Visit a parse tree produced by the {@code IfElse}
	 * labeled alternative in {@link MyDSLParser#stmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIfElse(MyDSLParser.IfElseContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Print}
	 * labeled alternative in {@link MyDSLParser#stmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPrint(MyDSLParser.PrintContext ctx);
	/**
	 * Visit a parse tree produced by {@link MyDSLParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpr(MyDSLParser.ExprContext ctx);
}