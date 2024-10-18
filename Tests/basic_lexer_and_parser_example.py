import re

# Define token types
class TokenType:
    NUMBER = 'NUMBER'
    PLUS = 'PLUS'
    TIMES = 'TIMES'
    LPAREN = 'LPAREN'
    RPAREN = 'RPAREN'
    EOF = 'EOF'

# Define a Token class
class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f'Token({self.type}, {self.value})'

# Lexer implementation
class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception('Invalid character')

    def advance(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None  # End of input
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return Token(TokenType.NUMBER, int(result))

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            if self.current_char.isdigit():
                return self.integer()
            if self.current_char == '+':
                self.advance()
                return Token(TokenType.PLUS, '+')
            if self.current_char == '*':
                self.advance()
                return Token(TokenType.TIMES, '*')
            if self.current_char == '(':
                self.advance()
                return Token(TokenType.LPAREN, '(')
            if self.current_char == ')':
                self.advance()
                return Token(TokenType.RPAREN, ')')
            self.error()
        return Token(TokenType.EOF, None)

# Parser implementation
class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception('Invalid syntax')

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        token = self.current_token
        if token.type == TokenType.NUMBER:
            self.eat(TokenType.NUMBER)
            return token.value
        elif token.type == TokenType.LPAREN:
            self.eat(TokenType.LPAREN)
            result = self.expr()
            self.eat(TokenType.RPAREN)
            return result

    def term(self):
        result = self.factor()
        while self.current_token.type == TokenType.TIMES:
            self.eat(TokenType.TIMES)
            result *= self.factor()
        return result

    def expr(self):
        result = self.term()
        while self.current_token.type == TokenType.PLUS:
            self.eat(TokenType.PLUS)
            result += self.term()
        return result

# Example usage
def main():
    text = "3 + 5 * (2 + 4)"
    lexer = Lexer(text)
    parser = Parser(lexer)
    result = parser.expr()
    print(f'Result: {result}')  # Output: Result: 33

if __name__ == '__main__':
    main()
