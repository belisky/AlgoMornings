# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def repairBst(tree):
    nodeOne=nodeTwo=previousNode=None
    stack=[]
    currentNode=tree
    while currentNode is not None or len(stack)>0:
        while currentNode is not None:
            stack.append(currentNode)
            currentNode=currentNode.left
        currentNode=stack.pop()

        if previousNode is not None and previousNode.value>currentNode.value:
            if nodeOne is None:
                nodeOne=previousNode
            nodeTwo=currentNode
        previousNode=currentNode
        currentNode=currentNode.right
    nodeOne.value,nodeTwo.value=nodeTwo.value,nodeOne.value
    return tree
    # Write your code here.
    return None
