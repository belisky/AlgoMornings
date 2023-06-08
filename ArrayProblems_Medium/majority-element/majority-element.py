def majorityElement(array):
    # Write your code here.
    count=0
    majorityElementValue=None
    for value in array:
        if count==0:
            majorityElementValue=value
        if value==majorityElementValue:
            count+=1
        else:
            count-=1
            
    return majorityElementValue
