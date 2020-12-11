#include "pch.h"

#include <iostream>
#include <string>

using namespace std;

int to_number(char roman_letter) {
    switch (roman_letter)
    {
    case 'I':
        return 1;
    case 'V':
        return 5;
    case 'X':
        return 10;
    case 'L':
        return 50;
    case 'C':
        return 100;
    case 'D':
        return 500;
    case 'M':
        return 1000;
    default:
        return 0;
    }
}

int solution(string roman) {
    auto result = 0;

    for (auto it = roman.begin(); it != roman.end(); it++) {
        auto value = to_number(*it);
        auto factor = 1;

        if (it != roman.end()-1 && to_number(*(it+1)) > value)
            factor = -1;

        result += value * factor;
    }

    return result;
}

TEST(RomanNumerals, RomanNumerals) {
    //EXPECT_EQ(1, 1);
     //EXPECT_TRUE(true);

    EXPECT_EQ(solution("XXI"), 21);
    EXPECT_EQ(solution("I"), 1);
    EXPECT_EQ(solution("IV"), 4);
    EXPECT_EQ(solution("MMVIII"), 2008);
    EXPECT_EQ(solution("MDCLXVI"), 1666);
}