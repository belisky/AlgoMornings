# Feel free to add new properties and methods to the class.
class MinMaxStack:
    def __init__(self):
        self.minMaxStack=[]
        self.stack=[]
    def peek(self):
        return self.stack[-1]
        # Write your code here.
        pass

    def pop(self):
        self.minMaxStack.pop()
        return self.stack.pop()
         
        # Write your code here.
         

    def push(self, number):
        newMinMax={'min':number,'max':number}
        if len(self.minMaxStack):
            lastMinMax=self.minMaxStack[-1]
            newMinMax['min']=min(lastMinMax['min'],number)
            newMinMax['max']=max(lastMinMax['max'],number)
        self.minMaxStack.append(newMinMax)
        self.stack.append(number)
        
  
    def getMin(self):
        return self.minMaxStack[-1]['min']
        # Write your code here.
        pass

    def getMax(self):
        return self.minMaxStack[-1]['max']
        # Write your code here.
       
