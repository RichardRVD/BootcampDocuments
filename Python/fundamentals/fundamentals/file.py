num1 = 42 # variable declaration 'num1' with the variable value as a primative data type (int). 
num2 = 2.3 # variable declaration 'num2' with the variable value as a primative data type (float).
boolean = True # variable declaration 'boolean' with the value as a primative data type (boolean).
string = 'Hello World' # variable declaration 'string' with value as an initialized string.
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}#initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana')#initialize tuple
print(type(fruit)) #log statement tuple 'fruit'
print(pizza_toppings[1])#log statement list item one index from pizza toppings 'sausage'
pizza_toppings.append('Mushrooms')#list add value 'mushrooms'
print(person['name'])# log statement from dictionary ;name: John
person['name'] = 'George' # dictionary change value name from John to George.
person['eye_color'] = 'blue' # dictionary add key value pair "eye_color: blue"
print(fruit[2])# log statement of two index from fruit "banana"

if num1 > 45: #conditional if statement
    print("It's greater")#log statement
else:#conditional else statement
    print("It's lower")#log statement "will log 'It's lower"

if len(string) < 5: #conditional if statement
    print("It's a short word!")#log statement
elif len(string) > 15:#conditional else if statement
    print("It's a long word!")# log statement
else:#conditional else statement
    print("Just right!")# log statement

for x in range(5):#for loop start
    print(x)#log statement
for x in range(2,5):#for loop start
    print(x)#log statement
for x in range(2,10,3):#for loop start
    print(x)#log statement
x = 0 #variable declaration
while(x < 5):#while loop start
    print(x)#log statement
    x += 1#while loop incriment/stop

pizza_toppings.pop()#list delete value 'last value'
pizza_toppings.pop(1)#list delete value in one index

print(person)#log statement 'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False, 'eye_color: 'blue"}
person.pop('eye_color')#dictionary delete value eye_color
print(person)#log statement 'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}

for topping in pizza_toppings:#for loop initialize
    if topping == 'Pepperoni':#if conditional
        continue#for loop continue
    print('After 1st if statement')#log statement
    if topping == 'Olives':#if conditional
        break#for loop break

def print_hello_ten_times(): #function
    for num in range(10):
        print('Hello')#log statement

print_hello_ten_times()#function call

def print_hello_x_times(x):#function
    for num in range(x):
        print('Hello')#log statement

print_hello_x_times(4)#function call

def print_hello_x_or_ten_times(x = 10):#function
    for num in range(x):
        print('Hello')#log statement

print_hello_x_or_ten_times()#function call
print_hello_x_or_ten_times(4)#function call


"""
Bonus section
"""

# print(num3)                    #name num3 is not defined
# num3 = 72                      #variable declaration (int)
# fruit[0] = 'cranberry'         TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) KeyError: 'favorite_team'
# print(pizza_toppings[7])       IndexError: list index out of range
#   print(boolean)               IndentationError: unexpected indent
# fruit.append('raspberry')      AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1)                   AttributeError: 'tuple' object has no attribute 'pop'