class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sample=[]
        for i,num in enumerate(nums):
            sample.append([num,i])

        sample.sort()
        i = 0
        j = len(sample)-1
        while i < j :
            current = sample[i][0]+sample[j][0]
            if current == target:
                return [min(sample[i][1],sample[j][1]),
                max(sample[i][1],sample[j][1])]
            elif current < target:
                i+=1
            else:
                j-=1
        return[]