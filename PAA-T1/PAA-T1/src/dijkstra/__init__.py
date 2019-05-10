class DijkstraComVetor:

    vertices = []
    vertice_fonte = []
    arestas = []
    distancias_de_vertices = []
    distancias_de_arestas = []
    preds = {}
    
    vertices_com_menor_caminho_determinado = []
    
    def __init__(self, vertices, arestas, vertice_fonte):
        self.vertices = vertices
        self.arestas = arestas
        self.vertice_fonte = vertice_fonte
        self.iniciarVetorDeDistancias()
    
    def iniciarVetorDeDistancias(self):
        for vertice in self.vertices:
            if (vertice == self.vertice_fonte[0]):
                self.distancias_de_vertices.append(0)
            else:
                self.distancias_de_vertices.append(float('inf'))
        contar_vertice_fonte = 0
        for vertice_fonte_a_contar in self.vertice_fonte:
            contar_vertice_fonte = contar_vertice_fonte+1
        print(contar_vertice_fonte)
        if (contar_vertice_fonte > 0):
            fonte = self.vertice_fonte[0]
            self.preds[fonte] = 0
    
    def encontrarMenorCaminhoAVertices(self):
        return
      
    def checarTodosOsValores(self):
        print("Vertices = ")
        print(self.vertices)
        print("Vertice fonte = ")
        print(self.vertice_fonte)
        print("Arestas = ")
        print(self.arestas)
        print("Distancias de Vertices = ")
        print(self.distancias_de_vertices)
        print("Distancias de Arestas = ")
        print(self.distancias_de_arestas)
        print("Preds = ")
        print(self.preds)
        print("Vertices com Menor Caminho Determinado = ")
        print(self.vertices_com_menor_caminho_determinado)