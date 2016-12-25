import Data.Char
import Data.List.Split
toggle 0 = 1
toggle 1 = 0

step_process xs = xs ++ [0] ++ (map toggle $ reverse xs)

fill len inp = if length inp > len then
  take len inp else
  fill len (step_process inp)

is_same (x:y:_) = if x == y then 1 else 0

checksum xs = if odd (length xs) then xs else
  checksum $ map is_same $ chunksOf 2 xs

main = putStrLn $
       show $
       map intToDigit $
       checksum $ fill 35651584 $ map digitToInt "10111011111001111"
