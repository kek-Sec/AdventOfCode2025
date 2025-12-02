import os

def is_periodic(number):
    """
    Checks if a number is formed by a sequence repeated at least twice.
    Logic: If s is periodic, s will be found in (s+s) starting at an index 
    between 1 and len(s)-1.
    """
    s = str(number)
    doubled = s + s
    
    # .find(substring, start_index) returns the lowest index where substring is found
    # We start searching at 1 to skip the obvious match at index 0.
    # If the first finding is less than len(s), we found a shifted match, 
    # meaning the string repeats.
    first_occurrence = doubled.find(s, 1)
    
    return first_occurrence < len(s)

def solve_part2(input_text):
    total_sum = 0
    clean_text = input_text.replace('\n', '').strip()
    ranges = clean_text.split(',')
    
    for r in ranges:
        if not r: continue
        
        parts = r.split('-')
        start = int(parts[0])
        end = int(parts[1])
        
        for num in range(start, end + 1):
            if is_periodic(num):
                total_sum += num
                
    return total_sum

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'input.txt')

    try:
        with open(file_path, 'r') as f:
            content = f.read()
            
        result = solve_part2(content)
        print(f"The Part 2 sum of invalid IDs is: {result}")
        
    except FileNotFoundError:
        print(f"Error: Could not find 'input.txt' in {script_dir}")
    except ValueError:
        print("Error: Input format appears incorrect.")

if __name__ == "__main__":
    main()