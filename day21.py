#day21.py 2021
import unittest

def turn(pos, roll):
    return ((pos-1+roll)%10)+1

def part1(p1,p2):
    score = [0,0]
    pos = [p1,p2]
    i = 1
    d = 1
    while True:
        i = (i+1)&1
        roll = (d+1)*3
        d += 3
        pos[i] = turn(pos[i],roll)
        score[i] += pos[i]
        if score[i] >= 1000:
            return score[i-1]*(d-1)


WEIGHT = {3:1, 4:3, 5:6, 6:7, 7:6, 8:3, 9:1}
TURNS = {}

#build table (startpos, roll) -> (nextpos, score)
def make_turns():
    for p in range(1,11):
        for r in range(3,10):
            TURNS[(p,r)] = turn(p,r)

def init_nodes(start):
    nodes = []
    for r in range(3,10):
        newpos = TURNS[start,r]
        nodes.append((newpos, WEIGHT[r], newpos))
    return nodes

def nextlevel(nodes):
    notdone = []
    total = 0
    for n in nodes:
        for r in range(3,10):
            np = TURNS[n[0],r]
            w = n[1] * WEIGHT[r]
            s = np + n[2]
            if s >= 21:
                total += w
            else:
                notdone.append((np,w,s))
    return notdone, total

def gettotals(start):
    nodes = init_nodes(start)
    totals = [0]
    while len(nodes) > 0:
        nodes, t = nextlevel(nodes)
        totals.append(t)
    return totals

def calc1(p1, p2):
    t1 = 0
    d = 1
    for i in range(1,len(p1)):
        d = d*27 - p2[i-1]
        t1 += p1[i] * d
    return t1

def calc2(p1,p2):
    t2 = 0
    d = 1
    for i in range(len(p2)):
        d = d*27 - p1[i]
        t2 += p2[i] * d
    return t2

def part2(s1, s2):
    make_turns()
    p1 = gettotals(s1)
    p2 = gettotals(s2)
    t1 = calc1(p1, p2)
    t2 = calc2(p1, p2)
    return max(t1,t2)

class TestDay21(unittest.TestCase):
    def test_1a(self):
        self.assertEqual(part1(4,8), 739785)

    def test_1(self):
        self.assertEqual(part1(8,6), 503478)

    def test_2a(self):
        self.assertEqual(part2(4,8), 444356092776315)

    def test_2(self):
        self.assertEqual(part2(8,6), 716241959649754)

if __name__ == '__main__':
    unittest.main()
