with open("input.txt") as f:
    data = f.read().strip()

parts = data.split("\n\n")
ranges_section = parts[0]
ids_section = parts[1]

# Parse ranges
ranges = []
for line in ranges_section.split("\n"):
    start, end = map(int, line.split("-"))
    ranges.append((start, end))

# Parse available ingredient IDs
available_ids = [int(line) for line in ids_section.split("\n")]

# Count fresh ingredients
def is_fresh(ingredient_id):
    for start, end in ranges:
        if start <= ingredient_id <= end:
            return True
    return False

fresh_count = sum(1 for id in available_ids if is_fresh(id))
print(fresh_count)
