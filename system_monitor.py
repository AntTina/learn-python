#!/usr/bin/python
import os
from commands import getoutput
import psutil

def menu():
    print '**** *** Linux System monitor *** ****'
    print '1.cpu info' 
    print '2.mem info' 
    print '3.disk info'
    print '4.exit'

def cpu():
    usage = psutil.cpu_percent(interval=1)
    if usage < 80:
        print "Don't worry,cpu usage less than 80"
    else:
        print "Warning!!!cpu usage greater than 80"
    print 'Cpu usage is %s' % usage

def mem():
    usage = psutil.virtual_memory().percent
    if usage < 60:
        print "Don't worry,mem usage less than 60"
    elif usage > 60 and usage < 80:
        print "Warning!!!mem usage between 60 and 80" 
    else:
        print "Memory is not enough!!!mem usage geater than 80"
    print 'Memory usage is %s' % usage

def disk():
    r_usage = psutil.disk_usage('/').percent
    b_usage = psutil.disk_usage('/boot').percent
    if r_usage < 60 and b_usage < 60:
        print "Don't worry, / and /boot usage less than 60"
    elif 60 < r_usage < 80 and 60 <b_usage < 80:
        print "Disk space is insufficient! / and /boot usage between 60 and 80" 
    elif r_usage > 80 and b_usage > 80:
        print "Disk is seriously insufficient!!! / and /boot usage geater than 80"
    print "/ usage is %s, /boot usage is %s" % (r_usage, b_usage)

def io():
    io = getoutput("iostat -x|awk '/^sda/{print $NF}'")
    if float(io) > 80:
        print 'IO busy'
    else:
		print 'IO working properly'
    print 'IO is %s' % io
def main():
    while True:
        os.system('clear')
        menu()
        num = raw_input('Please input your choice:')
        if num == '1':
            cpu()
        elif num == '2':
            mem()
        elif num == '3':
            disk()
            io()
        elif num == '4':
            break
        else:
            break
        print
        raw_input('Please type <Enter> key to continue')

main()
