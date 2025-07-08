
num =str(input('Digite o número: '))
contrato =str(input('Digite o número do Contrato: '))
Lcontrato =list(contrato)
x = 0
contrato=''
9
for i in Lcontrato:
    if(i==num):
        Lcontrato[x]=""
    x+=1
contrato = ''.join(Lcontrato)
contrato = int(contrato)

print(contrato)
