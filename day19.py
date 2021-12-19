#day19.py 2021
from types import resolve_bases
from typing import get_origin
import unittest
import numpy as np

rotation_matrix = [
    np.array([[1,0,0],
              [0,1,0],
              [0,0,1]]),
    np.array([[1,0,0],
              [0,0,-1],
              [0,1,0]]),
    np.array([[1,0,0],
              [0,-1,0],
              [0,0,-1]]),
    np.array([[1,0,0],
              [0,0,1],
              [0,-1,0]]),

    np.array([[0,-1,0],
              [1,0,0],
              [0,0,1]]),
    np.array([[0,0,1],
              [1,0,0],
              [0,1,0]]),
    np.array([[0,1,0],
              [1,0,0],
              [0,0,-1]]),
    np.array([[0,0,-1],
              [1,0,0],
              [0,-1,0]]),

    np.array([[-1,0,0],
              [0,-1,0],
              [0,0,1]]),
    np.array([[-1,0,0],
              [0,0,-1],
              [0,-1,0]]),
    np.array([[-1,0,0],
              [0,1,0],
              [0,0,-1]]),
    np.array([[-1,0,0],
              [0,0,1],
              [0,1,0]]),

    np.array([[0,1,0],
              [-1,0,0],
              [0,0,1]]),
    np.array([[0,0,1],
              [-1,0,0],
              [0,-1,0]]),
    np.array([[0,-1,0],
              [-1,0,0],
              [0,0,-1]]),
    np.array([[0,0,-1],
              [-1,0,0],
              [0,1,0]]),

    np.array([[0,0,-1],
              [0,1,0],
              [1,0,0]]),
    np.array([[0,1,0],
              [0,0,1],
              [1,0,0]]),
    np.array([[0,0,1],
              [0,-1,0],
              [1,0,0]]),
    np.array([[0,-1,0],
              [0,0,-1],
              [1,0,0]]),

    np.array([[0,0,-1],
              [0,-1,0],
              [-1,0,0]]),
    np.array([[0,-1,0],
              [0,0,1],
              [-1,0,0]]),
    np.array([[0,0,1],
              [0,1,0],
              [-1,0,0]]),
    np.array([[0,1,0],
              [0,0,-1],
              [-1,0,0]]),
]

class Day19:
    def __init__(self, lines):
        self.scanmap = {}
        self.foundmap = {}
        self.beacons = set()
        self.scanners = {}
        self.parse(lines)
        self.compared = set() #tuples of (a,b) (b,a) if no overlop

    def parse(self, lines):
        scanner = 0
        getbeacons = False
        for line in lines:
            if len(line) == 0:
                getbeacons = False
            elif getbeacons:
                x,y,z = map(int,line.split(','))
                self.scanmap[scanner].append((x,y,z))
            else:
                line, _ = line[12:].split(' ')
                scanner = int(line)
                self.scanmap[scanner] = list()
                getbeacons = True

    def movebeacons(self, scanner, beacons, dx, dy, dz):
        #add scanner beacons to found relative to 0,0,0
        self.foundmap[scanner] = list()
        self.scanners[scanner] = (dx,dy,dz)
        for x,y,z in beacons:
            self.foundmap[scanner].append((x+dx, y+dy, z+dz))
            self.beacons.add((x+dx,y+dy,z+dz))
        del self.scanmap[scanner]

    def overlaps(self, a, beacons, dx, dy, dz):
        count = 0
        for bx,by,bz in beacons:
            if (bx+dx, by+dy, bz+dz) in self.foundmap[a]:
                count += 1
                if count >= 12:
                    return True
        #print('overlaps',count)
        return False

    def compare(self, a, beacons):
        for ax,ay,az in self.foundmap[a]:
            for bx,by,bz in beacons:
                # move b and check if in a
                dx,dy,dz = ax-bx, ay-by, az-bz
                if self.overlaps(a,beacons,dx,dy,dz):
                    #print('({},{},{}) ({},{},{}) : ({},{},{})'.format(ax,ay,az,bx,by,bz,dx,dy,dz))
                    return dx,dy,dz
        return None

    def getrotation(self, b, r):
        rot = []
        for x,y,z in self.scanmap[b]:
            rot.append(rotation_matrix[r].dot(np.array([x,y,z])))
        return rot

    def rotatecompare(self, a, b):
        #get all rotations
        for r in range(24):
            rot = self.getrotation(b, r)
            #print('compare',a,b,r,rot[0])
            result = self.compare(a, rot)
            if result is not None:
                dx, dy, dz = result
                self.movebeacons(b, rot, dx, dy, dz)
                return True
                #found.append(b)
        return False

    def search(self):
        tofind = list(range(1,len(self.scanmap)))
        nextfind = []
        self.movebeacons(0, self.getrotation(0,0), 0, 0, 0) #make scanner 0 at 0,0
        
        while len(tofind) > 0:
            print('Searching',len(tofind),'scanners')
            for scanner in tofind:
                found = False
                for a in self.foundmap.keys():
                    if (a,scanner) in self.compared:
                        continue
                    print('compare',a,'to',scanner)
                    self.compared.add((a,scanner))
                    if self.rotatecompare(a, scanner):
                        found = True
                        break
                if not found:
                    nextfind.append(scanner)
            tofind = nextfind
            nextfind = []

        return len(self.beacons)

    def maxdistance(self):
        d = 0
        for a in range(len(self.scanners)):
            for b in range(a+1,len(self.scanners)):
                ax,ay,az = self.scanners[a]
                bx,by,bz = self.scanners[b]
                t = sum([abs(ax-bx),abs(ay-by),abs(az-bz)])
                d = max(d,t)

        return d

    def test(self):
        for r in range(24):
            rot = self.getrotation(0, r)
            for x in rot:
                print(x)
            print()

    def test1(self):
        self.movebeacons(0, self.getrotation(0,0), 0, 0, 0) #make scanner 0 at 0,0
        for x in self.foundmap[0]:
            print(x)

def part1(lines):
    d = Day19(lines)
    numbeacons = d.search()
    distance = d.maxdistance()
    return numbeacons, distance

def part1a(lines):
    d = Day19(lines)
    return d.test1()

def part2(lines):
    return 0

class TestDay19(unittest.TestCase):
    def test_1a(self):
        with open('./test19.txt', 'r') as f:
            self.assertEqual(part1([s.strip() for s in list(f)]), (79, 3621))
    def test_1(self):
        with open('./input19.txt', 'r') as f:
            self.assertEqual(part1([s.strip() for s in list(f)]), (326, 10630))
    # def test_1q(self):
    #     with open('./test19.txt', 'r') as f:
    #         self.assertEqual(part1a([s.strip() for s in list(f)]), 79)

    # def test_1(self):
    #     with open('./input19.txt', 'r') as f:
    #         self.assertEqual(part1(list(f)), None)

    # def test_2a(self):
    #     with open('./test19.txt', 'r') as f:
    #         self.assertEqual(part2(list(f)), None)

    # def test_2(self):
    #     with open('./input19.txt', 'r') as f:
    #         self.assertEqual(part2(list(f)), None)

if __name__ == '__main__':
    unittest.main()
