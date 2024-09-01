-- função em haskell que realiza a ordenação dos elementos de uma lista usando o algoritmo de Merge-Sort
-- Divide a lista em partes iguais
-- tamanho da lista
size_list [] = 0
size_list (x:xs) = 1 + size_list xs

-- divide a lista
divide :: [Int] -> ([Int], [Int])
divide xs =
  (take i xs, drop i xs)
  where i = div (size_list xs) 2

-- junta duas listas de forma ordenada
merge :: [Int] -> [Int] -> [Int]
merge = \s1 -> \s2 ->
    case s1 of
        [] -> s2
        x:xs ->
            case s2 of
                [] -> s1
                y:ys | x>y -> y:merge s1 ys
                _ -> x:merge xs s2

-- ordena a lista usando  o merge sort
mergesort :: [Int] -> [Int]
mergesort = \list ->
    case list of
        [] -> []
        [x] -> [x]
        _ ->
            let (par, impar) = divide list
            in merge (mergesort par) (mergesort impar)

main = print (mergesort [1,4,5,3,2]) -- testando merge