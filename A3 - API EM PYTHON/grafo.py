import networkx as nx  # Importa o NetworkX, que permite trabalhar com grafos


def criar_grafo():
    # Cria um grafo não-direcionado (as estradas funcionam nos dois sentidos)
    grafo = nx.Graph()

    # Adiciona conexões (arestas) entre cidades com as respectivas distâncias (pesos)
    grafo.add_weighted_edges_from([
        ('Belem', 'Recife', 2100),
        ('Belem', 'Brasilia', 2200),
        ('Recife', 'Brasilia', 1500),
        ('Recife', 'São Paulo', 2700),
        ('Brasilia', 'São Paulo', 1000),
        ('São Paulo', 'Florianópolis', 600),
        ('Florianópolis', 'Recife', 2800),
        ('Belem', 'Florianópolis', 3200),
        # Adicione mais conexões se necessário
    ])

    return grafo  # Retorna o grafo montado
