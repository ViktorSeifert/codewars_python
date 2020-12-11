#include "pch.h"

#include <sstream>

using namespace std;

vector<string> split(const string& input) {
    vector<string> result;

    stringstream input_stream(input);

    string token;

    while (getline(input_stream, token, ' '))
    {
        result.push_back(token);
    }

    return result;
}

string spinWords(const string& str)
{
    vector<string> tokens = split(str);

    string result;

    for (auto it = tokens.begin(); it != tokens.end(); it++) {

        if ((*it).length() >= 5)
            reverse((*it).begin(), (*it).end());

        result += move(*it);

        if (it + 1 != tokens.end())
            result += " ";
    }

    return result;
}

TEST(SpinWords, SingleWordSpin) {
    //EXPECT_EQ(1, 1);
    //EXPECT_TRUE(true);

    EXPECT_EQ(spinWords("Welcome"), "emocleW");
}

TEST(SpinWords, SingleWordNoSpin) {
    EXPECT_EQ(spinWords("to"), "to");
}

TEST(SpinWords, SingleCamelCaseWordSpin) {
    EXPECT_EQ(spinWords("CodeWars"), "sraWedoC");
}

TEST(SpinWords, HeySentence) {
    EXPECT_EQ(spinWords("Hey fellow warriors"), "Hey wollef sroirraw");
}

TEST(SpinWords, BurgersSentence) {
    EXPECT_EQ(spinWords("Burgers are my favorite fruit"), "sregruB are my etirovaf tiurf");
}

TEST(SpinWords, PizzaSentence) {
    EXPECT_EQ(spinWords("Pizza is the best vegetable"), "azziP is the best elbategev");
}