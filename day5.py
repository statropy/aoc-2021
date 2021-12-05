#day5.py 2021
import unittest

def vents(lines, diag=False):
    grid = {}
    for line in lines:
        x1,y1,x2,y2 = [int(x) for x in line.replace(' -> ', ',').split(',')]
        if x1 == x2:
            if y2 < y1:
                y1, y2 = y2, y1
            for y in range(y1, y2+1):
                grid[(x1,y)] = grid.get((x1,y),0) + 1
        elif y1 == y2:
            if x2 < x1:
                x1, x2 = x2, x1
            for x in range(x1, x2+1):
                grid[(x,y1)] = grid.get((x,y1),0) + 1
        elif diag:
            x, y = x1, y1
            xd, yd = 1, 1
            if x2 < x1:
                xd = -1
            if y2 < y1:
                yd = -1
            while x != x2 and y != y2:
                grid[(x,y)] = grid.get((x,y),0) + 1
                x += xd
                y += yd
            grid[(x,y)] = grid.get((x,y),0) + 1
            
    return len([k for k,v in grid.items() if v > 1])

def part1(lines):
    return vents(lines)

def part2(lines):
    return vents(lines, True)

class TestDay5(unittest.TestCase):
    def test_1a(self):
        with open('./test5.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 5)

    def test_1(self):
        with open('./input5.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 7297)

    def test_2a(self):
        with open('./test5.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 12)

    def test_2(self):
        with open('./input5.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 21038)

if __name__ == '__main__':
    unittest.main()
