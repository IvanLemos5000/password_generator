import string
import random

upperLetters = string.ascii_uppercase
lowerLetters = string.ascii_lowercase
numbers = string.digits
special = string.punctuation
password = ''
n = 0

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
    while n <= 3:
        caracters = list(random.choice(str(numbers)))
        random.shuffle(caracters)
        password = ''.join(map(str,caracters)) + password
        n += 1

elif (secure == '2'):
    while n <= 5:
        caracters = list(random.choice(str(numbers)))
        random.shuffle(caracters)
        password = ''.join(map(str,caracters)) + password
        n += 1
        
elif (secure == '3'):
    while n <= 7:
        caracters = list(random.choice(str(numbers)))
        random.shuffle(caracters)
        password = ''.join(map(str,caracters)) + password
        n += 1

elif (secure == '4'):
    while n <= 5:
        caracters = list(random.choice(str(numbers)+lowerLetters))
        random.shuffle(caracters)
        password = ''.join(map(str,caracters)) + password
        n += 1
        
elif (secure == '5'):
    while n <= 7:
        caracters = list(random.choice(str(numbers)+lowerLetters))
        random.shuffle(caracters)
        password = ''.join(map(str,caracters)) + password
        n += 1

elif (secure == '6'):
    while n <= 7:
        caracters = list(random.choice(str(numbers)+lowerLetters+upperLetters))
        random.shuffle(caracters)
        password = ''.join(map(str,caracters)) + password
        n += 1
        
elif (secure == '7'):
    while n <= 7:
        caracters = list(random.choice(str(numbers)+lowerLetters+upperLetters+special))
        random.shuffle(caracters)
        password = ''.join(map(str,caracters)) + password
        n += 1
                
elif (secure == '8'):
    while n <= 9:
        caracters = list(random.choice(str(numbers)+lowerLetters+upperLetters+special))
        random.shuffle(caracters)
        password = ''.join(map(str,caracters)) + password
        n += 1
                
elif (secure == '9'):
    while n <= 11:
        caracters = list(random.choice(str(numbers)+lowerLetters+upperLetters+special))
        random.shuffle(caracters)
        password = ''.join(map(str,caracters)) + password
        n += 1
                
elif (secure == '10'):
    while n <= 15:
        caracters = list(random.choice(str(numbers)+lowerLetters+upperLetters+special))
        random.shuffle(caracters)
        password = ''.join(map(str,caracters)) + password
        n += 1 
        
else:
    print('Invalid Option - Try Again!')
        
print('-' * 60)
print('Your Password is:', password)