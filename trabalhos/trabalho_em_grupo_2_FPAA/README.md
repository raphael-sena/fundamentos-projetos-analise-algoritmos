# Flood Fill – Colorindo regiões de um terreno com obstáculos

Trabalho em grupo 2 – Fundamentos de Projeto e Análise de Algoritmos
Professor: João Paulo Carneiro Aramuni

Este projeto implementa o algoritmo **Flood Fill** para identificar e preencher automaticamente
todas as regiões navegáveis de um terreno representado por um **grid 2D**, respeitando obstáculos
e eventuais regiões já coloridas.

---

## 1. Descrição do problema

O terreno é representado por uma matriz `n x m`, onde cada célula pode assumir:

- `0` – Terreno navegável (branco)
- `1` – Obstáculo (preto, não navegável)
- `2, 3, 4, ...` – Cores já preenchidas em outras regiões (vermelho, laranja, amarelo, etc.)

Também é fornecida uma **célula inicial** `(x, y)`, de onde o preenchimento começa.

O algoritmo deve:

1. Determinar todas as células conectadas à célula inicial que possuem valor `0`.
2. Substituir o valor `0` dessas células por uma **cor específica** (`2` para a primeira região,
   `3` para a próxima, `4` para a seguinte e assim por diante).
3. Após preencher uma região, localizar automaticamente a próxima célula navegável (`0`) e
   repetir o processo com a cor seguinte, até que **todo o terreno esteja mapeado e colorido**.

A conexão entre células é feita **apenas ortogonalmente** (cima, baixo, esquerda e direita).

---

## 2. Algoritmo Flood Fill implementado

### 2.1. Ideia geral

O algoritmo Flood Fill é um método clássico para preencher regiões conectadas em uma grade.
Nesta implementação, ele é usado para:

- Partir de uma célula inicial navegável (`0`),
- Visitar todas as células `0` conectadas ortogonalmente,
- Atribuir a elas um novo valor de cor (por exemplo, `2`),
- Repetir o processo para todas as demais regiões ainda não preenchidas.

### 2.2. Estratégia utilizada

Foi utilizada uma abordagem **iterativa com fila (BFS – Breadth-First Search)** para evitar
problemas de estouro de pilha em grids grandes.

Passos principais:

1. Verificar se a célula inicial está dentro do grid e é navegável (`0`).
2. Colocar a célula inicial em uma fila e marcar com a cor escolhida.
3. Enquanto a fila não estiver vazia:
   - Remover uma célula da fila;
   - Visitar seus **4 vizinhos ortogonais**;
   - Se o vizinho for navegável (`0`), marcá-lo com a cor e adicioná-lo à fila.

Após preencher a região da célula inicial, o programa:

1. Procura a **próxima célula 0** no grid (percorrendo linha por linha);
2. Incrementa o valor da cor (`2`, `3`, `4`, ...);
3. Executa o Flood Fill novamente a partir dessa nova célula;
4. Repete o processo até que não existam mais células navegáveis (`0`).

### 2.3. Respeito a obstáculos e regiões já coloridas

- As células com valor `1` são tratadas como **obstáculos**: não podem ser preenchidas e
  não são atravessadas pelo algoritmo.
- Células com valor `>= 2` são consideradas **regiões já coloridas**: o algoritmo não
  altera seus valores, apenas inicia novas cores a partir de `max(cor_existente) + 1`
  (se for o caso).

### 2.4. Complexidade

Seja `N = n * m` o número total de células do grid.

- Cada célula é visitada no máximo uma vez por região, logo a complexidade temporal é
  **O(N)**.
- A complexidade espacial é **O(N)** no pior caso (fila contendo praticamente toda a região).

---

## 3. Estrutura do projeto

- `flood_fill.py` – Script principal contendo:
  - Implementação do algoritmo Flood Fill;
  - Funções auxiliares para impressão do grid;
  - Funções de visualização gráfica com `matplotlib`;
  - Interface simples via terminal (menu com exemplos e entrada manual).

---

## 4. Como executar o projeto

### 4.1. Pré-requisitos

- Python 3.x instalado
- Biblioteca `matplotlib` para a visualização gráfica

Instalação do `matplotlib` (opcional, mas recomendada):

```bash
pip install matplotlib
```

### 4.2. Executando o script

No terminal, dentro da pasta do projeto, execute:

```bash
python flood_fill.py
```

Será exibido um menu:

```text
Algoritmo Flood Fill - Mapeamento de Terreno
1 - Executar exemplos do enunciado
2 - Digitar um grid manualmente
```

#### Opção 1 – Exemplos prontos

Reproduz automaticamente os **Exemplos 1 e 2** do enunciado, mostrando:

- Grid original (no terminal);
- Grid preenchido (no terminal);
- Visualização gráfica colorida (se o `matplotlib` estiver instalado).

#### Opção 2 – Entrada manual

Permite informar:

1. Dimensões do grid `n m`
2. O grid, linha a linha, com valores `0`, `1` ou `>= 2`
3. As coordenadas iniciais `x y` (linha e coluna, iniciando em 0)

Exemplo de entrada manual:

```text
4 5
0 0 1 0 0
0 1 1 0 0
0 0 1 1 1
1 1 0 0 0
0 0
```

---

## 5. Exemplos de entrada e saída

### Exemplo 1 (do enunciado)

**Entrada – Grid inicial:**

```text
0 0 1 0 0
0 1 1 0 0
0 0 1 1 1
1 1 0 0 0
Coordenadas iniciais: (0, 0)
```

**Saída – Grid preenchido:**

```text
2 2 1 3 3
2 1 1 3 3
2 2 1 1 1
1 1 4 4 4
```

### Exemplo 2 (do enunciado)

**Entrada – Grid inicial:**

```text
0 1 0 0 1
0 1 0 0 1
0 1 1 1 1
0 0 0 1 0
Coordenadas iniciais: (0, 2)
```

**Saída – Grid preenchido:**

```text
3 1 2 2 1
3 1 2 2 1
3 1 1 1 1
3 3 3 1 4
```

Em ambos os casos, o programa:

1. Preenche a região conectada à célula inicial com a cor `2`;
2. Localiza automaticamente as próximas regiões navegáveis;
3. Atribui cores `3`, `4`, ... para cada nova região até que não restem células `0`.

---

## 6. Visualização gráfica com cores

A versão gráfica utiliza `matplotlib` para exibir o grid como uma imagem, com o seguinte
mapeamento de cores base:

- `0` – Branco (terreno navegável)
- `1` – Preto (obstáculo)
- `2` – Vermelho
- `3` – Laranja
- `4` – Amarelo

Cores adicionais (`>= 5`) recebem outras cores distintas para facilitar a visualização em
grids com muitas regiões.

São geradas janelas separadas para:

- Grid original;
- Grid preenchido (para os exemplos e para a entrada manual).

---

## 7. Conclusão

O projeto implementa de forma completa o algoritmo **Flood Fill** para mapeamento de
regiões conectadas em um grid 2D com obstáculos. A solução:

- Identifica corretamente as regiões navegáveis;
- Respeita obstáculos e regiões já coloridas;
- Preenche automaticamente todas as regiões, atribuindo cores distintas;
- Oferece visualização tanto em formato de matriz (terminal) quanto em forma gráfica
  colorida, facilitando a compreensão do comportamento do algoritmo.
