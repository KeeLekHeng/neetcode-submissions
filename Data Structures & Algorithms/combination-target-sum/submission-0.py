class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
            res = []

            def backtracking(i, curr, total):
                if i >= len(nums):
                    return

                if total == target:
                    res.append(curr.copy())
                    return
                
                if total > target:
                    return
                
                
                #include at least one nums[i]
                curr.append(nums[i])
                backtracking(i, curr, total + nums[i])

                #dont include nums[i] anymore and move on next
                curr.pop()
                backtracking(i + 1, curr, total)


            backtracking(0, [], 0)
            return res
