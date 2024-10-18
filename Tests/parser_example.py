class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

class ASTNode:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value
        self.children = []

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current_token(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def eat(self, token_type):
        if self.current_token() and self.current_token().type == token_type:
            print(f"Eating token: {self.current_token().type, self.current_token().value}")  # Debug statement
            self.pos += 1
        else:
            raise Exception(f"Unexpected token: {self.current_token().type, self.current_token().value}")

    def parse(self):
        root = ASTNode("Program")
        while self.current_token():
            if self.current_token().type == 'COMMENT':
                root.children.append(self.parse_comment())
            elif self.current_token().type == 'IDENTIFIER' and self.current_token().value == 'myFunc':
                root.children.append(self.parse_function_declaration())
            else:
                self.pos += 1  # Skip unknown tokens for simplicity
        return root

    def parse_comment(self):
        node = ASTNode("Comment", self.current_token().value)
        self.eat('COMMENT')
        return node

    def parse_function_declaration(self):
        node = ASTNode("FunctionDeclaration")
        node.children.append(ASTNode("Identifier", self.current_token().value))
        self.eat('IDENTIFIER')
        self.eat('PUNCTUATION')  # '('
        node.children.append(self.parse_parameters())
        self.eat('PUNCTUATION')  # ')'
        node.children.append(self.parse_block())
        return node

    def parse_parameters(self):
        params = ASTNode("Parameters")
        while self.current_token().type != 'PUNCTUATION' or self.current_token().value != ')':
            if self.current_token().type == 'IDENTIFIER':
                params.children.append(ASTNode("Identifier", self.current_token().value))
                self.eat('IDENTIFIER')
        return params

    def parse_block(self):
        block = ASTNode("Block")
        self.eat('PUNCTUATION')  # '{'
        while self.current_token().type != 'PUNCTUATION' or self.current_token().value != '}':
            if self.current_token().type == 'IDENTIFIER' and self.current_token().value == 'x':
                block.children.append(self.parse_variable_declaration())
            elif self.current_token().type == 'COMMENT':
                block.children.append(self.parse_comment())
            elif self.current_token().type == 'IDENTIFIER' and self.current_token().value == 'if':
                block.children.append(self.parse_if_statement())
            else:
                self.pos += 1  # Skip unknown tokens for simplicity
        self.eat('PUNCTUATION')  # '}'
        return block

    def parse_variable_declaration(self):
        node = ASTNode("VariableDeclaration")
        node.children.append(ASTNode("Identifier", self.current_token().value))
        self.eat('IDENTIFIER')
        node.children.append(ASTNode("Operator", self.current_token().value))
        self.eat('OPERATOR')
        node.children.append(ASTNode("Number", self.current_token().value))
        self.eat('NUMBER')
        self.eat('PUNCTUATION')  # ';'
        return node

    def parse_if_statement(self):
        node = ASTNode("IfStatement")
        self.eat('IDENTIFIER')  # 'if'
        self.eat('PUNCTUATION')  # '('
        node.children.append(self.parse_condition())
        self.eat('PUNCTUATION')  # ')'
        node.children.append(self.parse_block())
        return node

    def parse_condition(self):
        condition = ASTNode("Condition")
        condition.children.append(ASTNode("Identifier", self.current_token().value))
        self.eat('IDENTIFIER')
        condition.children.append(ASTNode("Operator", self.current_token().value))
        self.eat('OPERATOR')
        condition.children.append(ASTNode("Number", self.current_token().value))
        self.eat('NUMBER')
        return condition

# Example usage
tokens = [
    Token('COMMENT', ' This is a single-line comment'),
    Token('NEWLINE', '\n'),
    Token('COMMENT', '\nThis is a,\nmulti-line comment\n'),
    Token('NEWLINE', '\n'),
    Token('IDENTIFIER', 'myFunc'),
    Token('PUNCTUATION', '('),
    Token('IDENTIFIER', 'arg'),
    Token('PUNCTUATION', ')'),
    Token('PUNCTUATION', '{'),
    Token('NEWLINE', '\n'),
    Token('IDENTIFIER', 'x'),
    Token('OPERATOR', '='),
    Token('NUMBER', '10'),
    Token('PUNCTUATION', ';'),
    Token('COMMENT', ' Initialize x'),
    Token('NEWLINE', '\n'),
    Token('IDENTIFIER', 'if'),
    Token('PUNCTUATION', '('),
    Token('IDENTIFIER', 'x'),
    Token('OPERATOR', '>'),
    Token('NUMBER', '5'),
    Token('PUNCTUATION', ')'),
    Token('PUNCTUATION', '{'),
    Token('NEWLINE', '\n'),
    Token('IDENTIFIER', 'x'),
    Token('OPERATOR', '+'),
    Token('OPERATOR', '='),
    Token('NUMBER', '1'),
    Token('PUNCTUATION', ';'),
    Token('NEWLINE', '\n'),
    Token('PUNCTUATION', '}'),
    Token('NEWLINE', '\n'),
    Token('PUNCTUATION', '}'),
]

parser = Parser(tokens)
ast = parser.parse()

def print_ast(node, indent=0):
    print(' ' * indent + f"{node.type}: {node.value if node.value else ''}")
    for child in node.children:
        print_ast(child, indent + 2)

print_ast(ast)