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
print('1:  4 numbers')
print('2:  6 numbers')
print('3:  8 numbers')
print('4:  6 numbers + letters (only lower case)')
print('5:  8 numbers + letters (only lower case)')
print('6:  8 numbers + letters')
print('7:  8 numbers + letters + special caracters')
print('8:  10 numbers + letters + special caracters')
print('9:  12 numbers + letters + special caracters')
print('10: 16 numbers + letters + special caracters')

secure = input('Enter the desired password security level (1 to 10): ')

if (secure == '1'):
    weak(3)

elif (secure == '2'):
    weak(5)
        
elif (secure == '3'):
    weak(7)

elif (secure == '4'):
    regular(5)
        
elif (secure == '5'):
    regular(7)

elif (secure == '6'):
    good(7)
        
elif (secure == '7'):
    strong(7)
                
elif (secure == '8'):
    strong(9)
                
elif (secure == '9'):
    strong(11)
                
elif (secure == '10'):
    strong(15)
        
else:
    print('-' * 60)
    print('Invalid Option - Try Again!')