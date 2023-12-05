'''парадокс дней рождения заключается в удивительно
высокой вероятности того, что у двух человек совпадает день 
рождения даже в относительно небольшой группе людей.'''
import datetime, random


def getBrithdays(numberOfBirthdays):
    '''Возвращаем список объектов дат для случайных дней рождения.'''
    birthdays = []
    for i in range(numberOfBirthdays):
        startOfyear = datetime.date(2001, 1, 1)
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday =  startOfyear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays


def getMatch(birthdays):
    '''Возвращаем объект даты дян рождения, встречающегося несколько раз в списке дней рождения'''
    if len(birthdays) == len(set(birthdays)):
        return None
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA == birthdayB:
                return birthdayA
            

#Отображаем вводную информацию
print('''парадокс дней рождения заключается в удивительно
высокой вероятности того, что у двух человек совпадает день 
рождения даже в относительно небольшой группе людей.''')

MONTHS = ('Январь', 'Февраль', 'Март', 'Апрель',
'Май', 'Июнь', 'Июль', 'Август', 
'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь')

while True:
    print('Сколько дат генерировать?')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break  #Введено допустимое значение
print()

#Генерация и отображение дней рождения
print('Here are', numBDays, 'birthdays:')
birthdays = getBrithdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(', ', end='')
    monthName = MONTHS[birthday.month - 1]
    dateText = '{} {}'.format(monthName, birthday.day)
    print(dateText, end='')
print()
print()

match = getMatch(birthdays)

print('in this simulation, ', end='')
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthName, match.day)
    print('multiple people have a birthday on', dateText)
else:
    print('Совпадений нет')
print()

#Производим 100 000 операций имитационного моделирования
print('Generating', numBDays, 'random birthdays 100,000 times...')
input('Press Enter to begin...')

print('Let\'s run another 100,000 simulations.')
simMatch = 0
for i in range(100_000):
    if i % 10_000 == 0:
        print(i, 'simulations run...')
    birthday = getBrithdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1
print('100,000 simulations run.')

#Отображение результатов имитационного моделирования
print('out of 100,000 simulation of', numBDays, 'people, there was a')
print('matching birthday in that group', simMatch, 'times. Thes means')
print('that', numBDays, 'pepople have a', 'процентов chance of')
print('having a matching birthday in their group.')
print('That\'s probably more rhan you would think!')   