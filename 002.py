import random

print("Seja - bem vindo ao Ligrinho!")

aleatório = random.randint(1,4)
aleatório2 = random.randint(1,4)
aleatório3 = random.randint(1,52)
saldo_aleatório = random.randint(100,200)
saldo_aleatório_derrota = random.randint(1,100)
saldo_aleatório_cavalo = random.randint(1,100)
saldo = 0
carta = 0

def continuacao_jogo():
    saldo = int(input("Seu saldo atual: "))
    voltar = "y"

    aleatório3 = random.randint(1,52)
    print('-'*30)
    print("JOGO DECISIVO")
    print('-'*30)
    print("\nNeste jogo ha 52 cartas espalhadas na mesa e voce tera que escolher a carta que eu estou pensando")
    carta = int(input("\nEscolha a carta: "))
    print("A carta que eu estava pensando foi a ",aleatório3)

    if carta == aleatório3:
        print("Voce ganhou o jogo meus parabens")
    elif carta != aleatório3:
        saldo = saldo - saldo
        if carta != aleatório3 and saldo == 0:
            print("Voce perdeu, que decepcao. Seu saldo e de ",saldo)
            while voltar != "S" or voltar != "s" or voltar != "N" or voltar != "n":
                voltar = str(input("\nDeseja tentar novamente?(S/N): "))
                if voltar == "S" or voltar == "s":
                    main()
                elif voltar == "N" or voltar == "n":
                    print("\nJogo finalizado")

def jogo():

    aleatório2 = random.randint(1,4)
    saldo_aleatório_cavalo
    voltar = "x"

    saldo = int(input("Seu saldo atual: "))

    print("Corrida dos cavalos:")
    print("\nEscolha seu cavalo")
    print("\n[1] - Cavalo azul")
    print("\n[2] - Cavalo vermelha")
    print("\n[3] - Cavalo verde")
    print("\n[4] - Cavalo rosa")
    cavalo = int(input("\nQual cavalo vai ganhar a corrida?: "))
    while cavalo < 1 or cavalo > 4:
        cavalo = int(input("\nQual cavalo vai ganhar a corrida?: "))
    print("\nO cavalo vencedor foi o ",aleatório2)
    if cavalo == aleatório2:
        saldo = saldo + 1000000
        print("Voce ganhou o jogo!! Agora esta milionario, seu saldo eh de ",saldo)
        continuacao_jogo()
        if cavalo != aleatório2:
            saldo = saldo - saldo_aleatório_cavalo
    elif cavalo != aleatório2 or saldo == 0:
        saldo = saldo - saldo_aleatório_cavalo
        print("Você perdeu ", saldo_aleatório_cavalo)
        print("Saldo de ",saldo)
        while voltar != "S" or voltar != "s" or voltar != "N" or voltar != "n":
            voltar = str(input("\nDeseja tentar novamente?(S/N): "))
            if voltar == "S" or voltar == "s":
                main()
            elif voltar == "N" or voltar == "n":
                print("\nJogo finalizado")
    elif cavalo != aleatório2 and saldo != 0:
        print("Vamos para o proximo jogo. Saldo de ",saldo)
        continuacao_jogo()

def main():

    aleatório = random.randint(1,4)

    saldo = int(input("Adicione seu saldo: "))

    print("Ok, seu saldo é de ",saldo)

    progredir = str(input("Deseja continuar?"))
    while progredir != "sim" and progredir != "Sim":
        progredir = str(input("Deseja continuar?"))

    if progredir == "sim" or progredir == "Sim":
        print("Competição de qual lagartixa vai ser atropelada por um caminhão da itaipava")
        print("\nEscolha sua lagartixa")
        print("\n[1] - Lagartixa azul")
        print("\n[2] - Lagartixa vermelha")
        print("\n[3] - Lagartixa verde")
        print("\n[4] - Lagartixa rosa")

        lagartixa = int(input("\nSelecione a lagartixa: "))
        while lagartixa < 1 or lagartixa >4:
            lagartixa = int(input("\nSelecione a lagartixa: "))
        print("\nA lagartixa atropelada foi a ",aleatório)

        if lagartixa != aleatório:
            print("Errou")
            print("Você perdeu ",saldo_aleatório_derrota," reais")
            saldo = saldo - saldo_aleatório_derrota
            print("Seu saldo é de ",saldo)
            jogo()

        elif lagartixa == aleatório:
            print("Acertou!!")
            print("Você ganhou ",saldo_aleatório)
            saldo = saldo + saldo_aleatório
            print("Seu saldo é de ", saldo)
            jogo()
    else:
      print("\nErro")

main()