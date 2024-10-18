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

Ignoring Spaces and Comments
    Ignoring Spaces:
        Reason: In most programming languages, whitespace (spaces, tabs, and newlines) is used to separate tokens but doesn't affect the semantics of the code. It simply makes the code more readable.
        Effect: By ignoring spaces, the lexer focuses on the meaningful parts of the code (tokens). For example, int a = 5; and int a=5; should be treated the same by the lexer.

    Ignoring Comments:
        Reason: Comments are used for documentation and explanation in the code and are not executed. They can be single-line (e.g., // comment) or multi-line (e.g., /* comment */). Since they don't affect the execution, they should be ignored during the tokenization process.
        Effect: This allows the lexer to focus solely on the functional code. For example, in int a = 5; // initialize a, the lexer should ignore everything after //.

Example GSC Code:
// This is a single-line comment
/*
This is a,
multi-line comment
/*
x = 10; // Initialize x
if (x > 5) {
    x += 1;
}

Output:
    Token Type      Token Value
    comment         "This is a comment"
    identifier      "x"
    operator        "="
    number          "10"
    punctuation     ";"
    comment	        "Initialize x"
    keyword	        "if"
    punctuation	    "("
    identifier	    "x"
    operator	    ">"
    number	        "5"
    punctuation	    ")"
    punctuation	    "{"
    identifier	    "x"
    operator	    "+="
    number	        "1"
    punctuation	    ";"
    punctuation	    "}"

Note: A newline is treated as a single character when iterating through a string.
"""

class Lexer:

    CODE: str
    POSITION: int
    TOKENS: list

    @classmethod
    def currPos(cls) -> int:
        return cls.POSITION
    
    @classmethod
    def incrementPosition(cls, amount: int=1) -> None:
        cls.POSITION += amount
    
    @classmethod
    def endOfInput(cls) -> bool:
        return cls.currPos() >= len(cls.CODE)

    @classmethod
    def isCurrChar(cls, char: str) -> bool:
        return cls.CODE[cls.currPos()] == char
    
    @classmethod
    def isNextChar(cls, char: str) -> bool:
        return cls.CODE[cls.currPos() + 1] == char

    @classmethod
    def reset(cls) -> None:
        cls.CODE = ""
        cls.POSITION = 0
        cls.TOKENS = []

class Token:

    @classmethod
    def getType(cls, value: str) -> tuple:
        match value:
            # Keywords
            case value if value in {'if', 'else', 'while', 'for', 'switch', 'case', 'break', 'continue', 'return', 'true', 'false', 'undefined', 'include'}:
                return ('keyword', value)
            
            # Identifiers (can be var, function, etc.)  var, var1, func, func1, etc.
            # Alphabetical chars
            case value if value.isalpha():  # (this checks all chars in value)
                return ('identifier', value)
            # Alphanumeric and Numeric chars
            case value if cls.containsBothLettersAndDigits(value):
                return ('identifier', value)

            # Numbers
            case value if value.isdigit():
                return ('number', value)

            # Whitespace
            case value if value in {' ', '\t', '\n', '\r'}:
                return ('comment', value)

            # Operators
            case value if value in {'+', '=', '-', '*', '/'}:
                return ('operator', value)

            # Punctuation
            case value if value in {';', '(', ')', '{', '}'}:
                return ('punctuation', value)
            
            # Anything else (default case)
            case _:
                return ('unknown', value)  # Can handle unknown characters if needed
    
    def containsBothLettersAndDigits(value: str) -> bool:
        return any(char.isalpha() for char in value) and any(char.isdigit() for char in value)

class GscToPyLexer(Lexer):
    
    @classmethod
    def tokenize(cls, code: str) -> list:
        # Tokenize the GSC code
        cls.CODE = code.strip()
        cls.POSITION = 0
        cls.TOKENS = []
        cls.getNextToken()
        return cls.TOKENS
    
    @classmethod
    def getNextToken(cls) -> None:
        # Get the next token
        code_len = len(cls.CODE)
        curr_char = cls.CODE[cls.POSITION]
        next_char = cls.CODE[cls.POSITION + 1]

        # Ignore spaces
        while not cls.endOfInput() and curr_char.isspace():
            cls.incrementPosition()

        # Ignore comments
        if curr_char == '/':
            # Check for single-line comment
            if next_char == '/':
                # Skip to the end of the line
                while not cls.endOfInput() and not cls.isCurrChar('\n'):
                    cls.incrementPosition()

                # Skip to the next line
                cls.incrementPosition()

            # Check for multi-line comment
            elif next_char == '*':
                while not cls.endOfInput() and (not cls.isCurrChar('*') or not cls.isNextChar('/')):
                    cls.incrementPosition()
                
                # Skip to the next line
                cls.incrementPosition(2)

            else:
                cls.TOKENS.append(Token.getType(curr_char))
                cls.incrementPosition()
                cls.getNextToken()

        else:
            cls.TOKENS.append(curr_char)
            cls.incrementPosition()
            cls.getNextToken()
        
        # End of input
        if cls.currPos() >= code_len:
            return

class PyToGscLexer(Lexer):
    
    @classmethod
    def tokenize(cls, code: str) -> list:
        # Tokenize the Python code
        pass