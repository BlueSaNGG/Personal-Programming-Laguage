####################################################
#NODE
####################################################

class NumberNode:
    def __init__(self, tok) -> None:
        self.tok = tok

        self.pos_start = self.tok.pos_start
        self.pos_end = self.tok.pos_end
    
    def __repr__(self) -> str:
        return f'{self.tok}'

class StringNode:
    def __init__(self, tok) -> None:
        self.tok = tok

        self.pos_start = self.tok.pos_start
        self.pos_end = self.tok.pos_end
    
    def __repr__(self) -> str:
        return f'{self.tok}'

class ListNode:
    def __init__(self, element_nodes, pos_start, pos_end) -> None:
        self.element_nodes = element_nodes

        self.pos_start = pos_start
        self.pos_end = pos_end
    
    def __repr__(self) -> str:
        return f'{self.element_nodes}'

class VarAccessNode:
    def __init__(self, var_name_tok) -> None:
        self.var_name_tok = var_name_tok
        self.pos_start = self.var_name_tok.pos_start
        self.pos_end = self.var_name_tok.pos_end

    def __repr__(self) -> str:
        return f'{self.var_name_tok}'

class VarAssignNode:
    def __init__(self, var_name_tok, value_node) -> None:
        self.var_name_tok = var_name_tok
        self.value_node = value_node

        self.pos_start = self.var_name_tok.pos_start
        self.pos_end = self.value_node.pos_end

    def __repr__(self) -> str:
        return f'({self.var_name_tok} = {self.value_node})'

class BinOpNode:
    def __init__(self, left_node, op_tok, right_node) -> None:
        self.left_node = left_node
        self.right_node = right_node
        self.op_tok = op_tok

        self.pos_start = self.left_node.pos_start
        self.pos_end = self.right_node.pos_end

    def __repr__(self) -> str:
        return f'({self.left_node}, {self.op_tok}, {self.right_node})'

class UnaryOpNode:
    def __init__(self, op_tok, node) -> None:
        self.op_tok = op_tok
        self.node = node

        self.pos_start = self.op_tok.pos_start
        self.pos_end = self.node.pos_end

    def __repr__(self) -> str:
        return f'({self.op_tok} -> {self.node})'

class IfNode:
    def __init__(self, cases, else_case) -> None:
        self.cases = cases
        self.else_case = else_case
        

        self.pos_start = self.cases[0][0].pos_start
        self.pos_end = (self.else_case or self.cases[-1])[0].pos_end

    def __repr__(self) -> str:
        return f'IF: {" | ELIF: ".join(f"{condition}->{expr}" for (condition, expr, bool) in self.cases)} , ELSE: {"None" if not self.else_case else self.else_case[0] }'

class ForNode:
    def __init__(self, var_name_tok, start_value_node, end_value_node, step_value_node, body_node, should_return_null) -> None:
        self.var_name_tok = var_name_tok
        self.start_value_node = start_value_node
        self.end_value_node = end_value_node
        self.step_value_node = step_value_node
        self.body_node = body_node
        self.should_return_null = should_return_null

        self.pos_start = self.var_name_tok.pos_start
        self.pos_end = self.body_node.pos_end

    def __repr__(self) -> str:
        return f'( let {self.var_name_tok} from {self.start_value_node} to {self.end_value_node} do {self.body_node} in step {self.step_value_node} )'

class WhileNode:
    def __init__(self, condition_node, body_node, should_return_null) -> None:
        self.condition_node = condition_node
        self.body_node = body_node
        self.should_return_null = should_return_null

        self.pos_start = self.condition_node.pos_start
        self.pos_end = self.body_node.pos_end

    def __repr__(self) -> str:
        return f'( while {self.condition_node} do {self.body_node} )'

class FuncDefNode:
    def __init__(self, var_name_tok, arg_name_toks, body_node, should_auto_return) -> None:
        self.var_name_tok = var_name_tok
        self.arg_name_toks = arg_name_toks
        self.body_node = body_node
        self.should_auto_return = should_auto_return

        if self.var_name_tok:
            self.pos_start = self.var_name_tok.pos_start
        elif len(self.arg_name_toks) > 0:
            self.pos_start = self.arg_name_toks[0].pos_start
        else:
            self.pos_start = self.body_node.pos_start

        self.pos_end = self.body_node.pos_end

    def __repr__(self) -> str:
        return f'(FUNCTION {self.var_name_tok.value})'

class CallNode:
    def __init__(self, node_to_call, arg_nodes) -> None:
        self.node_to_call = node_to_call
        self.arg_nodes = arg_nodes

        self.pos_start = self.node_to_call.pos_start

        if len(self.arg_nodes) > 0:
            self.pos_end = self.arg_nodes[len(self.arg_nodes) - 1].pos_end
        else:
            self.pos_end = self.node_to_call.pos_end
        
    def __repr__(self) -> str:
        return f'(CALL {self.node_to_call} {self.arg_nodes})'

class ReturnNode:
    def __init__(self, node_to_return, pos_start, pos_end) -> None:
        self.node_to_return = node_to_return
        self.pos_start = pos_start
        self.pos_end = pos_end

    def __repr__(self) -> str:
        return f'RETURN {self.node_to_return}'
        
class ContinueNode:
    def __init__(self, pos_start, pos_end) -> None:
        self.pos_start = pos_start
        self.pos_end = pos_end
    
    def __repr__(self) -> str:
        return f'CONTINUE'

class BreakNode:
    def __init__(self, pos_start, pos_end) -> None:
        self.pos_start = pos_start
        self.pos_end = pos_end
    
    def __repr__(self) -> str:
        return f'BREAK'