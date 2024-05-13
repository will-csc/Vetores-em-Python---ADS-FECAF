#------- INSIRIR VALORES DENTRO DA VARIAVEIS ----------
qnt = int(input("Digite quantos valores seu vetor vai ter: \n"))
valores = []
valores_quadrado = []

for i in range(qnt):
    valores.append(float(input("Digite um número real: \n")))
    valores_quadrado.append(valores[i]*valores[i])
    
#------- MOSTRA VALORES ----------
print("\nOs valores inseridos foram: \n",valores,"\n")
print("O quadrado desses valores são: \n",valores_quadrado)