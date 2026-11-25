class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        curr = []

        candidates.sort()

        def backtracking(i, total):
            if total == target:
                res.append(curr.copy())
                return

            if total > target:
                return

            if i >= len(candidates):
                return
            


            #include current candidate
            curr.append(candidates[i])
            backtracking(i + 1, total + candidates[i])
            curr.pop()


            #do not include current candidate
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                    i += 1
                
            backtracking(i + 1, total)
            


        backtracking(0, 0)
        return res

