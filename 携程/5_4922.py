import sys

def solve():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    
    cnt = [0] * 26      # 26个字母的出现次数
    used = 0            # 已经用了几个不同字母
    res = []            # 结果字符串
    
    for x in a:
        if x == 0:
            # 需要全新字符
            if used >= 26:
                print(-1)
                return
            # 分配第 'used' 个字母
            c = chr(ord('a') + used)
            res.append(c)
            cnt[used] += 1
            used += 1
        else:
            # 找 cnt[j] == x 的字母 j
            found = False
            for j in range(26):
                if cnt[j] == x:
                    c = chr(ord('a') + j)
                    res.append(c)
                    cnt[j] += 1
                    found = True
                    break
            if not found:
                print(-1)
                return
    
    print(''.join(res))

T = int(sys.stdin.readline())
for _ in range(T):
    solve()