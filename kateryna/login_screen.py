from register_screen import createlogin

def loginfailurescreen():
    a = input('Try again(1)\nRegister(2)\n')
    if a == "1":
        loginscreen()
    elif a == "2":
       createlogin()
    else:
        print('Error 404\nTry again')
        loginfailurescreen()
        
def loginscreen():
    logins = open('logins_for_something.txt', 'r')
    login = input('Your login: ')

    if any(login == l.strip() for l in logins):
        print('Ja rodyvsia!')

    else:                             
        print('There is no such a user')
        logins.close()
        loginfailurescreen()            

    
if __name__ == '__main__':
    loginscreen()
