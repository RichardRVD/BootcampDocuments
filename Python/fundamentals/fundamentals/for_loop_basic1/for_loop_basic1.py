for i in range(151):
    print(i)

for i in range(5, 1000, 5):
    print(i)

for i in range(1, 101):
    if i % 10 == 0:
        print('Coding Dojo')
    elif i % 5 == 0:
        print('Coding')
    else:
        print(i)

temp = 0
for i in range(500000):
    if i % 2 == 1:
        temp = temp + i
print(temp)
        
for i in range(2018, 0, -4):
    print(i)

lowNum = 2
highNum = 17
mult = 3
for i in range(lowNum, highNum):
    if i % mult == 0:
        print(i)