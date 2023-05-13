def arrayOfProducts(array):
    prod=[1 for _ in range(len(array))]
    leftProd=1
    for i in range(len(array)):
        prod[i]=leftProd
        leftProd*=array[i]
    rightProd=1
    for i in reversed(range(len(array))):
        prod[i]*=rightProd
        rightProd*=array[i]
    return prod
                    
    # Write your code here.
    pass

# Solution 2
# from functools import reduce
# def arrayOfProducts(array):
#     res=[]
#     for i in range(len(array)):
#         newarr=array[:i]+array[i+1:]
#         res.append(reduce(lambda x,y:x*y,newarr,1))
#     return res
#     # Write your code here.
   
