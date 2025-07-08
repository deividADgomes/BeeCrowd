qtde = int(input())
for i in range(qtde):
	
	a,b = input().split()
	
	if b==a[-len(b):]:
		print("encaixa")
	else:
		print("nao encaixa")