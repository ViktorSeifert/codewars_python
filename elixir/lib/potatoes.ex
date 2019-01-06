# https://www.codewars.com/kata/58ce8725c835848ad6000007/train/elixir

defmodule Potatoes do
  @spec potatoes(integer, integer, integer) :: integer
  def potatoes(p0, w0, p1) do
    trunc(((100-p0)/100)*w0*(100/(100-p1)))
  end
end
