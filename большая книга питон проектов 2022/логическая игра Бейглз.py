import random

def rand_number(len_numb):
    return ''.join(random.choices('0123456789', k=len_numb))

def chek(attempt, win):
    value_good = 0
    value_bad = 0
    if attempt == win:
        return [100]
    for i in range(len(attempt)):
        if attempt[i] == win[i]:
            value_good += 1
        elif attempt[i] in win:
            value_bad += 1
    return [value_good, value_bad]
            
    

def main():
    print('''
          В этой игре вам предлагается угадать задуманное число
          У вас есть определенное количество попыток.
          
          ver 0.1
          ''')
    while True:     #Основной блок
        out = 0
        len_number = int(input('Введите длинну последовательности от 1 до 10: '))
        count_attempts = int(input('Введите количество попыток: '))
        number = rand_number(len_number)
        for _ in range(count_attempts):
            att = input('Вы предпологаете что загадано:')
            value = chek(att, number)
            if value[0] == 100:
                out = 1
                break
            print('\nЧисел стоит на правильных позициях:{} \nЧисел находящихся в задуманном, но не на своих позициях:{}\n'.format(value[0], value[1]))
        if out == 1:
            print('Вы угадали задуманное число и это:{} \n      Поздравляем с победой!!!'.format(number))
            print('Чтобы сыграть ещё раз введите 1, чтобы выйти введите 0')
        else:
            print('К сожалению вы проиграли 0_o')
            print('Чтобы сыграть ещё раз введите 1, чтобы выйти введите 0')
        param = int(input())
        if param == 0:
            break
        
        
if __name__ == '__main__':
    main()
    