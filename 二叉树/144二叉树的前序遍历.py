import sys
raw=sys.stdin.readline().split()
nums=[int(x) if x !='null' else None for x in raw ]
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

def build_tree(nums):#最好用
    from collections import deque
    if not nums or nums[0] is None:
        return None
    
    root=TreeNode(nums[0])
    queue=deque([root])
    i=1#i 指向 nums 的下一个要处理的位置
    
    while queue and i <len(nums):
        node=queue.popleft()
        if i <len(nums) and nums[i] is not None:
            node.left=TreeNode(nums[i])
            queue.append(node.left)
        i+=1
        if i <len(nums) and nums[i] is not None:
            node.right=TreeNode(nums[i])
            queue.append(node.right)
        i+=1
    return root
    
def build_tree_digui(nums,i=0):
    if i>=len(nums) or nums[i] is None:
        return None,i+1
    root=TreeNode(nums[i])
    root.left,i=build_tree_digui(nums,i+1)
    root.right,i=build_tree_digui(nums,i)
    return root,i

def preorder(root):
    if not root:
        return []
    return [root.val]+preorder(root.left)+preorder(root.right)

# print(preorder(build_tree(nums)))
root, _ = build_tree_digui(nums)
print(preorder(root))