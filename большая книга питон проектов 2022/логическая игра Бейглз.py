import random

def rand_number(len_numb):
    return ''.join(random.choices('0123456789', k=len_numb))

def chek(attempt):
    pass

def main():
    print('''
          В этой игре вам предлагается угадать задуманное число
          У вас есть определенное количество попыток.
          
          ver 0.1
          ''')
    while True:     #Основной блок
        len_number = int(input('Введите длинну последовательности от 1 до 10: '))
        count_attempts = int(input('Введите количество попыток: '))
        rand_number(len_number)
        
        
        
if __name__ == '__main__':
    main()
    