with open("input.txt") as f:
    data = f.read().strip()

# Parse ranges
ranges = []
for part in data.split(","):
    if part:
        start, end = part.split("-")
        ranges.append((int(start), int(end)))

def generate_invalid_in_range(start, end):
    """Generate all invalid IDs in the range [start, end]
    An invalid ID is a sequence repeated at least twice.
    """
    invalid_ids = set()

    max_digits = len(str(end))

    # For each possible base pattern length
    for pattern_len in range(1, max_digits // 2 + 1):
        # Pattern ranges from 10^(pattern_len-1) to 10^pattern_len - 1
        if pattern_len == 1:
            min_pattern = 1
        else:
            min_pattern = 10 ** (pattern_len - 1)
        max_pattern = 10 ** pattern_len - 1

        for pattern in range(min_pattern, max_pattern + 1):
            pattern_str = str(pattern)

            # Repeat the pattern 2, 3, 4, ... times
            for repeats in range(2, max_digits // pattern_len + 1):
                invalid_id = int(pattern_str * repeats)
                if start <= invalid_id <= end:
                    invalid_ids.add(invalid_id)
                elif invalid_id > end:
                    break  # No point continuing with more repeats

    return invalid_ids

total = 0
for start, end in ranges:
    invalid_ids = generate_invalid_in_range(start, end)
    total += sum(invalid_ids)

print(total)
