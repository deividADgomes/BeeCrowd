import math

while True:
    try:
        linha = input()
        if linha.strip() == "":
            continue

        n, l, c = map(int, linha.strip().split())
        palavras = input().strip().split()

        linhas = 1
        tamanho_linha = 0

        for palavra in palavras:
            if tamanho_linha == 0:
                tamanho_linha = len(palavra)
            elif tamanho_linha + 1 + len(palavra) <= c:
                tamanho_linha += 1 + len(palavra)
            else:
                linhas += 1
                tamanho_linha = len(palavra)

        paginas = math.ceil(linhas / l)
        print(paginas)

    except EOFError:
        break
