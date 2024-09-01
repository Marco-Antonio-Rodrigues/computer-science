% Quick sort in Prolog
% quicksort1([8, 3, 4, 12, 25, 4, 6, 1, 9, 22, 6], S).

append1( [], X, X).   
append1( [X | Y], Z, [X | W]) :- append1( Y, Z, W).

partition(_, [], [], []).
partition(P, [H|T], [H|L], R) :-
    H =< P,
    partition(P, T, L, R).
partition(P, [H|T], L, [H|R]) :-
    H > P,
    partition(P, T, L, R).

quicksort1([], []).
quicksort1([H|T], S) :-
    partition(H, T, L, R),
    quicksort1(L, SL),
    quicksort1(R, SR),
    append1(SL, [H|SR], S).