with open("input.txt") as f:
    banks = f.read().strip().split("\n")

def max_joltage(bank, k):
    """Find the maximum k-digit number by selecting k digits from bank in order."""
    n = len(bank)
    if k > n:
        return 0

    result = []
    start = 0

    for i in range(k):
        # We need to pick (k - i) more digits including this one
        # So we can search from 'start' up to index (n - (k - i - 1) - 1) = n - k + i
        remaining_to_pick = k - i
        end = n - remaining_to_pick  # last valid index to pick from (inclusive)

        # Find the maximum digit in range [start, end]
        best_idx = start
        best_digit = bank[start]
        for j in range(start, end + 1):
            if bank[j] > best_digit:
                best_digit = bank[j]
                best_idx = j

        result.append(best_digit)
        start = best_idx + 1

    return int(''.join(result))

total = 0
for bank in banks:
    total += max_joltage(bank, 12)

print(total)
