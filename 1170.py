qtde = int(input())

for i in range(qtde):

    dias = 0
    comida = int(input())

    while comida>1:
        metade = comida/2
        comida = comida-metade
        dias = dias+1
        #print(comida)
    print (str(dias)+ ' dias')    

