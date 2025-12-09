with open("input.txt") as f:
    lines = f.read().strip().split("\n")

# Parse red tile coordinates
tiles = []
for line in lines:
    x, y = map(int, line.split(","))
    tiles.append((x, y))

n = len(tiles)
max_area = 0

# Check all pairs of tiles as opposite corners
for i in range(n):
    for j in range(i + 1, n):
        x1, y1 = tiles[i]
        x2, y2 = tiles[j]

        # Calculate rectangle area (opposite corners, inclusive)
        width = abs(x2 - x1) + 1
        height = abs(y2 - y1) + 1
        area = width * height

        max_area = max(max_area, area)

print(max_area)
