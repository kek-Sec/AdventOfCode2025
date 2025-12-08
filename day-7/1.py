with open("input.txt") as f:
    grid = [list(line.rstrip('\n')) for line in f]

rows = len(grid)
cols = len(grid[0]) if rows > 0 else 0

# Find starting position S
start_row, start_col = 0, 0
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 'S':
            start_row, start_col = r, c
            break

# Simulate beams - each beam is (row, col) moving downward
# Use a set to track active beam positions (beams at same position merge)
active_beams = {(start_row, start_col)}
split_count = 0

while active_beams:
    new_beams = set()

    for row, col in active_beams:
        # Move downward
        new_row = row + 1

        # Check if out of bounds
        if new_row >= rows:
            continue

        cell = grid[new_row][col]

        if cell == '.' or cell == 'S':
            # Beam continues downward
            new_beams.add((new_row, col))
        elif cell == '^':
            # Beam hits splitter - split left and right
            split_count += 1
            # Left beam
            if col - 1 >= 0:
                new_beams.add((new_row, col - 1))
            # Right beam
            if col + 1 < cols:
                new_beams.add((new_row, col + 1))

    active_beams = new_beams

print(split_count)
