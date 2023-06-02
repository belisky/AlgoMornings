def zigzagTraverse(array):
    h=len(array)-1
    w=len(array[0])-1
    row,col=0,0
    goingDown=True
    result=[]
    while not isOutOfBounds(row,col,h,w):
        result.append(array[row][col])
        if goingDown:
            if col==0 or row==h:
                goingDown=False
                if row==h:
                    col+=1
                else:
                    row+=1
            else:
                row+=1
                col-=1
        else:
            if col==w or row==0:
                goingDown=True
                if col==w:
                    row+=1
                else:
                    col+=1
            else:
                col+=1
                row-=1
    return result

def isOutOfBounds(row,col,h,w):
    return row<0 or row>h or col<0 or col>w
    # Write your code here.
 
