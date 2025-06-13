from roteamento import centro_mais_proximo, calcular_rota
from grafo import criar_grafo

centros = ['Belem', 'Recife', 'Brasilia', 'São Paulo', 'Florianópolis']

cenarios = {
    "Cenário 1": [
        {'destino': 'São Paulo', 'peso': 10},
        {'destino': 'Recife', 'peso': 5}
    ],
    "Cenário 2": [
        {'destino': 'Brasilia', 'peso': 20},
        {'destino': 'Florianópolis', 'peso': 8},
        {'destino': 'São Paulo', 'peso': 15}
    ],
    "Cenário 3": [
        {'destino': 'Florianópolis', 'peso': 10},
        {'destino': 'Recife', 'peso': 15},
        {'destino': 'São Paulo', 'peso': 25},
        {'destino': 'Brasilia', 'peso': 30},
        {'destino': 'Recife', 'peso': 7}
    ]
}


def testar_cenarios():
    grafo = criar_grafo()

    for nome, entregas in cenarios.items():
        print(f"\n== {nome} ==")

        for entrega in entregas:
            centro = centro_mais_proximo(entrega, centros, grafo)
            if centro:
                rota, distancia = calcular_rota(
                    grafo, centro, entrega['destino'])
                print(f"\nEntrega para {entrega['destino']}")
                print(f"Centro mais próximo: {centro}")
                print(f"Rota: {' -> '.join(rota)}")
                print(f"Distância total: {distancia} km")
            else:
                print(
                    f"\nEntrega para {entrega['destino']} não pode ser realizada. Nenhum centro acessível.")
