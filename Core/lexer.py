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
    Token Type          Token Value
    ('COMMENT',         ' This is a single-line comment')    
    ('NEWLINE',         '\n')
    ('COMMENT',         '\nThis is a,\nmulti-line comment\n')
    ('NEWLINE',         '\n')
    ('IDENTIFIER',      'myFunc')
    ('LPAREN',          '(')
    ('IDENTIFIER',      'arg')
    ('RPAREN',          ')')
    ('LBRACE',          '{')
    ('NEWLINE',         '\n')
    ('IDENTIFIER',      'x')
    ('ASSIGNMENT',      '=')
    ('NUMBER',          '10')
    ('SEMICOLON',       ';')
    ('COMMENT',         ' Initialize x')
    ('NEWLINE',         '\n')
    ('IDENTIFIER',      'if')
    ('LPAREN',          '(')
    ('IDENTIFIER',      'x')
    ('GREATER_THAN',    '>')
    ('NUMBER',          '5')
    ('RPAREN',          ')')
    ('LBRACE',          '{')
    ('NEWLINE',         '\n')
    ('IDENTIFIER',      'x')
    ('PLUS_EQUALS',     '+=')
    ('NUMBER',          '1')
    ('SEMICOLON',       ';')
    ('NEWLINE',         '\n')
    ('RBRACE',          '}')
    ('NEWLINE',         '\n')
    ('RBRACE',          '}')

Note: A newline is treated as a single character when iterating through a string.
"""

import traceback
from PySide6.QtWidgets import QPlainTextEdit

class Lexer:

    CODE: str
    POSITION: int
    TOKENS: list
    PLAIN_TEXT_EDIT: QPlainTextEdit

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
    def getLineNumber(cls):
        # Create a QTextCursor at the given character position
        text_cursor = cls.PLAIN_TEXT_EDIT.textCursor()
        text_cursor.setPosition(cls.POSITION)
        
        # Get the block (line) number
        line_number = text_cursor.blockNumber()
        return line_number
    
    @classmethod
    def prevChar(cls) -> str:
        return cls.CODE[cls.POSITION - 1]

    @classmethod
    def prevPos(cls) -> int:
        return cls.POSITION - 1

    @classmethod
    def endOfInput(cls) -> bool:
        """ return cls.POSITION >= len(cls.CODE) """
        return cls.POSITION >= len(cls.CODE)

    @classmethod
    def reset(cls) -> None:
        cls.CODE = ""
        cls.POSITION = 0
        cls.TOKENS = []
        cls.PLAIN_TEXT_EDIT = None

class GscToPyLexer(Lexer):
    
    @classmethod
    def tokenize(cls, plainTextEdit, code: str) -> list:
        # Tokenize the GSC code
        cls.CODE = code.strip()
        cls.POSITION = 0
        cls.TOKENS = []
        cls.PLAIN_TEXT_EDIT = plainTextEdit
        try:
            while not cls.endOfInput():
                cls.getNextToken()
        except Exception as e:
            print(f"""
An error occurred while tokenizing the GSC code: {e}
Offending character: '{cls.prevChar()}'
Char Position: {cls.prevPos()}
Line Number: {cls.getLineNumber() + 1}
/*========================================
{traceback.format_exc()}========================================*/""")
            # print(f"An error occurred while tokenizing the GSC code: {e}")
        return cls.TOKENS
    
    @classmethod
    def getNextToken(cls) -> None:
        # Get the next token

        # print(f"Current char: '{cls.currChar()}'")

        # Spaces: Ignore
        while cls.isCustomWhitespace(cls.currChar()):
            cls.incrementPosition()
        
        # Newline
        if cls.isCurrChar('\n'):
            cls.TOKENS.append(('NEWLINE', cls.currChar()))
            cls.incrementPosition()

        # Single-line or multi-line comment | Divide equals | Divide
        elif cls.isCurrChar('/'):
            # Edge case where there is no next character
            try:
                next_char = cls.nextChar()
            except IndexError:
                return

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
            # Divide equals
            elif cls.isNextChar('='):
                cls.TOKENS.append(('DIVIDE_EQUALS', '/='))
                cls.incrementPosition(2)
            # Divide
            else:
                cls.TOKENS.append(('DIVIDE', cls.currChar()))
                cls.incrementPosition()
        
        # Identifier | Number
        elif cls.currChar().isalpha() or cls.currChar().isdigit() or cls.isCurrChar('_'):
            # Number
            # if cls.currChar().isdigit():
            #     number = ''
            #     while not cls.endOfInput() and cls.currChar().isdigit():
            #         number += cls.currChar()
            #         cls.incrementPosition()
                
            #     cls.TOKENS.append(('NUMBER', number))
            
            # Identifier
            identifier = ''
            while not cls.endOfInput() and (cls.currChar().isalpha() or cls.currChar().isdigit() or cls.isCurrChar('_')):
                identifier += cls.currChar()
                cls.incrementPosition()
            
            cls.TOKENS.append(('IDENTIFIER', identifier))
        
        # Modulus
        elif cls.isCurrChar('%'):
            cls.TOKENS.append(('MODULUS', cls.currChar()))
            cls.incrementPosition()
        
        # Equals to | Assignment
        elif cls.isCurrChar('='):
            # Edge case where there is no next character
            try:
                # Equals to
                if cls.isNextChar('='):
                    cls.TOKENS.append(('EQUALS', '=='))
                    cls.incrementPosition(2)
                else:
                    # Assignment
                    cls.TOKENS.append(('ASSIGNMENT', cls.currChar()))
                    cls.incrementPosition()
            except IndexError:
                # Assignment
                cls.TOKENS.append(('ASSIGNMENT', cls.currChar()))
                cls.incrementPosition()
        
        # Greater than or equal to | Greater than
        elif cls.isCurrChar('>'):
            # Greater than or equal to
            if cls.isNextChar('='):
                cls.TOKENS.append(('GREATER_THAN_OR_EQUAL_TO', '>='))
                cls.incrementPosition(2)
            # Greater than
            else:
                cls.TOKENS.append(('GREATER_THAN', cls.currChar()))
                cls.incrementPosition()
        
        # Less than or equal to
        elif cls.isCurrChar('<'):
            # Less than or equal to
            if cls.isNextChar('='):
                cls.TOKENS.append(('LESS_THAN_OR_EQUAL_TO', '<='))
                cls.incrementPosition(2)
            # Less than
            else:
                cls.TOKENS.append(('LESS_THAN_OR_EQUAL_TO', cls.currChar()))
                cls.incrementPosition()
        
        # Plus equals | Addition
        elif cls.isCurrChar('+'):
            # Plus equals
            if cls.isNextChar('='):
                cls.TOKENS.append(('PLUS_EQUALS', '+='))
                cls.incrementPosition(2)
            # Addition
            else:
                cls.TOKENS.append(('PLUS', cls.currChar()))
                cls.incrementPosition()
        
        # Subtract equals | Subtraction
        elif cls.isCurrChar('-'):
            # Subtract equals
            if cls.isNextChar('='):
                cls.TOKENS.append(('SUBTRACT_EQUALS', '-='))
                cls.incrementPosition(2)
            # Subtraction
            else:
                cls.TOKENS.append(('SUBTRACT', cls.currChar()))
                cls.incrementPosition()
        
        # Multiply equals | Multiplication
        elif cls.isCurrChar('*'):
            # Multiply equals
            if cls.isNextChar('='):
                cls.TOKENS.append(('MULTIPLY_EQUALS', '*='))
                cls.incrementPosition(2)
            # Multiplication
            else:
                cls.TOKENS.append(('MULTIPLY', cls.currChar()))
                cls.incrementPosition()
        
        # Keyword
        elif cls.currChar() in {'if', 'else', 'while', 'for', 'switch', 'case', 'break', 'continue', 'return', 'true', 'false', 'undefined', 'include', 'level', 'self', 'thread'}:
            cls.TOKENS.append(('KEYWORD', cls.currChar()))
            cls.incrementPosition()
        
        # Semicolon
        elif cls.isCurrChar(';'):
            cls.TOKENS.append(('SEMICOLON', cls.currChar()))
            cls.incrementPosition()
        
        # LParen
        elif cls.isCurrChar('('):
            cls.TOKENS.append(('LPAREN', cls.currChar()))
            cls.incrementPosition()
        
        # RParen
        elif cls.isCurrChar(')'):
            cls.TOKENS.append(('RPAREN', cls.currChar()))
            cls.incrementPosition()
        
        # LBrace
        elif cls.isCurrChar('{'):
            cls.TOKENS.append(('LBRACE', cls.currChar()))
            cls.incrementPosition()
        
        # RBrace
        elif cls.isCurrChar('}'):
            cls.TOKENS.append(('RBRACE', cls.currChar()))
            cls.incrementPosition()
        
        # LBracket
        elif cls.isCurrChar('['):
            cls.TOKENS.append(('LBRACKET', cls.currChar()))
            cls.incrementPosition()
        
        # RBracket
        elif cls.isCurrChar(']'):
            cls.TOKENS.append(('RBRACKET', cls.currChar()))
            cls.incrementPosition()
        
        # Quote
        elif cls.isCurrChar('"'):
            cls.TOKENS.append(('QUOTE', cls.currChar()))

            # Move past opening quote
            cls.incrementPosition()

            # String
            string = ''
            while not cls.endOfInput() and not cls.isCurrChar('"'):
                string += cls.currChar()
                cls.incrementPosition()
            
            cls.TOKENS.append(('STRING', string))

            cls.TOKENS.append(('QUOTE', cls.currChar()))

            # Move past closing quote
            cls.incrementPosition()
        
        # Double Colon | Single Colon
        elif cls.isCurrChar(':'):
            # Double Colon
            if cls.isNextChar(':'):
                cls.TOKENS.append(('DOUBLE_COLON', cls.currChar() + cls.nextChar()))
                cls.incrementPosition(2)
            # Single Colon
            else:
                cls.TOKENS.append(('SINGLE_COLON', cls.currChar()))
                cls.incrementPosition()
        
        # Preprocessor Directive
        elif cls.isCurrChar('#'):
            line = ''
            while not cls.endOfInput() and not cls.currChar().isspace():
                line += cls.currChar()
                cls.incrementPosition()
            
            cls.TOKENS.append(('PREPROCESSOR_DIRECTIVE', line))
        
        # Dot
        elif cls.isCurrChar('.'):
            cls.TOKENS.append(('DOT', cls.currChar()))
            cls.incrementPosition()
        
        # Comma
        elif cls.isCurrChar(','):
            cls.TOKENS.append(('COMMA', cls.currChar()))
            cls.incrementPosition()
        
        # Local String | Logical And
        elif cls.isCurrChar('&'):
            # Logical And
            if cls.isNextChar('&'):
                cls.TOKENS.append(('LOGICAL_AND', cls.currChar() + cls.nextChar()))
                cls.incrementPosition(2)
            # Local String
            else:
                cls.TOKENS.append(('LOCAL_STRING', cls.currChar()))
                cls.incrementPosition()
        
        # Logical Or
        elif cls.isCurrChar('|') and cls.isNextChar('|'):
            cls.TOKENS.append(('LOGICAL_OR', cls.currChar() + cls.nextChar()))
            cls.incrementPosition(2)
        
        # Logical Not
        elif cls.isCurrChar('!'):
            cls.TOKENS.append(('LOGICAL_NOT', cls.currChar()))
            cls.incrementPosition()
        
        # Path Separator
        elif cls.isCurrChar('\\'):
            cls.TOKENS.append(('PATH_SEPARATOR', cls.currChar()))
            cls.incrementPosition()
        
        # End of input
        elif cls.endOfInput():
            print('End of input reached')
            cls.TOKENS.append(('END', 'EOF'))
            return
        
        # Unrecognized character
        else:
            cls.unrecognizedCharacter()
    
    @classmethod
    def unrecognizedCharacter(cls):
        if not cls.endOfInput():
            # print(f'Unrecognized character: {cls.currChar()}, Pos: {cls.currPos()}')
            print(f"""/*========================================
Unrecognized character: '{cls.currChar()}'
Char Position: {cls.currPos()}
Line Number: {cls.getLineNumber()}
========================================*/""")

            cls.TOKENS.append(('UNKNOWN', cls.currChar()))
            cls.incrementPosition()

class PyToGscLexer(Lexer):
    
    @classmethod
    def tokenize(cls, code: str) -> list:
        # Tokenize the Python code
        pass