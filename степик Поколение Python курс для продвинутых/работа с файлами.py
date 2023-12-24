with open('C:/profil/learning_python/learning_python/степик Поколение Python курс для продвинутых/test.txt', 'r', encoding='utf-8') as file:
    text = file.readlines()
    
b = sum(map(lambda x: len(x.split()), text))
c = ''.join(text).replace('.', '').replace(' ', '').replace('\n', '')
print('''Input file contains:
{} letters 
{} words 
{} lines'''.format(len(c), b, len(text)))