#!/usr/bin/env python3
"""game_of_life2 - Conway's Game of Life with patterns."""
import sys,time,os
PATTERNS={"glider":[(0,1),(1,2),(2,0),(2,1),(2,2)],"blinker":[(1,0),(1,1),(1,2)],
    "block":[(0,0),(0,1),(1,0),(1,1)],"beacon":[(0,0),(0,1),(1,0),(2,3),(3,2),(3,3)],
    "rpentomino":[(0,1),(0,2),(1,0),(1,1),(2,1)]}
def step(grid,rows,cols):
    new=set()
    candidates=set()
    for r,c in grid:
        for dr in(-1,0,1):
            for dc in(-1,0,1):candidates.add(((r+dr)%rows,(c+dc)%cols))
    for r,c in candidates:
        n=sum(1 for dr in(-1,0,1) for dc in(-1,0,1) if(dr or dc) and((r+dr)%rows,(c+dc)%cols) in grid)
        if(r,c) in grid:
            if n in(2,3):new.add((r,c))
        elif n==3:new.add((r,c))
    return new
def display(grid,rows,cols):
    for r in range(rows):print("".join("█" if(r,c) in grid else " " for c in range(cols)))
if __name__=="__main__":
    pattern=sys.argv[1] if len(sys.argv)>1 else "glider"
    steps=int(sys.argv[2]) if len(sys.argv)>2 else 50
    rows,cols=24,60;grid=set()
    cells=PATTERNS.get(pattern,PATTERNS["glider"])
    for r,c in cells:grid.add((r+rows//2,c+cols//2))
    for i in range(steps):
        os.system("clear" if os.name!="nt" else "cls")
        print(f"Step {i}, alive: {len(grid)}");display(grid,rows,cols);grid=step(grid,rows,cols)
        time.sleep(0.1)
