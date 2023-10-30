s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
s_arr = s.split(' ') 
counter = {}
m = 0
buf = ' '
for i in s_arr:
    if s.count(i) >= m:
        if s.count(i) == m:
            if i < buf:
                buf = i
        else:
            m = s.count(i)
            buf = i
print(buf)
            

    
