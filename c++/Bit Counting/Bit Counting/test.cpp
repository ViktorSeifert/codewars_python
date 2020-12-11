#include "pch.h"

#include <bitset>
#include <limits>

using namespace std;

typedef unsigned long long numtype;

unsigned int countBits(numtype n) {
    return bitset<numeric_limits<numtype>::digits>(n).count();
}

TEST(CountBits, Zero) {
    EXPECT_EQ(countBits(0), 0);
}

TEST(CountBits, Four) {
    EXPECT_EQ(countBits(4), 1);
}

TEST(CountBits, Seven) {
    EXPECT_EQ(countBits(7), 3);
}

TEST(CountBits, Nine) {
    EXPECT_EQ(countBits(9), 2);
}
