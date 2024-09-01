#include <stdlib.h>
#include <stdio.h>

#ifndef TR89_511354
#define TR89_511354

// vertices: numero de elementos no grafo
// arestas: numero de ligacoes entre elementos do grafo
// **set: ponteiro para ponteiro que forma uma matriz
// com as linhas sendo o elementos e a coluna as suas ligacoes.
// *setgrau: uma lista com o valor do grau(numero de ligacoes que um elemento tem)
typedef struct grafo{
  int vertices;
  int arestas;
  int **set;
  int *setgrau;
}GF;

// ler o arquivo que contem os dados do grafo e preenche toda 
// a struct grafo depois retornando a mesma.
GF *readfile(FILE *read);

// Responsavel por escrever a struct grafo em um arquivo passado como parametro.
void writeSet(FILE *write, int *read,GF *grafo);

// reponsavel por voce a interseccao de cada No para saber se eles compatilham
// dos mesmos elementos e assim talvez formando um grafo.
// retorna -1 se nao
// retorna o numero de graus/elementos da inseccao se  sim.
int intersecSet(GF *grafo,int new, int *solucao);


// Algoritmo Guloso para tentar encontrar a clique maxima de forma heuristica
// com grande possibidade de nao ser a clique maxima mas constantemente bem proximo da realidade

// comeca varrendo do inicio ->
int* gulosa_inicio(GF *grafo);

// comeca varrendo do final <-
int* gulosa_final(GF *grafo);

// comeca do meio e pega pra esquerda ^ <-
int* gulosa_meio_esq(GF *grafo);

// comeca do meio e pega pra direita ^ ->
int* gulosa_meio_dir(GF *grafo);

// faz o processo pra descobrir qual funcao da gulosa gerou o maior clique.
int* maior_clique(GF *grafo);

#endif