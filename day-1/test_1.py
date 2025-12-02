# Tests for Day 1 Part 1 - Safe Dial Problem
# The dial starts at 50, L decreases, R increases, mod 100
# Count how many times we land on 0

def solve(rotations, start=50):
    """Original solution logic"""
    position = start
    count_zeros = 0
    for rotation in rotations:
        direction = rotation[0]
        distance = int(rotation[1:])
        if direction == 'L':
            position = (position - distance) % 100
        else:
            position = (position + distance) % 100
        if position == 0:
            count_zeros += 1
    return count_zeros

# Test cases from the problem description
def test_example():
    rotations = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
    # Expected trace:
    # Start: 50
    # L68 -> 82
    # L30 -> 52
    # R48 -> 0  (count: 1)
    # L5  -> 95
    # R60 -> 55
    # L55 -> 0  (count: 2)
    # L1  -> 99
    # L99 -> 0  (count: 3)
    # R14 -> 14
    # L82 -> 32
    assert solve(rotations) == 3, "Example test failed"
    print("✓ Example test passed")

def test_basic_movements():
    # From 50, R50 should land on 0
    assert solve(["R50"]) == 1, "R50 from 50 should land on 0"
    print("✓ R50 test passed")

    # From 50, L50 should land on 0
    assert solve(["L50"]) == 1, "L50 from 50 should land on 0"
    print("✓ L50 test passed")

def test_wraparound():
    # From 50, L60 should land on 90 (50-60 = -10 -> 90)
    assert solve(["L60"]) == 0, "L60 from 50 should land on 90, not 0"
    print("✓ Wraparound test passed")

    # From 50, R60 should land on 10
    assert solve(["R60"]) == 0, "R60 from 50 should land on 10, not 0"
    print("✓ R60 test passed")

def test_multiple_zeros():
    # L50 lands on 0, then R100 lands on 0 again
    assert solve(["L50", "R100"]) == 2, "Should count 2 zeros"
    print("✓ Multiple zeros test passed")

def test_no_zeros():
    assert solve(["R1", "L1", "R2"]) == 0, "Should count 0 zeros"
    print("✓ No zeros test passed")

def test_actual_input():
    with open("input.txt") as f:
        rotations = f.read().strip().split("\n")
    assert solve(rotations) == 1135, "Actual input should give 1135"
    print("✓ Actual input test passed")

if __name__ == "__main__":
    test_example()
    test_basic_movements()
    test_wraparound()
    test_multiple_zeros()
    test_no_zeros()
    test_actual_input()
    print("\n✅ All tests passed!")
