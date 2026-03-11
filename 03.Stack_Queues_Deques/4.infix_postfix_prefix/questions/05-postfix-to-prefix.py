'''
5. Postfix to Prefix

Problem Statement: Given a postfix expression, convert it to a prefix expression.

Examples:
    Input : abcd^e-fgh*+^*+i-
    Output: -+a*b^-^cde^+fghi

    Input : pq+mn-*
    Output: *+pq-mn

Approach — Stack (read left-to-right):
    1. Read tokens LEFT-to-RIGHT.
    2. Operand  → push onto stack.
    3. Operator → pop op2 (right operand), pop op1 (left operand),
                  form the string "operator op1 op2",
                  push result back onto stack.
    4. End      → single element on stack is the prefix expression.

Time Complexity : O(n)
Space Complexity: O(n)
'''

OPERATORS = set('+-*/^')


def postfix_to_prefix(expression):
    stack = []

    for token in expression.replace(' ', ''):
        if token not in OPERATORS:          # operand
            stack.append(token)
        else:                               # operator
            op2 = stack.pop()               # first pop  → right operand
            op1 = stack.pop()               # second pop → left operand
            stack.append(token + op1 + op2)

    return stack[0]


# --- Driver ---
test_cases = [
    ("abcd^e-fgh*+^*+i-", "-+a*b^-^cde^+fghi"),
    ("pq+mn-*",            "*+pq-mn"),
    ("abc*+",              "+a*bc"),
    ("ab+c*",              "*+abc"),
    ("abc^^",              "^a^bc"),
    ("ab*cd*+",            "+*ab*cd"),
]

for postfix, expected in test_cases:
    result = postfix_to_prefix(postfix)
    status = "PASS" if result == expected else "FAIL"
    print(f"[{status}]  Postfix: {postfix:<25}  =>  {result}  (expected: {expected})")
