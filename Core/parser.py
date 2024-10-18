"""
Parser

The parser's job is to analyze the list of tokens produced by the lexer and organize them according to the grammatical rules of the target language (either GSC or Python). Essentially, it takes the raw tokens from the lexer and builds a structure (commonly called an Abstract Syntax Tree, or AST) that represents the logical flow of the code.

For this particular project, the parser will translate the structure of GSC code to Python code (and vice versa) by reading the tokens and determining how they relate to one another (e.g., a function, loop, or condition). The result will be a structured form that can be translated into the other language.

Steps:
1. Take a list of tokens from the lexer.
2. Check the tokens against the grammar of the language (GSC or Python).
3. Build an AST or equivalent structure to represent the code's logic.
4. Translate the AST to the target language (GSC <-> Python).

Attributes:
- `tokens`: The list of tokens from the lexer.
- `position`: The current token position in the list.
- `ast`: The abstract syntax tree or equivalent representation.

Methods:
- `parse_expression()`: Parse an expression (e.g., `x = 5`).
- `parse_statement()`: Parse a statement (e.g., `if`, `while`, `function
"""

def parseGscToPython(tokens):
    """
    Parse an expression (e.g., `x = 5`).

    Steps:
    1. Check if the current token is an identifier.
    2. Check if the current token is an operator.
    3. Check if the current token is a number.
    4. Check if the current token is a parenthesis.
    """

    pass
def parsePythonToGsc(tokens):
    """
    Parse a statement (e.g., `if`, `while`, `function`).

    Steps:
    1. Check if the current token is an identifier.
    2. Check if the current token is an operator.
    3. Check if the current token is a number.
    4. Check if the current token is a parenthesis.
    """

    pass