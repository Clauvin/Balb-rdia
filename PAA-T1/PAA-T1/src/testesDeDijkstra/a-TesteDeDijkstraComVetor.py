import dijkstra

vertices_teste = [1,2,3,4,5,6]
arestas_teste = [[1,2], [2,3], [3,4], [4,5], [5,6], [2,6]]
vertice_fonte_teste = [1]
comVetor = dijkstra.DijkstraComVetor(vertices_teste, arestas_teste,
                                      vertice_fonte_teste)

comVetor.checarTodosOsValores()