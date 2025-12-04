import os

def get_max_joltage(line):
    """
    Finds the largest 2-digit number where the first digit appears 
    before the second digit in the string.
    """
    # Convert string to list of integers
    digits = [int(c) for c in line.strip() if c.isdigit()]
    
    max_score = 0
    
    # We need at least 2 digits to make a pair
    if len(digits) < 2:
        return 0
        
    # Iterate through every digit (except the last one) to be the 'Tens' place
    for i in range(len(digits) - 1):
        tens = digits[i]
        
        # Optimization: Find the max digit in the remaining slice to be the 'Ones' place
        # slicing digits[i+1:] gets all numbers after the current index
        max_ones = max(digits[i+1:])
        
        score = (tens * 10) + max_ones
        
        if score > max_score:
            max_score = score
            
    return max_score

def solve_batteries(input_text):
    total_joltage = 0
    lines = input_text.strip().split('\n')
    
    for line in lines:
        if not line.strip(): 
            continue
        total_joltage += get_max_joltage(line)
            
    return total_joltage

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'input.txt')

    try:
        with open(file_path, 'r') as f:
            content = f.read()
            
        result = solve_batteries(content)
        print(f"The total output joltage is: {result}")
        
    except FileNotFoundError:
        print(f"Error: Could not find 'input.txt' in {script_dir}")

if __name__ == "__main__":
    main()