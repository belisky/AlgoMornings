# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
class TreeInfo:
    def __init__(self,numOfVisit,latestVisit):
        self.numOfVisit=numOfVisit
        self.latestVisit=latestVisit


def findKthLargestValueInBst(tree, k):
    treeInfo=TreeInfo(0,0)
    rvrsInorder(tree,k,treeInfo)
    return treeInfo.latestVisit
    
def rvrsInorder(node,k,treeInfo):
    if node is None or treeInfo.numOfVisit>=k :
        return
    rvrsInorder(node.right,k,treeInfo)
    if k>treeInfo.numOfVisit:
        treeInfo.numOfVisit+=1
        treeInfo.latestVisit(node.value)
    rvrsInorder(node.left,k,treeInfo)
    # Write your code here.
     
