def criar_grafo():
    """
    Cria e retorna uma estrutura de grafo com lista de arestas e lista de vértices.

    Passos:
    1. Criar uma lista vazia chamada 'vertices'.
    2. Criar uma lista vazia chamada 'arestas', onde cada elemento será uma lista de tamanho 2 (origem, destino)
    3. Retornar vertices e arestas
    """
    vertices = []
    arestas = []
    return vertices, arestas


def inserir_vertice(vertices, vertice):
    """
    Adiciona um novo vértice no grafo.

    Passos:
    1. Verificar se o vértice já existe em 'vertices'.
    2. Se não existir, adicionar à lista 'vertices'.
    """
    if vertice not in vertices:
        vertices.append(vertice)

def inserir_aresta(vertices, arestas, origem, destino, nao_direcionado=False):
    """
    Adiciona uma aresta entre dois vértices.

    Passos:
    1. Garantir que 'origem' e 'destino' existam em 'vertices'.
       - Se não existirem, chamar 'inserir_vertice' para adicioná-los.
    2. Adicionar uma lista [origem, destino] na lista 'arestas'.
    3. Se nao_direcionado=True, adicionar também [destino, origem].
    """
    inserir_vertice(vertices, origem)
    inserir_vertice(vertices, destino)
    if [origem, destino] not in arestas:
        arestas.append([origem, destino])
    if nao_direcionado and [destino, origem] not in arestas:
        arestas.append([destino, origem])

def remover_aresta(arestas, origem, destino, nao_direcionado=False):
    """
    Remove uma aresta entre dois vértices.

    Passos:
    1. Percorrer a lista de Arestas procurando [origem, destino]
    2. Se encontrar, remover
    3. Se nao_direcionado=True, também procurar por [destino, origem]
    """
    if [origem, destino] in arestas:
        arestas.remove([origem, destino])
    if nao_direcionado and [destino, origem] in arestas:
        arestas.remove([destino, origem])

def remover_vertice(vertices, arestas, vertice):
    """
    Remove um vértice e todas as arestas conectadas a ele.

    Passos:
    1. Verificar se o vértice existe na lista de vertices.
    2. Caso encontrado, remover o vértice da lista 'vertices'.
    3. Percorrer a lista de 'arestas' e remover todas onde o vértice aparece
       como origem ou destino.
    """
    if vertice not in vertices:
        return
    vertices.remove(vertice)
    for aresta in arestas[:]:
        if vertice in aresta:
            arestas.remove(aresta)

def existe_aresta(arestas, origem, destino):
    """
    Verifica se existe uma aresta entre origem e destino.

    Passos:
    1. Percorrer a lista de aresta procurando [origem, destino]
    2. Retornar True se encontrar
    3. Caso não encontre na lista, retornar False no final.
    """
    return [origem, destino] in arestas


def vizinhos(vertices, arestas, vertice):
    """
    Retorna a lista de vizinhos (vértices alcançáveis a partir de 'vertice').

    Passos:
    1. Criar uma lista vazia chamada 'vizinhos'.
    2. Percorrer todas as arestas [origem, destino].
    3. Se origem == vertice, adicionar destino na lista de vizinhos.
    4. Retornar a lista final.
    """
    lista = []
    if vertice not in vertices:
        return lista
    for origem, destino in arestas:
        if origem == vertice:
            lista.append(destino)
    return lista


def grau_vertices(vertices, arestas):
    """
    Calcula o grau de entrada, saída e total de cada vértice.

    Passos:
    1. Criar um dicionário vazio 'graus'.
    2. Percorrer todas as arestas [origem, destino]:
        I. Se o grafo for não direcionado:
            - incrementar grau analisando apenas se origem ou destino equivale ao vértice analisado
        II. Se o grafo for direcionado
            - Se o vértice for origem Incrementar grau de saída do vértice origem
            - Se o vértice for destino incrementar grau de entrada do vértice destino.
            - Calcular o grau total (entrada + saída).
    4. Retornar o dicionário 'graus' para cada vértice.
    """
    graus = {}
    for vertice in vertices:
        entrada = 0
        saida = 0
        for origem, destino in arestas:
            if origem == vertice:
                saida += 1
            if destino == vertice:
                entrada += 1
        graus[vertice] = {"saida": saida, "entrada": entrada, "total": entrada + saida}
    return graus


def percurso_valido(arestas, caminho):
    """
    Verifica se um percurso é possível (seguindo as arestas na ordem dada).

    Passos:
    1. Percorrer o caminho de 0 até len(caminho) - 2.
    2. Para cada par consecutivo (u, v):
        - Verificar se (u, v) existe na lista de 'arestas' (funcao existe_aresta).
        - Se alguma não existir, retornar False.
    3. Se todas existirem, retornar True.
    """
    for i in range(len(caminho) - 1):
        if not existe_aresta(arestas, caminho[i], caminho[i + 1]):
            return False
    return True


def listar_vizinhos(vertices, arestas, vertice):
    """
    Exibe os vizinhos de um vértice.

    Passos:
    1. Chamar a função vizinhos() para obter a lista.
    2. Exibir a lista formatada.
    """
    if vertice not in vertices:
        print("Vértice não encontrado.")
    else:
        print("Vizinhos de", vertice, ":", vizinhos(vertices, arestas, vertice))


def exibir_grafo(vertices, arestas):
    """
    Exibe todas as arestas do grafo.

    Passos:
    1. Exibir a lista de vértices.
    2. Exibir todas as arestas no formato (origem -> destino).
    """
    print("Vértices:", vertices)
    if not arestas:
        print("Nenhuma aresta cadastrada.")
    for origem, destino in arestas:
        print(origem, "->", destino)


def main():
    vertices, arestas = criar_grafo()
    nao_direcionado = input("Grafo não direcionado? (s/n): ").strip().lower() == "s"
    
    while True:
        print("\n--- MENU DO GRAFO ---")
        print("1 - Exibir grafo")
        print("2 - Inserir vértice")
        print("3 - Inserir aresta")
        print("4 - Remover vértice")
        print("5 - Remover aresta")
        print("6 - Listar vizinhos")
        print("7 - Mostrar graus")
        print("8 - Verificar aresta")
        print("9 - Verificar percurso")
        print("0 - Sair")
        opcao = input("Escolha: ").strip()
    
        if opcao == "1":
            exibir_grafo(vertices, arestas)
        elif opcao == "2":
            vertice = input("Vértice: ").strip()
            if vertice:
                inserir_vertice(vertices, vertice)
        elif opcao == "3":
            origem = input("Origem: ").strip()
            destino = input("Destino: ").strip()
            if origem and destino:
                inserir_aresta(vertices, arestas, origem, destino, nao_direcionado)
        elif opcao == "4":
            vertice = input("Vértice para remover: ").strip()
            remover_vertice(vertices, arestas, vertice)
        elif opcao == "5":
            origem = input("Origem: ").strip()
            destino = input("Destino: ").strip()
            remover_aresta(arestas, origem, destino, nao_direcionado)
        elif opcao == "6":
            vertice = input("Consultar vizinhos de: ").strip()
            listar_vizinhos(vertices, arestas, vertice)
        elif opcao == "7":
            for vertice, dados in grau_vertices(vertices, arestas).items():
                print(vertice, dados)
        elif opcao == "8":
            origem = input("Origem: ").strip()
            destino = input("Destino: ").strip()
            print("Existe aresta:", existe_aresta(arestas, origem, destino))
        elif opcao == "9":
            caminho = input("Caminho separado por espaços (ex: A B C): ").split()
            print("Percurso válido:", percurso_valido(arestas, caminho))
        elif opcao == "0":
            print("Até mais!")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
