from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
        """

        def _brute_force():
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    if nums[i] + nums[j] == target:
                        return [i, j]

        def _using_in():
            for i, n in enumerate(nums):
                complement = target - n

                # in 의 시간 복잡도 O(n)
                if complement in nums[i + 1 :]:
                    return [nums.index(n), nums[i + 1].index(complement) + (i + 1)]

        def _convert_key_value():
            nums_map = {}
            for i, n in enumerate(nums):
                nums_map[n] = i

            for i, n in enumerate(nums):
                if target - n in nums_map and i != nums_map[target - n]:
                    return [i, nums_map[target - n]]
