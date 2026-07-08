class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        res = maxnum = 0

        for n in nums:
            count[n] += 1
            if maxnum < count[n]:
                res = n
                maxnum = count[n]
        return res