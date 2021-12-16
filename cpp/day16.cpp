// day16.cpp
#include <gtest/gtest.h>
#include <string>
#include <fstream>
#include <numeric>
using namespace std;

class Day16 {
protected:
    const string bitstream;
    int64_t pos;
    int64_t version_total;

    inline int64_t nibble(char c) {
        if (c > '9') {
            return c-'A'+10;
        }
        return c-'0';
    }

public:
    Day16(const string& hexstream) 
    : bitstream(hexstream), pos(0), version_total(0) {}

    int64_t total() { return version_total; }

    int64_t remaining() { return bitstream.size()*4 - pos; }

    int64_t getint(int64_t length) {
        if (length > remaining()) {
            return -1;
        }
        int64_t v = 0;
        int64_t end = pos+length;
        while (pos < end) {
            int64_t n = nibble(bitstream[pos / 4]);
            int64_t rem = end-pos;
            int64_t read = 4 - (pos % 4);
            if (rem < read) {
                n >>= (read - rem);
                read = rem;
            }
            v = (v << read) | (((1<<read) - 1) & n);
            pos += read;
        }
        return v;
    }

    bool has_more(int64_t I, int64_t &L) {
        if (I == 0) {
            return pos < L;
        } else {
            L--;
            return L >= 0;
        }
    }

    int64_t parse() {
        int64_t version = getint(3);
        version_total += version;
        int64_t opcode = getint(3);

        int64_t v = 0;

        if (opcode == 4) {
            bool cont = true;
            while(cont) {
                cont = getint(1);
                v = (v << 4) | getint(4);
            }
            return v;
        }

        int64_t I = getint(1);
        int64_t L = 0;
        if (I == 0) {
            //while (pos < L)
            L = getint(15) + pos;
        } else {
            //run L times
            L = getint(11);
        }

        switch(opcode) {
            case 0: //sum
                while (has_more(I, L)) {
                    v += parse();
                }
                break;
            case 1: //prod
                v = 1;
                while (has_more(I, L)) {
                    v *= parse(); 
                }
                break;
            case 2: //min
                v = INT64_MAX;
                while(has_more(I, L)) {
                    v = min(v, parse());
                }
                break;
            case 3: //max
                v = INT64_MIN;
                while(has_more(I, L)) {
                    v = max(v, parse());
                }
                break;
            case 5: //gt
                if (parse() > parse()) {
                    v = 1;
                }
                break;
            case 6: //lt
                if (parse() < parse()) {
                    v = 1;
                }
                break;
            case 7: //eq
                if (parse() == parse()) {
                    v = 1;
                }
        }
        return v;
    }
};

TEST(Day16, Part1_testA) {
    ASSERT_EQ(Day16("A").getint(3), 5);
}

TEST(Day16, Part1_testB) {
    Day16 d("B");
    ASSERT_EQ(d.getint(2), 2);
    ASSERT_EQ(d.getint(2), 3);
}

TEST(Day16, Part1) {
    ifstream infile("../input16.txt");
    string line;
    getline(infile,line);
    infile.close();
    Day16 d(line);
    d.parse();
    ASSERT_EQ(d.total(), 1007);
}

TEST(Day16, Part2_testA) {
    ASSERT_EQ(Day16("C200B40A82").parse(), 3);
}

TEST(Day16, Part2_testB) {
    ASSERT_EQ(Day16("04005AC33890").parse(), 54);
}

TEST(Day16, Part2_testC) {
    ASSERT_EQ(Day16("880086C3E88112").parse(), 7);
}

TEST(Day16, Part2_testD) {
    ASSERT_EQ(Day16("CE00C43D881120").parse(), 9);
}

TEST(Day16, Part2_testE) {
    ASSERT_EQ(Day16("D8005AC2A8F0").parse(), 1);
}

TEST(Day16, Part2_testF) {
    ASSERT_EQ(Day16("F600BC2D8F").parse(), 0);
}

TEST(Day16, Part2_testG) {
    ASSERT_EQ(Day16("9C005AC2F8F0").parse(), 0);
}

TEST(Day16, Part2_testH) {
    ASSERT_EQ(Day16("9C0141080250320F1802104A08").parse(), 1);
}

TEST(Day16, Part2) {
    ifstream infile("../input16.txt");
    string line;
    getline(infile,line);
    infile.close();
    ASSERT_EQ(Day16(line).parse(), 834151779165);
}
