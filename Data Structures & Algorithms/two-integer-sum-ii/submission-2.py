class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashset = {}

        for i, v in enumerate(numbers):
            diff = target - v
            if diff in hashset:
                return [hashset[diff]+1 , i + 1]
            else:
                hashset[v] = i
        