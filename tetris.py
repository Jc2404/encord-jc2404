#!/usr/bin/env python3
"""
Simplified Tetris Game

Simulation of a simplified Tetris for the Encord programming challenge by Jiaqi Cao.
"""

import sys
from typing import Dict, List, Tuple, Set

GRID_WIDTH = 10

# Piece definition
# (0, 0) is the top-left corner of the peice
PIECES = {
    'Q': [(0, 0), (1, 0), (0, 1), (1, 1)],
    'Z': [(0, 0), (1, 0), (1, 1), (2, 1)],
    'S': [(1, 0), (2, 0), (0, 1), (1, 1)],
    'T': [(0, 0), (1, 0), (2, 0), (1, 1)],
    'I': [(0, 0), (1, 0), (2, 0), (3, 0)],
    'L': [(0, 0), (0, 1), (0, 2), (1, 2)],
    'J': [(1, 0), (1, 1), (0, 2), (1, 2)],
}


class TetrisGrid:
    """
    Represents the Tetris game grid using sparse grid.
    """
    
    def __init__(self, width: int = GRID_WIDTH):
        self.width = width
        self.filled: Dict[Tuple[int, int], bool] = {}
        self.column_heights = [0] * width
    
    def add_piece(self, piece_type: str, column: int) -> None:
        """
        Input:
            piece_type: Type of piece (Q, Z, S, T, I, L, J)
            column: column where the piece enters (left)
        """
        piece_coords = PIECES[piece_type]
        
        # Find the lowest valid y-position
        drop_y = self._find_drop_position(piece_coords, column)
        
        for dx, dy in piece_coords:
            x, y = column + dx, drop_y + dy
            self.filled[(x, y)] = True
            self.column_heights[x] = max(self.column_heights[x], y + 1)
        
        self._clear_complete_rows()
    
    def _find_drop_position(self, piece_coords: List[Tuple[int, int]], column: int) -> int:
        """
        Inputs:
            piece_coords: List of coordinates for the piece
            column: position of piece (left)
        """
        max_landing_height = 0
        
        for dx, dy in piece_coords:
            x = column + dx
            
            # Find the highest occupied cell in this column
            for y in range(self.column_heights[x], -1, -1):
                if (x, y) in self.filled:
                    landing_y = y + 1 - dy
                    max_landing_height = max(max_landing_height, landing_y)
                    break
        
        return max_landing_height
    
    def _clear_complete_rows(self) -> None:
        if not self.filled:
            return
        
        # Find the range of rows to check
        max_height = max(self.column_heights)
        if max_height == 0:
            return
        
        # Identify complete rows
        rows_to_clear = []
        for y in range(max_height):
            if self._is_row_complete(y):
                rows_to_clear.append(y)
        
        if not rows_to_clear:
            return
        
        rows_to_clear_set = set(rows_to_clear)
        new_filled = {}
        
        for (x, y), val in self.filled.items():
            if y in rows_to_clear_set:
                continue
            
            # Count how many cleared rows are below this cell
            rows_below = sum(1 for cleared_y in rows_to_clear if cleared_y < y)
            new_y = y - rows_below
            new_filled[(x, new_y)] = val
        
        self.filled = new_filled
        
        self.column_heights = [0] * self.width
        for x, y in self.filled.keys():
            self.column_heights[x] = max(self.column_heights[x], y + 1)
    
    def _is_row_complete(self, y: int) -> bool:
        return all((x, y) in self.filled for x in range(self.width))
    
    def get_height(self) -> int:
        return max(self.column_heights) if self.column_heights else 0


def process_line(line: str) -> int:
    """
    Process a single line of input and return the resulting height.
    """
    line = line.strip()
    if not line:
        return 0
    
    grid = TetrisGrid()
    
    # Parse and process each piece
    pieces = line.split(',')
    for piece_str in pieces:
        piece_type = piece_str[0]
        column = int(piece_str[1])
        grid.add_piece(piece_type, column)
    
    return grid.get_height()


def main():
    for line in sys.stdin:
        height = process_line(line)
        print(height)


if __name__ == '__main__':
    main()

