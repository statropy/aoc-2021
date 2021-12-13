#day13.py 2021
import unittest
import matplotlib.pyplot as plt

def parseinput(lines):
    getpoints = True
    points = set()
    folds = []
    for line in lines:
        line = line.strip()
        if len(line) == 0:
            getpoints = False
        elif getpoints:
            x,y = line.split(',')
            points.add((int(x),int(y)))
        else:
            coord,value = line[11:].split('=')
            folds.append((coord,int(value)))
    return points, folds

def foldup(points, f):
    folded = set()
    for x,y in points:
        if y > f:
            y = f + f - y
        folded.add((x,y))
    return folded

def foldleft(points, f):
    folded = set()
    for x,y in points:
        if x > f:
            x = f + f - x
        folded.add((x,y))
    return folded

def foldit(points, folds):
    for coord, value in folds:
        if coord == 'y':
            points = foldup(points, value)
        else:
            points = foldleft(points, value)
    return points

def part1(lines):
    points, folds = parseinput(lines)
    points = foldit(points,folds[:1])
    return len(points)

def part2(lines):
    points, folds = parseinput(lines)
    points = foldit(points,folds)
    x, y = list(zip(*points))
    print()
    for r in range(max(y)+1):
        for c in range(max(x)+1):
            if (c,r) in points:
                print('#', end='')
            else:
                print(' ', end='')
        print()
    print()
    s = plt.scatter(x, y)
    s.axes.invert_yaxis()
    plt.axis('scaled')
    plt.show()

class TestDay13(unittest.TestCase):
    def test_1a(self):
        with open('./test13.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 17)

    def test_1(self):
        with open('./input13.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 647)

    def test_2a(self):
        with open('./test13.txt', 'r') as f:
            self.assertEqual(part2(list(f)), None)

    def test_2(self):
        with open('./input13.txt', 'r') as f:
            self.assertEqual(part2(list(f)), None)

    @classmethod
    def tearDownClass(cls):
        print('Done!')

if __name__ == '__main__':
    unittest.main()
    