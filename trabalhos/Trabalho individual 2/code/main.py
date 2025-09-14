import argparse
import random
import sys
from typing import List, Tuple


def maxmin_divide_conquer(arr: List[float], left: int, right: int) -> Tuple[float, float, int]:
    """
    Função recursiva que retorna (min, max, comparações) para arr[left:right+1].

    Base cases:
    - se left == right: um elemento, 0 comparações
    - se right == left + 1: dois elementos, 1 comparação

    Caso geral: divide o segmento em duas metades, resolve recursivamente e
    combina os resultados com 2 comparações (uma para os máximos e outra para
    os mínimos).
    """
    # Caso com um elemento
    if left == right:
        return arr[left], arr[left], 0

    # Caso com dois elementos
    if right == left + 1:
        # apenas 1 comparação para definir min e max
        if arr[left] <= arr[right]:
            return arr[left], arr[right], 1
        else:
            return arr[right], arr[left], 1

    # Caso geral: dividir em duas metades
    mid = (left + right) // 2

    min1, max1, c1 = maxmin_divide_conquer(arr, left, mid)
    min2, max2, c2 = maxmin_divide_conquer(arr, mid + 1, right)

    comparisons = c1 + c2

    # Combinar: 1 comparação para os máximos e 1 para os mínimos
    # comparar máximos
    comparisons += 1
    if max1 >= max2:
        overall_max = max1
    else:
        overall_max = max2

    # comparar mínimos
    comparisons += 1
    if min1 <= min2:
        overall_min = min1
    else:
        overall_min = min2

    return overall_min, overall_max, comparisons


def maxmin(arr: List[float]) -> Tuple[float, float, int]:
    """
    Wrapper que valida entrada e chama a função recursiva.
    Retorna (min, max, comparisons).
    """
    n = len(arr)
    if n == 0:
        raise ValueError("A sequência não pode ser vazia")
    return maxmin_divide_conquer(arr, 0, n - 1)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="MaxMin Select (divisão e conquista)")
    p.add_argument("values", nargs="*", help="lista de números (ex: 3 1 4 2)")
    p.add_argument("--random", "-r", type=int, help="gera n números aleatórios")
    p.add_argument("--seed", type=int, default=None, help="seed para gerador aleatório")
    return p.parse_args()


def main() -> int:
    args = parse_args()

    if args.random is not None:
        if args.random <= 0:
            print("--random deve ser um inteiro positivo")
            return 1
        if args.seed is not None:
            random.seed(args.seed)
        arr = [random.randint(-1000, 1000) for _ in range(args.random)]
    elif args.values:
        try:
            arr = [float(x) for x in args.values]
        except ValueError:
            print("Todos os valores devem ser números")
            return 1
    else:
        # leitura interativa se nenhum argumento for passado
        print("Forneça números como argumentos ou use --random N. Exemplo: python3 main.py 3 1 4 2")
        return 0

    print("Sequência:", arr)
    minimum, maximum, comps = maxmin(arr)
    print(f"Menor: {minimum}")
    print(f"Maior: {maximum}")
    print(f"Comparações realizadas: {comps}")

    # Verificação simples (checar com min()/max() do Python)
    assert minimum == min(arr), "Min incorrect"
    assert maximum == max(arr), "Max incorrect"

    return 0


if __name__ == "__main__":
    sys.exit(main())