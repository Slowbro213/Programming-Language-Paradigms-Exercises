
'''
A lexical analyzer for simple arithmetic expressions
To run this script: python lex.py filepath
'''

input_file = None
char_class = None
next_char = None
prev_lexeme = ''
# character classes
LETTER = 0
DIGIT = 1
UNKNOWN = 2

# tokens
INT_LIT = 'int literal'
FLOATING_POINT_LIT = "floating-point literal"
COMMENT_BEIGN = "opening comment bracket"
COMMENT_LIT = "comment content"
COMMENT_END = "closing comment bracket"
IDENT = 'identifier'
ASSIGN_OP = 'assign operator'
ADD_OP = 'add operator'
SUB_OP = 'subtract operator'
MULT_OP = 'multiply operator'
DIV_OP = 'divide operator'
LEFT_PAREN = 'left parentheses'
RIGHT_PAREN = 'right parentheses'
EOF = 'EOF'
WHILE = "while statement"
LEFT_CURLY_BRACKET = "left curly bracket"
RIGHT_CURLY_BRACKET = "right curly bracket"
SMALLER_THAN = "smaller than operator"
BIGER_THAN = "biger than operator"
# lookup

LOOKUP_TABLE = {
    '(': LEFT_PAREN,
    ')': RIGHT_PAREN,
    '{':LEFT_CURLY_BRACKET,
    '}':RIGHT_CURLY_BRACKET,
    '<':SMALLER_THAN,
    '>':BIGER_THAN,
    '+': ADD_OP,
    '-': SUB_OP,
    '*': MULT_OP,
    '/': DIV_OP,
    '=': ASSIGN_OP,
    '/*': COMMENT_BEIGN,
    '*/': COMMENT_END,
    'while': WHILE

}

def Letter():
    global prev_lexeme
    temp = ''
    lexeme = ''
    lexeme += next_char
    get_char()
    if prev_lexeme == '/*':
        while True:
            lexeme+=next_char
            if temp =='*':
                temp+=next_char
                if temp == '*/':
                    lexeme = lexeme[:-2]
                    prev_lexeme = '*/'
                    get_char()
                    break
                else:
                    temp = ''
            if next_char == '*':
                temp = '*'
            get_char()
        next_token = COMMENT_LIT
        if prev_lexeme!='*/':
            prev_lexeme = ''
    elif char_class == LETTER:
        while char_class == LETTER or char_class == DIGIT:
            lexeme += next_char
            get_char()
        next_token = LOOKUP_TABLE.get(lexeme, IDENT)
    else:
        next_token = IDENT
        while char_class == LETTER or char_class == DIGIT:
            lexeme += next_char
            get_char()
    return (lexeme, next_token)


def Digit():
    lexeme = ''
    lexeme += next_char
    get_char()
    while char_class == DIGIT:
        lexeme += next_char
        get_char()
    if(next_char == '.'):
        lexeme+=next_char
        get_char()
        while char_class == DIGIT:
            lexeme += next_char
            get_char()
        next_token = FLOATING_POINT_LIT
        return (lexeme, next_token)
    next_token = INT_LIT
    return (lexeme, next_token)


def Unknown():
    global prev_lexeme
    lexeme = ''
    next_token = LOOKUP_TABLE.get(next_char, EOF)
    if(next_char=='/'):
        get_char()
        if (next_char == "*"):
            lexeme = '/*'
            next_token = COMMENT_BEIGN
            prev_lexeme = '/*'
            get_char()
            return (lexeme, next_token)
        else:
            lexeme = '/'
    else:
        lexeme += next_char
        get_char()
    return (lexeme, next_token)


def Eof():
    return (EOF,EOF)

DICT = {
    LETTER : Letter,
    DIGIT : Digit,
    UNKNOWN : Unknown,
    EOF: Eof,
}


def get_char():
    global next_char
    global char_class
    next_char = input_file.read(1)
    if next_char != '':
        if next_char.isalpha():
            char_class = LETTER
        elif next_char.isdigit():
            char_class = DIGIT
        else:
            char_class = UNKNOWN
    else:
        char_class = EOF


def lex():
    global prev_lexeme
    if prev_lexeme == '*/':
        next_token = COMMENT_END
        lexeme = '*/'
        prev_lexeme = ''
        return (lexeme, next_token)
    next_token = None
    lexeme = ''
    # get next non blank
    while next_char.isspace():
        get_char()
    # parse identifiers
    # made the dictionary change mentioned in class
    tuple = DICT[char_class]()
    lexeme , next_token = tuple[0] , tuple[1]
    return (lexeme, next_token)


if __name__ == '__main__':
    input_file = open("program.txt", 'r')
    get_char()
    while True: # do ... while next token is EOF
        lexeme, token = lex()
        print(f'Next token is: {token}, Next lexeme is {lexeme}')
        if token == EOF:
            break

