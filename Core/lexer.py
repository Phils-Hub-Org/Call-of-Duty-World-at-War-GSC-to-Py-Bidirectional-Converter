"""
Lexer (Lexical Analyzer)

The purpose of the lexer is to break down the input code (whether GSC or Python) into smaller, manageable components known as "tokens".
A token can be a keyword, operator, identifier, or symbol (e.g., `int`, `+`, `while`, `{`, `}`, etc.).
This tokenization process allows the parser to understand the structure of the code more easily by focusing on individual parts.

The lexer scans through the input code character by character, groups them into tokens, and assigns a type (e.g., identifier, number, operator) to each token.
It effectively reduces the complexity of the input code by producing a list of tokens, making it easier for the parser to analyze and process.

Steps:
1. Take input (GSC or Python code).
2. Scan characters to create tokens.
3. Return a list of tokens for the parser to consume.

Class Attributes:
- `code`: The source code (GSC or Python) to be tokenized.
- `position`: The current character position in the input.
- `tokens`: The list of generated tokens.

Methods:
- `tokenize()`: Breaks down the entire code into tokens.
- `get_next_token()`: Returns the next token in the input.
"""

class GscToPyLexer:
    
    CODE: str
    POSITION: int
    TOKENS: list

    @classmethod
    def tokenize(cls):
        pass

class PyToGscLexer:
    
    @classmethod
    def tokenize(cls):
        pass