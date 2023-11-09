# Definition for a binary tree node.
# preorder
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
         #preorder
        string = "" # 空字符串 string，表示現在的路徑
        ret=[]      # 空列表 ret，表示所有找到的路徑
        stack = []  #空堆棧 stack，表示待處理的節點
        while stack or root: # 如果 stack 非空或者 root 非空，就繼續循環
            if root: # root不是空的
                #vist
                if string == "": # 如果 string 為空，表示這是第一個節點
                    string = str(root.val) #不需要箭頭記號，只需要加入值即可
                else:           # 如果 string 不為空，表示這是第二個以後的節點  
                    string += "->" + str(root.val)   #值前面須加上箭頭記號
                
                #如果 root 沒有左子節點和右子節點，表示這是一條從根節點到葉子節點的路徑
                if root.left is None and root.right is None:
                    ret.append(string) # 將string 加入 ret 中
                # 把 (root, string) 的truple加入 stack 中，表示將其訪問到
                stack.append((root,string))
                # 當前節點移動到其左子節點
                root = root.left

            else:# 如果 root 為空 (null) 不能構成一條路線
                root,string = stack.pop()  #  從 stack 中取出最後加入的root,string
                # 當前節點移動到其右子節點
                root = root.right
        # 返回 ret，表示二叉樹中所有從根節點到葉子節點的路徑。
        return ret  