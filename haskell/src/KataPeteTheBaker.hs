module KataPeteTheBaker where
  import qualified Data.Map as Map

  type Ingredient = String
  type Amount = Int
  type Recipe = [(Ingredient, Amount)]
  type Storage = [(Ingredient, Amount)]
  type StorageMap = Map.Map Ingredient Amount

  cakes :: Recipe -> Storage -> Int
  cakes recipe storage = calcNumberOfCakes recipe (Map.fromList storage)

  calcNumberOfCakes :: Recipe -> StorageMap -> Int
  calcNumberOfCakes recipe storage = minimum $ map (\(i, a) -> timesStored storage i a) recipe

  timesStored :: StorageMap -> Ingredient -> Amount -> Int
  timesStored storage i a = (findInStorage i storage) `quot` a
    where findInStorage = Map.findWithDefault 0