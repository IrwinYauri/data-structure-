'''
def merge(left,right):
    merged=left + right
    print(sorted(merged))
    return mySorted(merged)
'''
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    else:
        mid=len(arr)//2
        left=merge_sort(arr[0:mid])
        right=merge_sort(arr[mid:])        
        return merge(left,right)

def merge(left,right):
    indL=0
    indR=0
    arrAux=[]
    while indL<len(left) and indR<len(right):
        if left[indL]<right[indR]:
            arrAux.append(left[indL])
            indL+=1
        else:
            arrAux.append(right[indR])
            indR+=1
    
    if indL<len(left):
        for i in range(indL,len(left)):            
            arrAux.append(left[i])
    if indR<len(right):
        for i in range(indR,len(right)):            
            arrAux.append(right[i])
    
    return arrAux
            
print(merge_sort([6,5,3,1,8,7,2,4,9,8,8,0,10,5,1,4,11,12,2]))
