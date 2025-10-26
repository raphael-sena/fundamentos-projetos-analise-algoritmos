import os
from typing import List, Tuple
import networkx as nx
import matplotlib.pyplot as plt
from main import encontrar_caminho_hamiltoniano


def ler_grafo_visualizacao():
    """
    Lê o grafo do stdin, bem parecido com ler_grafo() do main.py,
    mas aqui eu também retorno:
    - tipo ('D' ou 'U')
    - lista de arestas brutas (u,v) pra jogar no NetworkX depois
    """

    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        raise ValueError("Entrada vazia. Informe o grafo via stdin.")

    tipo = data[0].upper()
    if tipo not in ("D", "U"):
        raise ValueError("Tipo inválido. Use 'D' (direcionado) ou 'U' (não direcionado).")

    if len(data) < 3:
        raise ValueError("Entrada incompleta. Esperado: tipo, n, m.")

    n = int(data[1])
    m = int(data[2])

    if n <= 0:
        raise ValueError("Número de vértices precisa ser > 0.")
    if m < 0:
        raise ValueError("Número de arestas não pode ser negativo.")

    if len(data) != 3 + 2 * m:
        raise ValueError(
            f"Quantidade de valores não bate com m={m}. "
            f"Esperado {3 + 2*m} tokens e recebi {len(data)}."
        )

    # monta adjacência pro algoritmo
    adj = [[] for _ in range(n)]
    arestas: List[Tuple[int, int]] = []

    idx = 3
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2

        if u < 0 or u >= n or v < 0 or v >= n:
            raise ValueError(f"Aresta fora do intervalo de vértices: {u} {v}")

        # guarda aresta crua
        arestas.append((u, v))

        # preenche lista de adjacência (igual ao main.py)
        adj[u].append(v)
        if tipo == "U" and u != v:
            adj[v].append(u)

    return tipo, n, adj, arestas


def construir_grafo_networkx(tipo: str, n: int, arestas: List[Tuple[int, int]]):
    """
    Cria um grafo NetworkX:
    - nx.DiGraph() se for direcionado
    - nx.Graph() se for não direcionado
    e popula nós e arestas.
    """
    G = nx.DiGraph() if tipo == "D" else nx.Graph()
    G.add_nodes_from(range(n))
    G.add_edges_from(arestas)
    return G


def desenhar_grafo(G: nx.Graph, caminho: List[int] | None, output_path: str = "assets/grafo.png"):
    """
    Desenha o grafo com NetworkX e Matplotlib:
    - todos os nós e arestas "normais" em cinza
    - as arestas que fazem parte do caminho Hamiltoniano destacadas (ex: vermelho, grossas)

    Salva como PNG em output_path.
    """

    # Layout (posicionamento visual dos nós)
    # spring_layout tenta "espalhar" o grafo de forma legível.
    pos = nx.spring_layout(G, seed=42)

    # Conjunto de arestas que fazem parte do caminho Hamiltoniano
    caminho_edges = set()
    if caminho and len(caminho) > 1:
        # pega pares consecutivos (v[i] -> v[i+1])
        for i in range(len(caminho) - 1):
            a = caminho[i]
            b = caminho[i + 1]
            caminho_edges.add((a, b))
            # Se for grafo não direcionado, também marca a volta (b,a)
            if not G.is_directed():
                caminho_edges.add((b, a))

    # Vamos montar listas de cores e larguras por aresta
    edge_colors = []
    edge_widths = []

    for e in G.edges():
        if e in caminho_edges:
            edge_colors.append("red")   # destaque
            edge_widths.append(3.0)     # mais grosso
        else:
            edge_colors.append("gray")  # padrão
            edge_widths.append(1.0)

    # Desenha nós (bolinhas)
    nx.draw_networkx_nodes(
        G,
        pos,
        node_color="white",      # fundo branco
        edgecolors="black",      # contorno preto no nó
        linewidths=1.5,
        node_size=800,
    )

    # Desenha rótulo de cada nó (o número do vértice)
    nx.draw_networkx_labels(
        G,
        pos,
        font_size=10,
        font_color="black",
        font_weight="bold",
    )

    # Desenha arestas com cores/larguras personalizadas
    nx.draw_networkx_edges(
        G,
        pos,
        edge_color=edge_colors,
        width=edge_widths,
        arrows=G.is_directed(),  # seta se for direcionado
        arrowsize=20,            # tamanho da seta
        connectionstyle="arc3,rad=0.05",  # leve curvinha pra diferenciar arestas sobrepostas
    )

    plt.axis("off")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()

    print(f"Imagem salva em: {output_path}")


def main():
    # 1. Ler grafo da stdin
    tipo, n, adj, arestas = ler_grafo_visualizacao()

    # 2. Achar caminho Hamiltoniano usando a função do main.py
    caminho = encontrar_caminho_hamiltoniano(adj, n)

    if caminho is not None:
        print("CAMINHO HAMILTONIANO ENCONTRADO:")
        print(" -> ".join(map(str, caminho)))
    else:
        print("NAO EXISTE CAMINHO HAMILTONIANO")

    # 3. Montar grafo NetworkX + desenhar e salvar PNG
    G = construir_grafo_networkx(tipo, n, arestas)
    desenhar_grafo(G, caminho, output_path="assets/grafo.png")


if __name__ == "__main__":
    main()
