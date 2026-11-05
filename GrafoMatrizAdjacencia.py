def criar_grafo():
    """
    Cria e retorna uma matriz de adjacência vazia e uma lista de vértices.

    Passos:
    1. Criar uma lista vazia chamada matriz (para armazenar as conexões).
    2. Criar uma lista vazia chamada vertices (para armazenar os nomes dos vértices).
    3. Retornar (matriz, vertices).
    """
    matriz = []
    vertices = []
    return matriz, vertices


def inserir_vertice(matriz, vertices, vertice):
    """
    Adiciona um novo vértice ao grafo.

    Passos:
    1. Verificar se o vértice já existe em 'vertices'.
    2. Caso não exista:
        - Adicionar o vértice à lista 'vertices'.
        - Aumentar o tamanho da matriz:
            a) Para cada linha existente, adicionar um valor 0 no final (nova coluna).
            b) Adicionar uma nova linha com zeros do tamanho atualizado.
    """
    if vertice not in vertices:
        vertices.append(vertice)
        for linha in matriz:
            linha.append(0)
        matriz.append([0] * len(vertices))


def inserir_aresta(matriz, vertices, origem, destino, nao_direcionado=False):
    """
    Adiciona uma aresta entre dois vértices.

    Passos:
    1. Garantir que 'origem' e 'destino' existam em 'vertices':
        - Se não existirem, chamar 'inserir_vertice' para adicioná-los.
    2. Localizar o índice da origem (i) e do destino (j).
    3. Marcar a conexão na matriz: matriz[i][j] = 1.
    4. Se nao_direcionado=True, também marcar a conexão inversa matriz[j][i] = 1.
    """
    inserir_vertice(matriz, vertices, origem)
    inserir_vertice(matriz, vertices, destino)
    i = vertices.index(origem)
    j = vertices.index(destino)
    matriz[i][j] = 1
    if nao_direcionado:
        matriz[j][i] = 1


def remover_vertice(matriz, vertices, vertice):
    """
    Remove um vértice e todas as arestas associadas.

    Passos:
    1. Verificar se o vértice existe em 'vertices'.
    2. Caso exista:
        - Descobrir o índice correspondente (usando vertices.index(vertice)).
        - Remover a linha da matriz na posição desse índice.
        - Remover a coluna (mesmo índice) de todas as outras linhas.
        - Remover o vértice da lista 'vertices'.
    """
    if vertice in vertices:
        i = vertices.index(vertice)
        matriz.pop(i)
        for linha in matriz:
            linha.pop(i)
        vertices.remove(vertice)

def remover_aresta(matriz, vertices, origem, destino, nao_direcionado=False):
    """
    Remove uma aresta entre dois vértices.

    Passos:
    1. Verificar se ambos os vértices existem.
    2. Localizar os índices (i e j).
    3. Remover a aresta: matriz[i][j] = 0.
    4. Se nao_direcionado=True, também remover a inversa: matriz[j][i] = 0.
    """
    if origem in vertices and destino in vertices:
        i = vertices.index(origem)
        j = vertices.index(destino)
        matriz[i][j] = 0
        if nao_direcionado:
            matriz[j][i] = 0


def existe_aresta(matriz, vertices, origem, destino):
    """
    Verifica se existe uma aresta direta entre dois vértices.

    Passos:
    1. Verificar se ambos os vértices existem em 'vertices'.
    2. Obter os índices (i, j).
    3. Retornar True se matriz[i][j] == 1, caso contrário False.
    """
    if origem not in vertices or destino not in vertices:
        return False
    i = vertices.index(origem)
    j = vertices.index(destino)
    return matriz[i][j] == 1


def vizinhos(matriz, vertices, vertice):
    """
    Retorna a lista de vizinhos (vértices alcançáveis a partir de 'vertice').

    Passos:
    1. Verificar se 'vertice' existe em 'vertices'.
    2. Obter o índice 'i' correspondente.
    3. Criar uma lista de vizinhos vazia
    4. Para cada item da linha matriz[i], verificar se == 1
        - Adicionar o vértice correspondente na lista de vizinhos
    5. Retornar essa lista.
    """
    lista = []
    if vertice not in vertices:
        return lista
    i = vertices.index(vertice)
    for j in range(len(vertices)):
        if matriz[i][j] == 1:
            lista.append(vertices[j])
    return lista


def grau_vertices(matriz, vertices):
    """
    Calcula o grau de entrada, saída e total de cada vértice.

    Passos:
    1. Criar um dicionário vazio 'graus'.
    2. Para cada vértice i:
        - Se o grafo for direcionado:
            - Grau de saída: somar os valores da linha i.
            - Grau de entrada: somar os valores da coluna i.
            - Grau total = entrada + saída.
        - Se não:
            - calcular apenas o grau de saida ou entrada
    3. Armazenar no dicionário no formato:
        graus[vértice] = {"saida": x, "entrada": y, "total": z} ou graus[vértice] = x.
    4. Retornar 'graus'.
    """
    graus = {}
    for i in range(len(vertices)):
        saida = sum(matriz[i])
        entrada = 0
        for linha in matriz:
            entrada += linha[i]
        graus[vertices[i]] = {"saida": saida, "entrada": entrada, "total": entrada + saida}
    return graus


def percurso_valido(matriz, vertices, caminho):
    """
    Verifica se um percurso (sequência de vértices) é possível no grafo.

    Passos:
    1. Percorrer a lista 'caminho' de forma sequencial (de 0 até len-2).
    2. Para cada par consecutivo (u, v):
        - Verificar se existe_aresta(matriz, vertices, u, v) é True.
        - Se alguma não existir, retornar False.
    3. Se todas existirem, retornar True.
    """
    for i in range(len(caminho) - 1):
        if not existe_aresta(matriz, vertices, caminho[i], caminho[i + 1]):
            return False
    return True


def listar_vizinhos(matriz, vertices, vertice):
    """
    Exibe (ou retorna) os vizinhos de um vértice.

    Passos:
    1. Verificar se o vértice existe.
    2. Chamar a função vizinhos() para obter a lista.
    3. Exibir a lista formatada (ex: print(f"Vizinhos de {v}: {lista}")).
    """
    if vertice not in vertices:
        print("Vértice não encontrado.")
    else:
        print("Vizinhos de", vertice, ":", vizinhos(matriz, vertices, vertice))


def exibir_grafo(matriz, vertices):
    """
    Exibe o grafo em formato de matriz de adjacência.

    Passos:
    1. Exibir cabeçalho com o nome dos vértices.
    2. Para cada linha i:
        - Mostrar o nome do vértice.
        - Mostrar os valores da linha (0 ou 1) separados por espaço.
    """
    if not vertices:
        print("Grafo vazio.")
        return
    print("     " + " ".join(f"{v:>4}" for v in vertices))
    for i in range(len(vertices)):
        print(f"{vertices[i]:>4} " + " ".join(f"{valor:>4}" for valor in matriz[i]))


def main():

    matriz, vertices = criar_grafo()
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
            exibir_grafo(matriz, vertices)
        elif opcao == "2":
            vertice = input("Vértice: ").strip()
            if vertice:
                inserir_vertice(matriz, vertices, vertice)
        elif opcao == "3":
            origem = input("Origem: ").strip()
            destino = input("Destino: ").strip()
            if origem and destino:
                inserir_aresta(matriz, vertices, origem, destino, nao_direcionado)
        elif opcao == "4":
            vertice = input("Vértice para remover: ").strip()
            remover_vertice(matriz, vertices, vertice)
        elif opcao == "5":
            origem = input("Origem: ").strip()
            destino = input("Destino: ").strip()
            remover_aresta(matriz, vertices, origem, destino, nao_direcionado)
        elif opcao == "6":
            vertice = input("Consultar vizinhos de: ").strip()
            listar_vizinhos(matriz, vertices, vertice)
        elif opcao == "7":
            for vertice, dados in grau_vertices(matriz, vertices).items():
                print(vertice, dados)
        elif opcao == "8":
            origem = input("Origem: ").strip()
            destino = input("Destino: ").strip()
            print("Existe aresta:", existe_aresta(matriz, vertices, origem, destino))
        elif opcao == "9":
            caminho = input("Caminho separado por espaços (ex: A B C): ").split()
            print("Percurso válido:", percurso_valido(matriz, vertices, caminho))
        elif opcao == "0":
            print("Até mais!")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
