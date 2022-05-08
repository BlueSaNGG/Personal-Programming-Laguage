import unittest
from Lexer import *

class TestLexer(unittest.TestCase):
    # ""
    def test_empty(self):
        result = run_Lexer("")
        self.assertEqual(result, [TT_EOF])
    # "1.8 / 4 + (5 + 3) * 2 + 3 ^ 5"
    def test_simple_caculation(self):
        result = run_Lexer( "1.8 / 4 + (5 + 3) * 2 + 3 ^ 5")
        self.assertEqual(result, [
            (TT_FLOAT, 1.8),
            TT_DIV,
            (TT_INT, 4),
            TT_PLUS,
            TT_LPAREN,
            (TT_INT, 5),
            TT_PLUS,
            (TT_INT, 3),
            TT_RPAREN,
            TT_MUL,
            (TT_INT, 2),
            TT_PLUS,
            (TT_INT, 3),
            TT_POWER,
            (TT_INT, 5),
            TT_EOF
            ])
    # "BS a = True IF a THEN BS b = False ELSE b = Truse"
    def test_condition(self):
        result = run_Lexer("BS a = True IF a THEN BS b = False ELSE b = True")
        self.assertEqual(result, [
            (TT_KEYWORD, 'BS'), 
            (TT_IDENTIFIER, 'a'), 
            TT_EQ, 
            (TT_IDENTIFIER, 'True'), 
            (TT_KEYWORD, 'IF'), 
            (TT_IDENTIFIER, 'a'), 
            (TT_KEYWORD, 'THEN'), 
            (TT_KEYWORD, 'BS'), 
            (TT_IDENTIFIER, 'b'), 
            TT_EQ, 
            (TT_IDENTIFIER, 'False'), 
            (TT_KEYWORD, 'ELSE'), 
            (TT_IDENTIFIER, 'b'), 
            TT_EQ, 
            (TT_IDENTIFIER, 'True'), 
            TT_EOF
            ])
    # "BS result = 1 FOR i = 5 TO 0 STEP -1 THEN BS result = result * i FOR i = 1 TO 9 THEN 2^i"
    def test_loop(self):
        result = run_Lexer("BS result = 1 FOR i = 5 TO 0 STEP -1 THEN BS result = result * i FOR i = 1 TO 9 THEN 2^i")
        self.assertEqual(result, [
            (TT_KEYWORD, 'BS'), 
            (TT_IDENTIFIER, 'result'), 
            TT_EQ, 
            (TT_INT, 1), 
            (TT_KEYWORD, 'FOR'), 
            (TT_IDENTIFIER, 'i'), 
            TT_EQ, (TT_INT, 5), 
            (TT_KEYWORD, 'TO'), 
            TT_INT, 
            (TT_KEYWORD, 'STEP'), 
            TT_MINUS, 
            (TT_INT, 1), 
            (TT_KEYWORD, 'THEN'), 
            (TT_KEYWORD, 'BS'), 
            (TT_IDENTIFIER, 'result'), 
            TT_EQ, 
            (TT_IDENTIFIER, 'result'), 
            TT_MUL, 
            (TT_IDENTIFIER, 'i'), 
            (TT_KEYWORD, 'FOR'), 
            (TT_IDENTIFIER, 'i'), 
            TT_EQ, 
            (TT_INT, 1), 
            (TT_KEYWORD, 'TO'), 
            (TT_INT, 9), 
            (TT_KEYWORD, 'THEN'), 
            (TT_INT, 2), 
            TT_POWER, 
            (TT_IDENTIFIER, 'i'), 
            TT_EOF
            ])
    # FUN add(a,b) -> a + b
    def test_function(self):
        result = run_Lexer("FUN add(a,b) -> a + b")
        self.assertEqual(result, [
            (TT_KEYWORD, 'FUN'), 
            (TT_IDENTIFIER, 'add'), 
            TT_LPAREN, 
            (TT_IDENTIFIER, 'a'), 
            TT_COMMA, 
            (TT_IDENTIFIER, 'b'), 
            TT_RPAREN, 
            TT_ARROW, 
            (TT_IDENTIFIER, 'a'), 
            TT_PLUS, 
            (TT_IDENTIFIER, 'b'), 
            TT_EOF
            ])
    # # this is a comment -> EOF
    def test_comments(self):
        result = run_Lexer("#This is a comment")
        self.assertEqual(result, [TT_EOF])

def run_Lexer(input_String):
    tokens, error = Lexer("<QJL>",input_String).make_tokens()
    result = []
    for token in tokens:
        if token.value:
            result.append((token.type, token.value))
        else:
            result.append(token.type)
    return result
        

if __name__ == "__main__" :
    unittest.main()