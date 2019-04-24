module KataFindTheParityOutlierSpec where
  import KataFindTheParityOutlier (findOutlier)
  import Test.Hspec

  spec = describe "Find Outlier" $ do
      it "more tests" $ do
        findOutlier [2,6,8,-10,3] `shouldBe` 3
        findOutlier [206847684,1056521,7,17,1901,21104421,7,1,35521,1,7781] `shouldBe` 206847684
        findOutlier [2147483647,0,1] `shouldBe` 0
