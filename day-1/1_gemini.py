import re
import os

def solve_safe_password(input_text):
    """
    Parses rotation commands and calculates how often the dial lands on 0.
    
    Args:
        input_text (str): The raw text containing commands (e.g., "R20", "L10").
    
    Returns:
        int: The number of times the dial settles on position 0.
    """
    # The dial starts pointing at 50
    pos = 50
    password_count = 0
    
    # Extract all pairs of Direction + Distance, ignoring metadata lines
    commands = re.findall(r"([LR])(\d+)", input_text)
    
    for direction, val_str in commands:
        val = int(val_str)
        
        # Apply rotation using modular arithmetic for the circular 0-99 dial
        if direction == 'R':
            pos = (pos + val) % 100
        elif direction == 'L':
            pos = (pos - val) % 100
            
        if pos == 0:
            password_count += 1
            
    return password_count

def main():
    # Resolve the absolute path to input.txt based on the script's location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'input.txt')

    try:
        with open(file_path, 'r') as f:
            content = f.read()
            
        result = solve_safe_password(content)
        print(f"The actual password is: {result}")
        
    except FileNotFoundError:
        print(f"Error: Could not find 'input.txt' in {script_dir}")

if __name__ == "__main__":
    main()