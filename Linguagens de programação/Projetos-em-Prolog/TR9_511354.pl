% esse código inverte uma lista
% inverte1([0,1,2],[2,1,0]).
inverte1(L,LI):-inverte1(L,[ ],LI).
inverte1([ ],L,L).
inverte1([X|L],L2,L3):- write([X|L2]),nl,
                        inverte1(L,[X|L2],L3).