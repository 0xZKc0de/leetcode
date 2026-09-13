from collections import Counter, OrderedDict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        result = []
        d = Counter(nums)
        # print(d)
        res = OrderedDict(sorted(d.items(), key=lambda item: item[1]))
        # print(res)
        for key, value in res.items():
            result.append(key)
        # print(result)
        return result[::-1][:k]
