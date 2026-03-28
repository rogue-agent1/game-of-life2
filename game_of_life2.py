#!/usr/bin/env python3
"""game_of_life2 - Conway Game of Life with pattern library."""
import argparse, time, os

PATTERNS = {
    "glider": [(0,1),(1,2),(2,0),(2,1),(2,2)],
    "blinker": [(1,0),(1,1),(1,2)],
    "block": [(0,0),(0,1),(1,0),(1,1)],
    "beacon": [(0,0),(0,1),(1,0),(2,3),(3,2),(3,3)],
    "pulsar": [(2,4),(2,5),(2,6),(2,10),(2,11),(2,12),(4,2),(5,2),(6,2),(4,7),(5,7),(6,7),
               (4,9),(5,9),(6,9),(4,14),(5,14),(6,14),(7,4),(7,5),(7,6),(7,10),(7,11),(7,12),
               (9,4),(9,5),(9,6),(9,10),(9,11),(9,12),(10,2),(11,2),(12,2),(10,7),(11,7),(12,7),
               (10,9),(11,9),(12,9),(10,14),(11,14),(12,14),(14,4),(14,5),(14,6),(14,10),(14,11),(14,12)],
    "rpentomino": [(0,1),(0,2),(1,0),(1,1),(2,1)],
    "gosper_gun": [(5,1),(5,2),(6,1),(6,2),(3,13),(3,14),(4,12),(4,16),(5,11),(5,17),(6,11),(6,15),(6,17),(6,18),(7,11),(7,17),(8,12),(8,16),(9,13),(9,14),(3,21),(3,22),(4,21),(4,22),(5,21),(5,22),(2,23),(6,23),(1,25),(2,25),(6,25),(7,25),(3,35),(3,36),(4,35),(4,36)],
}

class Life:
    def __init__(self, w, h):
        self.w = w; self.h = h; self.cells = set()

    def add_pattern(self, name, ox=0, oy=0):
        for y, x in PATTERNS.get(name, []):
            self.cells.add((y + oy, x + ox))

    def step(self):
        neighbors = {}
        for y, x in self.cells:
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    if dy == 0 and dx == 0: continue
                    n = (y+dy, x+dx)
                    neighbors[n] = neighbors.get(n, 0) + 1
        new = set()
        for cell, count in neighbors.items():
            if count == 3 or (count == 2 and cell in self.cells):
                y, x = cell
                if 0 <= y < self.h and 0 <= x < self.w:
                    new.add(cell)
        self.cells = new

    def display(self):
        lines = []
        for y in range(self.h):
            line = ""
            for x in range(self.w):
                line += "█" if (y, x) in self.cells else " "
            lines.append(line)
        return "\n".join(lines)

def main():
    p = argparse.ArgumentParser(description="Game of Life")
    p.add_argument("-p", "--pattern", default="glider", choices=list(PATTERNS.keys()))
    p.add_argument("-W", "--width", type=int, default=40)
    p.add_argument("-H", "--height", type=int, default=20)
    p.add_argument("-g", "--generations", type=int, default=50)
    p.add_argument("-d", "--delay", type=float, default=0.1)
    p.add_argument("--static", action="store_true")
    args = p.parse_args()
    life = Life(args.width, args.height)
    life.add_pattern(args.pattern, 5, 5)
    for gen in range(args.generations):
        if args.static:
            if gen % 10 == 0: print(f"Gen {gen}: {len(life.cells)} cells")
        else:
            os.system('clear' if os.name != 'nt' else 'cls')
            print(f"Gen {gen} | Cells: {len(life.cells)} | Pattern: {args.pattern}")
            print(life.display())
            time.sleep(args.delay)
        life.step()
        if not life.cells: print("Extinct!"); break
    print(f"Final: {len(life.cells)} cells after {args.generations} generations")

if __name__ == "__main__":
    main()
