with open("input.txt") as f:
    grid = [list(line.rstrip('\n')) for line in f]

rows = len(grid)
cols = len(grid[0]) if rows > 0 else 0

def count_adjacent_rolls(r, c):
    """Count rolls of paper (@) in the 8 adjacent positions."""
    count = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
                count += 1
    return count

total_removed = 0

while True:
    # Find all accessible rolls (< 4 adjacent rolls)
    to_remove = []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                if count_adjacent_rolls(r, c) < 4:
                    to_remove.append((r, c))

    if not to_remove:
        break

    # Remove all accessible rolls
    for r, c in to_remove:
        grid[r][c] = '.'

    total_removed += len(to_remove)

print(total_removed)
