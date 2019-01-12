# https://www.codewars.com/kata/ip-validation/train/elixir

defmodule IpValidation do
  def is_valid_ip(ip) do
    ip
    |> String.split(".")
    |> Enum.map(&to_octet/1)
    |> is_valid
  end

  @single_ip_part ~r{^((\d)|([1-9]\d)|([1-9]\d\d))$}

  defp to_octet(str) do
    Regex.match?(@single_ip_part, str) && octet? String.to_integer(str)
  end

  defp is_valid(ip) when length(ip) == 4 do
    Enum.all?(ip, &octet?/1)
  end

  defp is_valid(_), do: false

  defp octet?(n) when is_integer(n) and n >= 0 and n <= 255, do: n
  defp octet?(_), do: false
end
