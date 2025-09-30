

def eval_rpn(tokens):
    stack = []

    for token in tokens:
        if token in {"+", "-", "*", "/"}:
            # Pop the last two numbers from the stack
            b = stack.pop()
            a = stack.pop()

            # Perform the operation
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                # Python division needs truncation toward zero
                stack.append(int(a / b))
        else:
            # Token is a number, push to stack
            stack.append(int(token))

    # The final result will be the only element left in the stack
    return stack[0]

# Example usage:
print(eval_rpn(["2","1","+","3","*"]))  # Output: 9
print(eval_rpn(["4","13","5","/","+"])) # Output: 6

