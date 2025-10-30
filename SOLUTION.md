# Tetris Engine Solution

## Overview

A Python implementation of simplified Tetris that processes lines of piece placements and returns the resulting grid height.

## Usage

### Dependencies
- Built and tested on Python 3.10
- No libraries or other external dependencies required

### Running the Program

#### On Linux:
```bash
chmod +x tetris
./tetris < input.txt
```
or provide input directly:
```bash
echo "Q0,I4,Q8" | ./tetris
```

#### On Windows:
```bash
python tetris.py < input.txt
```
or directly:
```bash
echo Q0,I4,Q8 | python tetris.py
```

## Complexity

### Space Complexity
Input is processed line by line, so the memory usage is O(1) regardless of the file size.
The sparse grid implementation uses O(n) space where n is the number of filled cells. It can handle arbitrarily tall grids without pre-allocating memory.

### Time Complexity
For each piece, the placement takes the most time which is O(p x h) where p is the number of cells in the piece and h is the maximumcolumn height (at that moment).
Hence the total complexity is O(m x p x h_avg) where m is the number of pieces.


## Extensibility

The solution is designed for easy extension:

### Adding New Pieces
Simply add to the `PIECES` dictionary:
```python
PIECES = {
    'Q': [(0, 0), (1, 0), (0, 1), (1, 1)],
    # Add new piece:
    'X': [(0, 1), (1, 0), (1, 1), (1, 2)],  # Cross shape
}
```

### Changing Grid Width
The `GRID_WIDTH` constant can be modifed for different variations of the game

### Adding movements
The `add_piece` method is designed to be modular and are seperated into different steps. To add more extensions (e.g. shifts, rotations), simply add new steps inside the method.
However, due to the nature of the task, the most efficient way to return the height is to directly return the grid after each step. This is different from the original game where pieces fall step by step.


## Testing
The sample_test.py is modified to support Windows.
The test cases are passed and some extra testing were done.


