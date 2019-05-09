module KataPascalsTriangleSpec where
  import KataPascalsTriangle
  import Test.Hspec

  spec = describe "pascalsTriangle" $ do
    it "should work for some examples" $ do
      pascalsTriangle 1  `shouldBe` [1]
      pascalsTriangle 2  `shouldBe` [1, 1, 1]
      pascalsTriangle 3  `shouldBe` [1, 1, 1, 1, 2, 1]
      pascalsTriangle 4  `shouldBe` [1, 1, 1, 1, 2, 1, 1, 3, 3, 1]
      pascalsTriangle 5  `shouldBe` [1, 1, 1, 1, 2, 1, 1, 3, 3, 1, 1, 4, 6, 4, 1]