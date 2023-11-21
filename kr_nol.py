import os
from random import randint, choice

# функция очистки игры
def clear():
    os.system('cls')

# функция основного меню игры
def enter_game():
    clear()
    print('Привет Друг, сыграешь со мной в крестики-нолики?\n')
    while True:

        button = input('Введи "y" для игры или "q" для выхода\n')
        if button == 'q':
            print('До новых встреч!')
            break
        if button == 'y':
            clear()
            # вызов основной функции игры
            winer = game_progress()
            if winer == '':
                print('До новых встреч!')
                break
            if winer[0] == winer[1]:
                print(f'машины победили человечество =) Хочешь сыграть еще?\n')
            else:
                print(f'на этот раз тебе повезло =) Хочешь сыграть еще?\n')

        
            


# функция случайного выбора кто чем играет
def choise_x_o():
    x_o = ['x','o']
    x_o_comp = choice(x_o)
    x_o_man = 'xo'.replace(x_o_comp,'')
    return x_o_comp, x_o_man


# функция создания поля в начале игры
def kreate_field():
    field = [[ '.' for j in range(1,4)] for i in range(1,4)]
    return field


# функция вывода поля на экран
def print_field(field):
    print('Игровое поле:')
    for i in field:
        print(i)
    print()


# функция хода человека
def man_step(field, base_turns):
    while True:        
        print('введи два числа от 1 до 3 через пробел - столбец и строку')
        turn = input()
        if turn == 'q':
            return 0
        if len(turn) != 3:
            print('ввел не в формате: <число> <число>')
        elif turn[1] != ' ':
            print('нужен пробел между числами')
        else:
            turn = turn.split()
            turn[0] = int(turn[0])
            turn[1] = int(turn[1])
            if turn in base_turns:
                print('прости, но эта клетка уже использована')
            elif not 0 < turn[0] < 4 or not 0 < turn[1] < 4:
                print('введенные числа ушли за границу') 
            else:
                clear()
                return turn


# функция хода компьютера
def comp_step(field, base_turns):
    while True:
        turn = [randint(1,3),randint(1,3)]
        if turn not in base_turns:
            return turn


# функция изменения поля
def change_field(turn, x_o, field):
    hor = turn[0] -1 #затычка для range
    ver = turn[1] -1
    field[ver][hor] = x_o
    print(f'так пошел "{x_o}"\n')

    print_field(field)


# функция основной проверки
def check_win(field):


    # проверка если в строчке три одинаковых
    def triple(field):
        x = False
        o = False
        for i in field:
            if 'x' in i and i.count('x') == 3:
                x = True
                break
            if 'o' in i and i.count('o') == 3:
                o = True    
                break
        if x == True:
            return 'x'
        elif o == True:
            return 'o'
        else:
            return ''


    # переворот столбцов таблицы
    def field_reverce(field):
        new_field = [['0','0','0'] for _ in range(3)]
        for row in range(len(field)):
            for j in range(len(field[0])):
                new_field[j][row] = field[row][j]
        return new_field


    # переворот строки
    def revers_str(field):
        exp_f =[]
        for i in field:
            exp_f.append(i[::-1])
        return exp_f


    # проверка диагонали таблицы
    def diag(field):
        cnt =[]
        for i in range(len(field)):
            for j in range(len(field)):
                if i == j:
                    cnt.append(field[i][j])
        if cnt.count('x') == 3:
            return 'x'
        elif cnt.count('o') == 3:
            return 'o'
        else:
            return ''


    # основные проверки
    winer = triple(field)
    if winer:
        return winer
    elif winer := triple(field_reverce(field)):
        print(f'победил {winer}')
        return winer
    elif winer := diag(field):
        print(f'победил {winer}')
        return winer
    else:
        winer = diag(revers_str(field))
        if winer:
            print(f'победил {winer}')
            return winer


# основная работа игры
def game_progress():
    field = kreate_field()
    clear()
    print_field(field)
    base_turns = []
    x_o_comp, x_o_man = choise_x_o()
    while True:
        print(f'ты играешь "{x_o_man}"')
        turn_m = man_step(field, base_turns)
        if turn_m == 0:
            return ''
        base_turns.append(turn_m)
        change_field(turn_m, x_o_man, field)
        
        winer = check_win(field)
        if winer:
            return winer, x_o_comp, x_o_man

        turn_c = comp_step(field, base_turns)
        base_turns.append(turn_c)
        change_field(turn_c, x_o_comp, field)

        winer = check_win(field)
        if winer:
            return winer, x_o_comp, x_o_man

        
enter_game()


