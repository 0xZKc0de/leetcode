class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]: 

        if len(arr) == 1:
            return [-1]

        def get_index(arr : List[int], element : int):
            index = 0
            for i in range(len(arr)):
                if arr[i] == element:
                    index = i
            
            return index

        
        mx = max(arr[ 1 : len(arr)])
        index = get_index(arr, mx)
        result = []
        for i in range(len(arr) - 1):
            if i < index :
                result.append(mx)

            else :
                mx = max(arr[i + 1: len(arr)])
                index = get_index(arr, mx)
                result.append(mx)
        
        result.append(-1)
        return result



                  
