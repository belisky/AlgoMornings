# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    def dfs(lower,upper,tree):
        if not tree:
            return True
        elif tree.value<lower or tree.value>=upper:
            return False
        else:
            return dfs(lower,tree.value,tree.left) and dfs(tree.value,upper,tree.right)

    return dfs(float('-inf'),float('inf'),tree)
 