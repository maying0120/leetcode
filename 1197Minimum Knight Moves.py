class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        queue = deque([(0, 0, 0)]) #(x, y, steps)
        visited = set((0, 0))
        
        directions = [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]
        
        while queue:
            x0, y0, step = queue.popleft()
            if x0 == x and y0 == y:
                return step

            for dx, dy in directions:
                next_p = (x0 + dx, y0 + dy)
                if next_p not in visited:
                    visited.add(next_p)
                    queue.append((x0 + dx, y0 + dy, step + 1))
            