import networkx as nx  # Usado para acessar Dijkstra e manipular o grafo

# Função que determina o centro de distribuição mais próximo de um destino


def centro_mais_proximo(entrega, centros, grafo):
    menor_distancia = float('inf')  # Inicializa com infinito
    centro_mais_proximo = None

    for centro in centros:
        try:
            # Calcula a menor distância do centro até o destino usando Dijkstra
            distancia = nx.dijkstra_path_length(
                grafo, centro, entrega['destino'])

            # Se a distância for menor que a menor registrada, atualiza
            if distancia < menor_distancia:
                menor_distancia = distancia
                centro_mais_proximo = centro
        except nx.NetworkXNoPath:
            # Caso não exista caminho entre o centro e o destino
            continue

    return centro_mais_proximo

# Função que retorna a rota e a distância entre origem e destino


def calcular_rota(grafo, origem, destino):
    rota = nx.dijkstra_path(grafo, origem, destino)  # Caminho mais curto
    distancia = nx.dijkstra_path_length(
        grafo, origem, destino)  # Distância total
    return rota, distancia
