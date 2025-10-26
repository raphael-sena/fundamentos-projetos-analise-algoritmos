import re
import time

def encontrarSoma(str1, str2):
    # Garante que str1 seja o menor número
    if len(str1) > len(str2):
        str1, str2 = str2, str1

    resultado = ""
    n1, n2 = len(str1), len(str2)

    # Preenche com zeros à esquerda para igualar os tamanhos
    str1, str2 = str1.zfill(n2), str2.zfill(n2)

    vai_um = 0

    # Soma dígito por dígito da direita para a esquerda
    for i in range(n2 - 1, -1, -1):
        soma = int(str1[i]) + int(str2[i]) + vai_um
        resultado = str(soma % 10) + resultado
        vai_um = soma // 10

    # Se sobrou "vai um", adiciona no início
    if vai_um:
        resultado = str(vai_um) + resultado

    return resultado

def encontrarDiferenca(str1, str2):
    resultado = ""
    n1, n2 = len(str1), len(str2)

    # Preenche com zeros à esquerda para igualar os tamanhos
    str1, str2 = str1.zfill(n2), str2.zfill(n2)

    emprestimo = 0

    # Subtrai dígito por dígito da direita para a esquerda
    for i in range(n2 - 1, -1, -1):
        sub = int(str1[i]) - int(str2[i]) - emprestimo

        if sub < 0:
            sub += 10
            emprestimo = 1
        else:
            emprestimo = 0

        resultado = str(sub) + resultado

    return resultado


def removerZerosAEsquerda(s):
    padrao = "^0+(?!$)"  # Regex que remove zeros à esquerda, mas não remove se for só "0"
    s = re.sub(padrao, "", s)
    return s


def multiplicar(A, B): # +1
    # Caso base: se os números forem pequenos, multiplica diretamente
    if len(A) < 10 or len(B) < 10: # +1
        return str(int(A) * int(B)) # +1

    n = max(len(A), len(B)) # +1
    n2 = n // 2 # +1

    # Preenche os números com zeros à esquerda para igualar os tamanhos
    A = A.zfill(n) # +1
    B = B.zfill(n) # +1

    # Divide os números ao meio
    Al, Ar = A[:n2], A[n2:] # +1
    Bl, Br = B[:n2], B[n2:] # +1

    # Karatsuba: calcula os 3 produtos parciais recursivamente
    p = multiplicar(Al, Bl) # +1
    q = multiplicar(Ar, Br) # +1
    r = multiplicar(encontrarSoma(Al, Ar), encontrarSoma(Bl, Br)) # +1
    r = encontrarDiferenca(r, encontrarSoma(p, q)) # +1

    # Combina os resultados (p * 10^2m + r * 10^m + q)
    return removerZerosAEsquerda(encontrarSoma(encontrarSoma(p + '0' * (2 * n2), r + '0' * n2), q)) # +1


if __name__ == "__main__": # +1
    # Leitura dos números do teclado
    A = input("Digite o primeiro número: ").strip() # +1
    B = input("Digite o segundo número: ").strip() # +1

    # Medir o tempo de execução
    inicioKaratsuba = time.time() # +1

    resultadoKaratsuba = multiplicar(A, B) # +1

    fimKaratsuba = time.time() # +1

    # Mostrar o resultado e o tempo
    print(f"\nResultado Karatsuba: {resultadoKaratsuba}") # +1
    print(f"Tempo de execução: {fimKaratsuba - inicioKaratsuba:.6f} segundos") # +1

    inicioMultiplicaçãoNormal = time.time() # +1

    resultadoMultiplicaçãoNormal  = str(int(A) * int(B)) # +1

    fimMultiplicaçãoNormal = time.time() # +1

    # Mostrar o resultado e o tempo
    print(f"\nResultado Multiplicação Normal: {resultadoMultiplicaçãoNormal}") # +1
    print(f"Tempo de execução: {fimMultiplicaçãoNormal - inicioMultiplicaçãoNormal:.6f} segundos") # +1



