class Token:

    @classmethod
    def getType(cls, value):
        match value:
            case value if value.isalpha():  # Match any alphabetic character
                return ('identifier', value)
            case value if value.isdigit():  # Match any digit
                return ('number', value)
            case value if value in {' ', '\t', '\n', '\r'}:  # Ignore whitespace
                return None  # We can choose to return None or do nothing
            case value if value in {'+', '=', '-', '*', '/'}:  # Operators
                return ('operator', value)
            case value if value in {';', '(', ')', '{', '}'}:  # Punctuation
                return ('punctuation', value)
            case _:  # Anything else (default case)
                return ('unknown', value)  # Can handle unknown characters if needed
            
print(Token.getType("x"))  # ('identifier', 'x')  || sweet!