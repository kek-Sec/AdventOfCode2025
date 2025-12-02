import re
import os

def solve_part2(input_text):
    """
    Calculates the password by counting every time the dial touches 0.
    
    Args:
        input_text (str): The raw text containing commands.
        
    Returns:
        int: The total count of times 0 was reached or passed.
    """
    pos = 50
    total_hits = 0
    
    commands = re.findall(r"([LR])(\d+)", input_text)
    
    for direction, val_str in commands:
        val = int(val_str)
        
        # 1. Count hits from full rotations (every 100 clicks hits 0 once)
        total_hits += val // 100
        
        # 2. handle the remaining movement
        remainder = val % 100
        
        if remainder > 0:
            if direction == 'R':
                # If moving Right (up), we hit 0 if we cross or reach 100
                if pos + remainder >= 100:
                    total_hits += 1
                pos = (pos + remainder) % 100
                
            elif direction == 'L':
                # If moving Left (down), we hit 0 if we reach 0 or wrap past it.
                # Exception: If we START at 0, moving left immediately leaves 0 (to 99),
                # so we don't count that as a hit unless we wrap all the way around 
                # (which is handled by the full rotation logic above).
                if pos != 0 and (pos - remainder <= 0):
                    total_hits += 1
                pos = (pos - remainder) % 100
                
    return total_hits

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'input.txt')

    try:
        with open(file_path, 'r') as f:
            content = f.read()
            
        password = solve_part2(content)
        print(f"The Method 0x434C49434B password is: {password}")
        
    except FileNotFoundError:
        print(f"Error: Could not find 'input.txt' in {script_dir}")

if __name__ == "__main__":
    main()