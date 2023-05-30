# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        cur=self    
        while True:
            if value<cur.value:
                if cur.left is None:
                    cur.left=BST(value)
                    break
                else:
                    cur=cur.left
            else:
                if cur.right is None:
                    cur.right=BST(value)
                    break
                else:
                    cur=cur.right          
               
        # Write your code here.
        # Do not edit the return statement of this method.
        return self

    def contains(self, value):
        cur=self  
        while cur is not None:
            if value>cur.value:
                cur=cur.right
            elif value<cur.value:
                cur=cur.left
            else:
                return True
        return False
        # Write your code here.
        pass

    def remove(self, value):        
        if self.value is None:
            return None
        if value<self.value:
            if self.left:
                self.left=self.left.remove(value)
 
        elif value>self.value:
            if self.right:
                self.right=self.right.remove(value)
 
        else:
            if not self.right and not self.left:
                return None
            elif self.left is None:
                self.value=self.right.value                 
                self.left=self.right.left
                self.right=self.right.right
                return self
            elif self.right is None:
                self.value=self.left.value
                self.right=self.left.right
                self.left=self.left.left                
                return self
            node=self.right
            while node.left:
                node=node.left
            self.value=node.value
            self.right=self.right.remove(node.value)    
                            
                
        # Write your code here.
        # Do not edit the return statement of this method.
        return self
