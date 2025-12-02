with open("input.txt") as f:
    rotations = f.read().strip().split("\n")

position = 50
count_zeros = 0

for rotation in rotations:
    direction = rotation[0]
    distance = int(rotation[1:])

    if direction == 'L':
        position = (position - distance) % 100
    else:  # R
        position = (position + distance) % 100

    if position == 0:
        count_zeros += 1

print(count_zeros)
