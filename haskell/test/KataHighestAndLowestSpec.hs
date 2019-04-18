module KataHighestAndLowestSpec where

import Test.Hspec
import KataHighestAndLowest (highAndLow)

spec :: Spec
spec = describe "Example Tests" $ do
    it "4 5 29 54 4 0 -214 542 -64 1 -3 6 -6" $ 
      highAndLow "4 5 29 54 4 0 -214 542 -64 1 -3 6 -6" `shouldBe`  "542 -214"
