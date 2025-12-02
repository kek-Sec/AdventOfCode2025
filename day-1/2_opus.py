with open("input.txt") as f:
    rotations = f.read().strip().split("\n")

position = 50
count_zeros = 0

for rotation in rotations:
    direction = rotation[0]
    distance = int(rotation[1:])

    if direction == 'L':
        # Moving left (decreasing), check how many times we pass through 0
        # We pass through 0 if we cross from low numbers to high numbers (wrapping)
        # or if we land on 0
        new_position = (position - distance) % 100

        # Count how many times we hit 0
        # If moving left by 'distance' from 'position':
        # We hit 0 once for each full wrap, plus once if we cross or land on 0

        # Number of times we pass 0:
        # We start at position, move left by distance
        # We hit 0 if position >= 0 and we go past it (or land on it)
        # Each 100 clicks is one full rotation

        # Simpler: count how many times we cross from 0 to 99 (going left)
        # This happens when floor((position) / 100) != floor((position - distance) / 100)
        # But we need to count crossings, not just check if different

        # Going left from position by distance:
        # We cross 0 each time we go from 1->0 or wrap from 0->99
        # Number of zeros hit = (position - new_position + 100) // 100 if we wrap
        # Actually: if position >= new_position (no wrap), zeros = 1 if we passed/hit 0
        # Easier: how many times does the value go through 0?

        # position to position-distance (before mod)
        # zeros crossed = how many multiples of 100 are in range (position-distance, position]
        # which is: floor(position/100) - floor((position-distance)/100)
        # but position < 100, so floor(position/100) = 0
        # floor((position-distance)/100) could be negative
        # zeros = 0 - floor((position-distance)/100) = -floor((position-distance)/100)
        # = ceil((distance-position)/100) when distance > position

        # Let's think differently:
        # We move from position down by distance (with wrapping)
        # We hit 0 once for landing on it, and once each time we wrap past it
        # If distance <= position: we hit 0 only if new_position == 0 (we land on it)
        # If distance > position: we definitely pass 0 at least once, then possibly more

        # Number of zeros = (distance - 1) // 100 + (1 if (position - distance) % 100 <= position or new_position == 0 ...)
        # Hmm, let me think again.

        # Counting zeros when going LEFT by distance from position:
        # We visit positions: position-1, position-2, ..., position-distance (mod 100)
        # How many of these are 0?
        # 0 appears at position-k where position-k ≡ 0 (mod 100), i.e., k ≡ position (mod 100)
        # So k = position, position+100, position+200, ... up to distance
        # Number of such k: floor(distance / 100) + (1 if position <= distance and position > 0 else 0)
        # Wait, we need k in range [1, distance]
        # k = position + 100*m for m = 0, 1, 2, ...
        # k >= 1 means position + 100*m >= 1
        # k <= distance means position + 100*m <= distance
        # So m ranges from ceil((1-position)/100) to floor((distance-position)/100)
        # If position >= 1: m_min = 0, m_max = floor((distance-position)/100)
        # count = m_max - m_min + 1 = floor((distance-position)/100) + 1 if distance >= position else 0

        if distance >= position and position > 0:
            zeros = (distance - position) // 100 + 1
        elif position == 0:
            # starting at 0, going left, we hit 0 again every 100 steps
            zeros = distance // 100
        else:
            zeros = (distance - position) // 100 + 1 if distance >= position else 0

        # Simpler formula: how many times do we hit 0?
        # zeros = (distance + (100 - position) % 100) // 100 if we account for first crossing
        # Actually let's just compute: floor((position + 99) / 100) after traveling distance
        # No wait, cleanest:
        # zeros hit = number of times we complete going through 0
        # = floor(distance / 100) + (1 if distance % 100 >= position and position != 0 else 0)
        #   + (1 if position == 0 and distance > 0 ... no this is getting complicated

        # Let me just use: (position - (position - distance)) // 100 isn't right either

        # Clean approach:
        # after moving left by d from p, how many zeros?
        # = number of integers k in [1,d] such that (p - k) % 100 == 0
        # = number of integers k in [1,d] such that k % 100 == p % 100 == p
        # = number of integers k in [1,d] that are congruent to p mod 100
        # if p == 0: k = 100, 200, ... -> count = d // 100
        # if p != 0: k = p, p+100, p+200, ... -> first is p, count = 1 + (d-p)//100 if d >= p else 0

        if position == 0:
            zeros = distance // 100
        elif distance >= position:
            zeros = 1 + (distance - position) // 100
        else:
            zeros = 0

        position = new_position

    else:  # R - moving right (increasing)
        new_position = (position + distance) % 100

        # Similar logic but going right
        # We visit position+1, position+2, ..., position+distance (mod 100)
        # 0 appears at position+k where (position+k) % 100 == 0
        # i.e., k % 100 == (100 - position) % 100 == (100 - position) if position != 0 else 0
        # k = (100 - position), (100 - position) + 100, ... for position != 0
        # k = 100, 200, 300, ... for position == 0

        if position == 0:
            zeros = distance // 100
        else:
            first_zero = 100 - position  # first k where we hit 0
            if distance >= first_zero:
                zeros = 1 + (distance - first_zero) // 100
            else:
                zeros = 0

        position = new_position

    count_zeros += zeros

print(count_zeros)
