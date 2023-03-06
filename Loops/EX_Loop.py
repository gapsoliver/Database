data = {'colour':'red',
        'fruit': 'apple',
        'pet': 'dog',
        'car': 'van'
        }
T = list(data.keys())
i = 0
while i < len(T):
    t = T[i]
    value = data[t]
    print(t, + '---', + value )
    i+=1
