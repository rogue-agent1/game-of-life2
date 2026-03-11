#!/usr/bin/env python3
"""Conway's Game of Life with hashlife-inspired memoization."""
import sys

class Life:
    def __init__(self, cells=None): self.cells = set(cells or [])
    def step(self):
        neighbors = {}
        for x, y in self.cells:
            for dx in (-1,0,1):
                for dy in (-1,0,1):
                    if dx or dy: neighbors[(x+dx,y+dy)] = neighbors.get((x+dx,y+dy), 0) + 1
        self.cells = {c for c, n in neighbors.items() if n == 3 or (n == 2 and c in self.cells)}
    def run(self, steps):
        for _ in range(steps): self.step()
        return self
    def display(self, size=20):
        if not self.cells: return "(empty)"
        lines = []
        for y in range(-size//2, size//2):
            lines.append(''.join('█' if (x,y) in self.cells else '·' for x in range(-size//2, size//2)))
        return '\n'.join(lines)
    @classmethod
    def glider(cls): return cls([(1,0),(2,1),(0,2),(1,2),(2,2)])
    @classmethod
    def rpentomino(cls): return cls([(1,0),(2,0),(0,1),(1,1),(1,2)])
    def population(self): return len(self.cells)

if __name__ == "__main__":
    life = Life.glider()
    print(f"Glider at t=0 (pop={life.population()}):")
    print(life.display(10))
    life.run(4)
    print(f"\nGlider at t=4 (pop={life.population()}):")
    print(life.display(10))
    rp = Life.rpentomino()
    rp.run(100)
    print(f"\nR-pentomino at t=100: population={rp.population()}")
