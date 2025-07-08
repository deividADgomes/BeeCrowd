
qtde = int(input())

for o in range(qtde):
    i = int(input())
    aux = 1
    for a in range(i):
        aux*=2

    kg= aux //12000

   # while (12000<aux):
    #    aux-=12000
    #    kg+=1

    print(str(kg) + ' kg')