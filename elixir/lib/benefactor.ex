defmodule Benefactor do
  def new_avg(arr, newavg) do
    result = _new_avg(arr, newavg)
    if result <= 0 do
      raise ArgumentError, message: "Expected New Average is too low"
    else
      Float.ceil(result / 1.0)
    end
  end

  defp _new_avg(arr, newavg), do: (1 + Enum.count(arr)) * newavg - Enum.sum(arr)
end