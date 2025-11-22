#!/usr/bin/env python3
"""
Trabalho em grupo 2 - Flood Fill - Colorindo regiões de um terreno com obstáculos

Disciplina: Fundamentos de Projeto e Análise de Algoritmos
Professor: João Paulo Carneiro Aramuni

Implementação em Python do algoritmo Flood Fill para identificação e preenchimento
de todas as regiões navegáveis (células com valor 0) em um grid 2D contendo obstáculos (1)
e, opcionalmente, regiões já coloridas (>= 2).
"""

from collections import deque
from typing import List, Tuple, Optional

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm

Grid = List[List[int]]


# ---------------------------- Funções de utilidade ----------------------------

def print_grid(grid: Grid, title: str = "") -> None:
    """Imprime o grid no terminal como matriz de inteiros."""
    if title:
        print(title)
    for row in grid:
        print(" ".join(str(cell) for cell in row))
    print()


def max_color_in_grid(grid: Grid) -> int:
    """Retorna o maior valor inteiro presente no grid (usado para definir a próxima cor)."""
    max_c = 0
    for row in grid:
        if row:
            row_max = max(row)
            if row_max > max_c:
                max_c = row_max
    return max_c


def find_next_empty_cell(grid: Grid) -> Optional[Tuple[int, int]]:
    """Encontra a próxima célula navegável (valor 0) percorrendo o grid linha a linha."""
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 0:
                return i, j
    return None


# ------------------------- Algoritmo Flood Fill (BFS) -------------------------

def flood_fill_region(grid: Grid, start_x: int, start_y: int, color: int) -> bool:
    """
    Preenche uma região conectada a partir da célula (start_x, start_y) com a cor dada.

    A região é composta apenas por células:
    - navegáveis (valor 0 no momento do preenchimento);
    - conectadas ortogonalmente (cima, baixo, esquerda, direita).

    Obstáculos (1) e células já coloridas (>= 2) não são modificados.

    Retorna True se alguma célula foi preenchida; False se a célula inicial não é navegável.
    """
    n = len(grid)
    if n == 0:
        return False
    m = len(grid[0])

    # Verifica se a célula inicial está dentro dos limites do grid
    if not (0 <= start_x < n and 0 <= start_y < m):
        return False

    # Só preenche se a célula inicial for navegável (0)
    if grid[start_x][start_y] != 0:
        return False

    fila = deque()
    fila.append((start_x, start_y))
    grid[start_x][start_y] = color

    # Vizinhos ortogonais (4-direções)
    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while fila:
        x, y = fila.popleft()

        for dx, dy in direcoes:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0:
                grid[nx][ny] = color
                fila.append((nx, ny))

    return True


def fill_all_regions(grid: Grid, start_x: int, start_y: int) -> Grid:
    """
    Executa o Flood Fill em todas as regiões navegáveis do grid.

    1. Calcula a próxima cor disponível:
       - Se o grid só tem 0 e 1, começa em 2.
       - Se já existem cores (>= 2), começa em max(cor existente) + 1.

    2. Preenche a região conectada à célula inicial (start_x, start_y), se ela for 0.

    3. Em seguida, procura automaticamente a próxima célula 0 no grid e
       preenche essa nova região com a próxima cor, incrementando o valor
       da cor (2, 3, 4, ...) até que não restem células navegáveis.
    """
    max_color = max_color_in_grid(grid)
    if max_color < 2:
        next_color = 2
    else:
        next_color = max_color + 1

    # Preenche a região da célula inicial (se for navegável)
    if flood_fill_region(grid, start_x, start_y, next_color):
        max_color = next_color

    # Preenche automaticamente as próximas regiões navegáveis
    while True:
        cell = find_next_empty_cell(grid)
        if cell is None:
            break  # Não há mais células 0
        max_color += 1
        flood_fill_region(grid, cell[0], cell[1], max_color)

    return grid


# ------------------------ Visualização gráfica (matriz) -----------------------

def grid_to_numpy(grid: Grid) -> np.ndarray:
    """Converte o grid (lista de listas) para um array NumPy."""
    return np.array(grid, dtype=int)


def show_grid_as_image(grid: Grid, title: str) -> None:
    """
    Mostra o grid em uma janela gráfica, usando cores para cada valor inteiro.

    Mapeamento principal:
        0 – Branco (Terreno navegável)
        1 – Preto  (Obstáculo)
        2 – Vermelho
        3 – Laranja
        4 – Amarelo
    Cores acima de 4 recebem outras cores distintas para facilitar a visualização.
    """
    data = grid_to_numpy(grid)
    max_val = int(data.max()) if data.size > 0 else 0

    # Paleta base com as cores sugeridas no enunciado
    colors = [
        "#FFFFFF",  # 0 - branco (terreno navegável)
        "#000000",  # 1 - preto (obstáculo)
        "#FF0000",  # 2 - vermelho
        "#FF8C00",  # 3 - laranja
        "#FFFF00",  # 4 - amarelo
        "#00FF00",  # 5 - verde
        "#00FFFF",  # 6 - ciano
        "#0000FF",  # 7 - azul
        "#800080",  # 8 - roxo
        "#FFC0CB",  # 9 - rosa
        "#A52A2A",  # 10 - marrom
    ]

    # Garante que temos cores suficientes para todos os valores presentes no grid
    if max_val >= len(colors):
        colors.extend(["#808080"] * (max_val - len(colors) + 1))

    boundaries = list(range(len(colors) + 1))
    cmap = ListedColormap(colors)
    norm = BoundaryNorm(boundaries, cmap.N)

    plt.figure()
    plt.imshow(data, cmap=cmap, norm=norm)
    plt.title(title)
    plt.colorbar(ticks=range(0, max_val + 1), label="Valores da célula")

    # Exibe grade (linhas) para destacar cada célula
    plt.xticks(range(data.shape[1]))
    plt.yticks(range(data.shape[0]))
    plt.gca().set_xticks(np.arange(-0.5, data.shape[1], 1), minor=True)
    plt.gca().set_yticks(np.arange(-0.5, data.shape[0], 1), minor=True)
    plt.grid(which="minor", color="gray", linestyle="-", linewidth=0.5)

    plt.show()


# --------------------------- Entrada / Saída (CLI) ----------------------------

def read_grid_from_input() -> Tuple[Grid, int, int]:
    """
    Lê as dimensões do grid, o próprio grid e as coordenadas iniciais do usuário.

    Formato esperado (exemplo):
        n m
        linha1...
        linha2...
        ...
        linhaN...
        x y
    """
    print("Digite as dimensões do grid (n m):")
    n, m = map(int, input().split())

    print(f"Digite o grid com {n} linhas e {m} colunas (valores 0, 1 ou >= 2 separados por espaço):")
    grid: Grid = []
    for i in range(n):
        row = list(map(int, input().split()))
        if len(row) != m:
            raise ValueError(f"Linha {i} deve conter exatamente {m} valores.")
        grid.append(row)

    print("Digite as coordenadas iniciais x y (linha e coluna, começando em 0):")
    x, y = map(int, input().split())

    return grid, x, y


def run_with_custom_input() -> None:
    """Executa o algoritmo Flood Fill com dados digitados pelo usuário."""
    grid, x, y = read_grid_from_input()
    original = [row[:] for row in grid]

    print_grid(original, "Grid original:")
    fill_all_regions(grid, x, y)
    print_grid(grid, "Grid preenchido:")

    # Tenta mostrar visualização gráfica (opcional)
    try:
        show_grid_as_image(original, "Grid original (visualização gráfica)")
        show_grid_as_image(grid, "Grid preenchido (visualização gráfica)")
    except Exception as e:
        print("Não foi possível abrir a visualização gráfica. "
              "Certifique-se de ter o matplotlib instalado (pip install matplotlib).")
        print("Detalhes do erro:", e)


def run_examples() -> None:
    """Executa os exemplos do enunciado para validar a implementação."""
    # Exemplo 1 (do enunciado)
    example1 = [
        [0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 1, 1, 1],
        [1, 1, 0, 0, 0],
    ]
    start1 = (0, 0)
    g1 = [row[:] for row in example1]

    print("=== Exemplo 1 (do enunciado) ===")
    print_grid(g1, "Grid original:")
    fill_all_regions(g1, *start1)
    print_grid(g1, "Grid preenchido:")

    # Exemplo 2 (do enunciado)
    example2 = [
        [0, 1, 0, 0, 1],
        [0, 1, 0, 0, 1],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 1, 0],
    ]
    start2 = (0, 2)
    g2 = [row[:] for row in example2]

    print("=== Exemplo 2 (do enunciado) ===")
    print_grid(g2, "Grid original:")
    fill_all_regions(g2, *start2)
    print_grid(g2, "Grid preenchido:")

    # Visualização gráfica opcional
    try:
        show_grid_as_image(example1, "Exemplo 1 - Grid original")
        show_grid_as_image(g1, "Exemplo 1 - Grid preenchido")
        show_grid_as_image(example2, "Exemplo 2 - Grid original")
        show_grid_as_image(g2, "Exemplo 2 - Grid preenchido")
    except Exception as e:
        print("Não foi possível abrir a visualização gráfica nos exemplos.")
        print("Detalhes do erro:", e)


def main() -> None:
    print("Algoritmo Flood Fill - Mapeamento de Terreno")
    print("1 - Executar exemplos do enunciado")
    print("2 - Digitar um grid manualmente")
    choice = input("Escolha uma opção (1 ou 2): ").strip()

    if choice == "1":
        run_examples()
    else:
        run_with_custom_input()


if __name__ == "__main__":
    main()
