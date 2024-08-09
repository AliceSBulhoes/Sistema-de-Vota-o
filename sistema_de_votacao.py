import datetime
h = []
z = []
l = []
n = []
v = []
votos = [h,z,l,n,v]

continuar = "S"


def menu():
    menu = input(f"Bem vindo a votação! Digite uma das opções a seguir \n\tH - Vote no Huguinho \n\tZ - Vote no Zezinho \n\tL - Vote no Luizinho \n\tN - Vote nulo \n\tS- Termina a votação\n").upper()
    return menu


def votar(voto):
    if voto == "H":
        h.append("H")
    elif voto == "Z":
        z.append("Z")
    elif voto == "L":
        l.append("L")
    elif voto == "N":
        n.append("N")
    elif voto == "S":
        return "N"
    else:
        v.append("I")
    print("Voto Computado! \n")


def contarVotos():

    for i in range(0,len(votos)):
        if i == 0:
            print(f"Votos dos participantes!\nHuguinho:{len(votos[i])}")
        elif i == 1:
            print(f"\nZezinho:{len(votos[i])}")
        elif i == 2:
            print(f"\nLuizinho:{len(votos[i])}")
        elif i == 3:
            print(f"\nNulos:{len(votos[i])}")
        elif i == 4:
            print(f"\nInválidos:{len(votos[i])}")

            
def vencedor():
    vencedor = 0
    vencedorNome = ""
    for i in range(0,len(votos)):
        for j in votos:
            if i == 0:
                vencedor = len(j)
                vencedorNome = "Huguinho"
                break
            if vencedor < len(j):
                vencedor = len(j)
                if i == 1:
                    vencedorNome = "Zezinho"
                elif i == 2:
                    vencedorNome = "Luizinho"
            elif vencedor == len(j):
                vencedorNome = "Empate! Não foi possível realizar a votação :C"

    if vencedor == 0:
        print("Não houve votos!")
    elif vencedorNome != "Empate! Não foi possível realizar a votação :C":
        print(f"\nO vencedor é {vencedorNome} com {vencedor} votos!")
    else:
        print(vencedorNome)


def resultado():
    contarVotos()
    vencedor()


while continuar == "S":
    opcao = menu()
    if opcao == "S":
        break
    else:
        votar(opcao)

resultado()
