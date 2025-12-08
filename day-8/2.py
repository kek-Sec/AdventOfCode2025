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
        return False  # Already in same circuit
    if rank[px] < rank[py]:
        px, py = py, px
    parent[py] = px
    if rank[px] == rank[py]:
        rank[px] += 1
    return True  # Successfully merged two circuits

# Connect pairs until all are in one circuit
# We need n-1 successful unions to connect n nodes into one circuit
num_circuits = n
last_pair = None

for dist, a, b in distances:
    if union(a, b):
        num_circuits -= 1
        last_pair = (a, b)
        if num_circuits == 1:
            break

# Get X coordinates of the last pair
x1 = boxes[last_pair[0]][0]
x2 = boxes[last_pair[1]][0]
result = x1 * x2

print(result)
