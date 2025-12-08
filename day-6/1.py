with open("input.txt") as f:
    lines = [line.rstrip('\n') for line in f]

# Make all lines the same length
max_len = max(len(line) for line in lines)
lines = [line.ljust(max_len) for line in lines]

# Find problem boundaries by looking for columns that are all spaces
# A separator is a column where all characters are spaces
def is_separator_col(col_idx):
    return all(line[col_idx] == ' ' for line in lines)

# Find groups of consecutive non-separator columns (these are problems)
problems = []
in_problem = False
start_col = 0

for col in range(max_len):
    if is_separator_col(col):
        if in_problem:
            # End of a problem
            problems.append((start_col, col))
            in_problem = False
    else:
        if not in_problem:
            # Start of a problem
            start_col = col
            in_problem = True

# Don't forget the last problem if it extends to the end
if in_problem:
    problems.append((start_col, max_len))

# For each problem, extract the numbers and operator
grand_total = 0

for start_col, end_col in problems:
    numbers = []
    operator = None

    for line in lines:
        segment = line[start_col:end_col].strip()
        if segment == '+' or segment == '*':
            operator = segment
        elif segment:
            # It's a number
            numbers.append(int(segment))

    # Calculate result
    if operator == '+':
        result = sum(numbers)
    else:  # operator == '*'
        result = 1
        for n in numbers:
            result *= n

    grand_total += result

print(grand_total)
