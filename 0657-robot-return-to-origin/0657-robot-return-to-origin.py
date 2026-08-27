class Solution:
    def judgeCircle(self, moves: str) -> bool:
        start = [0, 0]

        moves_dict = {
            'U': lambda x: [x[0], x[1] - 1],
            'D': lambda x: [x[0], x[1] + 1],
            'L': lambda x: [x[0] - 1, x[1]],
            'R': lambda x: [x[0] + 1, x[1]],
        }

        for move in moves:
            start = moves_dict[move](start)
        
        return start == [0, 0]
        