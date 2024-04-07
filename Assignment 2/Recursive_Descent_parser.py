import lex

next_token = ''
leme = ''

def expr():
    global next_token
    global leme
    print("<expr>")
    term()
    while next_token == lex.ADD_OP or next_token == lex.SUB_OP:
        tuple = lex.lex()
        leme, next_token = tuple[0], tuple[1]
        term()




def term():
    global next_token
    global leme
    print("<term>")
    factor()
    while next_token == lex.MULT_OP or next_token == lex.DIV_OP:
        tuple = lex.lex()
        leme, next_token = tuple[0], tuple[1]
        factor()


def factor():
    global next_token
    global leme
    print("<factor>")

    if next_token == lex.IDENT or next_token == lex.INT_LIT or next_token == lex.FLOATING_POINT_LIT:

        print(leme)
        tuple = lex.lex()
        leme, next_token = tuple[0], tuple[1]
    elif next_token == lex.LEFT_PAREN:
        tuple = lex.lex()
        leme , next_token = tuple[0],tuple[1]
        expr()
        if next_token == lex.RIGHT_PAREN:
            next_token = lex.lex()[1]
        else:
            print("Error: Expected ')' in factor")
            exit(1)
    elif next_token == lex.RIGHT_PAREN and next_token == lex.EOF:
        print("Error: Expected '(' in factor")
        exit(1)
    else:
        print("Error: Invalid factor")
        exit(1)
def main():
    # Open your input file
    global next_token
    global leme
    input_file = open("test_input.txt", 'r')
    lex.input_file = input_file
    lex.get_char()
    next_token = lex.lex()[1]

    expr()
    input_file.close()

if __name__ == '__main__':
    main()