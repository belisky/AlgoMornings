def minHeightBst(array):
    return constructMinBST(array,0,len(array)-1)
    
def constructMinBST(array,start,end):
    if end<start:
        return None
    mid=(end+start)//2
    bst=BST(array[mid])
    bst.left=constructMinBST(array,start,mid-1)
    bst.right=constructMinBST(array,mid+1,end)
    return bst



class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
