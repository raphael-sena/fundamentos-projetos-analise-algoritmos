# Projeto de Implementação do Algoritmo de Karatsuba em Python

O projeto de implementação do algoritmo de Karatsuba em Python, é um projeto para a elucidação e análise dos conceitos de complexidade ciclomática e breve introdução das complexidades assintóticas. Além de explorar a multiplicação eficiente de números inteiros grandes.

## Descrição do Projeto

O algoritmo de Karatsuba é um método recursivo para multiplicação de inteiros grandes, proposto em 1960 por Anatolii Karatsuba. Diferente da multiplicação tradicional (complexidade O(n²)), ele reduz a quantidade de operações necessárias, atingindo complexidade O(n^log₂3).

A lógica implementada pode ser encontrada no arquivo [`main.py`](./codigo/main.py)

## Execução do Projeto

#### Pré-requisitos

- Python 3.8 ou superior instalado no sistema.
- Nenhuma dependência externa é necessária.

#### Como rodar

1. Clone este repositório e acesse o código do projeto:
    ```bash
    git clone https://github.com/raphael-sena/fundamentos-projetos-analise-algoritmos.git
    cd Trabalho\ individual\ 1/codigo/
    ```

2. Execute o programa:
    ```bash
    python main.py
    ```

3. Informe os dois números inteiros quando solicitado:
    ```bash
    Digite o primeiro número: 123456789
    Digite o segundo número: 987654321
    ```

4. A saída exibirá:
    - Resultado Karatsuba
    - Tempo de execução
    - Resultado da multiplicação normal
    - Tempo de execução

## Relatório Técnico

#### Análise da complexidade ciclomática:
**Grafo:**

<img alt="banner"  src="./assets/images/Grafo.png"/>

**Nós (N):**
- N1: Início da função.
- N2: Decisão do caso base (len(A) < 10 ou len(B) < 10).
- N3: Retorno do caso base (multiplicação direta).
- N4: Cálculo de n = max(len(A), len(B)) 
- N5: Cálculo de n2 = n // 2.
- N6: Normalização: preenchimento com zeros à esquerda de A.
- n7: Normalização: preenchimento com zeros à esquerda de B.
- N8: Particionamento: Al, Ar, 
- N9: Particionamento: Bl, Br.
- N10: p = multiplicar(Al, Bl).
- N11: q = multiplicar(Ar, Br).
- N12: r_parcial = multiplicar(encontrarSoma(Al, Ar), encontrarSoma(Bl, Br)).
- N13: r = encontrarDiferenca(r_parcial, encontrarSoma(p, q)).
- N14: Retorno final (combinação dos resultados).

Número total de nós: N = 14.

**Arestas (N):**
1. N1 → N2 (do início para a decisão do caso base).
2. N2(True) → N3 (se o caso base for verdadeiro).
3. N2(False) → N4 (se não for caso base).
4. N4 → N5 (após calcular n).
5. N5 → N6 (após calcular n2).
6. N6 → N7 (após normalizar A).
7. N7 → N8 (após normalizar B).
8. N8 → N9 (após particionar).
9. N9 → N10 (após calcular p).
10. N10 → N11 (após calcular q).
11. N11 → N12 (após calcular r_parcial).
12. N12 → N13 (após ajustar r).
13. N13 → N14 (retorno final encerra a função).

Número total de arestas: E = 13.

**Agora, usamos a fórmula da complexidade ciclomática:**
- `𝑀 = 𝐸 - 𝑁 + 2𝑃`

M = 14 - 14 + 2*1
M = 2

#### Análise da complexidade assintótica:

**Multiplicação Tradicional:**
- Tempo: O(n²)
- Espaço: O(n)

**Karatsuba:**
- Tempo: O(n^log₂3)
- Espaço: O(n)

**Casos:**
- Melhor caso: números pequenos (resolvido no caso base direto).
- Caso médio: números de tamanho arbitrário.
- Pior caso: números muito grandes (a complexidade ainda é melhor que O(n²)).