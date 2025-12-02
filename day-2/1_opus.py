with open("input.txt") as f:
    data = f.read().strip()

# Parse ranges
ranges = []
for part in data.split(","):
    if part:
        start, end = part.split("-")
        ranges.append((int(start), int(end)))

def is_invalid(n):
    """Check if n is made of a sequence repeated twice (like 11, 6464, 123123)"""
    s = str(n)
    length = len(s)
    # Must have even length to be a repeated sequence
    if length % 2 != 0:
        return False
    half = length // 2
    return s[:half] == s[half:]

def generate_invalid_in_range(start, end):
    """Generate all invalid IDs in the range [start, end]"""
    invalid_ids = []

    # Determine the range of half-lengths we need to check
    # An invalid ID of length 2k is formed by repeating a k-digit number
    # Smallest k-digit number: 10^(k-1) (or 1 if k=1)
    # Largest k-digit number: 10^k - 1
    # The invalid ID would be: n * (10^k + 1) for a k-digit n

    # Find min and max digits in range
    min_digits = len(str(start))
    max_digits = len(str(end))

    # Check all possible half-lengths
    for half_len in range(1, max_digits // 2 + 1):
        # Invalid IDs have 2*half_len digits
        total_digits = 2 * half_len

        # The repeated number ranges from 10^(half_len-1) to 10^half_len - 1
        # (for half_len=1, it's 1 to 9)
        if half_len == 1:
            min_half = 1
        else:
            min_half = 10 ** (half_len - 1)
        max_half = 10 ** half_len - 1

        # The invalid ID is formed by concatenating the half with itself
        # This equals: half * (10^half_len + 1)
        multiplier = 10 ** half_len + 1

        for half in range(min_half, max_half + 1):
            invalid_id = half * multiplier
            if start <= invalid_id <= end:
                invalid_ids.append(invalid_id)

    return invalid_ids

total = 0
for start, end in ranges:
    invalid_ids = generate_invalid_in_range(start, end)
    total += sum(invalid_ids)

print(total)
