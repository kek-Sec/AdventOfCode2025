import os

def get_max_12_digit_subsequence(line):
    """
    Finds the largest subsequence of length 12 using a monotonic stack.
    """
    digits = line.strip()
    target_len = 12
    
    # If line is too short, we can't form a 12-digit number (shouldn't happen based on rules)
    if len(digits) < target_len:
        return 0
        
    # We need to remove exactly this many characters to reach length 12
    to_remove = len(digits) - target_len
    stack = []
    
    for digit in digits:
        # While we can still remove digits, if the current digit is 
        # bigger than the last one we kept, throw the small one away.
        while to_remove > 0 and stack and stack[-1] < digit:
            stack.pop()
            to_remove -= 1
        stack.append(digit)
        
    # If we didn't use up our removals (e.g., input was "98765..."),
    # we just trim the excess from the end.
    result_digits = stack[:target_len]
    
    return int("".join(result_digits))

def solve_part2(input_text):
    total_joltage = 0
    lines = input_text.strip().split('\n')
    
    for line in lines:
        if not line.strip(): 
            continue
        total_joltage += get_max_12_digit_subsequence(line)
            
    return total_joltage

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'input.txt')

    try:
        with open(file_path, 'r') as f:
            content = f.read()
            
        result = solve_part2(content)
        print(f"The new total output joltage is: {result}")
        
    except FileNotFoundError:
        print(f"Error: Could not find 'input.txt' in {script_dir}")

if __name__ == "__main__":
    main()