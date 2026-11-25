class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)

        for s in strs:
            #Count of each character
            count = [0] * 26

            for c in s:
                #ord is ASCII value
                count[ord(c) - ord("a")] += 1
            
            #python cant let list be keys
            res[tuple(count)].append(s)

        return res.values()