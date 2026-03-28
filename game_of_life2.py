#!/usr/bin/env python3
"""Conway's Game of Life — patterns, RLE import, ASCII animation."""
import sys, time

PATTERNS = {
    "glider": [(0,1),(1,2),(2,0),(2,1),(2,2)],
    "blinker": [(1,0),(1,1),(1,2)],
    "toad": [(1,1),(1,2),(1,3),(2,0),(2,1),(2,2)],
    "beacon": [(0,0),(0,1),(1,0),(2,3),(3,2),(3,3)],
    "rpentomino": [(0,1),(0,2),(1,0),(1,1),(2,1)],
    "acorn": [(0,1),(1,3),(2,0),(2,1),(2,4),(2,5),(2,6)],
}

def step(cells):
    neighbors = {}
    for r,c in cells:
        for dr in (-1,0,1):
            for dc in (-1,0,1):
                if dr or dc: neighbors[(r+dr,c+dc)] = neighbors.get((r+dr,c+dc), 0) + 1
    new = set()
    for pos, count in neighbors.items():
        if count == 3 or (count == 2 and pos in cells): new.add(pos)
    return new

def display(cells, w=40, h=20, offset=(0,0)):
    or_, oc = offset
    grid = [["."]*w for _ in range(h)]
    for r,c in cells:
        r2, c2 = r-or_, c-oc
        if 0<=r2<h and 0<=c2<w: grid[r2][c2] = "█"
    for row in grid: print("".join(row))

def cli():
    pattern = sys.argv[1] if len(sys.argv)>1 else "glider"
    gens = int(sys.argv[2]) if len(sys.argv)>2 else 20
    cells = set(PATTERNS.get(pattern, PATTERNS["glider"]))
    for g in range(gens):
        print(f"[2J[HGeneration {g} ({len(cells)} cells):")
        display(cells); cells = step(cells)
        time.sleep(0.2)
    print(f"Final: {len(cells)} cells")

if __name__ == "__main__": cli()
