with open("input.txt") as f:
    lines = [line.rstrip('\n') for line in f]

# Make all lines the same length
max_len = max(len(line) for line in lines)
lines = [line.ljust(max_len) for line in lines]

# Find problem boundaries by looking for columns that are all spaces
def is_separator_col(col_idx):
    return all(line[col_idx] == ' ' for line in lines)

# Find groups of consecutive non-separator columns (these are problems)
problems = []
in_problem = False
start_col = 0

for col in range(max_len):
    if is_separator_col(col):
        if in_problem:
            problems.append((start_col, col))
            in_problem = False
    else:
        if not in_problem:
            start_col = col
            in_problem = True

if in_problem:
    problems.append((start_col, max_len))

# For each problem, read columns right-to-left to form numbers
# Each column is a number (digits top to bottom = most to least significant)
# Last row is the operator

grand_total = 0

for start_col, end_col in problems:
    numbers = []
    operator = None

    # Read columns from right to left
    for col in range(end_col - 1, start_col - 1, -1):
        # Get all characters in this column
        column_chars = [line[col] for line in lines]

        # Last row is operator row
        op_char = column_chars[-1].strip()
        if op_char in ['+', '*']:
            operator = op_char

        # Build number from digits (excluding last row which is operator)
        digits = []
        for char in column_chars[:-1]:  # Exclude operator row
            if char.isdigit():
                digits.append(char)

        if digits:
            number = int(''.join(digits))
            numbers.append(number)

    # Calculate result
    if operator == '+':
        result = sum(numbers)
    else:  # operator == '*'
        result = 1
        for n in numbers:
            result *= n

    grand_total += result

print(grand_total)
