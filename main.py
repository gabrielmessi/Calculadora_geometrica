# Fórmulas para trabalhar com o quadrado
import math

def Area(L):
    return L**2

def Perimetro(L):
    return 4 * L

def Diagonal(L):
    return L * math.sqrt(2)

def Raio_inscrito(L):
    return L / 2

def Raio_circunscrito(L):
    return L * math.sqrt(2) / 2


# Fórmulas para trabalhar com o retângulo
def area(b, h):
    return b * h

def perimetro(b, h):
    return 2 * (b + h)

def diagonal(b, h):
    return math.sqrt(b**2 + h**2)


# Função para calcular
def calcular():

    while True:
        print("\n====MENU====")
        print("1- Trabalhar com quadrado.")
        print("2- Trabalhar com retângulo.")
        print("3- Sair.\n")

        try:
            escolha = int(input("O que gostaria de fazer? "))

            if escolha == 3:
                print("\nPrograma encerrado.")
                break

            # QUADRADO
            elif escolha == 1:

                while True:
                    print("\n====OPÇÕES====")
                    print("1- Medir área.")
                    print("2- Medir perímetro.")
                    print("3- Medir diagonal.")
                    print("4- Medir raio do círculo inscrito.")
                    print("5- Medir raio do círculo circunscrito.")
                    print("6- Voltar.\n")

                    try:
                        opcao = int(input("O que gostaria de fazer? "))

                        if opcao == 1:
                            L = float(input("\nQual a medida do lado? "))

                            if L <= 0:
                                print("Valor inválido.")
                                continue

                            print("\nA =", Area(L))

                        elif opcao == 2:
                            L = float(input("\nQual a medida do lado? "))

                            if L <= 0:
                                print("Valor inválido.")
                                continue

                            print("\nP =", Perimetro(L))

                        elif opcao == 3:
                            L = float(input("\nQual a medida do lado? "))

                            if L <= 0:
                                print("Valor inválido.")
                                continue

                            print(f"\nd = {Diagonal(L):.2f}")

                        elif opcao == 4:
                            L = float(input("\nQual a medida do lado? "))

                            if L <= 0:
                                print("Valor inválido.")
                                continue

                            print(f"\nr = {Raio_inscrito(L):.2f}")

                        elif opcao == 5:
                            L = float(input("\nQual a medida do lado? "))

                            if L <= 0:
                                print("Valor inválido.")
                                continue

                            print(f"\nR = {Raio_circunscrito(L):.2f}")

                        elif opcao == 6:
                            print("\nVoltando...")
                            break

                        else:
                            print("Opção inexistente.")

                    except ValueError:
                        print("Apenas valores numéricos.")


            # RETÂNGULO
            elif escolha == 2:

                while True:
                    print("\n====OPÇÕES====")
                    print("1- Medir área.")
                    print("2- Medir perímetro.")
                    print("3- Medir diagonal.")
                    print("4- Voltar.\n")

                    try:
                        opcao = int(input("O que gostaria de fazer? "))

                        if opcao == 1:
                            b = float(input("\nQual a medida da base? "))
                            h = float(input("Qual a medida da altura? "))

                            if b <= 0 or h <= 0:
                                print("Valor inválido.")
                                continue

                            print("\nA =", area(b, h))

                        elif opcao == 2:
                            b = float(input("\nQual a medida da base? "))
                            h = float(input("Qual a medida da altura? "))

                            if b <= 0 or h <= 0:
                                print("Valor inválido.")
                                continue

                            print("\nP =", perimetro(b, h))

                        elif opcao == 3:
                            b = float(input("\nQual a medida da base? "))
                            h = float(input("Qual a medida da altura? "))

                            if b <= 0 or h <= 0:
                                print("Valor inválido.")
                                continue

                            print(f"\nd = {diagonal(b, h):.2f}")

                        elif opcao == 4:
                            print("\nVoltando...")
                            break

                        else:
                            print("Opção inexistente.")

                    except ValueError:
                        print("Apenas valores numéricos.")

            else:
                print("Opção inexistente.")

        except ValueError:
            print("Apenas valores numéricos.")


calcular()
