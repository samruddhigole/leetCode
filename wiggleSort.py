# Given an integer array nums, reorder it such that nums[0] <= nums[1] >= nums[2] <= nums[3]....
# You may assume the input array always has a valid answer.

def wiggleSort( arr):
    if(len(arr) == 2):
        if(arr[1] >= arr[0]):
            pass
        else:
            arr[1],arr[0] = arr[0],arr[1]

    for i in range(1,len(arr)-1):
        print(i%2)
        if(i%2!=0):
            if(arr[i] >= arr[i-1]):
                print(arr[i])
                print(arr[i-1])
                continue
            else:
                arr[i],arr[i-1] = arr[i-1],arr[i]
            if(arr[i] >= arr[i+1]):
                continue
            else:
                    arr[i],arr[i+1] = arr[i+1],arr[i]
            
        elif(i%2==0):
            if(arr[i] <= arr[i-1]):
                continue
            else:
                arr[i],arr[i-1] = arr[i-1],arr[i]
            if(arr[i] <= arr[i+1]):
                continue
            else:
                arr[i],arr[i+1] = arr[i+1],arr[i]
            
    print(arr)

# wiggleSort([3,5,2,1,6,4])
# wiggleSort([6,6,5,6,3,8])
# wiggleSort([1, 1, 1, 3, 3, 3, 2, 2, 2])
# wiggleSort( [1, 3, 2, 3, 2, 3, 1, 2, 1])
wiggleSort([2,1,3])
