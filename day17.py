#day17.py 2021
import unittest
import sys

def getminx(xleft):
    n = 1
    x = 1
    while True:
        # print(n,x,sum(list(range(n+1))))
        if x < xleft:
            n += 1
            x += n
        else:
            return n

def hitmaxy(x,y,xleft, xright, ybottom, ytop):
    px, py = 0,0
    maxy = -sys.maxsize - 1
    while True:
        px += x
        py += y
        maxy = max(maxy,py)
        #print(px,py,x,y,maxy)
        if px >= xleft and px <= xright and py <= ytop and py >= ybottom:
            return maxy
        elif px > xright or py < ybottom:
            return -sys.maxsize - 1

        if x > 0:
            x -= 1
        y -= 1

def isahit(x,y,xleft, xright, ybottom, ytop):
    px, py = 0,0
    while True:
        px += x
        py += y
        if px >= xleft and px <= xright and py <= ytop and py >= ybottom:
            return 1
        elif px > xright or py < ybottom:
            return 0

        if x > 0:
            x -= 1
        y -= 1

def part1(xleft, xright, ybottom, ytop):
    minx = getminx(xleft)
    maxy = -sys.maxsize - 1
    for y in range(ybottom, 100):
        for x in range(minx, xright+1):
            hit = hitmaxy(x,y,xleft, xright, ybottom, ytop)
            maxy = max(hit,maxy)
    return maxy

def part2(xleft, xright, ybottom, ytop):
    minx = getminx(xleft)
    found = 0
    for y in range(ybottom, 1000):
        foundthisy = 0
        for x in range(minx, xright+1):
            hit = isahit(x,y,xleft, xright, ybottom, ytop)
            # if hit == 1:
            #     print(x,y)
            foundthisy += hit
        # if found > 0 and foundthisy == 0:
        #     break
        found += foundthisy
    return found

class TestDay17(unittest.TestCase):
    def test_1a(self):
        self.assertEqual(part1(20,30,-10,-5), 45)

    def test_1b(self):
        self.assertEqual(hitmaxy(7,2,20,30,-10,-5), 3)

    def test_1c(self):
        self.assertEqual(hitmaxy(6,9,20,30,-10,-5), 45)

    def test_1(self):
        self.assertEqual(part1(195,238,-93,-67), 4278)

    def test_2a(self):
        self.assertEqual(part2(20,30,-10,-5), 112)

    def test_2(self):
        self.assertEqual(part2(195,238,-93,-67), 1994)
    
if __name__ == '__main__':
    unittest.main()
