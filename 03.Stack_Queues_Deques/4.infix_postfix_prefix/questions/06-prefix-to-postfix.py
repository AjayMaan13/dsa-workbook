'''
6. Prefix to Postfix

Problem Statement: Given a prefix expression, convert it to a postfix expression.

Examples:
    Input : -+a*b^-^cde^+fghi
    Output: abcd^e-fgh*+^*+i-

    Input : *+pq-mn
    Output: pq+mn-*

Approach — Stack (read right-to-left):
    1. Read tokens RIGHT-to-LEFT.
    2. Operand  → push onto stack.
    3. Operator → pop op1 (left operand), pop op2 (right operand),
                  form the string "op1 op2 operator",
                  push result back onto stack.
    4. End      → single element on stack is the postfix expression.

    Why right-to-left?
    Prefix has the operator before its operands. Scanning in reverse means
    we always see operands before their operator, mirroring the left-to-right
    postfix scan used in postfix-to-prefix.

    Pop order:
    FIRST pop → left operand (op1)
    SECOND pop → right operand (op2)
    Result → op1 + op2 + operator

Time Complexity : O(n)
Space Complexity: O(n)
'''

OPERATORS = set('+-*/^')


def prefix_to_postfix(expression):
    stack  = []
    tokens = list(expression.replace(' ', ''))

    for token in reversed(tokens):          # scan right-to-left
        if token not in OPERATORS:          # operand
            stack.append(token)
        else:                               # operator
            op1 = stack.pop()               # first pop  → left operand
            op2 = stack.pop()               # second pop → right operand
            stack.append(op1 + op2 + token)

    return stack[0]


# --- Driver ---
test_cases = [
    ("-+a*b^-^cde^+fghi", "abcd^e-fgh*+^*+i-"),
    ("*+pq-mn",            "pq+mn-*"),
    ("+a*bc",              "abc*+"),
    ("*+abc",              "ab+c*"),
    ("^a^bc",              "abc^^"),
    ("+*ab*cd",            "ab*cd*+"),
]

for prefix, expected in test_cases:
    result = prefix_to_postfix(prefix)
    status = "PASS" if result == expected else "FAIL"
    print(f"[{status}]  Prefix: {prefix:<25}  =>  {result}  (expected: {expected})")
