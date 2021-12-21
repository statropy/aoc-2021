import unittest

class Node():
    root = None
    searched = set()
    leaves = []


    def __init__(self, left=None, right=None, v=None, parent=None):
        self.v = v
        self.left = left
        self.right = right
        self.parent = parent

    @staticmethod
    def reset():
        Node.searched = set()
        Node.leaves = []

    @staticmethod
    def add(right):
        return Node.combine(Node.root, right)

    @staticmethod
    def combine(left, right):
        if left is None:
            left = Node.root
        n = Node(left=left, right=right)
        left.parent = n
        right.parent = n
        Node.root = n

        again = True
        while again:
            Node.reset()
            again = Node.explode()
            if not again:
                again = Node.split()
        return Node.root

    @staticmethod
    def __parse(s, parent=None):
        #s[0] == [
        n = Node(parent=parent)
        if s[1] == '[':
            n.left, s = Node.__parse(s[1:], n)
        else:
            n.left = Node(v=int(s[1]), parent=n)
        #skip to comma
        _, s = s.split(',',1)
        if s[0] == '[':
            n.right, s = Node.__parse(s, n)
        else:
            n.right = Node(v=int(s[0]), parent=n)

        return n, s[1:]

    @staticmethod
    def create(s):
        n, _ = Node.__parse(s)
        return n

    def __repr__(self):
        if self.isleaf():
            return repr(self.v)
        return '['+repr(self.left)+','+repr(self.right)+']'

    @staticmethod
    def nextleaf(n):
        if n.isleaf():
            n = n.parent
        while n is not None:
            if n.left not in Node.searched:
                if n.left.isleaf():
                    Node.searched.add(n.left)
                    Node.leaves.append(n.left)
                    return n.left
                else:
                    n = n.left
            elif n.right not in Node.searched:
                if n.right.isleaf():
                    Node.searched.add(n.right)
                    Node.leaves.append(n.right)
                    return n.right
                else:
                    n = n.right
            else:
                Node.searched.add(n)
                n = n.parent
        return n

    @staticmethod
    def doexplode(leaf):
        p = leaf.parent
        if len(Node.leaves) > 1:
            Node.leaves[-2].v += leaf.v

        right = Node.nextleaf(leaf)
        eright = Node.nextleaf(right)
        if eright is not None:
            eright.v += right.v
        p.right = None
        p.left = None
        p.v = 0

    @staticmethod
    def explode(n=None):
        if n is None:
            n = Node.root
        leaf = Node.nextleaf(n)
        while leaf is not None:
            d = leaf.depth()
            if d > 4:
                Node.doexplode(leaf)
                return True
            leaf = Node.nextleaf(leaf)
        return False

    @staticmethod
    def split():
        for leaf in Node.leaves:
            if leaf.v > 9:
                leaf.left = Node(v=leaf.v // 2, parent=leaf)
                leaf.right = Node(v=leaf.v - leaf.left.v, parent=leaf)
                leaf.v = None
                return True
        return False

    def depth(self):
        d = 0
        n = self.parent
        while n is not None:
            n = n.parent
            d += 1
        return d

    def isleaf(self):
        return self.v is not None

    def magnitude(self):
        if self.left.isleaf():
            left = self.left.v
        else:
            left = self.left.magnitude()
        if self.right.isleaf():
            right = self.right.v
        else:
            right = self.right.magnitude()

        return left*3 + right*2

def part1(lines):
    n = Node.create(lines[0])
    for line in lines[1:]:
        n = Node.combine(n,Node.create(line))
    return n.magnitude()

def part2(lines):
    mm = 0
    for i in range(len(lines)):
        for j in range(i+1,len(lines)):
            mag1 = Node.combine(Node.create(lines[i]), Node.create(lines[j])).magnitude()
            mag2 = Node.combine(Node.create(lines[j]), Node.create(lines[i])).magnitude()
            mm = max(mm,mag1,mag2)
    return mm

class TestDay18(unittest.TestCase):

    def test_1(self):
         with open('./input18.txt', 'r') as f:
            self.assertEqual(part1([s.strip() for s in list(f)]), 3494)

    def test_2(self):
         with open('./input18.txt', 'r') as f:
            self.assertEqual(part2([s.strip() for s in list(f)]), 4712)

if __name__ == '__main__':
    unittest.main()
