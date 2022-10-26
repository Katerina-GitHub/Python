from random import *
import os

welcome = ('Берите конфеты, и не жадничайте, в одни руки максимум 28 конфет.\n')
print(welcome)

message = ['твоя очередь', 'еще', 'бери быстрее', 'а можно побыстрее?']


def player_vs_bot():
    chocolade_total = 2021
    max_take = 28
    player_1 = input('\nКак тебя зовут?: ')
    player_2 = 'Бот Гоги'
    players = [player_1, player_2]
    print(f'\nНачинаем, {player_1} и  {player_2} \n')
   # print('\nДля начала опеределим кто первый начнет игру.\n')

    lucky = randint(-1, 0)

    print(f'{players[lucky+1]} ты ходишь первым, дружище !')

    while chocolade_total > 0:
        lucky += 1

        if players[lucky % 2] == 'Бот':
            print(
                f'\nХодит {players[lucky%2]} \nНа кону {chocolade_total}. \n{choice(message)}: ')

            if chocolade_total < 29:
                step = chocolade_total
            else:
                devide = chocolade_total//28
                step = chocolade_total - ((devide*max_take)+1)
                if step == -1:
                    step = max_take - 1
                if step == 0:
                    step = max_take
            while step > 28 or step < 1:
                step = randint(1, 28)
            print(step)
        else:
            step = int(input(
                f'\nХоди,  {players[lucky%2]} \nНа кону {chocolade_total} {choice(message)}:  '))
            while step > max_take or step > chocolade_total:
                step = int(
                    input(f'\nЗа один ход можно взять {max_take} конфет, попробуй еще раз: '))
        chocolade_total = chocolade_total - step

    print(f'На кону осталось {chocolade_total} \nПобедил {players[lucky%2]}')


player_vs_bot()
