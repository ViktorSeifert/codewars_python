module KataPermutationsSpec where
  import KataPermutations
  import qualified Data.List as L
  import Test.Hspec

  spec = describe "permutations" $ do
    it "should work for some examples" $ do
      L.sort (permutations "a") `shouldBe` L.sort ["a"]
      L.sort (permutations "ab") `shouldBe` L.sort ["ab", "ba"]
      L.sort (permutations "aabb") `shouldBe` L.sort ["aabb","abab","abba","baab","baba","bbaa"]