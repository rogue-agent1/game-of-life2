#!/usr/bin/env python3
"""game_of_life2 - Conway's Game of Life with pattern library."""
import sys

def step(cells):
    if not cells:
        return set()
    neighbors = {}
    for x, y in cells:
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue
                n = (x + dx, y + dy)
                neighbors[n] = neighbors.get(n, 0) + 1
    new = set()
    for cell, count in neighbors.items():
        if count == 3 or (count == 2 and cell in cells):
            new.add(cell)
    return new

def run(cells, steps):
    for _ in range(steps):
        cells = step(cells)
    return cells

PATTERNS = {
    "blinker": {(0,0),(1,0),(2,0)},
    "glider": {(0,1),(1,2),(2,0),(2,1),(2,2)},
    "block": {(0,0),(0,1),(1,0),(1,1)},
    "beacon": {(0,0),(0,1),(1,0),(2,3),(3,2),(3,3)},
}

def test():
    # blinker oscillates with period 2
    b = PATTERNS["blinker"]
    b1 = step(b)
    b2 = step(b1)
    assert b2 == b
    assert b1 != b
    # block is still life
    bl = PATTERNS["block"]
    assert step(bl) == bl
    # glider moves
    g = PATTERNS["glider"]
    g4 = run(g, 4)
    assert len(g4) == 5
    # translated by (1,1) after 4 steps
    min_x = min(x for x, y in g4)
    min_y = min(y for x, y in g4)
    normalized = {(x - min_x, y - min_y) for x, y in g4}
    orig_norm = {(x - min(a for a,b in g), y - min(b for a,b in g)) for x, y in g}
    assert normalized == orig_norm
    print("OK: game_of_life2")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        test()
    else:
        print("Usage: game_of_life2.py test")
