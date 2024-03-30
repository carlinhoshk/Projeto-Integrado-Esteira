import random
from tqdm import tqdm
from time import sleep
import keyboard

def progresso():
    for progresso in tqdm(range(0,100)):
        if keyboard.is_pressed('x'):
            print("   Parando Sistema...")
            continuar()
        sleep(0.01)

def balança():
    global peso_minimo 
    novo_peso_minimo = float(input("Insira o novo peso mínimo desejado em gramas: "))
    peso_minimo = novo_peso_minimo
    return peso_minimo


## Tirando codigo desnessesario, removendo funcao .lower e adicionando input em maisculo 
def continuar():
    while True:
        print ('Limpe o terminal...')
        resposta = input("Pressione 'C' para continuar, 'S' para sair ou 'B' para configurar a balança ")
        if resposta == 'C':
            break
        elif resposta =='S':
            print ("Encerrando sistema...")
            exit()
        elif resposta == 'B':
            balança()
        else:
            print("Opção inválida, tente novamente!")

print ("   PARA PARAR O SISTEMA, APERTE E SEGURE O BOTÃO DE EMERGENCIA X   ")

loteap = 0
loteai = 0
lotebp = 0
lotebi = 0
lotec = 0

## adotando padrao de snake_case
peso_minimo = float(100)

L = ['A', 'B']

print("   SISTEMA INICIANDO...   ")
limite = int(input(" POR FAVOR, DIGITE QUAL SERÁ LIMITE DE PRODOUTOS DE CADA AREÁ: "))


while True:
    if loteap >= limite or loteai >= limite or lotebp >= limite or lotebi >= limite or lotec >= limite:
        print("AVISO: UM DOS LOTES ATINGIU O SEU LIMITE DE ",limite," CARGAS.")
        if loteap >= limite:
            print("Lote A 2 atingiu o limite.")
        if loteai >= limite:
            print("Lote A 1 atingiu o limite.")
        if lotebp >= limite:
            print("Lote B 2 atingiu o limite.")
        if lotebi >= limite:
            print("Lote B 1 atingiu o limite.")
        if lotec >= limite:
            print("Lote C atingiu o limite.")
        
        resposta = input("Caso o lote for esvaziado, aperte 1: ")
        if resposta == '1':
            if loteap >= limite:
                loteap = 0
            if loteai >= limite:
                loteai = 0
            if lotebp >= limite:
                lotebp = 0
            if lotebi >= limite:
                lotebi = 0
            if lotec >= limite:
                lotec = 0
            print("Lote esvaziado,Continuando...")
        else:
            break
    
    letra = random.choice(L)
    numero = random.randrange(10, 99)
    tipo = ''
    lote = ''

    etiqueta = letra + str(numero)
    print("\n lote da etiqueta: \n", etiqueta)
    
 # BARRA DE PROGRESSO 1
    print("    A CAMINHO DA SEPARAÇÃO >>>>    ")
    progresso()
    if letra == 'A':
        if numero % 2 == 0:
            tipo = '2'
            lote = 'A'
        else:
            tipo = '1'
            lote = 'A'
    elif letra == 'B':
        if numero % 2 == 0:
            tipo = '2'
            lote = 'B'
        else:
            tipo = '1'
            lote = 'B'

    print("\n A carga está a caminho do lote \n" , lote, tipo)

    # peso = float(input("Peso: "))  # Balança da o peso em gramas
    peso = random.randrange(99,15000) #Numero aleatorio simulando a balança

 # BARRA DE PROGRESSO 2
    
    print("    A CAMINHO DO LOTE >>>>    ")
    progresso()
    if peso > peso_minimo:
        if lote == 'A' and tipo == '2':
            loteap += 1
        elif lote == 'A' and tipo == '1':
            loteai += 1
        elif lote == 'B' and tipo == '2':
            lotebp += 1
        elif lote == 'B' and tipo == '1':
            lotebi += 1
        print("Produto de etiqueta ",etiqueta," Chegou ao lote",lote,tipo)
    else:
        print("Peso minimo da balança nao atingido")
        lotec = lotec + 1
        print("Produto enviado ao lote C para verificação ")
