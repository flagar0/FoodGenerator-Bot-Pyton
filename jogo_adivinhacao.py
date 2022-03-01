from random import randint
print("Bem  vindo  ao Jogo de Adivinhação")

aleatorio = randint(0, 10)
tentativas = True
tentativa = 1
# print(aleatorio)
while(tentativas):
    print("Tentativa", tentativa)
    resposta = input("Escreva um numero de 0 a 10: ")

    num = int(resposta)
    if(num < 0) or (num > 10):
        print("Digite um valor válido")
        continue

    if (num == aleatorio):
        print("Voce acertou!! Em {} tentativas \n".format(tentativa))
        tentativas = False
    else:
        print("Voce Errou :( \n")
        tentativa += 1
