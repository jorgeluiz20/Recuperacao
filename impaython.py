#Componentes: Amós, Edimael, Jorge, Luiz Fernando


from impaython_functions import *

print('BEM-VINDO AO IMPAYTHON')
player_name = input('INFORME SEU NOME: ')
cpu_name = 'JARVIS'
contador = 0
round = 0
if player_name.isalpha():
    print('###################################')
    print('# IMPAYTHON                       #')
    print('# Olá,', player_name,            '#')
    print('###################################')
    print('# 1 -> JOGAR                      #')
    print('# 2 -> VER RESULTADOS             #')
    print('# 3 -> SAIR                       #')
    print('###################################')
    opcao = int(input('Escolha uma opção: '))
    if opcao == 1:
        print('###################################')
        print('# IMPAYTHON                       #')
        print('# Olá', player_name,             '#')
        print('###################################')
        print('# 1 -> 3 ROUNDS                   #')
        print('# 2 -> 5 ROUNDS                   #')
        print('# 3 -> 9 ROUNDS                   #')
        print('# 4 <- VOLTAR AO MENU ANTERIOR    #')
        print('###################################')
        num_rounds = int(input('escolha uma opção: '))
        if num_rounds == 1:
            num_rounds = 3
        elif num_rounds == 2:
            num_rounds = 5
        elif num_rounds == 3:
            num_rounds = 9
        elif num_rounds == 4:
           pass
        else:
            print('Opcao invalida')
        cpu_ganha = 0
        player_ganha = 0
        while num_rounds > contador:
            round += 1
            print('###################################')
            print('# ROUND',round ,'de' ,num_rounds,'#')
            print('# Faça sua jogada                 #')
            print('###################################')
            player_number = int(input('Escolha um número de 1 a 10: '))
            print('###################################')
            print('# ROUND', round, 'de', num_rounds, '#')
            print('# 1 -> ÍMPAR                      #')
            print('# 2 -> PAR                        #')
            print('###################################')
            player_choice = int(input('Escolha uma opção:'))
            if player_choice == 1:
                player_choice = 'impar'
            elif player_choice == 2:
                player_choice = 'par'
            else:
                print('Opção inválida')
            generate_cpu_number()
            from random import randint
            cpu_number = randint(1, 11)
            soma = cpu_number + player_number
            get_round_winner(soma,player_choice)
            is_impar(cpu_number,player_number)
            get_winner_final(soma, player_choice, cpu_ganha, player_ganha)
            #print('voce:', player_ganha, 'Jarvis:', cpu_ganha)
            #record_results(player_name, num_rounds, generate_cpu_number, player_choice)
            contador +=1
    if opcao == 2:
        get_results(player_name)
    if opcao == 3:
        exit()
else:
    print('Digite corretamente seu nome.')
if cpu_ganha < player_ganha:
    print("Voce Ganhou o Jogo")
else:
    print('Jarvis Ganhou o Jogo')