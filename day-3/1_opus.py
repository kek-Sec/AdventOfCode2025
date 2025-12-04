with open("input.txt") as f:
    banks = f.read().strip().split("\n")

total = 0
for bank in banks:
    max_joltage = 0
    # Try all pairs (i, j) where i < j
    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            joltage = int(bank[i] + bank[j])
            max_joltage = max(max_joltage, joltage)
    total += max_joltage

print(total)
