class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        res = {}

        for n in nums:
            if n in res:
                res[n] += 1
            else:
                res[n] = 1
        

        sorted_keys = sorted(res.keys(), key=lambda x: res[x], reverse = True)

        #slice the result to get up to k results
        return sorted_keys[:k]