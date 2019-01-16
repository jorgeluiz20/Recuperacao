def get_results(player_name):
    open(player_name, 'r')
def generate_cpu_number():
    from random import randint
    cpu_number = randint(1,10)
    print('Jarvis lançou: ',cpu_number)
def get_round_winner(soma,player_choice):
    if soma % 2 == 0:
        if player_choice == 'par':
            print('voce ganhou')
        else:
            print('Jarvis ganhou')
    else:
        if player_choice == 'par':
            print('Jarvis ganhou')
        else:
            print('voce ganhou')
def record_results(player_name,num_rounds,generate_cpu_number,player_choice):
    open(player_name, 'w')
    player_name.append('ROUND',num_rounds,'=-=',player_name,':',player_choice,'=-= JARVIS:',generate_cpu_number,'=',player_name ,'VENCEU')
def get_winner_final(soma,player_choice,cpu_ganha,player_ganha):
    print('A soma dos dois numeros foi:', soma)
    if soma % 2 == 0:
        if player_choice == 'par':
            cpu_ganha += 1
        else:
            player_ganha += 1
    else:
        if player_choice == 'par':
            player_ganha += 1
        else:
            cpu_ganha += 1
def is_impar(cpu_number,player_number):
    soma = cpu_number + player_number
    if soma % 2 == 0:
        return True
    else:
        return False
def exit():
    for a in range(1):
        print('Adeus')
        break