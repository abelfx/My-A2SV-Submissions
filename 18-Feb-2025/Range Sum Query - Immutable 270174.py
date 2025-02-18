# Problem: Range Sum Query - Immutable - https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums_arr = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums_arr[left:right+1])


        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)