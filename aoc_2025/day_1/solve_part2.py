import sys

def solve():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = 'input.txt'

    try:
        with open(filename, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return

    # Parse input: split by whitespace to handle both newlines and spaces
    rotations = content.split()
    
    current_pos = 50
    zero_count = 0
    
    for rot in rotations:
        if not rot:
            continue
            
        direction = rot[0]
        try:
            amount = int(rot[1:])
        except ValueError:
            print(f"Skipping invalid rotation: {rot}")
            continue
            
        dist_to_zero = 0
        if direction == 'L':
            # Moving towards 0: 50 -> 49 ... -> 0
            # Distance is current_pos. If 0, distance is 100.
            dist_to_zero = current_pos if current_pos != 0 else 100
            
            # Update position
            current_pos = (current_pos - amount) % 100
        elif direction == 'R':
            # Moving towards 100 (which is 0): 50 -> 51 ... -> 99 -> 0
            # Distance is 100 - current_pos. If 0, distance is 100.
            dist_to_zero = (100 - current_pos) if current_pos != 0 else 100
            
            # Update position
            current_pos = (current_pos + amount) % 100
        else:
            print(f"Unknown direction in rotation: {rot}")
            continue
            
        if amount >= dist_to_zero:
            # We hit 0 at least once
            hits = 1 + (amount - dist_to_zero) // 100
            zero_count += hits
            
    print(f"Password: {zero_count}")

if __name__ == "__main__":
    solve()
