import Data.Maybe
import Data.ByteString.Char8 (unpack, pack)
import Data.ByteString.Base16 (encode)
import Crypto.Hash.MD5

data Room = R {
  x :: !Int,
  y :: !Int,
  path :: [Char]
} deriving Show

isUnlocked c = c > 'a'

basePathCtx = update Crypto.Hash.MD5.init $ pack "hhhxzeay"
hashpath p = unpack $ encode $ finalize $ update basePathCtx $ pack p
unlocked p = map snd $ filter (isUnlocked . fst) $ zip (hashpath p) "UDLR"

neighbors r = mapMaybe (makeNeighbor r) $ unlocked $ path r

makeNeighbor :: Room -> Char -> Maybe Room
makeNeighbor R {x=3,y=3} c = Nothing
makeNeighbor R {x=0} 'L' = Nothing
makeNeighbor R {x=3} 'R' = Nothing
makeNeighbor R {y=0} 'U' = Nothing
makeNeighbor R {y=3} 'D' = Nothing
makeNeighbor R {x=x,y=y,path=p} 'L' = Just $ R{x=x-1,y=y,path=p ++ "L"}
makeNeighbor R {x=x,y=y,path=p} 'R' = Just $ R{x=x+1,y=y,path=p ++ "R"}
makeNeighbor R {x=x,y=y,path=p} 'U' = Just $ R{x=x,y=y-1,path=p ++ "U"}
makeNeighbor R {x=x,y=y,path=p} 'D' = Just $ R{x=x,y=y+1,path=p ++ "D"}

start = R{x=0,y=0,path=""}

isFinish R{x=3,y=3} = True
isFinish _ = False

byDist = takeWhile (not . null ) $ iterate (concatMap neighbors) [start]
shortestPath = head $ filter isFinish $ concat byDist
longestPath = last $ filter isFinish $ concat byDist

