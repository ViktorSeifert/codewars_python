defmodule TestSolution do
  use ExUnit.Case

  test "Basic test1" do
    assert ToLeetSpeak.translate("LEET") == "1337"
  end
  test "Basic test2" do
    assert ToLeetSpeak.translate("CODEWARS") == "(0D3W@R$"
  end
  test "Basic test3" do
    assert ToLeetSpeak.translate("HELLO WORLD") == "#3110 W0R1D"
  end
  test "Basic test4" do
    assert ToLeetSpeak.translate("LOREM IPSUM DOLOR SIT AMET") == "10R3M !P$UM D010R $!7 @M37"
  end
  test "Basic test5" do
    assert ToLeetSpeak.translate("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG") == "7#3 QU!(K 8R0WN F0X JUMP$ 0V3R 7#3 1@2Y D06"
  end
end