import Text.Regex.PCRE
import Data.Maybe
import Data.List
import Debug.Trace
import Data.Char
--ops = [()]

updateIdx _ _ [] = []
updateIdx 0 c (x:xs) = c:xs
updateIdx n c (x:xs) = x:(updateIdx (n-1) c xs)

insertAtIdx 0 c s = c:s
insertAtIdx n c (x:xs) = x : (insertAtIdx (n-1) c xs)

rotateStringLeft n s
  | n >= 0 = take (length s) $ drop n $ cycle s
  | n < 0 = rotateStringLeft (n + length s) s

slice from to xs = take (to - from + 1) (drop from xs)

ops :: [(String, [String] -> String -> String)]
ops = [("swap position (\\d+) with position (\\d+)",
         \ts -> \s ->
           let ai = read $ ts!!1
               bi = read $ ts!!2
               a = s !! ai
               b = s !! bi in
             updateIdx bi a $ updateIdx ai b $ s),
       ("swap letter (\\w+) with letter (\\w+)",
         \ts -> \s -> 
           let ai = fromJust $ elemIndex (head $ ts!!1) s
               bi = fromJust $ elemIndex (head $ ts!!2) s
               a = s !! ai
               b = s !! bi in
             updateIdx bi a $ updateIdx ai b $ s),
       ("move position (\\d+) to position (\\d+)",
         \ts -> \s -> 
           let src = read $ ts!!1
               dst = read $ ts!!2
               c = s!!src
               a = (take src s) ++ (drop (src+1) s) in
             insertAtIdx dst c a),
       ("reverse positions (\\d+) through (\\d+)",
         \ts -> \s -> 
           let a = read $ ts!!1
               b = read $ ts!!2
               (x, u) = splitAt a s
               (y, z) = splitAt (b-a+1) u in
             x ++ (reverse y) ++ z),
       ("rotate (\\w+) (\\d+)",
         \ts -> \s -> 
           let dir = ts!!1
               steps = read $ ts!!2 in
             if dir == "left" then rotateStringLeft steps s
             else rotateStringLeft (-steps) s),
       ("rotate based on position of letter (\\w+)",
         \ts -> \s ->
           let i = fromJust $ elemIndex (head $ ts!!1) s in
             if i >= 4 then rotateStringLeft (-i - 2) s
             else rotateStringLeft (-i-1) s)]

tryOp :: String -> (String, [String] -> String -> String) -> Maybe (String -> String)
tryOp step (rx, f) =
  let matches = step =~ rx :: [[String]] in
    if null matches then Nothing
    else Just (f $ head matches)

getOp step = head $ mapMaybe (tryOp step) ops

compose = foldl (.) id

main = do
  ls <- getContents
  let scramble = compose $ map getOp $ filter (not . null) $ reverse $ lines ls in
    putStrLn $ head $ filter (\x -> scramble (traceShowId x) == "fbgdceah") $ permutations "abcdefgh"
