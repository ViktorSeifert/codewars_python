defmodule BenefactorTest do
  
  use ExUnit.Case

  test "Benefactor 1" do
    assert Benefactor.new_avg([14, 30, 5, 7, 9, 11, 16], 90) == 628
  end
  test "Benefactor 2" do
		assert_raise ArgumentError, "Expected New Average is too low", fn -> Benefactor.new_avg([14, 30, 5, 7, 9, 11, 15], 2) end
  end
end
