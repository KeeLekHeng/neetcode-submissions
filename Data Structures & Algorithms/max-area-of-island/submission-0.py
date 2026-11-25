class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        directions = [[0, 1], [1, 0], [-1,0], [0,-1]]
        maxArea = 0

        def bfs(r, c):  
            currArea = 0

            q = collections.deque()
            q.append((r, c))
            visit.add((r, c))

            while q:
                row, col = q.popleft()
                currArea += 1
                
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(ROWS) 
                        and c in range(COLS) 
                        and grid[r][c] == 1
                        and (r,c) not in visit):   

                        q.append((r,c))
                        visit.add((r,c))
                        
            return currArea
                

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visit:
                    area = bfs(r, c)
                    maxArea = max(area, maxArea)
        
        return maxArea
