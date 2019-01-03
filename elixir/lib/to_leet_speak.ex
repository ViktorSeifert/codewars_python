defmodule ToLeetSpeak do
  @translations %{
    "A" => "@",
    "B" => "8",
    "C" => "(",
    "D" => "D",
    "E" => "3",
    "F" => "F",
    "G" => "6",
    "H" => "#",
    "I" => "!",
    "J" => "J",
    "K" => "K",
    "L" => "1",
    "M" => "M",
    "N" => "N",
    "O" => "0",
    "P" => "P",
    "Q" => "Q",
    "R" => "R",
    "S" => "$",
    "T" => "7",
    "U" => "U",
    "V" => "V",
    "W" => "W",
    "X" => "X",
    "Y" => "Y",
    "Z" => "2"
  }

  def translate(str) when is_binary(str) do
    String.graphemes(str) |> Enum.map(&(Map.get(@translations, &1, &1))) |> Enum.join
  end
end
