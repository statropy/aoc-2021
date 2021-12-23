#day22.py 2021
import unittest

def parse(lines, cuboids, minv=None, maxv=None):
    for line in lines:
        action, line = line.strip().split(' ', 1)
        x,y,z = line.split(',')
        xmin, xmax = [int(v) for v in x[2:].split('..')]
        ymin, ymax = [int(v) for v in y[2:].split('..')]
        zmin, zmax = [int(v) for v in z[2:].split('..')]

        if minv is not None and maxv is not None:
            if xmin < minv or xmax > maxv or ymin < minv or ymax > maxv or zmin < minv or zmax > maxv:
                continue
        for x in range(xmin,xmax+1):
            for y in range(ymin, ymax+1):
                for z in range(zmin, zmax+1):
                        if action == 'on':
                            cuboids.add((x,y,z))
                        else:
                            cuboids.discard((x,y,z))
    return cuboids

#brute force
def part1(lines):
    cuboids = parse(lines, set(),-50,50)
    return len(cuboids)

class Cuboid():
    def __init__(self,xmin=0,xmax=0,ymin=0,ymax=0,zmin=0,zmax=0):
        self.coords = [[xmin,xmax],[ymin,ymax],[zmin,zmax]]
        self.volume = (xmax-xmin+1)*(ymax-ymin+1)*(zmax-zmin+1)
        self.overlaps = []

    def __len__(self):
        return self.volume - sum([len(o) for o in self.overlaps])

    def __repr__(self):
        return '{}'.format(self.coords)

    def overlap(self, other):
        for i in range(3):
            if (other.coords[i][0] > self.coords[i][1] or
                other.coords[i][1] < self.coords[i][0]):
                return
        z = [0]*6
        for i in range(3):
            z[i*2] = max(self.coords[i][0], other.coords[i][0])
            z[i*2+1] = min(self.coords[i][1], other.coords[i][1])
        neg = Cuboid(*z)
        for n in self.overlaps:
            n.overlap(neg)
        self.overlaps.append(neg)

def part2(lines, exclude=None):
    cuboids = []
    for line in lines:
        action, line = line.strip().split(' ', 1)
        x,y,z = line.split(',')
        xmin, xmax = [int(v) for v in x[2:].split('..')]
        ymin, ymax = [int(v) for v in y[2:].split('..')]
        zmin, zmax = [int(v) for v in z[2:].split('..')]

        if exclude is not None and (xmin < -exclude or xmax > exclude or ymin < -exclude or ymax > exclude or zmin < -exclude or zmax > exclude):
                continue
        newcb = Cuboid(xmin,xmax,ymin,ymax,zmin,zmax)
        for c in cuboids:
            c.overlap(newcb)
        if action == 'on':
            cuboids.append(newcb)
    return sum([len(c) for c in cuboids])

class TestDay22(unittest.TestCase):
    def test_1a(self):
        with open('./test22.txt', 'r') as f:
            self.assertEqual(part2(list(f),50), 39)

    def test_1b(self):
        with open('./test22b.txt', 'r') as f:
            self.assertEqual(part2(list(f),50), 590784)

    def test_1(self):
        with open('./input22.txt', 'r') as f:
            self.assertEqual(part2(list(f),50), 650099)

    def test_2a(self):
        with open('./test22c.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 2758514936282235)

    def test_2(self):
        with open('./input22.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 1254011191104293)

    def test_z1(self):
        c = Cuboid(10,12,10,12,10,12)
        self.assertEqual(len(c), 27)

if __name__ == '__main__':
    unittest.main()
