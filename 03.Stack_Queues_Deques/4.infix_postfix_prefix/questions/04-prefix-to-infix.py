'''
4. Prefix to Infix

Problem Statement: Given a prefix expression, convert it to an infix expression.

Examples:
    Input : -+a*b^-^cde^+fghi
    Output: ((a+(b*(((c^d)-e)^(f+(g*h)))))-i)

    Input : *+pq-mn
    Output: ((p+q)*(m-n))

Approach — Stack (read right-to-left):
    1. Read tokens RIGHT-to-LEFT.
    2. Operand  → push onto stack.
    3. Operator → pop two operands (op1 first, then op2),
                  form the string "(op1 operator op2)",
                  push result back onto stack.
    4. End      → the single element left on the stack is the infix expression.

    Why right-to-left?
    In prefix, the operator comes BEFORE its operands. Reading backwards
    means we always encounter operands before their operator — the same
    condition that postfix-to-infix relies on when reading left-to-right.

    Pop order vs postfix-to-infix:
    Here the FIRST pop is the LEFT operand and the SECOND pop is the RIGHT
    operand (opposite of postfix-to-infix) because we are scanning in reverse.

Time Complexity : O(n)
Space Complexity: O(n)
'''

OPERATORS = set('+-*/^')


def prefix_to_infix(expression):
    stack  = []
    tokens = list(expression.replace(' ', ''))

    for token in reversed(tokens):          # scan right-to-left
        if token not in OPERATORS:          # operand
            stack.append(token)
        else:                               # operator
            op1 = stack.pop()               # first pop → left operand
            op2 = stack.pop()               # second pop → right operand
            merged = f"({op1}{token}{op2})"
            stack.append(merged)

    return stack[0]


# --- Driver ---
test_cases = [
    ("-+a*b^-^cde^+fghi", "((a+(b*(((c^d)-e)^(f+(g*h)))))-i)"),
    ("*+pq-mn",           "((p+q)*(m-n))"),
    ("+a*bc",             "(a+(b*c))"),
    ("*+abc",             "((a+b)*c)"),
    ("^a^bc",             "(a^(b^c))"),
    ("+*ab*cd",           "((a*b)+(c*d))"),
]

for prefix, expected in test_cases:
    result = prefix_to_infix(prefix)
    status = "PASS" if result == expected else "FAIL"
    print(f"[{status}]  Prefix: {prefix:<25}  =>  {result}")
