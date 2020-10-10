def dosSuman(arr,target):
    max=0
    min=0
    sum=0
    for i in range(len(arr)):
        if(arr[i]<target):
            if(arr[i]>=min and arr[i]<=max):
                for j in range(i):
                    if((arr[j]+arr[i])==target):
                        print(target, "["+str(j)+" "+str(i)+"]")
                        return sum
                    sum+=1
            aux=target-arr[i]
            if(aux>max):
                max=aux
            elif(aux<min):
                min=aux
        
        sum+=1
    print(target, "don't exist solution")
    return sum

dosSuman([2,7,11,15],13)
