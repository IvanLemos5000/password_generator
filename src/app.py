import string
import random

upperLetters = string.ascii_uppercase
lowerLetters = string.ascii_lowercase
numbers = string.digits
special = string.punctuation

def weak(lenght):
    n = 0
    password = ''
    while n <= lenght:
        caracters = list(random.choice(str(numbers)))
        random.shuffle(caracters)
        password = ''.join(map(str,caracters)) + password
        n += 1
    output(password)

def regular(lenght):
    n = 0
    password = ''
    while n <= lenght:
        caracters = list(random.choice(str(numbers)+lowerLetters))
        random.shuffle(caracters)
        password = ''.join(map(str,caracters)) + password
        n += 1
    output(password)

def good(lenght):
    n = 0
    password = ''
    while n <= lenght:
        caracters = list(random.choice(str(numbers)+lowerLetters+upperLetters))
        random.shuffle(caracters)
        password = ''.join(map(str,caracters)) + password
        n += 1
    output(password)

def strong(lenght):
    n = 0
    password = ''
    while n <= lenght:
        caracters = list(random.choice(str(numbers)+lowerLetters+upperLetters+special))
        random.shuffle(caracters)
        password = ''.join(map(str,caracters)) + password
        n += 1
    output(password)
    
def output(password):
    print('-' * 60)
    print('Your Password is:', password)

print("Password's Security Levels:")
print('1: numbers                                - weak')
print('2: numbers and letters (only lower case)  - regular')
print('3: numbers and letters                    - good')
print('4: numbers, letters and special caracters - strong')

secure = input('Enter the desired password security level (1 to 4): ')

lenght = input("How many caracters do you need? ")

lenght = int(lenght) - 1

if (secure == '1'):
    weak(lenght)

elif (secure == '2'):
    regular(lenght)
        
elif (secure == '3'):
    good(lenght)

elif (secure == '4'):
    strong(lenght)
        
else:
    print('-' * 60)
    print('Invalid Security Level - Try Again!')