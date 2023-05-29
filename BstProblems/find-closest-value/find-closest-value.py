def findClosestValueInBst(tree, target):
    cur=tree
    closest=float('inf')
    while cur:
        if abs(target-closest)> abs(target-cur.value):
            closest=cur.value
        if target>cur.value:
            cur=cur.right
        elif target<cur.value:
            cur=cur.left         
        else:
            return cur.value
    return closest
    # Write your code here.
    pass


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
