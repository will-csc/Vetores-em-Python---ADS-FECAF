
# -------- FUNÇÃO PEGAR X E Y -----------
def get_xy():
    x = int(input("Digite uma posição para X:\n"))
    y = int(input("Digite uma posição para Y:\n"))
    return [x,y]

#------ CRIA UM VETOR COM 18 POSIÇÕES ------
vetor = [0]*18
for i in range(18):
    print("Digite um numero para ser adicionado ao vetor: ")
    vetor[i] = int(input())
print("O números adicionados foram: \n", vetor, "\n")

#------ PEGA POSIÇÕES X E Y ------
lista_xy = get_xy()
while lista_xy[0] >= len(vetor) or lista_xy[1] >= len(vetor): # VERIFICA ERRO DE POSIÇÃO
    print("Digite uma posição de x e y que estejam de 0 até", len(vetor) - 1)
    lista_xy = get_xy()

soma = vetor[lista_xy[0]] + vetor[lista_xy[1]]
print("A soma da posição", lista_xy[0], "(",vetor[lista_xy[0]],
      ") e", lista_xy[1], "(",vetor[lista_xy[1]],") foi de: \n", soma)
