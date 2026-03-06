def search(grid, what):
    for r, row in enumerate(grid):
        for c, spot in enumerate(row):
            if spot == what: return [r, c]