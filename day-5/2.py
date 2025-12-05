with open("input.txt") as f:
    data = f.read().strip()

parts = data.split("\n\n")
ranges_section = parts[0]

# Parse ranges
ranges = []
for line in ranges_section.split("\n"):
    start, end = map(int, line.split("-"))
    ranges.append((start, end))

# Sort ranges by start
ranges.sort()

# Merge overlapping ranges
merged = []
for start, end in ranges:
    if merged and start <= merged[-1][1] + 1:
        # Overlapping or adjacent, extend the previous range
        merged[-1] = (merged[-1][0], max(merged[-1][1], end))
    else:
        merged.append((start, end))

# Count total fresh IDs
total_fresh = sum(end - start + 1 for start, end in merged)
print(total_fresh)
