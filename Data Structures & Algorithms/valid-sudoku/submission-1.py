class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxs = collections.defaultdict(set)
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.': continue 
                k = (i//3) * 3 + (j//3)
                if num in rows[i] or num in cols[j] or num in boxs[k]:
                    return False 
                else:
                    rows[i].add(num)
                    cols[j].add(num)
                    boxs[k].add(num)

        return True                 
        