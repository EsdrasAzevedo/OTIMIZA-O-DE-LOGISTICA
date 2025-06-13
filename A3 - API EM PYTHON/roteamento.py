import networkx as nx  # Usado para acessar Dijkstra e manipular o grafo


def centro_mais_proximo(entrega, centros, grafo):
    menor_distancia = float('inf')
    centro_mais_proximo = None

    for centro in centros:
        if centro == entrega['destino']:
            continue  

        try:
            distancia = nx.dijkstra_path_length(
                grafo, centro, entrega['destino'])
            if distancia < menor_distancia:
                menor_distancia = distancia
                centro_mais_proximo = centro
        except nx.NetworkXNoPath:
            continue

    return centro_mais_proximo


def calcular_rota(grafo, origem, destino):
    rota = nx.dijkstra_path(grafo, origem, destino)
    distancia = nx.dijkstra_path_length(grafo, origem, destino)
    return rota, distancia
