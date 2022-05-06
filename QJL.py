from Interpreter import *
        
####################################################
#RUN
####################################################

global_symbol_table = SymbolTable()
global_symbol_table.set("MATH_PI", Number.math_PI)
global_symbol_table.set("NULL", Number.null)
global_symbol_table.set("TRUE", Number.true)
global_symbol_table.set("FALSE", Number.false)
global_symbol_table.set("PRINT", BuiltInFunction.print)
global_symbol_table.set("PRINT_RET", BuiltInFunction.print_ret)
global_symbol_table.set("INPUT", BuiltInFunction.input)
global_symbol_table.set("INPUT_INT", BuiltInFunction.input_int)
global_symbol_table.set("CLEAR", BuiltInFunction.clear)
global_symbol_table.set("CLS", BuiltInFunction.clear)
global_symbol_table.set("IS_NUM", BuiltInFunction.is_number)
global_symbol_table.set("IS_STR", BuiltInFunction.is_string)
global_symbol_table.set("IS_LIST", BuiltInFunction.is_list)
global_symbol_table.set("IS_FUN", BuiltInFunction.is_function)
global_symbol_table.set("APPEND", BuiltInFunction.append)
global_symbol_table.set("POP", BuiltInFunction.pop)
global_symbol_table.set("EXTEND", BuiltInFunction.extend)
global_symbol_table.set("LEN", BuiltInFunction.len)
global_symbol_table.set("RUN", BuiltInFunction.run)
global_symbol_table.set("TYPE", BuiltInFunction.type)

def run(fn, text):
    #generate tokens
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens()
    print(tokens)

    if error:
        return None, error
    #generate AST
    parser = Parser(tokens)
    ast = parser.parse()
    if ast.error: return None, ast.error
    print(ast.node)

    #Run program
    interpreter = Interpreter()
    context = Context('<QJ GLOBAL>')
    context.symbol_table = global_symbol_table
    result = interpreter.visit(ast.node, context)

    return result.value, result.error