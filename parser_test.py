import unittest
from Parser import *

class TestParser(unittest.TestCase):
    # ""
    def test_empty(self):
        result = run_Parser([Token(TT_EOF)])
        self.assertEqual(result, "")
    # "1.8 / 4 + (5 + 3) * 2 + 3 ^ 5"
    def test_simple_caculation(self):
        result = run_Parser([
            Token(TT_FLOAT, 1.8),
            Token(TT_DIV),
            Token(TT_INT, 4),
            Token(TT_PLUS),
            Token(TT_LPAREN),
            Token(TT_INT, 5),
            Token(TT_PLUS),
            Token(TT_INT, 3),
            Token(TT_RPAREN),
            Token(TT_MUL),
            Token(TT_INT, 2),
            Token(TT_PLUS),
            Token(TT_INT, 3),
            Token(TT_POWER),
            Token(TT_INT, 5),
            Token(TT_EOF)
            ])
        self.assertEqual(result, "[(((FLOAT:1.8, DIV, TT_INT:4), PLUS, ((TT_INT:5, PLUS, TT_INT:3), MUL, TT_INT:2)), PLUS, (TT_INT:3, POWER, TT_INT:5))]")
    # "BS a = True IF a THEN BS b = False ELSE b = Truse"
    def test_condition(self):
        result = run_Parser([
            Token(TT_KEYWORD, 'BS'), 
            Token(TT_IDENTIFIER, 'a'), 
            Token(TT_EQ), 
            Token(TT_IDENTIFIER, 'True'), 
            Token(TT_KEYWORD, 'IF'), 
            Token(TT_IDENTIFIER, 'a'), 
            Token(TT_KEYWORD, 'THEN'), 
            Token(TT_KEYWORD, 'BS'), 
            Token(TT_IDENTIFIER, 'b'), 
            Token(TT_EQ), 
            Token(TT_IDENTIFIER, 'False'), 
            Token(TT_KEYWORD, 'ELSE'), 
            Token(TT_IDENTIFIER, 'b'), 
            Token(TT_EQ), 
            Token(TT_IDENTIFIER, 'True'), 
            Token(TT_EOF)
        ])
        self.assertEqual(result, "[(IDENTIFIER:a = IDENTIFIER:True)]")
    # "BS result = 1 FOR i = 5 TO 0 STEP -1 THEN BS result = result * i FOR i = 1 TO 9 THEN 2^i"
    def test_loop(self):
        result = run_Parser([
            Token(TT_KEYWORD, 'BS'), 
            Token(TT_IDENTIFIER, 'result'), 
            Token(TT_EQ), 
            Token(TT_INT, 1), 
            Token(TT_KEYWORD, 'FOR'), 
            Token(TT_IDENTIFIER, 'i'), 
            Token(TT_EQ), 
            Token(TT_INT, 5), 
            Token(TT_KEYWORD, 'TO'), 
            Token(TT_INT), 
            Token(TT_KEYWORD, 'STEP'), 
            Token(TT_MINUS), 
            Token(TT_INT, 1), 
            Token(TT_KEYWORD, 'THEN'), 
            Token(TT_KEYWORD, 'BS'), 
            Token(TT_IDENTIFIER, 'result'), 
            Token(TT_EQ), 
            Token(TT_IDENTIFIER, 'result'), 
            Token(TT_MUL), 
            Token(TT_IDENTIFIER, 'i'), 
            Token(TT_KEYWORD, 'FOR'), 
            Token(TT_IDENTIFIER, 'i'), 
            Token(TT_EQ), 
            Token(TT_INT, 1), 
            Token(TT_KEYWORD, 'TO'), 
            Token(TT_INT, 9), 
            Token(TT_KEYWORD, 'THEN'), 
            Token(TT_INT, 2), 
            Token(TT_POWER), 
            Token(TT_IDENTIFIER, 'i'), 
            Token(TT_EOF)
        ])
        self.assertEqual(result, "[(IDENTIFIER:result = TT_INT:1)]") 
    # FUN add(a,b) -> a + b
    def test_function(self):
        result = run_Parser([
            Token(TT_KEYWORD, 'FUN'), 
            Token(TT_IDENTIFIER, 'add'), 
            Token(TT_LPAREN), 
            Token(TT_IDENTIFIER, 'a'), 
            Token(TT_COMMA), 
            Token(TT_IDENTIFIER, 'b'), 
            Token(TT_RPAREN), 
            Token(TT_ARROW), 
            Token(TT_IDENTIFIER, 'a'), 
            Token(TT_PLUS), 
            Token(TT_IDENTIFIER, 'b'), 
            Token(TT_EOF)
        ])
        self.assertEqual(result, "[(FUNCTION add)]") 
    # # this is a comment -> EOF
    def test_comments(self):
        pass


def run_Parser(tokens):
    parser = Parser(tokens)
    ast = parser.parse()
    node = ast.node
    if not node:
        return ""
    result = node.__repr__()
    return result


if __name__ == "__main__" :
    unittest.main()