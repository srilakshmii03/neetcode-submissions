class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        result=[]
        for num in nums:
            if num!= val:
                result.append(num)
        for i in range(len(result)):
            nums[i] = result[i]
        return len(result)