"""
This Module takes an infix notation string and
converts it to postfix notation and evaluates it.

Functions:
    in2post
    eval_postfix
    main
"""

from stack import Stack

def in2post(expr):
    """takes a string as an arguement and converts it from an
    infix mathmatical expression to a postfix"""
    if expr is None:
        raise ValueError
    operator_lyst = []
    precendance = {'*': 2, '/': 2, '+': 1, '-': 1}
    stack = Stack()
    value = ""
    expression = ""
    paren_left = 0
    paren_right = 0
    for oper in expr:
        if oper == "(":
            paren_left += 1
        elif oper == ")":
            paren_right += 1
        else:
            pass
    if paren_left != paren_right:
        raise SyntaxError
    for oper in expr:
        try:
            int(oper)
            operator_lyst.append(str(oper))
        except:
            if oper == "(":
                stack.push(oper)
            elif oper == ")":
                while value != "(":
                    value = stack.pop()
                    operator_lyst.append(value)
            elif oper in "*/+-":
                while (stack.lyst != []
                and stack.top() != "("
                and precendance[stack.top()] >= precendance[oper]):
                    operator_lyst.append(stack.pop())
                stack.push(oper)
    while stack.size() > 0:
        operator_lyst.append(stack.pop())
    for oper in operator_lyst:
        if oper != "(":
            expression += oper
    return expression

def eval_postfix(expr):
    """takes a postfix notation string as an arguement
    and evaluates it"""
    if not isinstance(expr, str):
        raise ValueError
    stack = Stack()
    fixed_expr = ""
    for x in expr:
        if x != " ":
            fixed_expr += x
    expr = fixed_expr
    for oper in expr:
        try:
            int(oper)
            stack.push(oper)
        except:
            try:
                num1 = stack.pop()
                num2 = stack.pop()
                result = num2 + oper + num1
                stack.push(str(eval(result)))
            except:
                raise SyntaxError
    return float(stack.top())

def main():
    """reads in a textfile of mathematical expressions"""
    with open('data.txt', 'r') as f:
        data = f.readlines()
        for expr in data:
            print("infix: " + expr
            + "postfix: " + in2post(expr) + "\n"
            + "answer: " + eval_postfix(in2post(expr)) + "\n")
if __name__ == '__main__':
    main()
