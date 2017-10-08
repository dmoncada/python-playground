#!/usr/bin/env python3

from stack import Stack


def eval_expression(expression):
    '''
    Evaluates a (simple) mathematical expression such as 9 + 2 * ( 7 - 3 / 4 )
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
                num2 = nums.pop()
                num1 = nums.pop()

                if top_op == '/' and num2 == 0:
                    raise ZeroDivisionError('division by zero is undefined')

                nums.push({
                    '+': lambda a, b: a + b,
                    '-': lambda a, b: a - b,
                    '*': lambda a, b: a * b,
                    '/': lambda a, b: a / b
                }[top_op](num1, num2))

            elif top_op == '(' and op == ')':
                return

        ops.push(op)

    ops = Stack()
    nums = Stack()

    # Initially, a left paren is pushed on the operators stack.
    ops.push('(')

    # 1. If the token is an operator, we must operate on the two stacks.
    # 2. If the token is a number, push it on the numbers stack.
    for token in expression:
        if token in ['(', ')', '+', '-', '*', '/']:
            operate(token, ops, nums)
        else:
            nums.push(int(token))

    # We operate on the stacks one last time with an extra right paren.
    operate(')', ops, nums)

    # The operators stack is now empty and numbers stack holds the result.
    return nums.pop()


if __name__ == '__main__':
    expr1 = '3 + 4 * 2 / ( 2 - 3 )'
    expr2 = '9 + 2 * ( 7 - 3 / 4 )'
    expr3 = '( 2 + 3 * 4 ) * 5 + 1'

    ans1 = eval_expression(expr1.split(' '))
    ans2 = eval_expression(expr2.split(' '))
    ans3 = eval_expression(expr3.split(' '))

    print(f'The evaluation of: {expr1} is: {ans1}')
    print(f'The evaluation of: {expr2} is: {ans2}')
    print(f'The evaluation of: {expr3} is: {ans3}')
