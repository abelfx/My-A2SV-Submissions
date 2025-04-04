# Problem: Create Sorted Array through Instructions - https://leetcode.com/problems/create-sorted-array-through-instructions/

class Solution:
    def createSortedArray(self, nums: List[int]) -> int:
        #ans stores the ind : [min , max] for each ind in nums
        ans = {i:[0 ,0] for i in range(len(nums))}

        def merge(left , right):
          
            l = len(left)-1
            r = len(right)-1
            while l > -1 and r > -1:
                if nums[left[l]] <= nums[right[r]]:
                    ans[right[r]][1] += ((len(left)-1) - l)
                    r -= 1
                else:
                    l -= 1

            #if the right pointer is not out of bound this means it is greater that all the numbers on the left list
            while r > -1:
                ans[right[r]][1] += len(left) 
                r -= 1  


            l = 0
            r = 0
            res = []
            while l < len(left) and r < len(right):
                #since the left and right lists hold indexes nums[ ... ] they go in here
                if nums[left[l]] < nums[right[r]]:
                    res.append(left[l])
                    l += 1
                else:
                    ans[right[r]][0] += l
                    res.append(right[r])
                    r += 1
            while r < len(right):
                ans[right[r]][0] += l
                res.append(right[r])
                r += 1

            res.extend(left[l:])
            return res
            
        def split(l , r , arr):
            if l == r:
                return [arr[r]]
            
            mid = (l+r)//2

            left = split(l , mid , arr)
            right = split(mid+1 , r , arr)

            return merge(left , right)
        
        split(0 , len(nums)-1 , [i for i in range(len(nums))])

        #take only the mean for the real answer
        real_ans = 0
        for i in ans.keys():
            real_ans += min(ans[i])

        return real_ans % ((10**9) + 7)

        
        