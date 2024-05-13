#---------- VETOR E VALORES -------------
vetor = [0]*10
for i in range(len(vetor)):
    print("Digite um número para posição ",i+1," do vetor") #Não coloquei 0 para nao confundir o usuario
    vetor[i] = int(input())
    
#--------- VERIFICAR QUAIS DELAS SÃO PARES -------------
for i in range(len(vetor)):
    if vetor[i] % 2 == 0:
        print("\nO vetor na posição:", i)
        print("Valor:", vetor[i])
        print("É um número par\n")