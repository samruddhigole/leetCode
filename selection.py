def selection(arr):
    for i in range (len(arr)):
        min = i
        for j in range (i+1,len(arr)):
            if(arr[min]>arr[j]):
                min=j
        arr[i],arr[min] = arr[min],arr[i]
    print (arr)

arr=[25,64,12,22,11]
selection(arr)