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
            
        if direction == 'L':
            current_pos = (current_pos - amount) % 100
        elif direction == 'R':
            current_pos = (current_pos + amount) % 100
        else:
            print(f"Unknown direction in rotation: {rot}")
            continue
            
        if current_pos == 0:
            zero_count += 1
            
    print(f"Password: {zero_count}")

if __name__ == "__main__":
    solve()
