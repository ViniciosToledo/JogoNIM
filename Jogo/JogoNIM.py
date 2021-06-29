def computador_escolhe_jogada(n,m):  #Definição para determinar a jogada do PC
    jogada = 0   #Variavel para salvar a jogado do computador na memoria.
    
    while jogada != m and jogada != n:  #Repetição para testar a estrategia vencedora.
        jogada +=1
        
        if (n-jogada)%(m+1)== 0:
            return jogada

def usuario_escolhe_jogada(n,m):  #Definição para o jogador escolher sua jogada

    jogada_valida = 0
    
    while jogada_valida == 0:  #Repetição para testar se a jogada é valida
        jogada_valida = int(input('Digite sua jogada: \n'))
        
        if jogada_valida > m or jogada_valida > n or jogada_valida == 0:
            print('Jogada invalida, digite novamente: ')
            jogada_valida = 0
        
        else:  #Retorna da jogada caso ela seja valida.
            return jogada_valida

def partida():  #Definição que cria uma partida

    n = int(input('Digite o número de peças iniciais: ')) #variavel obrigatoria
    m = int(input('Digite quantas peças podem ser retiradas por rodada: ')) #variavel obrigatoria

    while m > n or m == n: #Repetição para verificar se os valores n e m são validos.
        print('O número de peças inicias deve ser maior que o número de peças que podem ser retiradas\n')
        n = int(input('Digite o número de peças iniciais: ')) #variavel obrigatoria
        m = int(input('Digite quantas peças podem ser retiradas por rodada: ')) #variavel obrigatoria

    jogadaDoCoumputador = 0  #Variavel para gravar as jogadas durante a partida
    jogadaDoUsuario = 0  #Variavel para gravar as jogadas durante a partida
        
    if n % (m+1) == 0:  #Teste para decidir quem começa segundo a estrategia vencedora

        print('Você começa!!\n')
        while n > 0:  #Repetição para a partida acabar quando as peças acabarem
            jogadaDoUsuario = usuario_escolhe_jogada(n,m)
            n = n - jogadaDoUsuario
            print(f'O jogador removeu {jogadaDoUsuario} peças, restam {n} peças\n')

            jogadaDoCoumputador = computador_escolhe_jogada(n,m)
            n = n - jogadaDoCoumputador
            print(f'O computador removeu {jogadaDoCoumputador} peças, restam {n} peças\n')

        if n == 0:
            print('O comptador venceu.\n')

    else:

        print('\nComputador começa!!\n')

        while n > 0:  #Repetição para a partida acabar quando as peças acabarem
            jogadaDoCoumputador = computador_escolhe_jogada(n,m)
            n = n - jogadaDoCoumputador
            print(f'O computador removeu {jogadaDoCoumputador} peças, restam {n} peças\n')
            
            if n > 0:
                jogadaDoUsuario = usuario_escolhe_jogada(n,m)
                n = n - jogadaDoUsuario
                print(f'O jogador removeu {jogadaDoUsuario} peças, restam {n} peças\n')
            else:
                print('O comptador venceu.\n')


def campeonato():  #Definição que chama 3 partidas em sequencia. E acumula vitorias no placar
    vitoriasDoComputador = 0  #Variavel para salvar os resutados 
    rodada = 1  #Variavel para salvar qual rodada do campeonato está sendo jogada

    while vitoriasDoComputador < 3:  #Repetiçao para acabar o campeonato depois de 3 partidas
        print(f'\nrodada {rodada}\n')
        partida()
        vitoriasDoComputador += 1
        rodada += 1
        print(f'Placar: Você 0 X {vitoriasDoComputador} Computador')


    
print('######## BEM VINDO AO JOGO NIM ########\nModos de Jogo:\n')
escolha = 0  #Variavel para dar ao jogador a opção de modo de jogo

while escolha < 1 or escolha > 2:   #Repetiçáo para checar se o modo escolhido é valido
    escolha = int(input('1 - Para partida unica\n2 - Para campeonato\n'))

    if escolha == 1:
        print(partida())

    elif escolha == 2:
        print(campeonato())

    else:
        print('Modo invalido\n')