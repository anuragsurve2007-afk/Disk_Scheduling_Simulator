"""
Disk Scheduling Simulator
Operating Systems Mini Project
Algorithms: FCFS, SSTF, SCAN, C-SCAN
Run: python main.py
"""

def total_movement(sequence):
    """Return total disk-head movement for a sequence of head positions."""
    return sum(abs(sequence[i] - sequence[i - 1]) for i in range(1, len(sequence)))


def fcfs(requests, head):
    order = requests[:]
    path = [head] + order
    return order, path, total_movement(path)


def sstf(requests, head):
    pending = requests[:]
    order = []
    current = head
    while pending:
        # Stable tie-breaking: choose the first request among equal distances.
        next_request = min(pending, key=lambda track: abs(track - current))
        pending.remove(next_request)
        order.append(next_request)
        current = next_request
    path = [head] + order
    return order, path, total_movement(path)


def scan(requests, head, disk_size, direction):
    """SCAN (elevator): reaches the boundary before reversing."""
    left = sorted([r for r in requests if r < head])
    right = sorted([r for r in requests if r >= head])
    order = []
    path = [head]

    if direction == "left":
        for r in reversed(left):
            order.append(r)
            path.append(r)
        if path[-1] != 0:
            path.append(0)
        for r in right:
            order.append(r)
            path.append(r)
    else:
        for r in right:
            order.append(r)
            path.append(r)
        if path[-1] != disk_size - 1:
            path.append(disk_size - 1)
        for r in reversed(left):
            order.append(r)
            path.append(r)

    return order, path, total_movement(path)


def c_scan(requests, head, disk_size, direction):
    """C-SCAN: reaches one boundary, wraps to the other, then continues."""
    left = sorted([r for r in requests if r < head])
    right = sorted([r for r in requests if r >= head])
    order = []
    path = [head]

    if direction == "left":
        for r in reversed(left):
            order.append(r)
            path.append(r)
        if path[-1] != 0:
            path.append(0)
        # Wrap-around movement is counted, as is common in total head movement.
        if path[-1] != disk_size - 1:
            path.append(disk_size - 1)
        for r in reversed(right):
            order.append(r)
            path.append(r)
    else:
        for r in right:
            order.append(r)
            path.append(r)
        if path[-1] != disk_size - 1:
            path.append(disk_size - 1)
        if path[-1] != 0:
            path.append(0)
        for r in left:
            order.append(r)
            path.append(r)

    return order, path, total_movement(path)


def show_result(name, result, request_count):
    order, path, movement = result
    average = movement / request_count if request_count else 0
    print(f"\n{name}")
    print("-" * len(name))
    print("Service order :", " -> ".join(map(str, order)) if order else "No requests")
    print("Head path     :", " -> ".join(map(str, path)))
    print("Total movement:", movement, "tracks")
    print(f"Average/request: {average:.2f} tracks")


def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")


def main():
    print("=" * 42)
    print("      DISK SCHEDULING SIMULATOR")
    print("=" * 42)

    disk_size = read_int("Enter disk size (number of tracks): ")
    if disk_size < 1:
        print("Error: disk size must be at least 1.")
        return

    head = read_int(f"Enter initial head position (0 to {disk_size - 1}): ")
    if not 0 <= head < disk_size:
        print("Error: initial head position is outside the disk.")
        return

    raw = input("Enter disk requests separated by spaces (e.g. 98 183 37 122): ").strip()
    try:
        requests = [int(item) for item in raw.split()] if raw else []
    except ValueError:
        print("Error: requests must be whole numbers separated by spaces.")
        return

    if any(r < 0 or r >= disk_size for r in requests):
        print(f"Error: every request must be between 0 and {disk_size - 1}.")
        return

    if not requests:
        print("No disk requests were entered.")
        return

    direction = input("Initial direction for SCAN/C-SCAN (left/right): ").strip().lower()
    if direction not in ("left", "right"):
        print("Error: direction must be 'left' or 'right'.")
        return

    results = {
        "FCFS": fcfs(requests, head),
        "SSTF": sstf(requests, head),
        "SCAN": scan(requests, head, disk_size, direction),
        "C-SCAN": c_scan(requests, head, disk_size, direction),
    }

    print("\n\n========== COMPARISON ==========")
    for name, result in results.items():
        show_result(name, result, len(requests))

    best_name = min(results, key=lambda name: results[name][2])
    print("\nLowest total head movement:", best_name,
          f"({results[best_name][2]} tracks)")


if __name__ == "__main__":
    main()
