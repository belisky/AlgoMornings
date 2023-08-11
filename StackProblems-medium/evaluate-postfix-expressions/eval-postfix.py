def reversePolishNotation(tokens):
    stack = []

    for token in tokens:
        if token == '+':
            stack.append(stack.pop()+stack.pop())
        elif token == '-':
            firstNum = stack.pop()
            stack.append(stack.pop()-firstNum)
        elif token == '*':
            stack.append(stack.pop()*stack.pop())
        elif token == '/':
            firstNum = stack.pop()
            stack.append(int(stack.pop()/firstNum))
        else:
            stack.append(int(token))
    return stack.pop()
    # Write your code here.
    return -1
