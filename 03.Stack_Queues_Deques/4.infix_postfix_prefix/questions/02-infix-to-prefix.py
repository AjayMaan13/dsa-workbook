'''
2. Infix to Prefix (Reverse Method)

Problem Statement: Given an infix expression, convert it to a prefix expression.

Examples:
    Input : a + b * (c^d - e) ^ (f + g * h) - i
    Output: -+a*b^-^cde^+fghi

    Input : (p + q) * (m - n)
    Output: *+pq-mn

Approach — Reverse Method:
    Step 1: Reverse the infix expression.
    Step 2: Swap every '(' with ')' and vice versa.
    Step 3: Apply the Infix → Postfix algorithm on the modified expression.
            NOTE: '^' is right-associative in normal infix, but after reversing
            the expression the associativity flips — treat '^' as left-associative
            during this step so the final result is correct.
    Step 4: Reverse the postfix result → that is the prefix expression.

Why it works:
    Reversing mirrors the expression so the "last" operator (lowest precedence,
    rightmost) becomes the "first". Running postfix conversion on the mirrored
    expression and reversing again is equivalent to building the prefix string
    directly.

Precedence table:
    ^ : 3
    * : 2
    / : 2
    + : 1
    - : 1

Time Complexity : O(n)
Space Complexity: O(n)
'''

PRECEDENCE  = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1}


def _infix_to_postfix_for_prefix(expression):
    '''
    Standard Shunting-Yard, but '^' is treated as LEFT-associative.
    This is only used internally by infix_to_prefix after the expression
    has already been reversed.
    '''
    stack  = []
    output = []

    for token in expression:
        if token.isalnum():
            output.append(token)

        elif token == '(':
            stack.append(token)

        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()                     # discard '('

        else:                               # operator
            # treat ALL operators as left-associative here (including '^')
            while (stack and stack[-1] != '(' and stack[-1] in PRECEDENCE and
                   PRECEDENCE[stack[-1]] >= PRECEDENCE[token]):
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())

    return output


def infix_to_prefix(expression):
    # Step 1: reverse the expression (as a list of chars, no spaces)
    tokens  = list(expression.replace(' ', ''))
    tokens.reverse()

    # Step 2: swap parentheses
    swapped = []
    for ch in tokens:
        if ch == '(':
            swapped.append(')')
        elif ch == ')':
            swapped.append('(')
        else:
            swapped.append(ch)

    # Step 3: apply postfix conversion on modified expression
    postfix = _infix_to_postfix_for_prefix(swapped)

    # Step 4: reverse the postfix result → prefix
    postfix.reverse()
    return ''.join(postfix)


# --- Driver ---
test_cases = [
    ("a + b * (c^d - e) ^ (f + g * h) - i", "-+a*b^-^cde^+fghi"),
    ("(p + q) * (m - n)",                    "*+pq-mn"),
    ("a + b * c",                            "+a*bc"),
    ("(a + b) * c",                          "*+abc"),
    ("a ^ b ^ c",                            "^a^bc"),   # right-assoc: a^(b^c)
    ("a * b + c * d",                        "+*ab*cd"),
]

for infix, expected in test_cases:
    result = infix_to_prefix(infix)
    status = "PASS" if result == expected else "FAIL"
    print(f"[{status}]  {infix:<40}  =>  {result}  (expected: {expected})")
