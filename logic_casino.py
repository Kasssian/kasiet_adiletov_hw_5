from random import choice
from envparse import env
import os

env.read_envfile('my_money.env')
my_money = int(os.getenv('MY_MONEY'))


def casino(my_money):
    slots = [i for i in range(1, 31)]
    while True:
        stavka = int(input("Введите номер слота: "))
        if stavka <= 0:
            print('Вводите в числа в районе 1-30')
            continue
        elif stavka >= 31:
            print('Вводите в числа в районе 1-30')
            continue
        else:
            stavka_baks = int(input("Сумма ставки: "))
            if my_money < stavka_baks:
                print('У вас не так много денег.Надо было взять больше')
                continue
            my_money -= stavka_baks
            if stavka == choice(slots):
                stavka_baks * 2
                my_money += stavka_baks
                print('Вы выиграли.На этот раз.')
            else:
                print('Вы проиграли)')
                stavka_baks = 0
            print(f'У вас осталось {my_money}')
            if my_money <= 0:
                print('Тебе нечего ставить.Вали отсюда,нищий.')
                break
            continue_play = input('Вы хотите продолжить?Напишите "Да","Yes" или "Нет","No": ')
            if continue_play.isupper() == 'да' or 'yes':
                continue
            elif continue_play.isupper() == 'нет' or 'no':
                print('До скорой встречи!')
                break
            else:
                print('Пишите корректно')
                continue
