def grid_challenge(grid):
    sorted_grid = [sorted(row) for row in grid]
    return "YES" if all(col[i] <= col[i + 1] for i in range(len(grid) - 1) for col in zip(*sorted_grid)) else "NO"
