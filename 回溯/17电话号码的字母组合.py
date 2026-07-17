#主要还是涉及到字符串的处理
import sys
digits=sys.stdin.readline().strip()
mapping={
    "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
    "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
}

def abc(digits):
    if not digits:
        return []
    res=[]
    path=[]
    def backtrack(start):
        if len(path)==len(digits):
            res.append(''.join(path[:]))
            return
        for char in mapping[digits[start]]:
            path.append(char)
            backtrack(start+1)
            path.pop()
    backtrack(0)
    return res

print(abc(digits))