class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        id_e = 0
        for element in strs :
            id_e = str(sorted(element))
            d[id_e] = []

        for element in strs:
            d[str(sorted(element))].append(element)

        output = []
        for key, value in d.items():
            output.append(value)

        return output
