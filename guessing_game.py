import random

def jogar_brincadeira():
    print("Bem-vindo à brincadeira!")
    numero = random.randint(1, 100)
    tentativas = 0
    while True:
        palpite = int(input("Digite um número entre 1 e 100: "))
        tentativas += 1
        if palpite < numero:
            print("Muito baixo! Tente novamente.")
        elif palpite > numero:
            print("Muito alto! Tente novamente.")
        else:
            print(f"Parabéns, você adivinhou o número em {tentativas} tentativas!")
            break

jogar_brincadeira()
