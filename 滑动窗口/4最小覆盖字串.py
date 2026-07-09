'''
哈希表+滑动窗口（双指针）
1、先用need记录t中所需的元素及对应个数
2、双指针逐步记录window内的所有元素及其个数
3、当window中的某一个元素达到与need中元素相等时,计数器valid加一
4、当计数器的个数与len(need)相等时，说明找到符合要求的子串了
5、此时先统计当前窗口的长度以及开始位置
6、随后进行窗口衰减，window减去左边的元素，如果左边元素在need内，那就同时valid也减一
7、最后left前移
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}           # 记录 t 中每个字符需要的次数
        window = {}         # 记录当前窗口中每个字符的实际次数
        for c in t:         # 遍历 t，统计各字符频次
            need[c] = need.get(c, 0) + 1
        left = 0            # 左指针
        valid = 0           # 已经满足 need 要求的字符种类数
        start = 0           # 最短子串的起始位置
        length = float('inf')  # 最短子串的长度，初始无穷大
        for right in range(len(s)):   # 右指针遍历 s
            c = s[right]              # c 是即将进入窗口的字符
            window[c] = window.get(c, 0) + 1
            # 如果 c 在 need 中，且窗口里 c 的数量刚好达到 need 的要求
            if c in need and window[c] == need[c]:
                valid += 1
            # 当窗口已覆盖 t 中所有字符，尝试收缩左边界
            while valid == len(need):
                # 更新最短子串（如果当前窗口更短）
                if right - left + 1 < length:
                    start = left
                    length = right - left + 1 
                d = s[left]        # d 是即将移出窗口的字符
                window[d] -= 1     # 窗口里 d 的数量减 1
                # 如果 d 在 need 中，且移出后不再满足要求
                if d in need and window[d] < need[d]:
                    valid -= 1
                left += 1          # 左指针右移，收缩窗口
        # 如果 length 还是 inf，说明没找到，返回空串；否则返回子串
        return "" if length == float('inf') else s[start:start + length]

            
if __name__=="__main__":
    import sys
    s=sys.stdin.readline().strip()
    t=sys.stdin.readline().strip()
    solution=Solution()
    print(solution.abc(s,t))
