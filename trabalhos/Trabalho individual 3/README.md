# Caminho Hamiltoniano - Projeto em Python

## 1. Descrição do projeto

### 1.1. Objetivo
Este projeto implementa, em Python, um algoritmo baseado em **backtracking** para encontrar **um Caminho Hamiltoniano** em um grafo direcionado ou não direcionado.

**Caminho Hamiltoniano** = sequência de vértices onde:
- cada vértice do grafo aparece **exatamente uma vez**,
- e cada passo do caminho segue uma aresta válida do grafo.

O programa:
1. Lê o grafo da entrada padrão (stdin).
2. Monta a lista de adjacência.
3. Faz busca em profundidade tentando construir um caminho que passa por todos os vértices uma vez.
4. Imprime o caminho se encontrar, ou informa que não existe.

---

### 1.2. Explicação do algoritmo e da lógica (linha a linha)

A seguir está o resumo do arquivo `main.py`, seguido da explicação bloco a bloco.

#### Importações e docstring inicial
```python
"""
main.py
---------------------------------
...
"""
from typing import List
```

- A docstring explica o funcionamento esperado do programa, formato de entrada e saída.
- `from typing import List` é só para tipagem estática (`List[int]`, etc.). Não afeta lógica em runtime.

---

#### Função `ler_grafo()`
```python
def ler_grafo():
    import sys

    data = sys.stdin.read().strip().split()
    ...
```

- Lê **tudo** da entrada padrão (`stdin`), faz `split()` em tokens e guarda em `data`.

```python
    if not data:
        raise ValueError("Entrada vazia...")
```

- Proteção básica caso o programa rode sem entrada.

```python
    tipo = data[0].upper()
    if tipo not in ("D", "U"):
        raise ValueError("Tipo de grafo inválido...")
```

- `tipo` pode ser `"D"` (direcionado) ou `"U"` (não direcionado).
- Valida isso.

```python
    n = int(data[1])
    m = int(data[2])
```

- `n`: número de vértices (rotulados de `0` a `n-1`)
- `m`: número de arestas.

```python
    if n <= 0:
        raise ValueError("Número de vértices precisa ser > 0.")
    if m < 0:
        raise ValueError("Número de arestas não pode ser negativo.")
```

- Regras básicas de sanidade.

```python
    if len(data) != 3 + 2 * m:
        raise ValueError("Quantidade de valores não bate...")
```

- Cada aresta tem dois inteiros (`u v`), então esperamos exatamente `2*m` números depois dos 3 primeiros tokens.
- Se isso não bater, a entrada está malformada.

```python
    adj = [[] for _ in range(n)]
```

- Cria a **lista de adjacência**: `adj[v]` vai conter todos os vizinhos alcançáveis a partir de `v`.

```python
    idx = 3
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2

        if u < 0 or u >= n or v < 0 or v >= n:
            raise ValueError("Aresta fora do intervalo...")
```

- Lemos cada aresta.
- Verificamos se `u` e `v` existem no intervalo `[0, n-1]`.

```python
        adj[u].append(v)
        if tipo == "U" and u != v:
            adj[v].append(u)
```

- Se o grafo é direcionado, só adiciona `u -> v`.
- Se é não direcionado, adiciona dos dois lados: `u -> v` e `v -> u`.

**Retorno:**
```python
    return adj, n
```

- `adj`: lista de adjacência.
- `n`: número de vértices.

---

#### Função `encontrar_caminho_hamiltoniano(adj, n)`
```python
def encontrar_caminho_hamiltoniano(adj: List[List[int]], n: int) -> List[int] | None:
    visitado = [False] * n
    caminho = []
```

- `visitado[i] = True` significa que o vértice `i` já está no caminho atual.
- `caminho` guarda, em ordem, os vértices escolhidos até agora.

```python
    def backtrack(v_atual: int, profundidade: int) -> bool:
        caminho.append(v_atual)
        visitado[v_atual] = True
```

- A cada chamada recursiva:
  - Colocamos o vértice atual no caminho,
  - Marcamos como visitado.

```python
        if profundidade == n:
            return True
```

- Se já colocamos `n` vértices, significa que temos um caminho que visita TODOS exatamente uma vez -> sucesso.

```python
        for prox in adj[v_atual]:
            if not visitado[prox]:
                if backtrack(prox, profundidade + 1):
                    return True
```

- Para cada vizinho `prox` de `v_atual`, tentamos seguir o caminho se ele ainda não foi usado.
- Se qualquer chamada recursiva der certo, retornamos `True`.

```python
        visitado[v_atual] = False
        caminho.pop()
        return False
```

- Se nenhum vizinho funcionou, fazemos **backtracking**:
  - removemos `v_atual` do caminho,
  - desmarcamos como visitado,
  - retornamos `False`.

Agora, lado de fora da função interna:

```python
    for inicio in range(n):
        for i in range(n):
            visitado[i] = False
        caminho.clear()

        if backtrack(inicio, 1):
            return caminho[:]
```

- A busca tenta começar de **cada vértice possível** como ponto inicial.
- Antes de testar um novo vértice inicial, limpamos `visitado` e `caminho`.
- Se `backtrack(inicio, 1)` achar resposta, retornamos uma cópia do caminho encontrado.

```python
    return None
```

- Se nenhum vértice inicial gera um caminho que cobre todos os nós → não existe Caminho Hamiltoniano.

Resumo:
- É uma DFS com poda.
- A recursão explora permutações possíveis de vértices conectados por arestas.
- Se achar uma permutação válida que cobre todos, retorna e encerra.

---

#### Função `main()`
```python
def main():
    adj, n = ler_grafo()
    caminho = encontrar_caminho_hamiltoniano(adj, n)

    if caminho is not None:
        print("CAMINHO HAMILTONIANO ENCONTRADO:")
        print(" -> ".join(map(str, caminho)))
    else:
        print("NAO EXISTE CAMINHO HAMILTONIANO")
```

- Lê o grafo,
- Roda o algoritmo,
- Imprime o resultado.

```python
if __name__ == "__main__":
    main()
```

- Garante que `main()` só roda quando o arquivo é executado diretamente.

---

## 2. Como executar o projeto

### 2.1. Pré-requisitos
- Python 3.10+  
  (Versões anteriores de Python 3 também funcionam se você ajustar a tipagem `List[int] | None` para `Optional[List[int]]`.)

### 2.2. Estrutura mínima do projeto
```text
/.
├── main.py
├── view.py
└── assets/
    └── (grafo.png será salvo aqui)
```

> A pasta `assets/` pode ser criada automaticamente pelo próprio `view.py`, mas você também pode criar manualmente no repositório.

### 2.3. Executando o algoritmo principal (`main.py`)
Você roda o programa passando a descrição do grafo via entrada padrão (stdin).

Exemplo no terminal (Linux/Mac/WSL/PowerShell):

```bash
python3 main.py << EOF
U
4 4
0 1
1 2
2 3
0 2
EOF
```

#### Explicando essa entrada:
- `U` → grafo NÃO direcionado.
- `4 4` → 4 vértices (0..3) e 4 arestas.
- Linhas seguintes são as arestas:
  - `0 1`
  - `1 2`
  - `2 3`
  - `0 2`

#### Saída possível:
```text
CAMINHO HAMILTONIANO ENCONTRADO:
0 -> 1 -> 2 -> 3
```

Se não houver caminho Hamiltoniano:
```text
NAO EXISTE CAMINHO HAMILTONIANO
```

### 2.4. Execução interativa
Você também pode rodar e digitar manualmente:

```bash
python3 main.py
```

E depois digitar (ou colar):

```text
D
3 3
0 1
1 2
0 2
```

Em um grafo direcionado (`D`), a aresta `0 1` significa **somente** `0 -> 1`.

---

## 3. Relatório técnico

### 3.1. Análise da complexidade computacional

#### 3.1.1. Classes P, NP, NP-Completo e NP-Difícil

- **P**:  
  Problemas de decisão que podem ser resolvidos em tempo polinomial por um algoritmo determinístico.

- **NP**:  
  Problemas de decisão para os quais, se alguém te der uma solução candidata, você consegue **verificar** se ela é válida em tempo polinomial.

- **NP-Completo**:  
  Problemas que são:
  1. Estão em NP.
  2. São tão difíceis quanto qualquer problema em NP (ou seja, qualquer problema em NP pode ser reduzido a eles em tempo polinomial).

- **NP-Difícil (NP-Hard)**:  
  Problemas pelo menos tão difíceis quanto os NP-Completo, mas que não precisam estar em NP (podem não ser problemas de decisão, por exemplo problemas de otimização).

---

#### 3.1.2. Em qual classe está o problema do Caminho Hamiltoniano?

O problema que estamos resolvendo é:

> "Dado um grafo G, existe um caminho que visita todos os vértices exatamente uma vez?"

Esse é o **Problema do Caminho Hamiltoniano de decisão**.

- Ele está em **NP**, porque:
  - se alguém fornece um caminho candidato, conseguimos checar rapidamente:
    - se ele visita todos os vértices exatamente uma vez,
    - e se cada par consecutivo de vértices tem aresta válida.

- Ele é **NP-Completo**:
  - é tão difícil quanto qualquer problema em NP;
  - não existe algoritmo conhecido que sempre resolva em tempo polinomial (a menos que P = NP).

Logo:
- Caminho Hamiltoniano (decisão) ∈ NP-Completo.
- Isso implica que ele não está em P (a menos que P = NP).
- Por ser NP-Completo, ele também é NP-Difícil, mas a classificação mais precisa é NP-Completo.

---

#### 3.1.3. Relação com o Problema do Caixeiro Viajante (TSP)

O TSP versão decisão pergunta:

> "Existe um ciclo que passa por todas as cidades exatamente uma vez e tem custo total ≤ K?"

Se você modelar vértices como cidades e custos das arestas como distâncias, encontrar um Caminho Hamiltoniano vira muito parecido com perguntar se existe um tour válido passando em todos os vértices sem repetir.  
As reduções entre esses problemas mostram que:
- TSP (decisão) é NP-Completo.
- Caminho Hamiltoniano (decisão) também é NP-Completo.

Eles são problemas da mesma família de dificuldade.

---

### 3.2. Análise da complexidade assintótica de tempo

Agora vamos olhar o algoritmo implementado em `encontrar_caminho_hamiltoniano`.

#### 3.2.1. Ideia geral de custo

O algoritmo faz:
1. Para cada vértice possível como início:
2. Executa uma busca em profundidade recursiva (backtracking) tentando montar um caminho que visita todos os vértices exatamente uma vez.

O backtracking vai tentando construir uma permutação válida de todos os vértices.  
No pior caso, isso significa testar muitas ordens diferentes de visita.

#### 3.2.2. Custo aproximado

No pior cenário:
- a busca tenta praticamente todas as permutações possíveis dos `n` vértices,
- o que custa aproximadamente `n!` tentativas.

Além disso, em cada passo a função percorre vizinhos do vértice atual, o que pode custar até `O(n)` em grafos densos.  
Mas esse fator multiplicativo não muda a ordem de grandeza dominante.

Assim:
- **Complexidade de tempo no pior caso:** `O(n!)`.

Esse resultado já era esperado, porque o problema do Caminho Hamiltoniano é NP-Completo.

#### 3.2.3. Como essa complexidade foi determinada

Método usado:
- Contagem combinatória de quantas sequências possíveis de vértices podem ser exploradas.
- Assumimos um grafo denso (ou seja, quase sempre há aresta entre os vértices), então o algoritmo não consegue "podar" muita coisa cedo.
- Isso leva a uma busca quase exaustiva de permutações → `n!`.

---

### 3.3. Aplicação do Teorema Mestre

O **Teorema Mestre** resolve recorrências do tipo:

```text
T(n) = a * T(n/b) + f(n)
```

onde o problema é dividido em subproblemas de tamanho proporcional (`n/b`) e depois combinado.

Exemplos clássicos: Merge Sort, Busca Binária.

Nosso algoritmo de backtracking NÃO segue essa forma.  
Ele está mais para:

```text
T(n) ≈ n * T(n-1)
```

porque a cada passo escolhemos o próximo vértice entre os que sobraram.

Isso não é uma recorrência de divisão e conquista; é uma recorrência de enumeração de permutações.

Portanto:
- **Não é apropriado aplicar o Teorema Mestre** para analisar esse algoritmo.
- O Teorema Mestre não resolve recorrências que levam a `n!`.

---

### 3.4. Análise dos casos de complexidade

#### 3.4.1. Melhor caso

O melhor caso acontece quando:
- Logo no primeiro vértice inicial testado,
- Em cada passo da recursão existe exatamente um vizinho válido ainda não visitado,
- E isso constrói um caminho Hamiltoniano direto, sem precisar voltar (sem backtracking real).

Nesse cenário:
- A recursão desce por `n` níveis,
- Em cada nível, iterar pelos vizinhos custa no máximo `O(n)`.

Então, no melhor caso:
- **Tempo ≈ `O(n²)`** (ou `O(n * d)` se `d` for o grau médio de cada vértice).

Esse é um caso extremamente otimista.

#### 3.4.2. Caso médio

O caso médio prático (intuitivamente, em muitos grafos aleatórios densos):
- O algoritmo ainda precisa tentar várias escolhas erradas antes de achar um caminho correto,
- Ele faz um pouco de backtracking, mas não explora literalmente TODAS as permutações.

Mesmo assim, o custo ainda cresce exponencialmente/fatorial com `n`.  
Então o caso médio ainda é considerado não viável para valores grandes de `n`.

#### 3.4.3. Pior caso

No pior caso:
- Ou não existe caminho Hamiltoniano,
- Ou ele só é encontrado depois de testar quase todas as permutações possíveis.

Isso leva ao custo:
- **Pior caso: `O(n!)`.**

#### 3.4.4. Impacto prático

- Para `n` pequeno (tipo `n <= 12` ou `n <= 15`), ainda dá pra rodar esse algoritmo em tempo aceitável em máquina comum.
- Para grafos grandes, o tempo explode rapidamente.
- Isso ilustra por que problemas NP-Completo são considerados "intratáveis" em larga escala sem heurísticas ou aproximações.

---

## 4. Visualização do Caminho Hamiltoniano

Além do algoritmo em `main.py`, este projeto também fornece um script `view.py` para visualizar o grafo e destacar o Caminho Hamiltoniano encontrado.

### 4.1. O que o `view.py` faz

1. Lê o grafo da entrada padrão (mesmo formato do `main.py`).
2. Executa o algoritmo de busca de Caminho Hamiltoniano (reutilizando `encontrar_caminho_hamiltoniano`).
3. Constrói um grafo usando a biblioteca `networkx`:
   - `networkx.Graph()` para grafos não direcionados.
   - `networkx.DiGraph()` para grafos direcionados.
4. Desenha o grafo usando `matplotlib`:
   - Todos os nós e arestas originais aparecem.
   - Cada nó recebe um rótulo (0, 1, 2, ...).
   - As arestas que pertencem ao Caminho Hamiltoniano são destacadas com cor e espessura maiores.
5. Exporta a visualização final como imagem PNG em `assets/grafo.png`.

Isso atende aos requisitos do exercício:
- Desenhar o grafo original completo.
- Destacar o Caminho Hamiltoniano.
- Gerar uma imagem para colocar no repositório.

### 4.2. Dependências para visualização

Antes de rodar `view.py`, instale as bibliotecas necessárias:

```bash
pip install networkx matplotlib
```

- `networkx` é usada para modelar o grafo e desenhá-lo.
- `matplotlib` é usada para renderizar e salvar a figura em PNG.

### 4.3. Estrutura básica do `view.py` (resumo)

```python
import os
import networkx as nx
import matplotlib.pyplot as plt
from main import encontrar_caminho_hamiltoniano

# 1. Ler o grafo da stdin (tipo D/U, n, m, e lista de arestas)
# 2. Construir lista de adjacência para passar ao algoritmo
# 3. Rodar encontrar_caminho_hamiltoniano(adj, n)
# 4. Criar um Graph() ou DiGraph() em networkx e adicionar nós/arestas
# 5. Desenhar:
#    - Arestas normais em cinza
#    - Arestas do caminho Hamiltoniano em vermelho e mais grossas
# 6. Salvar em assets/grafo.png via plt.savefig(...)
```

Ou seja: o `view.py` não só te mostra visualmente como também já gera a imagem final pronta para commit.

### 4.4. Como gerar a imagem do grafo

Exemplo de uso (mesmo grafo do exemplo anterior):

```bash
python3 view.py << EOF
U
4 4
0 1
1 2
2 3
0 2
EOF
```

Após rodar:
- O terminal vai dizer se encontrou um Caminho Hamiltoniano (por exemplo: `0 -> 1 -> 2 -> 3`).
- Um arquivo `assets/grafo.png` será criado contendo:
  - Todos os nós e rótulos.
  - Todas as arestas originais do grafo.
  - As arestas que pertencem ao Caminho Hamiltoniano destacadas em vermelho e mais largas.
  - Setas (arrows) aparecem automaticamente se o grafo for direcionado.

Inclua a pasta `assets/` e o arquivo `assets/grafo.png` no seu commit do GitHub.

### 4.5. Exemplo visual (descrição)

O PNG gerado (`assets/grafo.png`) deve ter:

- Nós desenhados como círculos brancos com contorno preto e o número do vértice no centro.
- Arestas padrão em cinza.
- Arestas que fazem parte do Caminho Hamiltoniano em vermelho e com largura maior (destaque).
- Se o grafo for direcionado, as setas indicam o sentido entre os vértices.

Esse print é o que você pode colocar como evidência no relatório / README ou no PDF de entrega.

---

## 5. Conclusão

- O projeto implementa um resolvedor de Caminho Hamiltoniano usando backtracking.
- O problema do Caminho Hamiltoniano, na forma de decisão, é **NP-Completo**.
- O algoritmo tem custo de tempo `O(n!)` no pior caso, o que é esperado para esse tipo de problema.
- O Teorema Mestre não se aplica ao tempo desse algoritmo, pois não é um caso clássico de divisão e conquista.
- Foi adicionada uma camada de visualização (`view.py`) que:
  - usa `networkx` e `matplotlib`,
  - gera uma imagem destacando o Caminho Hamiltoniano,
  - salva essa imagem em `assets/grafo.png`,
  - e permite incluir a figura no repositório e no relatório final.
