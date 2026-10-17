class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency ={}
        for num in nums:
            if num in frequency:
                frequency[num] +=1
            else:
                frequency[num] = 1
        buckets = [[] for num in range(len(nums)+1)]
        for num, count in frequency.items():
            buckets[count].append(num)
        result = []
        for count in range(len(nums),0,-1):
            for num in buckets[count]:
                result.append(num)
                if len(result) == k:
                    break
            if len(result) == k:
                break
        return result                     
