def missPositive(arr):
    N = len(arr)
    sortArr = sorted(arr)
    print(sortArr)
    for i in range(N):
        if(sortArr[i]>0 and sortArr[i]>1):
            print("in first if")
            return 1
        if(sortArr[i]>0):
            print("in second ir")
            for j in range(i,N-1):
                if(sortArr[j]+1 == sortArr[j+1]):
                    continue
                else:
                    return sortArr[j]+1
        else:
            print("in first else")
            continue
        
    return sortArr[N-1]+1
    

res = missPositive([7,5,9,3])
print (res)