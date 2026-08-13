from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)

        if "0000" in deadends:
            return -1

        queue = deque([("0000", 0)])
        visited = {"0000"}

        while queue:
            state, moves = queue.popleft()

            if state == target:
                return moves

            for i in range(4):
                digit = int(state[i])

                for change in [-1, 1]:
                    new_digit = (digit + change) % 10

                    new_state = (
                        state[:i]
                        + str(new_digit)
                        + state[i + 1:]
                    )

                    if new_state in deadends or new_state in visited:
                        continue

                    visited.add(new_state)
                    queue.append((new_state, moves + 1))

        return -1