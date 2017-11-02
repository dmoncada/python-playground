#!/usr/bin/env python3

from stack import Stack


def eval_infix(expression):
    '''
    Evaluates an infix mathematical expression such as 9 + 2 * ( 7 - 3 / 4 )
    using Dijkstra's two-stack algorithm. Taken from Lee's and Hubbard's book
    [1].

    The input expression is assumed to be written correctly. It must be passed
    as a list of chars. where each item is either a number or a valid operator
    (currently, only +, -, *, and / are supported.) Parens within the
    expression, if any, must be well-formed.

    [1] Data Structures and Algorithms with Python
    '''

    # Multiplicaton and division have the highest precedence, followed by
    # addition and subtraction. Parens have the lowest.
    def precedence(op):
        return {'(': 0, ')': 0, '+': 1, '-': 1, '*': 2, '/': 2}[op]

    # This is were the magic happens. For details, check [1], pgs. 128-129.
    def operate(op, ops, nums):
        if op == '(':
            ops.push(op)
            return

        while precedence(op) <= precedence(ops.peek()):
            top_op = ops.pop()

            if top_op in ['+', '-', '*', '/']:
                do_operation(top_op, nums)

            elif top_op == '(' and op == ')':
                return

        ops.push(op)

    ops, nums = Stack(), Stack()

    # Initially, a left paren is pushed on the ops. stack.
    ops.push('(')

    for token in expression:
        if token in ['(', ')', '+', '-', '*', '/']:
            operate(token, ops, nums)
        else:
            nums.push(int(token))

    # We operate on the stacks one last time with an extra right paren.
    operate(')', ops, nums)

    return nums.pop()


def eval_postfix(expression):
    '''
    Evaluates a postfix (a.k.a. reverse Polish) mathematical expression such as
    1 2 - 4 5 + * using a single stack. Translated to Python from [1] by K&R.

    Notice the lack of parens in the expression; there's no ambiguity in the
    order of evaluation as long each operator receives exactly the number of
    operands it expects.

    The same caveats for the infix expression evaluator function apply here.

    [1] The C Programming Language
    '''

    nums = Stack()

    for token in expression:
        if token in ['+', '-', '*', '/']:
            do_operation(token, nums)
        else:
            nums.push(int(token))

    return nums.pop()


# Here is where ops. are actually performed.
def do_operation(op, nums):
    num2 = nums.pop()
    num1 = nums.pop()

    if op == '/' and num2 == 0:
        raise ZeroDivisionError('division by zero is undefined')

    nums.push({
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b
    }[op](num1, num2))


if __name__ == '__main__':
    infix1 = '3 + 4 * 2 / ( 2 - 3 )'
    infix2 = '9 + 2 * ( 7 - 3 / 4 )'
    infix3 = '( 2 + 3 * 4 ) * 5 + 1'

    for expression in [infix1, infix2, infix3]:
        ans = eval_infix(expression.split(' '))

        print(f'The evaluation of: {expression} is: {ans}')

    postfix = '1 2 - 4 5 + *'
    ans = eval_postfix(postfix.split(' '))

    print(f'The evaluation of: {postfix} is: {ans}')
