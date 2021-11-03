import random 
import string

  
secure = ['7Yo%<S7', 'v$[,trC4', '^7ob7XnW', 
            '<dOF+96J', 'PC#IrZ0e', '1S$j%wK', 
            '7Y]5?D[+', 'BSLl)#o', 'Z=+Qr*i4', ]

print('Welcome to Secure Password Selector ')

while True:
    secure = random.choice(secures)
    number = random.randrange(0, 100)
    special_char = random.choice(string, punctuation)

    password = secure +  str(number) + special_char
    print('Your new password is: %s' % password)

    response = input(' Would you like another password? Type y or n: ')
    if response == 'n':
        break
