# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def evaluateExpressionTree(tree):
    if tree.value>=0:
        return tree.value
    leftVal=evaluateExpressionTree(tree.left)
    rightVal=evaluateExpressionTree(tree.right)

    if tree.value==-1:
        return leftVal+rightVal
    if tree.value==-2:
        return leftVal-rightVal
    if tree.value==-3:
        return int(leftVal/rightVal)
    return leftVal*rightVal
 
