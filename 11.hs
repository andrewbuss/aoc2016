import Data.List hiding (insert, union)
import qualified Data.Set (filter, map, (\\))
import Data.Set (insert, empty, Set, union, fromList, difference)
import qualified Data.Set.Extra (concatMap)

data Floor = Floor [Char] [Char] deriving (Show, Eq, Ord)
data GameState = GameState Int [Floor] deriving (Show, Eq, Ord)

--start = GameState 0 [Floor "" "HL", Floor "H" "", Floor "L" "", Floor "" ""]
start = GameState 0 [Floor "DEPS" "DEPS", Floor "CRT" "CR", Floor "" "T", Floor "" ""]

combinations :: Int -> [a] -> [[a]]
combinations 0 _ = [[]]
combinations n xs = [ xs !! i : x | i <- [0..(length xs)-1] 
                                  , x <- combinations (n-1) (drop (i+1) xs) ]
floorValid (Floor [] _) = True
floorValid (Floor gs cs) = null $ cs \\ gs

floorMoves :: Floor -> [([Char], [Char])]
floorMoves f@(Floor generators chips) =
--  filter (\(g,c) ->
--             (length chips - length c)  <= (length generators - length g) ||
--             (length generators) == length g) $
  filter (\d -> floorValid $ floorRemove d f)
  [(g, c) |
    (ng,nc) <- [(0,2), (1,1),(2,0),(1,0), (0,1)],
    g <- (combinations ng generators),
    c <- (combinations nc chips)]

floorRemove (dg, dc) (Floor gs cs) =
  Floor (gs \\ dg) (cs \\ dc)

floorAdd (dg, dc) (Floor gs cs) =
  Floor (sort $ gs ++ dg) (sort $ cs ++ dc)

updateAtIdx f n xs =
  let (x, (h:t)) = splitAt n xs in
    x ++ ((f h) : t)

isValid (GameState e floors)
  | e >= 4 || e < 0 = False
  | otherwise = all floorValid floors

isDone (GameState 3 [Floor "" "", Floor "" "", Floor "" "", Floor gs cs]) = True
isDone _ = False

moves :: GameState -> Set GameState
moves (GameState e floors) = fromList $ filter isValid
  [GameState (e+j)
    $ updateAtIdx (floorAdd d) (e+j)
    $ updateAtIdx (floorRemove d) e $ floors |
    j <- [-1,1], d <- floorMoves (floors !! e)
  ]

moveTree :: [(Data.Set.Set GameState, Data.Set.Set GameState)]
moveTree = iterate (\(prev, allPrev) ->
                       let new = difference (Data.Set.Extra.concatMap moves prev) allPrev in
                         (new, union allPrev new)) (insert start empty, empty)
--moveTree = iterate (Data.Set.Extra.concatMap moves) $ insert start empty

main = do
  putStrLn $ show $ elemIndex 1 $ map (sum . (Data.Set.map $ fromEnum . isDone) . fst) moveTree
--  putStrLn $ show $ elemIndex 1 $ map (sum . (Data.Set.map $ fromEnum . isDone)) moveTree
           
