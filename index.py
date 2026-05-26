#botando bglh de save pra nao perdee o progresso d joguin(da uma nota extra prof, foi impossivel aprender isso aq mas consegui ;(   )
from rich import print
import time
import random
import json
import os

ARQUIVO_SAVE = "save_fundamentalism.json"

def carregar_progresso():
    if not os.path.exists(ARQUIVO_SAVE):
        return {"finais_vistos": []}
    try:
        with open(ARQUIVO_SAVE, "r") as f:
            return json.load(f)
    except:
        return {"finais_vistos": []}

def salvar_progresso(dados):
    with open(ARQUIVO_SAVE, "w") as f:
        json.dump(dados, f, indent=4)

progresso = carregar_progresso()

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    finais_vistos = progresso["finais_vistos"]
#menu do jogokk    
    print("="*45)
    print("           THE FUNDAMENTALISM")
    print("="*45)
    
    nome_prota = input("NOME DO DETETIVE: ").strip().upper()
    if not nome_prota: nome_prota = "DETETIVE"

    print(f"\n{nome_prota}, ESCOLHA SUA ESPECIALIDADE:")
    print("1 - INVESTIGADOR (MAIS PISTAS)")
    print("2 - NEGOCIADOR (MAIS LÁBIA)")

    if len(finais_vistos) >= 4:
        print("3 - ATIRADOR DE ELITE (LIBERADO)")
    else:
        print(f"3 - [BLOQUEADO] ({len(finais_vistos)}/4 FINAIS)")

    classe = input("\n> ")
#bglh de classe pq tem q ter copisa de rpg
    estresse_elias = 50
    precisao = 50
    bonus_fala = 1.0

    if classe == "1":
        investigacoes = 4
        estresse_elias = 60
    elif classe == "2":
        investigacoes = 2
        bonus_fala = 0.5
    elif classe == "3" and len(finais_vistos) >= 4:
        investigacoes = 2
        precisao = 95
    else:
        investigacoes = 2

    pista_desenhos = False
    pista_manifesto = False
    pista_policial = False
#aqui começa o jogo memo
    print(f"\n--- {nome_prota} ENTRA NO APARTAMENTO ---")
    time.sleep(1)

    while investigacoes > 0:
        print(f"\nAÇÕES: {investigacoes} | 1-QUARTO | 2-MESA | 3-FALAR COM GUARDA")
        esc = input("> ")
        
        if esc == "1" and not pista_desenhos:
            print("\nVocê encontra os desenhos da menina. Elias os mantinha na parede.")
            pista_desenhos = True
            investigacoes -= 1
        elif esc == "2" and not pista_manifesto:
            print("\nO manifesto de Elias está aberto na mesa. Ele acredita em purificação.")
            pista_manifesto = True
            investigacoes -= 1
        elif esc == "3" and not pista_policial:
            print("\nO policial avisa que Elias nunca disparou uma arma antes hoje.")
            pista_policial = True
            investigacoes -= 1
        else:
            print("\nNada novo por aqui, porra.")
        time.sleep(0.5)

    print(f"\n[RÁDIO]: '{nome_prota}! ELIAS ESTÁ NO TERRAÇO! ELE VAI PULAR!'")
    time.sleep(1.5)
#aqui que vai rolar o bglh de confronto com o eeliaszao agora o pau vai torakkkkkk   
    print("\n--- O TERRAÇO ---")
    finalizado = False
    tag = ""

    while not finalizado:
        print(f"\nESTADO MENTAL DE ELIAS: {estresse_elias}%")
        
        if estresse_elias > 80:
            print(f"Elias está tremendo violentamente. A menina grita por ajuda.")
        
        print(f"1 - '{nome_prota}: Elias, solte ela. Vamos conversar como homens.'")
        print(f"2 - '{nome_prota}: VOCÊ É UM MERDA, ELIAS! ACABA LOGO COM ISSO!'")
        if pista_desenhos: print(f"3 - (PISTA) {nome_prota}: 'Eu vi os desenhos que você guardou...'")
        if pista_manifesto: print(f"4 - (PISTA) {nome_prota}: 'Seu manifesto é uma mentira, Elias!'")
        
        fala = input("\nSUA ESCOLHA > ")

        if fala == "1":
            print(f"\n{nome_prota}: 'Eu sei que você não quer fazer isso, Elias. Me escuta.'")#codigo chato
            time.sleep(1)
            if estresse_elias > 65:
                print("ELIAS: 'VOCÊ NÃO SABE DE NADA! O MUNDO PRECISA DISSO!'")
            else:
                print("ELIAS: '...Eu não tive escolha. Eles me forçaram a acreditar nisso.'")
            estresse_elias -= (10 * bonus_fala)
        elif fala == "2":
            print(f"\n{nome_prota}: 'Você é um fraco, Elias! Usa uma criança porque tem medo!'")
            time.sleep(1)
            print("ELIAS: 'FRACO?! EU VOU TE MOSTRAR O QUE UM HOMEM COM FÉ PODE FAZER!'")
            estresse_elias += (25 * bonus_fala)
        elif fala == "3" and pista_desenhos:
            print(f"\n{nome_prota}: 'Elias, os desenhos... você se importa com ela. Eu vi.'")
            time.sleep(1)
            print("ELIAS: 'Eles são a única coisa pura que restou... por que eu faria isso?'")
            estresse_elias -= 35
            pista_desenhos = False
        elif fala == "4" and pista_manifesto:
            print(f"\n{nome_prota}: 'Eu li seu manifesto. É o delírio de um homem doente.'")
            time.sleep(1)
            print("ELIAS: 'DELÍRIO? É A VERDADE! Mas... e se eu li errado?'")#foi muito insuportavel fazer essee codigo(nao de dificil e sim de entediante msm pls me da nota boa prof)
            estresse_elias -= 30
            pista_manifesto = False

        if estresse_elias <= 10:
            print(f"\nElias larga a arma e cai de joelhos. {nome_prota} consegue resgatar a menina.")
            tag = "bom"
            finalizado = True
        elif estresse_elias >= 100:
            print(f"\nO surto de Elias é total. Ele pula da borda carregando a criança.")
            tag = "tragico"
            finalizado = True
        elif estresse_elias >= 65:
            print(f"\nELIAS ESTÁ NA BEIRA! {nome_prota}, DECIDA AGORA:")
            print("1 - Se jogar contra Elias")
            print("2 - Atirar para matar")
            dec = input("> ")
            if dec == "1":
                print(f"\n{nome_prota} corre e empurra Elias. A menina fica no terraço, mas {nome_prota} e Elias caem.")
                tag = "sacrificio"
                finalizado = True
            elif dec == "2":
                if random.randint(1, 100) <= precisao:
                    print(f"\nO disparo de {nome_prota} atinge a cabeça de Elias. A menina está salva.")
                    tag = "frieza"
                else:
                    print(f"\nO tiro acerta o ombro de Elias. No susto, ele despenca com a menina.")
                    tag = "carnificina"
                finalizado = True

    if tag not in progresso["finais_vistos"]:
        progresso["finais_vistos"].append(tag)
        salvar_progresso(progresso)
        print(f"\n[SISTEMA]: MEMÓRIA DE DESFECHO '{tag.upper()}' SALVA.")

    time.sleep(1)
    jogar_denovo = input(f"\nVOCÊ DESEJA JOGAR NOVAMENTE? {nome_prota} (S/N): ").strip().upper()
    if jogar_denovo != "S":
        print("\nENCERRANDO O CASO...")
        time.sleep(1)
        break