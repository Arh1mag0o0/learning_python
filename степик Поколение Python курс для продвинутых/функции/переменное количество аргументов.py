def greet(*args, hel='Hello,'):
    print(hel, end=' ')
    s = ' and '.join(args)
    print(s)
    print('!')
    
def print_products(*args):
    n = 1
    for i in args:
        if type(i) is str and i != '':
            print(f'{n}) {i}')
            n += 1
    if n == 1:
        print('Нет продуктов')
        
        
def info_kwargs(**kwargs):
    sorted_items = dict(sorted(kwargs.items()))
    for i in sorted_items:
        print(i, sorted_items[i], sep=': ')
        
info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher') 
    
        