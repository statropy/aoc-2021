#day16.py 2021
import unittest

bits = {
    '0':'0000',
    '1':'0001',
    '2':'0010',
    '3':'0011',
    '4':'0100',
    '5':'0101',
    '6':'0110',
    '7':'0111',
    '8':'1000',
    '9':'1001',
    'A':'1010',
    'B':'1011',
    'C':'1100',
    'D':'1101',
    'E':'1110',
    'F':'1111',
}

class BitsParser:
    def __init__(self, hexstring):
        self.version_total = 0
        self.bitstring = ''
        for c in hexstring:
            self.bitstring += bits[c]

    def parse(self, s):
        if len(s) < 6:
            return None
        version, s = int(s[:3],2), s[3:]
        self.version_total += version
        type, s = int(s[:3],2), s[3:]

        if type == 4:
            #literal
            v = 0
            while True:
                cont, nibble, s = s[0], int(s[1:5],2), s[5:]
                v = (v << 4) | nibble
                if cont == '0':
                    break
            return (s, v)
        else:
            allsubs = []
            i, s = s[0], s[1:]
            if i == '0':
                length, s = int(s[:15], 2), s[15:]
                subpacket, s = s[:length], s[length:]
                while True:
                    result = self.parse(subpacket)
                    if result is None:
                        break
                    subpacket, x = result
                    allsubs.append(x)
            else:
                length, s = int(s[:11], 2), s[11:]
                for numsubs in range(length):
                    result = self.parse(s)
                    if result is None:
                        break
                    s, x = result
                    allsubs.append(x)
            v = 0
            if type == 0: #sum
                v = sum(allsubs)
            elif type == 1: #product
                v = 1
                for x in allsubs:
                    v *= x
            elif type == 2: #minimum
                v = min(allsubs)
            elif type == 3: #maximum
                v=  max(allsubs)
            elif type == 5: #gt
                if allsubs[0] > allsubs[1]:
                    v = 1
            elif type == 6: #lt
                if allsubs[0] < allsubs[1]:
                    v = 1
            elif type == 7: #eq
                if allsubs[0] == allsubs[1]:
                    v = 1
            return (s, v)

class TestDay16(unittest.TestCase):
    def test_a2(self):
        bp = BitsParser('D2FE28')
        bp.parse(bp.bitstring)
        self.assertEqual(bp.version_total, 6)

    def test_a3(self):
        bp = BitsParser('8A004A801A8002F478')
        bp.parse(bp.bitstring)
        self.assertEqual(bp.version_total, 16)

    def test_a4(self):
        bp = BitsParser('620080001611562C8802118E34')
        bp.parse(bp.bitstring)
        self.assertEqual(bp.version_total, 12)

    def test_a5(self):
        bp = BitsParser('C0015000016115A2E0802F182340')
        bp.parse(bp.bitstring)
        self.assertEqual(bp.version_total, 23)

    def test_a6(self):
        bp = BitsParser('A0016C880162017C3686B18A3D4780')
        bp.parse(bp.bitstring)
        self.assertEqual(bp.version_total, 31)

    def test_1(self):
        with open('./input16.txt', 'r') as f:
            bp = BitsParser(list(f)[0])
            bp.parse(bp.bitstring)
            self.assertEqual(bp.version_total, 1007)

    def test_b1(self):
        bp = BitsParser('C200B40A82')
        s, v = bp.parse(bp.bitstring)
        self.assertEqual(v, 3)

    def test_b2(self):
        bp = BitsParser('04005AC33890')
        s, v = bp.parse(bp.bitstring)
        self.assertEqual(v, 54)

    def test_b3(self):
        bp = BitsParser('880086C3E88112')
        s, v = bp.parse(bp.bitstring)
        self.assertEqual(v, 7)

    def test_b4(self):
        bp = BitsParser('CE00C43D881120')
        s, v = bp.parse(bp.bitstring)
        self.assertEqual(v, 9)

    def test_b5(self):
        bp = BitsParser('D8005AC2A8F0')
        s, v = bp.parse(bp.bitstring)
        self.assertEqual(v, 1)

    def test_b6(self):
        bp = BitsParser('F600BC2D8F')
        s, v = bp.parse(bp.bitstring)
        self.assertEqual(v, 0)

    def test_b7(self):
        bp = BitsParser('9C005AC2F8F0')
        s, v = bp.parse(bp.bitstring)
        self.assertEqual(v, 0)

    def test_b8(self):
        bp = BitsParser('9C0141080250320F1802104A08')
        s, v = bp.parse(bp.bitstring)
        self.assertEqual(v, 1)

    def test_1(self):
        with open('./input16.txt', 'r') as f:
            bp = BitsParser(list(f)[0])
            s, v = bp.parse(bp.bitstring)
            self.assertEqual(v, 834151779165)

if __name__ == '__main__':
    unittest.main()
