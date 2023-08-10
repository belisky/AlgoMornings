def nextGreaterElement(array):
    res=[-1]*len(array)
    stack=[]
    for i in range(2*len(array)):
        cir=i%len(array)
        while len(stack)>0 and array[stack[-1]] <array[cir]:
            top=stack.pop()
            res[top]=array[cir]
        stack.append(cir)
    return res
            
    # Write your code here.
     
