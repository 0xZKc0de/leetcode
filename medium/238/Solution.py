class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product, output = 1, []
        d = Counter(nums)

        def product_without_zero(nums : List[int]) -> List[int]:
            result, output = 1, []
            for element in nums:
                if element != 0 :
                    result *= element
            for element in nums :
                if element != 0:
                    output.append(0)
                else:
                    output.append(result)

            
            return output
        print(d)
        if 0 in nums:
            if d[0] > 1:
                return [0] * len(nums)
            else :
                return product_without_zero(nums)
        
        for element in nums:
            product  *= element
        
        for element in nums:
            output.append(int(product/element))

        return output
