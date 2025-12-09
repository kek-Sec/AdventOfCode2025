with open("input.txt") as f:
    lines = f.read().strip().split("\n")

# Parse red tile coordinates
red_tiles = []
for line in lines:
    x, y = map(int, line.split(","))
    red_tiles.append((x, y))

n = len(red_tiles)
red_set = set(red_tiles)

# Build the polygon boundary as horizontal and vertical segments
h_segments = []  # (y, x_start, x_end)
v_segments = []  # (x, y_start, y_end)

for i in range(n):
    x1, y1 = red_tiles[i]
    x2, y2 = red_tiles[(i + 1) % n]
    
    if y1 == y2:  # Horizontal
        h_segments.append((y1, min(x1, x2), max(x1, x2)))
    else:  # Vertical
        v_segments.append((x1, min(y1, y2), max(y1, y2)))

def point_in_polygon(px, py):
    # Ray cast to the right
    crossings = 0
    for (x, y_start, y_end) in v_segments:
        if x > px and y_start <= py <= y_end:
            crossings += 1
    return crossings % 2 == 1

def point_on_boundary(px, py):
    for (y, x_start, x_end) in h_segments:
        if py == y and x_start <= px <= x_end:
            return True
    for (x, y_start, y_end) in v_segments:
        if px == x and y_start <= py <= y_end:
            return True
    return False

def point_valid(px, py):
    return point_on_boundary(px, py) or point_in_polygon(px, py)

def rect_valid(rx_min, rx_max, ry_min, ry_max):
    # Check all 4 corners
    corners = [(rx_min, ry_min), (rx_min, ry_max), (rx_max, ry_min), (rx_max, ry_max)]
    for cx, cy in corners:
        if not point_valid(cx, cy):
            return False
    
    # Check if any vertical polygon edge crosses through interior of rectangle
    for (x, y_start, y_end) in v_segments:
        if rx_min < x < rx_max:  # Edge is strictly inside x-range
            if y_start < ry_max and y_end > ry_min:
                return False
    
    # Check if any horizontal polygon edge crosses through interior of rectangle
    for (y, x_start, x_end) in h_segments:
        if ry_min < y < ry_max:  # Edge is strictly inside y-range
            if x_start < rx_max and x_end > rx_min:
                return False
    
    return True

max_area = 0

for i in range(n):
    for j in range(i + 1, n):
        x1, y1 = red_tiles[i]
        x2, y2 = red_tiles[j]
        
        rx_min, rx_max = min(x1, x2), max(x1, x2)
        ry_min, ry_max = min(y1, y2), max(y1, y2)
        
        if rect_valid(rx_min, rx_max, ry_min, ry_max):
            width = rx_max - rx_min + 1
            height = ry_max - ry_min + 1
            area = width * height
            max_area = max(max_area, area)

print(max_area)
