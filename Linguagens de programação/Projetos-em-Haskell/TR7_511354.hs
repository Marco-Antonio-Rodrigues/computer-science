-- :l arquivo.hs
-- função: inverte uma lista
inverte :: [l] -> [l]
inverte [] = []
inverte (x:xs) = (inverte xs) ++[x]
main = print (inverte [1,2,3]) -- Testando