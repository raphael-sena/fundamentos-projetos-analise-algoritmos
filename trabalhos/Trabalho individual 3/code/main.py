"""
main.py
---------------------------------
Algoritmo de busca em profundidade (backtracking)
para encontrar um Caminho Hamiltoniano em um grafo
direcionado OU não direcionado.

Formato de entrada (stdin):

Linha 1: tipo do grafo
    D  -> grafo direcionado
    U  -> grafo não direcionado

Linha 2: n m
    n = número de vértices (0 ... n-1)
    m = número de arestas

Próximas m linhas: u v
    Se D: aresta de u -> v
    Se U: aresta entre u e v (bidirecional)

Saída:
- Se existir caminho Hamiltoniano:
    CAMINHO HAMILTONIANO ENCONTRADO:
    v0 -> v1 -> v2 -> ... -> v(n-1)
- Caso contrário:
    NAO EXISTE CAMINHO HAMILTONIANO
"""

from typing import List


def ler_grafo():
    """
    Lê o grafo da entrada padrão e retorna:
    - adj: lista de adjacência (list[list[int]])
    - n: número de vértices
    """
    import sys

    data = sys.stdin.read().strip().split()
    if not data:
        raise ValueError("Entrada vazia. Verifique o arquivo / stdin.")

    # 1) tipo do grafo
    tipo = data[0].upper()
    if tipo not in ("D", "U"):
        raise ValueError("Tipo de grafo inválido. Use 'D' (direcionado) ou 'U' (não direcionado).")

    # 2) n m
    # data[1] = n, data[2] = m
    if len(data) < 3:
        raise ValueError("Entrada incompleta. Esperado: tipo, n, m.")

    n = int(data[1])
    m = int(data[2])

    # validações básicas
    if n <= 0:
        raise ValueError("Número de vértices precisa ser > 0.")
    if m < 0:
        raise ValueError("Número de arestas não pode ser negativo.")

    # 3) arestas
    # Próximos pares (u, v)
    if len(data) != 3 + 2 * m:
        raise ValueError(
            f"Quantidade de valores não bate com m={m}. "
            f"Era esperado {3 + 2*m} valores e chegaram {len(data)}."
        )

    # monta lista de adjacência
    adj = [[] for _ in range(n)]

    idx = 3
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2

        if u < 0 or u >= n or v < 0 or v >= n:
            raise ValueError(f"Aresta fora do intervalo de vértices: {u} {v}")

        # adiciona aresta
        adj[u].append(v)
        if tipo == "U" and u != v:
            # se não-direcionado, também adiciona o contrário
            adj[v].append(u)

    return adj, n


def encontrar_caminho_hamiltoniano(adj: List[List[int]], n: int) -> List[int] | None:
    """
    Tenta encontrar QUALQUER caminho Hamiltoniano.
    Retorna a lista de vértices na ordem do caminho se conseguir,
    senão retorna None.

    Estratégia:
    - Tenta começar de cada vértice possível (porque o caminho pode começar em qualquer um).
    - Faz backtracking tentando visitar todos os vértices exatamente uma vez.
    """

    visitado = [False] * n
    caminho = []

    def backtrack(v_atual: int, profundidade: int) -> bool:
        """
        v_atual: vértice atual
        profundidade: quantos vértices já temos no caminho até agora
        Retorna True se conseguimos completar um caminho Hamiltoniano.
        """
        caminho.append(v_atual)
        visitado[v_atual] = True

        # se já colocamos todos os vértices no caminho, sucesso
        if profundidade == n:
            return True

        # tenta expandir para vizinhos ainda não visitados
        for prox in adj[v_atual]:
            if not visitado[prox]:
                if backtrack(prox, profundidade + 1):
                    return True

        # backtrack (desfaz)
        visitado[v_atual] = False
        caminho.pop()
        return False

    # tenta iniciar o caminho a partir de cada vértice
    for inicio in range(n):
        # reset marcações entre tentativas
        for i in range(n):
            visitado[i] = False
        caminho.clear()

        if backtrack(inicio, 1):
            return caminho[:]  # cópia do caminho encontrado

    return None  # não achou nenhum caminho Hamiltoniano


def main():
    # 1. ler grafo
    adj, n = ler_grafo()

    # 2. tentar encontrar caminho hamiltoniano
    caminho = encontrar_caminho_hamiltoniano(adj, n)

    # 3. imprimir resultado
    if caminho is not None:
        print("CAMINHO HAMILTONIANO ENCONTRADO:")
        print(" -> ".join(map(str, caminho)))
    else:
        print("NAO EXISTE CAMINHO HAMILTONIANO")


if __name__ == "__main__":
    main()
