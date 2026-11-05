def criar_grafo():
    """
    Retorna um novo grafo vazio.
    Passos:
    1. Criar um dicionário vazio: {}
    2. Retornar o dicionário (representa o grafo)
    """
    return {}


def inserir_vertice(grafo, vertice):
    """
    Insere um vértice no grafo, sem arestas iniciais.
    Passos:
    1. Verificar se 'vertice' já é chave em grafo.
    2. Se não for, criar entrada grafo[vertice] = []
    3. Se já existir, não fazer nada (ou avisar)
    """
    if vertice not in grafo:
        grafo[vertice] = []


def inserir_aresta(grafo, origem, destino, nao_direcionado=False):
    """
    Adiciona aresta entre origem e destino.
    Passos:
    1. Garantir que 'origem' e 'destino' existam no grafo (inserir se necessário).
    2. adicionar destino como vizinho de origem (append).
    3. Se for Nâo Direcionado, também:
         - adicionar origem como vizinho de destino
    """
    inserir_vertice(grafo, origem)
    inserir_vertice(grafo, destino)
    if destino not in grafo[origem]:
        grafo[origem].append(destino)
    if nao_direcionado and origem not in grafo[destino]:
        grafo[destino].append(origem)

def vizinhos(grafo, vertice):
    """
    Retorna a lista de vizinhos de 'vertice'.
    Passos:
    1. Se 'vertice' estiver em grafo, retornar grafo[vertice] (lista).
    2. Se não existir, retornar lista vazia ou sinalizar erro.
    """
    if vertice in grafo:
        return grafo[vertice]
    return []

def listar_vizinhos(grafo, vertice):
    """
    Função semântica: imprimir/retornar os vizinhos de 'vertice'.
    Passos:
    1. Obter lista = vizinhos(grafo, vertice)
    2. Retornar/imprimir essa lista (ou informar que o vértice não existe)
    """
    if vertice not in grafo:
        print("Vértice não encontrado.")
    else:
        print("Vizinhos de", vertice, ":", vizinhos(grafo, vertice))

def exibir_grafo(grafo):
    """
    Exibe o grafo em forma legível (lista de adjacência).
    Passos:
    1. Para cada vertice em ordem
         - imprimir: vertic e -> vizinhos
    """
    if not grafo:
        print("Grafo vazio.")
    for vertice in grafo:
        print(vertice, "->", grafo[vertice])

def remover_aresta(grafo, origem, destino, nao_direcionado=False):
    """
    Remove a aresta entre origem e destino.
    Passos:
    1. Verificar se 'origem' existe; se não, terminar.
    2. Se destino estiver em grafo[origem], remover essa ocorrência.
    3. Se for não direcionado, também:
         - verificar se 'destino' existe e remover 'origem' de grafo[destino] se presente.
    """
    if origem in grafo and destino in grafo[origem]:
        grafo[origem].remove(destino)
    if nao_direcionado and destino in grafo and origem in grafo[destino]:
        grafo[destino].remove(origem)


def remover_vertice(grafo, vertice, nao_direcionado=True):
    """
    Remove um vértice e todas as arestas que o tocam.
    Passos:
    1. Verificar se 'vertice' existe em grafo; se não, terminar.
    2. Para cada outro vertice no grafo:
         - se 'vertice' estiver na lista de vizinhos, remover essa aresta.
    3. Remover o vertice do grafo
    4. Opcional: retornar confirmação/erro.
    """
    if vertice not in grafo:
        return
    for outro in grafo:
        if vertice in grafo[outro]:
            grafo[outro].remove(vertice)
    del grafo[vertice]


def existe_aresta(grafo, origem, destino):
    """
    Verifica se existe aresta direta origem -> destino.
    Passos:
    1. Verificar se 'origem' é chave no grafo.
    2. Retornar True se 'destino' estiver em grafo[origem], caso contrário False.
    """
    return origem in grafo and destino in grafo[origem]

def grau_vertices(grafo):
    """
    Calcula e retorna o grau (out, in, total) de cada vértice.
    Passos:
    1. Inicializar um dict de graus vazia
    2. Para cada vertice, colocar no dict uma estrutura com in, out e total zerado
    3. Para cada u em grafo:
         - out_degree[u] = tamanho de vizinhos
         - para cada v em grafo:
            - verificar se u está na lista de vizinho de v,
            - caso esteja, adicionar +1 para o grau de entrada de u
    4. Calcular o grau total somando entrada + saida
    5. Retornar uma estrutura contendo out,in,total por vértice (ex: dict de tuplas).
    """
    graus = {}
    for vertice in grafo:
        saida = len(grafo[vertice])
        entrada = 0
        for outro in grafo:
            if vertice in grafo[outro]:
                entrada += 1
        graus[vertice] = {"saida": saida, "entrada": entrada, "total": entrada + saida}
    return graus


def percurso_valido(grafo, caminho):
    """
    Verifica se uma sequência específica de vértices (caminho) é válida:
    i.e., se existem arestas consecutivas entre os nós do caminho.
    Passos:
    1. Se caminho tiver tamanho < 2, retornar True (trivial).
    2. Para i de 0 até len(caminho)-2:
         - origem = caminho[i], destino = caminho[i+1]
         - se não existe_aresta(grafo, origem, destino): retornar False
    3. Se todas as arestas existirem, retornar True.
    """
    for i in range(len(caminho) - 1):
        if not existe_aresta(grafo, caminho[i], caminho[i + 1]):
            return False
    return True



def main():
    """
    Crie um menu onde seja possível escolher qual ação deseja realizar
    ex:
        1 - Mostrar o Grafo
        2 - inserir vertice
        3 - inserir aresta
        4 - remover vértice.
        ....
    """
    grafo = criar_grafo()
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
            exibir_grafo(grafo)
        elif opcao == "2":
            vertice = input("Vértice: ").strip()
            if vertice:
                inserir_vertice(grafo, vertice)
        elif opcao == "3":
            origem = input("Origem: ").strip()
            destino = input("Destino: ").strip()
            if origem and destino:
                inserir_aresta(grafo, origem, destino, nao_direcionado)
        elif opcao == "4":
            vertice = input("Vértice para remover: ").strip()
            remover_vertice(grafo, vertice)
        elif opcao == "5":
            origem = input("Origem: ").strip()
            destino = input("Destino: ").strip()
            remover_aresta(grafo, origem, destino, nao_direcionado)
        elif opcao == "6":
            vertice = input("Consultar vizinhos de: ").strip()
            listar_vizinhos(grafo, vertice)
        elif opcao == "7":
            for vertice, dados in grau_vertices(grafo).items():
                print(vertice, dados)
        elif opcao == "8":
            origem = input("Origem: ").strip()
            destino = input("Destino: ").strip()
            print("Existe aresta:", existe_aresta(grafo, origem, destino))
        elif opcao == "9":
            caminho = input("Caminho separado por espaços (ex: A B C): ").split()
            print("Percurso válido:", percurso_valido(grafo, caminho))
        elif opcao == "0":
            print("Até mais!")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
