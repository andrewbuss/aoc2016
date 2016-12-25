nextwinner2 (n, prev) = 
  (n+1,
    if prev + 1 >= (quot n 2) then (mod (prev+2) n)
    else (mod (prev+1) n))

winners2 = iterate nextwinner2 (1,0)
winner2 n = 1 + (snd $ head $ drop n winners2)

main = putStrLn $ show $ winner2 3001330
