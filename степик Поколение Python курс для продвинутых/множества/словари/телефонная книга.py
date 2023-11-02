telephone_book = dict()
for _ in range(int(input())):
    phone, name_u = input().lower().split()
    if name_u not in telephone_book:
        telephone_book[name_u] = phone
    else:
        telephone_book[name_u] = telephone_book.get(name_u) + phone

for _ in range(int(input())):
    n = input().lower()
    if n in telephone_book:
        print(telephone_book[n])
    else:
        print('абонент не найден')