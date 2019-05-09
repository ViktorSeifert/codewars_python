module KataTribonacciSequenceSpec where
  import KataTribonacciSequence

  import Test.Hspec

  spec = describe "tribonacciSequence" $
    it "should work for some examples" $ do
      tribonacci (1, 1, 1) 10 `shouldBe` [1,1,1,3,5,9,17,31,57,105]
      tribonacci (0, 0, 1) 10 `shouldBe` [0,0,1,1,2,4,7,13,24,44]
      tribonacci (0, 1, 1) 10 `shouldBe` [0,1,1,2,4,7,13,24,44,81]
