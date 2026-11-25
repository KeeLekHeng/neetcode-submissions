class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        heap = []
        result = []

        #put the items in dictionary (key: num, value:frequency)
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        #put in heap where tuples is (frequency,num) so that we can sort easier
        for num, frequency in count.items():
            heapq.heappush(heap, (frequency, num))

            if len(heap) > k:
                heapq.heappop(heap)
        
        #lastly just extract the num into the results array
        for frequnecy, num in heap:
            result.append(num)

        return result



