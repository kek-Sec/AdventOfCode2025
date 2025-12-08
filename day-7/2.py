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

# Now we need to track each timeline separately
# Each timeline is a particle at a position
# When a particle hits a splitter, it creates 2 timelines
# We track: position -> number of timelines at that position

# Use a dict to count timelines at each position
timelines = {(start_row, start_col): 1}

while timelines:
    new_timelines = {}

    for (row, col), count in timelines.items():
        # Move downward
        new_row = row + 1

        # Check if out of bounds - these timelines end
        if new_row >= rows:
            continue

        cell = grid[new_row][col]

        if cell == '.' or cell == 'S':
            # Particle continues downward, same number of timelines
            pos = (new_row, col)
            new_timelines[pos] = new_timelines.get(pos, 0) + count
        elif cell == '^':
            # Particle hits splitter - each timeline splits into 2
            # Left path
            if col - 1 >= 0:
                pos = (new_row, col - 1)
                new_timelines[pos] = new_timelines.get(pos, 0) + count
            # Right path
            if col + 1 < cols:
                pos = (new_row, col + 1)
                new_timelines[pos] = new_timelines.get(pos, 0) + count

    timelines = new_timelines

# Wait, we need to count timelines that have completed (exited or stopped)
# Let me reconsider - we need to count all final timelines

# Actually, let's track total timelines that finish
with open("input.txt") as f:
    grid = [list(line.rstrip('\n')) for line in f]

timelines = {(start_row, start_col): 1}
total_finished = 0

while timelines:
    new_timelines = {}

    for (row, col), count in timelines.items():
        # Move downward
        new_row = row + 1

        # Check if out of bounds - these timelines finish
        if new_row >= rows:
            total_finished += count
            continue

        cell = grid[new_row][col]

        if cell == '.' or cell == 'S':
            # Particle continues downward
            pos = (new_row, col)
            new_timelines[pos] = new_timelines.get(pos, 0) + count
        elif cell == '^':
            # Particle hits splitter - each timeline splits into 2
            # Left path
            if col - 1 >= 0:
                pos = (new_row, col - 1)
                new_timelines[pos] = new_timelines.get(pos, 0) + count
            # Right path
            if col + 1 < cols:
                pos = (new_row, col + 1)
                new_timelines[pos] = new_timelines.get(pos, 0) + count

    timelines = new_timelines

print(total_finished)
