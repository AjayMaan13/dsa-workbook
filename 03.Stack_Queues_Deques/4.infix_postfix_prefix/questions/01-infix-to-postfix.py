'''
7. Infix to Postfix

Problem Statement: Given an infix expression, convert it to a postfix expression.

Examples:
    Input : a + b * (c^d - e) ^ (f + g * h) - i
    Output: abcd^e-fgh*+^*+i-

    Input : (p + q) * (m - n)
    Output: pq+mn-*

Approach — Shunting-Yard Algorithm (Dijkstra):
    1. Read tokens left-to-right.
    2. Operand      → append to output.
    3. '('          → push onto stack.
    4. ')'          → pop stack to output until '(' is found; discard both parentheses.
    5. Operator     → pop stack to output while:
                        - stack top is an operator, AND
                        - its precedence > current, OR
                          (precedence == current AND current is left-associative)
                      then push current operator.
    6. End of input → pop all remaining operators to output.

Precedence table:
    ^ : 3  (right-associative)
    * : 2  (left-associative)
    / : 2  (left-associative)
    + : 1  (left-associative)
    - : 1  (left-associative)

Time Complexity : O(n)
Space Complexity: O(n)
'''

PRECEDENCE    = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1}
RIGHT_ASSOC   = {'^'}   # operators that are right-associative


def infix_to_postfix(expression):
    stack  = []   # operator stack
    output = []   # postfix result tokens

    for token in expression.replace(' ', ''):   # strip spaces, iterate char by char
        if token.isalnum():                     # operand (letter or digit)
            output.append(token)

        elif token == '(':
            stack.append(token)

        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()                         # discard the '('

        else:                                   # operator
            while (stack and stack[-1] != '(' and stack[-1] in PRECEDENCE and
                   (PRECEDENCE[stack[-1]] > PRECEDENCE[token] or
                   (PRECEDENCE[stack[-1]] == PRECEDENCE[token] and token not in RIGHT_ASSOC))):
                output.append(stack.pop())
            stack.append(token)

    while stack:                                # flush remaining operators
        output.append(stack.pop())

    return ''.join(output)


# --- Driver ---
test_cases = [
    ("a + b * (c^d - e) ^ (f + g * h) - i", "abcd^e-fgh*+^*+i-"),
    ("(p + q) * (m - n)",                    "pq+mn-*"),
    ("a + b * c",                            "abc*+"),
    ("(a + b) * c",                          "ab+c*"),
    ("a ^ b ^ c",                            "abc^^"),     # right-associative: a^(b^c)
    ("a * b + c * d",                        "ab*cd*+"),
]

for infix, expected in test_cases:
    result = infix_to_postfix(infix)
    status = "PASS" if result == expected else "FAIL"
    print(f"[{status}]  {infix:<40}  =>  {result}  (expected: {expected})")
