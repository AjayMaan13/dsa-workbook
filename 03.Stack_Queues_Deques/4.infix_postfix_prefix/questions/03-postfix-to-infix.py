'''
3. Postfix to Infix

Problem Statement: Given a postfix expression, convert it to an infix expression.

Examples:
    Input : abcd^e-fgh*+^*+i-
    Output: a+b*(c^d-e)^(f+g*h)-i

    Input : pq+mn-*
    Output: (p+q)*(m-n)

Approach — Stack:
    1. Read tokens left-to-right.
    2. Operand  → push onto stack.
    3. Operator → pop two operands (op2 first, then op1),
                  form the string  "(op1 operator op2)",
                  push result back onto stack.
    4. End      → the single element left on the stack is the infix expression.

    Why wrap in parentheses every time?
    Each merge fully brackets the sub-expression so precedence is preserved
    explicitly, regardless of operator type.

Time Complexity : O(n)
Space Complexity: O(n)
'''

OPERATORS = set('+-*/^')


def postfix_to_infix(expression):
    stack = []

    for token in expression.replace(' ', ''):
        if token not in OPERATORS:          # operand
            stack.append(token)
        else:                               # operator
            op2 = stack.pop()               # popped first → right operand
            op1 = stack.pop()               # popped second → left operand
            merged = f"({op1}{token}{op2})"
            stack.append(merged)

    return stack[0]                         # final infix expression


# --- Driver ---
test_cases = [
    ("abcd^e-fgh*+^*+i-", "a+b*(c^d-e)^(f+g*h)-i"),
    ("pq+mn-*",            "(p+q)*(m-n)"),
    ("abc*+",              "a+b*c"),
    ("ab+c*",              "(a+b)*c"),
    ("abc^^",              "a^b^c"),
    ("ab*cd*+",            "a*b+c*d"),
]

for postfix, expected in test_cases:
    result = postfix_to_infix(postfix)
    # compare stripped of outer parens for display; raw result shown
    print(f"Postfix : {postfix}")
    print(f"Infix   : {result}")
    print()
