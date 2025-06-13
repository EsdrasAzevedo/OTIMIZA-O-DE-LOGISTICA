import networkx as nx


def criar_grafo():
    grafo = nx.Graph()
    grafo.add_weighted_edges_from([
        # Conexões principais
        ('Belem', 'Recife', 2100),
        ('Belem', 'Brasilia', 2200),
        ('Recife', 'Brasilia', 1500),
        ('Recife', 'São Paulo', 2700),
        ('Brasilia', 'São Paulo', 1000),
        ('São Paulo', 'Florianópolis', 600),
        ('Florianópolis', 'Recife', 2800),
        ('Belem', 'Florianópolis', 3200),

        # Novas conexões
        ('São Paulo', 'Curitiba', 400),
        ('São Paulo', 'Rio de Janeiro', 430),
        ('Brasilia', 'Salvador', 1440),
        ('Recife', 'João Pessoa', 120),
        ('Natal', 'João Pessoa', 180),
        ('Fortaleza', 'Natal', 500),
        ('Curitiba', 'Porto Alegre', 710),
        ('Vitória', 'Rio de Janeiro', 520),
        ('Campinas', 'São Paulo', 100),
        ('Campinas', 'Vitória', 650),
    ])
    return grafo
