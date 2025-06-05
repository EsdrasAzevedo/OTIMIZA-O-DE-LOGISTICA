from roteamento import centro_mais_proximo, calcular_rota
from grafo import criar_grafo

# Lista com os centros de distribuição disponíveis
centros = ['Belem', 'Recife', 'Brasilia', 'São Paulo', 'Florianópolis']

# Dicionário com diferentes cenários de entregas para testar o sistema
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

# Função que roda os testes de cada cenário
def testar_cenarios():
    grafo = criar_grafo()  # Cria o grafo com os dados das cidades

    for nome, entregas in cenarios.items():
        print(f"\n== {nome} ==")  # Título do cenário

        for entrega in entregas:
            centro = centro_mais_proximo(entrega, centros, grafo)  # Centro mais próximo
            rota, distancia = calcular_rota(grafo, centro, entrega['destino'])  # Rota ideal

            # Exibe os dados da entrega
            print(f"\nEntrega para {entrega['destino']}")
            print(f"Centro mais próximo: {centro}")
            print(f"Rota: {' -> '.join(rota)}")
            print(f"Distância total: {distancia} km")

# Roda os testes se o arquivo for executado diretamente
if __name__ == "__main__":
    testar_cenarios()
