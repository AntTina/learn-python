#!/usr/bin/python
import os
from commands import getoutput
import time

time = time.strftime('%F %X')
user = os.getlogin()
ip = getoutput("w|awk '/w$/{print $3}'")

def menu():
    print '**** *** User admin *** ****'
    print '1.add user' 
    print '2.delete user' 
    print '3.query user info'
    print '4.reset user password'
    print '5.exit'


def add():
    u_name = raw_input('please input username you want to add: ')
    if os.system('id %s &>/dev/null' % u_name) == 0:
        print 'User %s already exists' % u_name
    else:
        os.system('useradd %s' % u_name)
        print 'User %s create ok' % u_name
        f = open('/var/log/manager_user.log','a+')
        f.write('Date: %s  Current user: %s  Thing:create user %s  Ip: %s\n' % (time, user, u_name, ip))
        f.close()

def delete():
    u_name = raw_input('please input username you want to delete: ')
    if os.system('id %s &>/dev/null' % u_name) == 0:
        answer = raw_input('Are you sure you want to delete %s (y/n)?' % u_name)
        if answer == 'y':
            os.system('userdel -r  %s' % u_name)
            print 'User %s delete ok' % u_name
            f = open('/var/log/manager_user.log','a+')
            f.write('Date: %s  Current user: %s  Thing:delete user %s  Ip: %s\n' % (time, user, u_name, ip))
            f.close()
        else:
            print 'You abandon delete %s' % u_name
    else:
        print 'User %s does not exists' % u_name

def query():
    print 'All user: %s' % os.popen('cat /etc/passwd|cut -d: -f 1').read().split()
    u_name = raw_input('please input username you want to query: ')
    print getoutput("cat /etc/passwd |egrep '^%s:'" % u_name)

def reset():
    print 'All user: %s' % os.popen('cat /etc/passwd|cut -d: -f 1').read().split()
    u_name = raw_input('please input username you want to reset password: ')
    u_pin = raw_input('please input new password: ')
    os.system('echo %s|passwd %s --stdin &>/dev/null' % (u_pin, u_name))
    print 'reset user %s password ok' % u_name
    f = open('/var/log/manager_user.log','a+')
    f.write('Date: %s  Current user: %s  Thing:reset user %s password  Ip: %s\n' % (time, user, u_name, ip))
    f.close()
def main():
    while True:
        os.system('clear')
        menu()
        num = raw_input('Please input your choice:')
        if num == '1':
            add()
        elif num == '2':
            delete()
        elif num == '3':
            query()
        elif num == '4':
            reset()
        elif num == '5':
            break
        else:
            break
        print
        raw_input('Please type <Enter> key to continue')

main()
