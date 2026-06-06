class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = Counter(nums).most_common(k)
        y = []
        for num,count in x:
            y.append(num)
        return y


        