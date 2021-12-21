#day20.py 2021
import unittest

def parse(lines):
    algostring = lines[0].strip()
    algo = ['0']*512
    negalgo = ['1']*512
    for i,x in enumerate(algostring):
        if x == '#':
            algo[i] = '1'
            negalgo[i] = '0'

    image = ['']
        
    for line in lines[2:]:
        image.append('0'+line.strip().replace('.','0').replace('#','1')+'0')

    image[0] = '0'*len(image[1])
    image.append('0'*len(image[1]))

    return image, algo, negalgo

def convert(image, algo, invert=False):
    width = len(image[0])
    height = len(image)
    output = ['0'*(width+2)]
    for r,row in enumerate(image):
        output.append('0')
        for c,col in enumerate(row):
            istring = ''
            for rs in [r-1,r,r+1]:
                if rs < 0 or rs >= height:
                    istring += '000'
                elif c-1 < 0:
                    istring += '0'+image[rs][:2]
                elif c+1 == width:
                    istring += image[rs][c-1:]+'0'
                else:
                    istring += image[rs][c-1:c+2]
            i = int(istring,2)
            if invert:
                i = (~i) & 0x1ff 
            output[r+1] += algo[i]
        output[r+1] += '0'
    output.append('0'*(width+2))
    return output

def test1(lines, times=1):
    image, algo, negalgo = parse(lines)
    for _ in range(times):
        image = convert(image, algo)
    count = 0
    for line in image:
        count += line.count('1')
        # print(line.replace('1','#').replace('0','.'))
    return count

def part1(lines, times=2):
    image, algo, negalgo = parse(lines)
    for _ in range(times//2):
        image = convert(image, negalgo)
        image = convert(image, algo, True)

    count = 0
    for line in image:
        count += line.count('1')
        # print(line.replace('1','#').replace('0','.'))
    return count

class TestDay20(unittest.TestCase):
    def test_1a(self):
        with open('./test20.txt', 'r') as f:
            self.assertEqual(test1(list(f)), 35)

    def test_1(self):
        with open('./input20.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 5229)

    def test_2a(self):
        with open('./test20.txt', 'r') as f:
            self.assertEqual(test1(list(f),50), 3351)

    def test_2(self):
        with open('./input20.txt', 'r') as f:
            self.assertEqual(part1(list(f),50), 17009)

if __name__ == '__main__':
    unittest.main()
