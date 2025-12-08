import math
from collections import defaultdict

with open("input.txt") as f:
    lines = f.read().strip().split("\n")

# Parse junction boxes
boxes = []
for line in lines:
    x, y, z = map(int, line.split(","))
    boxes.append((x, y, z))

n = len(boxes)

# Calculate all pairwise distances
distances = []
for i in range(n):
    for j in range(i + 1, n):
        x1, y1, z1 = boxes[i]
        x2, y2, z2 = boxes[j]
        dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
        distances.append((dist, i, j))

# Sort by distance
distances.sort()

# Union-Find data structure
parent = list(range(n))
rank = [0] * n

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    px, py = find(x), find(y)
    if px == py:
        return  # Already in same circuit
    if rank[px] < rank[py]:
        px, py = py, px
    parent[py] = px
    if rank[px] == rank[py]:
        rank[px] += 1

# Connect the 1000 shortest pairs
for i in range(1000):
    dist, a, b = distances[i]
    union(a, b)

# Count circuit sizes
circuit_sizes = defaultdict(int)
for i in range(n):
    root = find(i)
    circuit_sizes[root] += 1

# Get the three largest circuits
sizes = sorted(circuit_sizes.values(), reverse=True)
result = sizes[0] * sizes[1] * sizes[2]

print(result)
