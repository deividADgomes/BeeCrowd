qtde = int(input())

for i in range(qtde):

    dias = 0
    food = int(input())

    while food>1:
        metade = food/2
        food = food-metade
        dias = dias+1
        #print(food)
    print (str(dias)+ ' dias')    

