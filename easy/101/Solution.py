class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        left_list, right_list = [], []

        def parcours_left(node: Optional[TreeNode], arr: List[int]):
            if not node:
                arr.append(None) 
                return
            
            arr.append(node.val)       
            parcours_left(node.left, arr)   
            parcours_left(node.right, arr)  

        def parcours_right(node: Optional[TreeNode], arr: List[int]):
            if not node:
                arr.append(None)
                return
            
            arr.append(node.val)         
            parcours_right(node.right, arr)  
            parcours_right(node.left, arr)   

        parcours_left(root.left, left_list)
        parcours_right(root.right, right_list)
        return left_list == right_list