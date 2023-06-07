def rightSmallerThan(array):
    Counts=[]
    for i in range(len(array)):
        rightSmaller=0
        for j in range(i+1,len(array)):
            if array[j]<array[i]:
                rightSmaller+=1
        Counts.append(rightSmaller)
    return Counts
    # Write your code here.
     



# # Solution 2 using BST
# class BST:
#     def __init__(self,index,val):
#         self.index=index
#         self.val=val
#         self.left=None
#         self.right=None
#     def insert(self,index,newVal):
#         if newVal<self.val:
#             if self.left is None:
#                 self.left=BST(index,newVal)
#             else:
#                 self.left.insert(index,newVal)
#         else:
#             if self.right is None:
#                 self.right=BST(index,newVal)
#             else:
#                 self.right.insert(index,newVal)

# class TreeInfo:
#     def __init__(self,targetIndex):
#         self.targetIndex=targetIndex
#         self.numNodes=0

# def createBST(array):
#     rootVal=array[0]
#     rootNode=BST(0,rootVal)
#     for i in range(1,len(array)):
#         rootNode.insert(i,array[i])
#     return rootNode

# def dfsHelper(value,tree,info):
#     if tree is None:
#         return
#     if tree.val<value and info.targetIndex<tree.index:
#         info.numNodes+=1
#     if value>=tree.val:
#         dfsHelper(value,tree.right,info)
#     dfsHelper(value,tree.left,info)

# def getRightSmaller(array,tree):
#     res=[]
#     for i in range(len(array)):
#         info=TreeInfo(i)
#         dfsHelper(array[i],tree,info)
#         res.append(info.numNodes)
#     return res

 
        
# def rightSmallerThan(array):
#     if len(array)==0:
#         return []
#     tree=createBST(array)
#     return getRightSmaller(array,tree)
#     # Write your code here.
    
