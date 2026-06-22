class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {}

        for i, num in enumerate(nums):
            com = target - num

            if com in prev_map:
                return [prev_map[com], i]

            prev_map[num] = i

        return []    

