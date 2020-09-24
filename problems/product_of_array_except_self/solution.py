class Solution(object):
    def productExceptSelf(self, nums):
        if  nums.count(0)>1:
            return [0]*len(nums)
    
        sum=1
        if nums.count(0)==1:

            for i in nums:
                if i!=0:
                    sum *=i
            for i in range(len(nums)):
                if nums[i]!=0:
                    #op.append(0)
                    nums[i]=0
                else:
                    #op.append(prod)
                    nums[i]=sum
            return nums


        #sum=1
        for i in nums:
            sum*=i

        for i in range(len(nums)):
            val=int((nums[i] ** -1)*sum)
            #op.append(val)
            nums[i]=val

        return nums
