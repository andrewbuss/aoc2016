import Data.Bool
import Data.Function.Memoize

nextrow xs =
  let n = length xs in
    (xs !! 1) : [(xs !! x) /= (xs !! (x+2)) | x <- [0 .. (n - 3)]] ++ [(xs !! (n - 2))]

main = do
  firstline <- getLine
  let width = length firstline
      height = 400000
      firstrow = map ((==) '^') firstline
      board = iterate nextrow firstrow in
    putStrLn $ show $ (width * height) - (sum $ map (sum . map fromEnum) $ take height board)
    
