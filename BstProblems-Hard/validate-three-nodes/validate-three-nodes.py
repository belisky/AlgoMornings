# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    if isDesc(nodeTwo,nodeOne):
        return isDesc(nodeThree,nodeTwo)
    if isDesc(nodeTwo,nodeThree):
        return isDesc(nodeOne,nodeTwo)
    return False
    # Write your code here.
def isDesc(node,target):
    if not node:
        return False
    if node is target:
        return True

    return isDesc(node.left,target) if target.value < node.value else isDesc(node.right,target)
