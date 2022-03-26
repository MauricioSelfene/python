def divisor(num):
    divisor = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisor.append(i)
    return divisor        

def run():
    num = int(input("Ingresa un numero: "))
    print(divisor(num))
    print("termino mi programa")
    

if __name__ == '__main__':
    run()


'''
Utilizacion de debugging de Vscode iniciando un error en el ciclo if de el modulo de i es igual a 1
cuando debiera ser 0
'''