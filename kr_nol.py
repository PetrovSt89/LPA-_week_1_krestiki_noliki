import os
import random

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
                print('так и не решили кто сильнее =) сыграем еще?!')
                continue
            if winer[0] == winer[1]:
                print(f'машины победили человечество =) Хочешь сыграть еще?\n')
            else:
                print(f'на этот раз тебе повезло =) Хочешь сыграть еще?\n')

        
            


# функция случайного выбора кто чем играет
def choise_x_o():
    x_o = ['x','o']
    x_o_comp = random.choice(x_o)
    x_o_man = 'o' if x_o_comp == 'x' else 'x'
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
def man_step(base_turns):
    while True:        
        print('введи два числа от 1 до 3 через пробел - столбец и строку')
        turn = input()
        if len(turn) != 3:
            print('ввел не в формате: <число> <число>')
        elif turn[1] != ' ':
            print('нужен пробел между числами')
        else:
            turn = turn.split()
            if turn[0].isdigit() and turn[1].isdigit():
                turn[0] = int(turn[0])
                turn[1] = int(turn[1])
            else:
                print('введены не цыфры')
                continue
            if turn in base_turns:
                print('прости, но эта клетка уже использована')
            elif not 0 < turn[0] < 4 or not 0 < turn[1] < 4:
                print('введенные числа ушли за границу') 
            else:
                clear()
                return turn


# функция хода компьютера
def comp_step(base_turns):
    all_steps = [[1,1],[1,2],[1,3],[2,1],[2,2],[2,3],[3,1],[3,2],[3,3]]
    if base_turns ==[]:
        steps = all_steps
    else:
        for i in base_turns:
            all_steps.remove(i)
        # steps = [all_steps.remove(i) for i in base_turns]
        if all_steps == []:
            clear()
            return False
    while True:
        turn = random.choice(all_steps)
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
        x = 'x'
        o = 'o'
        for i in field:
            if 'x' in i and i.count('x') == 3:
                return x
            if 'o' in i and i.count('o') == 3:
                return o
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
        return diag(exp_f)


    # проверка диагонали таблицы
    def diag(field):
        diag_f =[]
        fi = []
        for i in range(len(field)):
            for j in range(len(field)):
                if i == j:
                    fi.append(field[i][j])
        diag_f.append(fi)
        return diag_f


    # основные проверки
    sum_field = field + field_reverce(field) + diag(field) + revers_str(field)
    winer = triple(sum_field)
    if winer:
        return winer

def return_append_change(turn, x_o, field, base_turns):
    if turn == False:
        return ''
    base_turns.append(turn)
    change_field(turn, x_o, field)


# основная работа игры
def game_progress():
    field = kreate_field()
    clear()
    print_field(field)
    base_turns = []
    x_o_comp, x_o_man = choise_x_o()
    step = 'man'
    while True:
        if step == 'man':    
            print(f'ты играешь "{x_o_man}"')
            turn = man_step(base_turns)
            x_o = x_o_man
            step = 'comp'
        else:
            turn = comp_step(base_turns)
            x_o = x_o_comp
            step = 'man'
        return_append_change(turn, x_o, field, base_turns)
        
        winer = check_win(field)
        if winer:
            return winer, x_o_comp, x_o_man


enter_game()


