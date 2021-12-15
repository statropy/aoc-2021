#day15.py 2021
import unittest
from heapq import *
import sys

def getgrid(lines):
    grid = []
    for line in lines:
        grid.append([int(n) for n in line.strip()])
    return grid, len(grid), len(grid[0])

def getbiggrid(lines):
    grid = []
    for line in lines:
        r = [int(n) for n in line.strip()]
        row = r[:]
        for i in range(4):
            r = [n%9+1 for n in r]
            row.extend(r)
        grid.append(row)
    origheight = len(grid)
    for i in range(4):
        for row in grid[i*origheight:(i+1)*origheight]:
            grid.append([n%9+1 for n in row])
    return grid, len(grid), len(grid[0])

def dijkstra_q(grid, height, width):
    unvisited = []
    finder = {}
    distance = []
    prev = {}
    for row in range(height):
        distance.append([sys.maxsize]*width)
        for col in range(width):
            sz = sys.maxsize
            if row == 0 and col == 0:
                sz = 0
            entry = [sz, col, row]
            finder[(col,row)] = entry
            heappush(unvisited, entry)
    distance[0][0] = 0
    
    while unvisited:
        _, x, y = heappop(unvisited)
        if y == sys.maxsize:
            continue
        del finder[(x,y)]
        neighbors = [(x+1, y), (x,y+1), (x-1, y), (x,y-1)]
        neighbors = [(nx,ny) for nx,ny in neighbors if nx >= 0 and nx < width and ny >= 0 and ny < height] 

        for nx,ny in neighbors:
            d = distance[y][x] + grid[ny][nx]
            if d < distance[ny][nx]:
                distance[ny][nx] = d
                prev[(nx,ny)] = (x,y)
                if (nx,ny) in finder:
                    entry = finder.pop((nx,ny))
                    entry[-1] = sys.maxsize
                entry = [d, nx, ny]
                finder[(nx,ny)] = entry
                heappush(unvisited, entry)

    return distance[-1][-1]

def dijkstra(grid, height, width):
    unvisited = []
    distance = []
    for row in range(height):
        distance.append([sys.maxsize]*width)
        for col in range(width):
            unvisited.append((col,row))
    distance[0][0] = 0
    prev = {}
    
    while unvisited:
        x,y = None,None
        for nx,ny in unvisited:
            if x == None:
                x,y = nx,ny
            elif distance[ny][nx] < distance[y][x]:
                x,y = nx,ny
        neighbors = [(x+1, y), (x,y+1), (x-1, y), (x,y-1)]
        neighbors = [(nx,ny) for nx,ny in neighbors if nx >= 0 and nx < width and ny >= 0 and ny < height] 

        for nx,ny in neighbors:
            d = distance[y][x] + grid[ny][nx]
            if d < distance[ny][nx]:
                distance[ny][nx] = d
                prev[(nx,ny)] = (x,y)
        unvisited.remove((x,y))

    return distance[-1][-1]

def part1(lines):
    grid, height, width = getgrid(lines)
    return dijkstra_q(grid, height, width)

def part2(lines):
    grid, height, width = getbiggrid(lines)
    return dijkstra_q(grid, height, width)

class TestDay15(unittest.TestCase):
    def test_1a(self):
        with open('./test15.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 40)

    def test_1(self):
        with open('./input15.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 621)

    def test_2a(self):
        with open('./test15.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 315)

    def test_2(self):
        with open('./input15.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 2904)

if __name__ == '__main__':
    unittest.main()
