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
*/
myFunc(arg) {
    x = 10; // Initialize x
    if (x > 5) {
        x += 1;
    }
}

Output:
    Token Type      Token Value
    comment         "// This is a single-line comment"
    identifier      "x"
    operator        "="
    number          "10"
    punctuation     ";"
    comment	        "/* this is a multi-line\ncomment */"
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
    def currChar(cls) -> str:
        return cls.CODE[cls.POSITION]
    
    @classmethod
    def nextChar(cls) -> str:
        return cls.CODE[cls.POSITION + 1]

    @classmethod
    def isCurrChar(cls, char: str) -> bool:
        return cls.CODE[cls.POSITION] == char
    
    @classmethod
    def isNextChar(cls, char: str) -> bool:
        return cls.CODE[cls.POSITION + 1] == char
    
    @staticmethod
    def isCustomWhitespace(value: str) -> bool:
        # Cause str.isspace() returns true for '\n' of which we are not going to ignore
        return value in {' ', '\t', '\r', '\f', '\v'}

    @classmethod
    def endOfInput(cls) -> bool:
        return cls.POSITION >= len(cls.CODE)

    @classmethod
    def reset(cls) -> None:
        cls.CODE = ""
        cls.POSITION = 0
        cls.TOKENS = []

class GscToPyLexer(Lexer):
    
    @classmethod
    def tokenize(cls, code: str) -> list:
        # Tokenize the GSC code
        cls.CODE = code.strip()
        cls.POSITION = 0
        cls.TOKENS = []
        while not cls.endOfInput(): cls.getNextToken()
        return cls.TOKENS
    
    @classmethod
    def getNextToken(cls) -> None:
        # Get the next token

        # Spaces: Ignore
        while cls.isCustomWhitespace(cls.currChar()):
            cls.incrementPosition()
        
        # Newline
        if cls.isCurrChar('\n'):
            cls.TOKENS.append(('NEWLINE', cls.currChar()))
            cls.incrementPosition()

        # Comments
        elif cls.isCurrChar('/'):
            # Single-line comment
            if cls.isNextChar('/'):
                # Move past '//'
                cls.incrementPosition(2)
                comment = ''
                while not cls.endOfInput() and not cls.isCurrChar('\n'):
                    comment += cls.currChar()
                    cls.incrementPosition()
                
                cls.TOKENS.append(('COMMENT', comment))

            # Multi-line comment
            elif cls.isNextChar('*'):
                # Move past '/*'
                cls.incrementPosition(2)
                comment = ''
                
                # Capture multi-line comment content
                while not cls.endOfInput():
                    if cls.isCurrChar('*') and cls.isNextChar('/'):
                        # Move past '*/'
                        cls.incrementPosition(2)
                        break
                    comment += cls.currChar()
                    cls.incrementPosition()
            
                cls.TOKENS.append(('COMMENT', comment))
        
        # Operators
        elif cls.currChar() in {'+', '=', '-', '<', '>', '*', '/', '%'}:
            cls.TOKENS.append(('OPERATOR', cls.currChar()))
            cls.incrementPosition()
        
        # Punctuation
        elif cls.currChar() in {';', '(', ')', '{', '}', '[' ,']', '"', ':'}:
            cls.TOKENS.append(('PUNCTUATION', cls.currChar()))
            cls.incrementPosition()
        
        # Identifiers
        elif cls.currChar().isalpha() or cls.isCurrChar('_') or (cls.currChar().isalpha() and cls.nextChar().isdigit()) or (cls.currChar().isdigit() and cls.nextChar().isalpha()):
            identifier = ''
            while not cls.endOfInput() and cls.currChar().isalpha() or cls.currChar().isdigit() or cls.isCurrChar('_'):
                identifier += cls.currChar()
                cls.incrementPosition()
            
            cls.TOKENS.append(('IDENTIFIER', identifier))

        # Numbers
        elif cls.currChar().isdigit():
            number = ''
            while not cls.endOfInput() and cls.currChar().isdigit():
                number += cls.currChar()
                cls.incrementPosition()
            
            cls.TOKENS.append(('NUMBER', number))
        
        # Unrecognized character
        else:
            print(f'Unrecognized character: {cls.currChar()}')
            cls.TOKENS.append(('UNKNOWN', cls.currChar()))
            cls.incrementPosition()

class PyToGscLexer(Lexer):
    
    @classmethod
    def tokenize(cls, code: str) -> list:
        # Tokenize the Python code
        pass