class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])

        # adding water around boundaries of current grid to avoid condition check for end of the grid
        water = [0 for _ in range(col+2)]
        new_grid = [water]
        for c in grid:
            curr = [0]
            curr.extend(c)
            curr.append(0)
            new_grid.append(curr)
        new_grid.extend([water])
        
        perimeter = 0
        for r in range(1, row+1):
            for c in range(1, col+1):
                if new_grid[r][c] == 1:
                    if new_grid[r][c-1] == 0:
                        perimeter += 1
                    if new_grid[r-1][c] == 0:
                        perimeter += 1
                    if new_grid[r][c+1] == 0:
                        perimeter += 1
                    if new_grid[r+1][c] == 0:
                        perimeter += 1

        return perimeter    