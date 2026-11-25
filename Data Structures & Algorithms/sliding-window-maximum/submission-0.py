class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #Using a deque 

        output = []
        l = r = 0
        q = collections.deque() #collecting indexes

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            #remove left value from window if out
            if l > q[0]:
                q.popleft()
            
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output