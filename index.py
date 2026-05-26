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

# Loop principal do jogo todo
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    finais_vistos = progresso["finais_vistos"]
    
    print("="*45)
    print("         THE FUNDAMENTALISM")
    print("="*45)
    
    nome_prota = input("NOME DO DETETIVE: ").strip().upper()
    if not nome_prota: nome_prota = "DETETIVE"

    # --- VALIDAÇÃO DA CLASSE ---
    while True:
        print(f"\n{nome_prota}, ESCOLHA SUA ESPECIALIDADE:")
        print("1 - INVESTIGADOR (MAIS PISTAS)")
        print("2 - NEGOCIADOR (MAIS LÁBIA)")

        if len(finais_vistos) >= 4:
            print("3 - ATIRADOR DE ELITE (LIBERADO)")
        else:
            print(f"3 - [BLOQUEADO] ({len(finais_vistos)}/4 FINAIS)")

        classe = input("\n> ").strip()

        if classe == "1":
            investigacoes = 3
            estresse_elias = 60
            bonus_fala = 1.0
            precisao = 50
            break
        elif classe == "2":
            investigacoes = 2
            bonus_fala = 0.5
            estresse_elias = 50
            precisao = 50
            break
        elif classe == "3" and len(finais_vistos) >= 4:
            investigacoes = 2
            precisao = 95
            estresse_elias = 50
            bonus_fala = 1.0
            break
        else:
            print("[bold red]OPÇÃO INVÁLIDA, RECRUTA! DIGITE UM NÚMERO CORRESPONDENTE ÀS OPÇÕES DISPONÍVEIS.[/bold red]")

    pista_desenhos = False
    pista_manifesto = False
    pista_policial = False

    print(f"\n--- {nome_prota} ENTRA NO APARTAMENTO ---")
    time.sleep(1)

    # --- VALIDAÇÃO DA INVESTIGAÇÃO ---
    while investigacoes > 0:
        print(f"\nAÇÕES RESTANTES: {investigacoes} | 1-QUARTO | 2-MESA | 3-FALAR COM GUARDA")
        esc = input("> ").strip()
        
        if esc == "1" and not pista_desenhos:
            print("\n[bold gray]Você encontra os desenhos da menina. Elias os mantinha na parede.")
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
        elif esc in ["1", "2", "3"]:
            print("\nVocê já revirou isso aqui e não achou mais nada útil.")
        else:
            print("[bold yellow]COMANDO INVÁLIDO! FOQUE NA INVESTIGAÇÃO (USE 1, 2 OU 3).[/bold yellow]")
        time.sleep(0.5)

    print(f"\n[RÁDIO]: '{nome_prota}! ELIAS ESTÁ NO TERRAÇO! ELE VAI PULAR!'")
    time.sleep(1.5)

    print("\n--- O TERRAÇO ---")
    finalizado = False
    tag = ""

    # --- VALIDAÇÃO DO CONFRONTO ---
    while not finalizado:
        print(f"\nESTADO MENTAL DE ELIAS: {int(estresse_elias)}%")
        
        opcoes_validas = ["1", "2"]
        print(f"1 - '{nome_prota}: Elias, solte ela. Vamos conversar.'")
        print(f"2 - '{nome_prota}: VOCÊ É UM MERDA, ELIAS!'")
        
        if pista_desenhos: 
            print(f"3 - (PISTA) 'Eu vi os desenhos...'")
            opcoes_validas.append("3")
        if pista_manifesto: 
            print(f"4 - (PISTA) 'Seu manifesto é uma mentira!'")
            opcoes_validas.append("4")
        
        fala = input("\nSUA ESCOLHA > ").strip()

        if fala not in opcoes_validas:
            print("[bold red]VOCÊ SE ENGASGOU NAS PALAVRAS! ESCOLHA UMA OPÇÃO VÁLIDA![/bold red]")
            continue

        if fala == "1":
            print(f"\n{nome_prota}: 'Eu sei que você não quer fazer isso, Elias.'")
            if estresse_elias > 65:
                print("ELIAS: 'VOCÊ NÃO SABE DE NADA!'")
            else:
                print("ELIAS: '...Eu não tive escolha.'")
            estresse_elias -= (10 * bonus_fala)
        elif fala == "2":
            print(f"\n{nome_prota}: 'Você é um fraco, Elias!'")
            estresse_elias += (25 * bonus_fala)
        elif fala == "3":
            print(f"\n{nome_prota}: 'Elias, os desenhos... você se importa com ela.'")
            estresse_elias -= 35
            pista_desenhos = False
        elif fala == "4":
            print(f"\n{nome_prota}: 'Eu li seu manifesto. É o delírio de um homem doente.'")
            estresse_elias -= 30
            pista_manifesto = False

        # Checagem de Finais
        if estresse_elias <= 10:
            print(f"\nElias larga a arma. {nome_prota} resgatou a menina.")
            tag = "bom"
            finalizado = True
        elif estresse_elias >= 100:
            print(f"\n[bold red]Elias pulou com a criança.[/bold red]")
            tag = "tragico"
            finalizado = True
        elif estresse_elias >= 65:
            # --- VALIDAÇÃO DA DECISÃO FINAL ---
            while True:
                print(f"\nELIAS ESTÁ NA BEIRA! {nome_prota}, DECIDA AGORA:")
                print("1 - Se jogar contra Elias")
                print("2 - Atirar para matar")
                dec = input("> ").strip()
                if dec == "1":
                    print(f"\nVocê caiu com ele, mas salvou a menina.")
                    tag = "sacrificio"
                    finalizado = True
                    break
                elif dec == "2":
                    if random.randint(1, 100) <= precisao:
                        print(f"\nO disparo foi certeiro. Elias caiu morto.")
                        tag = "frieza"
                    else:
                        print(f"\nVocê errou o tiro fatal. Ambos caíram.")
                        tag = "carnificina"
                    finalizado = True
                    break
                else:
                    print("[bold red]NÃO HÁ TEMPO PARA HESITAR! 1 OU 2![/bold red]")

    # Sistema de Save
    if tag not in progresso["finais_vistos"]:
        progresso["finais_vistos"].append(tag)
        salvar_progresso(progresso)
        print(f"\n[SISTEMA]: FINAL '{tag.upper()}' REGISTRADO.")

    # --- VALIDAÇÃO DE REPLAY ---
    while True:
        jogar_denovo = input(f"\nJOGAR NOVAMENTE? (S/N): ").strip().upper()
        if jogar_denovo in ["S", "N"]:
            break
        print("[bold red]DIGITE 'S' PARA SIM OU 'N' PARA NÃO.[/bold red]")
    
    if jogar_denovo == "N":
        print("\nENCERRANDO...")
        break