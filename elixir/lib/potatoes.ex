# https://www.codewars.com/kata/58ce8725c835848ad6000007/train/elixir

defmodule Potatoes do
  @spec potatoes(integer, integer, integer) :: integer
  def potatoes(p0, w0, p1) do
    _potatoes(p0 / 1, w0 / 1, p1 / 1)
    |> Float.floor
    |> trunc
  end

  defp _potatoes(p0, w0, p1) do
    ((100 - p0) / 100) * w0 * (100 / (100 - p1))
  end
end
