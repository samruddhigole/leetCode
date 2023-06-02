def sortArray( nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def sortArray1 (nums,low,high):

            def partition(nums,low,high):
                pivot = nums[high]
                i =low-1
                for j in range(low,high):
                    if(nums[j]<=pivot):
                        i+=1
                        nums[i],nums[j] = nums[j],nums[i]
                nums[i+1],nums[high] = nums[high],nums[i+1]
                return i+1

            if(low<high):
                p = partition(nums,low,high)
                sortArray1(nums,low,p-1)
                sortArray1(nums,p+1,high)
                return nums

        high = len(nums)-1
        low = 0
        sortArray1(nums,low,high)
        print (nums)

sortArray([10,7,8,9,5])
sortArray([5,1,1,2,0,0])