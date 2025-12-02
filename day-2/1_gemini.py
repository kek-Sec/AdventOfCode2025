import os

def is_invalid_id(number):
    """
    Checks if a number is formed by a sequence repeated twice.
    Examples: 55 (True), 123123 (True), 101 (False), 121212 (False - 3 repeats)
    """
    s = str(number)
    length = len(s)
    
    # Must be even length to be split into two equal halves
    if length % 2 != 0:
        return False
        
    mid = length // 2
    first_half = s[:mid]
    second_half = s[mid:]
    
    return first_half == second_half

def solve_gift_shop(input_text):
    total_sum = 0
    
    # Remove newlines/whitespace and split by comma
    # The input might be spread across lines, so we clean it first.
    clean_text = input_text.replace('\n', '').strip()
    ranges = clean_text.split(',')
    
    for r in ranges:
        if not r: continue # Skip empty strings if any
        
        # Parse "min-max"
        parts = r.split('-')
        start = int(parts[0])
        end = int(parts[1])
        
        # Iterate through the range (inclusive)
        for num in range(start, end + 1):
            if is_invalid_id(num):
                total_sum += num
                
    return total_sum

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'input.txt')

    try:
        with open(file_path, 'r') as f:
            content = f.read()
            
        result = solve_gift_shop(content)
        print(f"The sum of invalid IDs is: {result}")
        
    except FileNotFoundError:
        print(f"Error: Could not find 'input.txt' in {script_dir}")
    except ValueError:
        print("Error: Input format appears incorrect. Ensure it is comma-separated ranges (e.g. 10-20,30-40).")

if __name__ == "__main__":
    main()