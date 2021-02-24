i = 1
b = 'Fizz'
c = 'Buzz'
while i < 101:
    if i % 3 == 0:
        a = b
        if i % 5 == 0:
            a += c
    elif i % 5 == 0:
        a = c
    else:
        a = i
    i += 1
    print(a)


#Cahracters: 133, Score: 0.67/20
"""
for i in range (1, 101):
    if i % 5 != 0  and i % 3 != 0:
        print(a)
    elif i % 5 == 0 and i % 3 != 0:
        print('Buzz')
    elif i % 5 != 0 and i % 3 == 0:
        print('Fizz')
    else:
        print('FizzBuzz')
"""

#Cahracters: 132, Score: 0.68/20
"""
i = 1
while i < 101:
    if i % 5 != 0  and i % 3 != 0:
        print(i)
    elif i % 5 == 0 and i % 3 != 0:
        print('Buzz')
    elif i % 5 != 0 and i % 3 == 0:
        print('Fizz')
    else:
        print('FizzBuzz')
    i += 1
"""

"""
#Cahracters: 94 , Score: 1.06/20
i = 1
while i < 101:
    if i % 15 == 0:
        a = 'FizzBuzz'
    elif i % 5 == 0:
        a = 'Buzz'
    elif i % 3 == 0:
        a ='Fizz'
    else:
        a = i
    i += 1
    print(a)
"""

#Score 1.07
"""
i = 1
b = 'Fizz'
c= 'Buzz'
while i < 101:
    if i % 15 == 0:
        a = b + c
    elif i % 5 == 0:
        a = c
    elif i % 3 == 0:
        a = b
    else:
        a = i
    i += 1
    print(a)
"""


