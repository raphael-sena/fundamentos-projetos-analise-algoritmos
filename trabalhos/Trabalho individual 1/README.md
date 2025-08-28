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

#### Análise da complexidade assintótica:

**Multiplicação Tradicional:**
- Tempo: O(n²)
- Espaço: O(n)

**Karatsuba:**
Tempo: O(n^log₂3)
Espaço: O(n), considerando armazenamento intermediário.

**Casos:**
- Melhor caso: números pequenos (resolvido no caso base direto).
- Caso médio: números de tamanho arbitrário.
- Pior caso: números muito grandes (a complexidade ainda é melhor que O(n²)).