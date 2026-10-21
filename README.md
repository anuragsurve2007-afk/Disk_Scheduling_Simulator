# Disk Scheduling Simulator

**Operating Systems Mini Project**  
**Student:** Anurag Surve  
**Roll No.:** 03

## Overview
A simple Python command-line simulator that demonstrates and compares four disk scheduling algorithms:

- **FCFS (First Come, First Served):** handles requests in arrival order.
- **SSTF (Shortest Seek Time First):** handles the nearest pending request first.
- **SCAN:** moves in one direction to the disk boundary, then reverses.
- **C-SCAN (Circular SCAN):** moves to a boundary, wraps to the other end, and continues in the same direction.

The program displays service order, the head path, total head movement, average movement per request, and the algorithm with the lowest total movement for the supplied input.

## Requirements
- Python 3.10 or later
- No external Python packages required

## Run locally
1. Install Python from [python.org](https://www.python.org/downloads/) if needed.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

```bash
python main.py
```

On some systems, use `python3 main.py`.

## Example input
```text
Enter disk size (number of tracks): 200
Enter initial head position (0 to 199): 53
Enter disk requests separated by spaces (e.g. 98 183 37 122): 98 183 37 122 14 124 65 67
Initial direction for SCAN/C-SCAN (left/right): left
```

## Calculation
Head movement between two consecutive positions is the absolute difference:

`movement = abs(current_position - previous_position)`

Total head movement is the sum of movement between every consecutive position in the head path. Average movement per request is total head movement divided by the number of requests.

For SCAN and C-SCAN, movement to disk boundaries and the C-SCAN wrap-around are included in the path and total movement.

## Project structure
```text
disk-scheduling-simulator/
├── main.py
├── README.md
├── .gitignore
└── LICENSE
```

## GitHub upload
1. Create a new repository on GitHub.
2. Upload `main.py`, `README.md`, `.gitignore`, and `LICENSE`, or upload this ZIP after extracting it.
3. To use Git commands instead, run:

```bash
git init
git add .
git commit -m "Add disk scheduling simulator"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

Replace the example remote URL with your own repository URL.

## Future improvements
- Add a graphical interface.
- Draw a head-movement chart.
- Add LOOK and C-LOOK.
- Export comparison results to a file.
