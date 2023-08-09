def sortStack(stack):
    if len(stack)==0:
        return stack

    top=stack.pop()
    sortStack(stack)
    insertInSorted(stack,top)
     
    return stack
def insertInSorted(stack,value):
    if len(stack)==0 or stack[-1]<=value:
        stack.append(value)
        return
    top=stack.pop()
    insertInSorted(stack,value)
    stack.append(top)
