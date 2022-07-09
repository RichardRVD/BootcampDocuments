def countdown(num = 0):
    i = num + 1
    counting = []
    while i > 0:
        i -= 1
        # print(i)
        counting.append([i])
        # print(counting)
        num = counting
    return num
num=countdown(10)
print(num)


#2

def print_and_return(num1,num2):
    print(num1)
    return num2
num2 = print_and_return(3,4)
print(num2)

#3

def first_plus_length(num):
    i = num
    num= i[0]
    j = len(i)
    value = num + j
    return value 
value = first_plus_length([1,2,3,4,5,12,24])
print(value)

#4

def values_greater_than_second(list):
    if len(list) < 2:
        return "false"

    new_list = []
    for num in list:
        if num > list[1]:
            new_list.append(num)
    print(len(new_list))
    return new_list
new_list = values_greater_than_second([5,2,3,2,1,4])
print(new_list)

#5
def length_and_value(size = 1, value = 1):
    list_1 = []
    for numbers in range(size):
        list_1.append(value)
    return list_1
list_1 = (length_and_value(size = 12,value = 14))
print(list_1)