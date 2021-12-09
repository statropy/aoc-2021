#day9.py 2021
import unittest
import math

def lowpoints(lines):
    lows = []
    grid = []
    for line in lines:
        grid.append([int(n) for n in line.strip()])
    for r,row in enumerate(grid):
        for c,item in enumerate(row):
            if r > 0 and grid[r-1][c] <= item:
                continue
            if r < len(grid)-1 and grid[r+1][c] <= item:
                continue
            if c > 0 and grid[r][c-1] <= item:
                continue
            if c < len(row)-1 and grid[r][c+1] <= item:
                continue
            lows.append((r,c))
    return grid, lows

def part1(lines):
    grid, lows = lowpoints(lines)
    return sum([grid[r][c]+1 for r,c in lows])

def addneighbors(grid, basin, r, c):
    basin.add((r,c))
    if r > 0:
        if (r-1,c) not in basin:
            if grid[r-1][c] < 9:
                addneighbors(grid, basin, r-1, c)
    if r < len(grid)-1:
        if (r+1,c) not in basin:
            if grid[r+1][c] < 9:
                addneighbors(grid, basin, r+1, c)
    if c > 0:
        if (r,c-1) not in basin:
            if grid[r][c-1] < 9:
                addneighbors(grid, basin, r, c-1)
    if c < len(grid[0])-1:
        if (r,c+1) not in basin:
            if grid[r][c+1] < 9:
                addneighbors(grid, basin, r, c+1)

def part2(lines):
    basins = []
    grid, lows = lowpoints(lines)
    for lr,lc in lows:
        basin = set()
        addneighbors(grid, basin, lr, lc)
        basins.append(len(basin))
    return math.prod(sorted(basins)[-3:])

class TestDay9(unittest.TestCase):
    def test_1a(self):
        with open('./test9.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 15)

    def test_1(self):
        with open('./input9.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 496)

    def test_2a(self):
        with open('./test9.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 1134)

    def test_2(self):
        with open('./input9.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 902880)

if __name__ == '__main__':
    unittest.main()
