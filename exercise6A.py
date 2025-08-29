# Function to define precedence of operators
def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0

# Function to check if character is operand
def is_operand(ch):
    return ch.isalnum()   # letters or numbers

# Function to convert infix to postfix
def infix_to_postfix(expression):
    stack = []   # stack for operators
    result = ""  # output string

    for ch in expression:
        # Step 2: If operand → add to result
        if is_operand(ch):
            result += ch

        # Step 3 & 4: If '(' → push to stack
        elif ch == '(':
            stack.append(ch)

        # Step 5: If ')' → pop until '('
        elif ch == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()   # discard '('

        # Step 3.1 & 3.2: Operator → pop higher/equal precedence
        else:
            while stack and precedence(stack[-1]) >= precedence(ch):
                result += stack.pop()
            stack.append(ch)

    # Step 8: Pop all remaining operators
    while stack:
        result += stack.pop()

    return result


# --------- Driver Code ---------
expr = input("Enter infix expression: ")
print("Postfix expression:", infix_to_postfix(expr))

