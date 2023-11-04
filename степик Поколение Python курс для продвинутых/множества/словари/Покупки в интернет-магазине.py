n = int(input())
my_dict = dict()
for _ in range(n):
    name, product, value = input().split()
    if name not in my_dict:
        my_dict[name] = {product: int(value)}
    else:
        if product not in my_dict[name]:
            my_dict[name][product] = int(value)
        else:
            my_dict[name][product] = my_dict[name][product] + int(value)
sorted_dict = dict(sorted(my_dict.items()))
for i in sorted_dict:
    print(i + ':')
    for j in dict(sorted(my_dict[i].items())):
        print(j, my_dict[i][j])