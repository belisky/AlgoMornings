def bestDigits(number, numDigits):
    stack=[]
    for digit in number:
        while numDigits>0 and len(stack)>0 and digit>stack[-1]:
            numDigits-=1
            stack.pop()
        stack.append(digit)

    while numDigits>0:
        numDigits-=1
        stack.pop()
        
    return ''.join(stack)
    # Write your code here.
     
