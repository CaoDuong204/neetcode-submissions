class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            if num in frequency:
                frequency[num]+=1
            else:
                frequency[num] = 1
        sorted_nums = sorted(frequency,
            key= lambda num: frequency[num],
            reverse = True )
        sorted_nums[:k]
        return(sorted_nums[:k])
        