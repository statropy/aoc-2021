#day11.py 2021
import unittest

delta = [(x,y) for y in range(-1,2) for x in range(-1,2)]

def do_step(grid, flashed, r, c):
    if r < 0 or c < 0 or r > 9 or c > 9 or grid[r][c] > 9:
        return
    grid[r][c] += 1
    if grid[r][c] > 9:
        flashed.add((r,c))
        for dr,dc in delta:
            do_step(grid, flashed, r+dr, c+dc)

def part1(lines):
    grid = []
    count = 0
    for line in lines:
        grid.append([int(n) for n in line.strip()])
    for step in range(100):
        flashed = set()
        for r,row in enumerate(grid):
            for c,octopus in enumerate(row):
                do_step(grid, flashed, r, c)
        for r,c in flashed:
            grid[r][c] = 0
        count += len(flashed)
    return count

def part2(lines):
    grid = []
    for line in lines:
        grid.append([int(n) for n in line.strip()])
    for step in range(1000):
        flashed = set()
        for r,row in enumerate(grid):
            for c,octopus in enumerate(row):
                do_step(grid, flashed, r, c)
        for r,c in flashed:
            grid[r][c] = 0
        if len(flashed) == 100:
            return step+1
    return None

class TestDay11(unittest.TestCase):
    def test_1a(self):
        with open('./test11.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 1656)

    def test_1(self):
        with open('./input11.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 1741)

    def test_2a(self):
        with open('./test11.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 195)

    def test_2(self):
        with open('./input11.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 440)

if __name__ == '__main__':
    unittest.main()
