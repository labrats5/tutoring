def checkpassword():
    global password
    password = input('Your password: ')
    count = len(password)
    digit = 0
    symbol = 0
    if count >= 5:
        for character in password:
            if character.isdigit():
                digit = digit + 1
            else:
                symbol = symbol + 1
        if symbol and digit > 0:
            print('Saving password...')
        else:
            print('Password must contain at least one digit and one symbol, try again')
            checkpassword()
    else:
        print('Password must be at least 5 charachters, try again')
        checkpassword()

def createlogin():
    login = input('Your login: ')
    logins = open('logins_for_something.txt', 'r') 
    for line in logins:
        if login in logins:
            print('This login is taken, try again')
            logins.close()
            createlogin()
        else:
            print('Saving login...')
            logins.close()
            logins = open('logins_for_something.txt', 'a')
            logins.write(login)
            logins.write('\n')
            logins.close()
            checkpassword()
            passwords = open(login + '.txt', 'w')
            passwords.write(password)
            passwords.close()
            

if __name__ == '__main__':
    createlogin()
