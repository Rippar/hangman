import random

def hangman(word):
    wrong=0
    stages=['',                  #0
            '_________        ', #1
            '|                ', #2
            '|        |       ', #3
            '|        0       ', #4
            '|       /|\      ', #5
            '|       / \      ', #6
            '|                '] #7
    rletters=list(word)
    board=['_']*len(word)
    win=False
    print('Добро пожаловать на казнь!')
    ###
    while wrong<len(stages)-1:
        print('\n')
        guess=input('Введите букву: ')
        if guess in rletters:
            cind=rletters.index(guess) #cind - это позиция угаданной буквы в отгадываемом слове
            board[cind]=guess
            rletters[cind]='$' # $ потому что отгадываемое слово вряд-ли содержит знак $ а не например какую-нибудь букву
        else:
            wrong+=1
        print((''.join(board)))
        e=wrong+1
        print('\n'.join(stages[0:e]))
        if '_' not in board:
            print('Вы выиграли! Было загадано слово: ')
            print(''.join(board))
            win=True
            break
    ###
    if not win: # то же самое, что и win==False
        print('\n'.join(stages[0: wrong]))
        print('Вы проиграли! Было загадано слово: {}.'.format(word))
        
list1=['волк','лиса','заяц']
x=random.randint(0,2)
y=list1[x]
y=str(y)
hangman(y)
