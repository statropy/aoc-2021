#day11.py 2021
import unittest

def delta(r,c):
    for dr in range(r-1,r+2):
        if dr >=0 and dr <=9:
            for dc in range(c-1,c+2):
                if dc >=0 and dc <=9:
                    yield(dr,dc)

def do_step(grid, flashed, r, c):
    if grid[r][c] > 9:
        return
    grid[r][c] += 1
    if grid[r][c] > 9:
        flashed.add((r,c))
        for dr,dc in delta(r,c):
            do_step(grid, flashed, dr, dc)

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
