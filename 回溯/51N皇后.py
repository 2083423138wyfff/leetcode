# import sys
# n = int(sys.stdin.readline())
# def abc(n):
#     res = []
#     cols = []
#     used_col = set()
#     diag1 = set()
#     diag2 = set()
#     def build_board(cols):
#         board = []
#         for col in cols:
#             row_str = ['.'] * n
#             row_str[col] = 'Q'
#             board.append(''.join(row_str))
#         return board
#     def backtrack(row):
#         if row == n:
#             res.append(build_board(cols))
#             return
#         for col in range(n):
#             if col in used_col:
#                 continue
#             if row - col in diag1:
#                 continue
#             if row + col in diag2:
#                 continue

#             cols.append(col)
#             used_col.add(col)
#             diag1.add(row - col)
#             diag2.add(row + col)

#             backtrack(row + 1)

#             cols.pop()
#             used_col.remove(col)
#             diag1.remove(row - col)
#             diag2.remove(row + col)
#     backtrack(0)
#     return res
# print(abc(n))

import sys
n=int(sys.stdin.readline())
def abc(n):
    res=[]
    cols=[]
    used_cols=set()
    used_dig1=set()
    used_dig2=set()
    
    def build_board(cols):
        board=[]
        for col in cols:
            raw_row=['.']*len(cols)
            raw_row[col]='Q'
            board.append(''.join(raw_row))
        return board
    
    def backtrack(row):#这个row其实就是start，只不过一行一行往后排
        if len(cols)==n:
            res.append(build_board(cols))
            return
        for col in range(n):
            if col in used_cols or row-col in used_dig1 or row+col in used_dig2:
                continue
            cols.append(col)
            used_cols.add(col)
            used_dig1.add(row-col)
            used_dig2.add(row+col)
            backtrack(row+1)
            cols.pop()
            used_cols.remove(col)
            used_dig1.remove(row-col)
            used_dig2.remove(row+col)
    
    backtrack(0)
print(abc(n))
            