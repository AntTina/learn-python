#!/usr/bin/python
import os
import MySQLdb

db = MySQLdb.connect('localhost', 'root', '123456')
cur = db.cursor()
cur.execute('create database g_dress character set utf8')
cur.execute('use g_dress')
cur.execute('create table g_brand(id int primary key,name varchar(10),size varchar(10),color varchar(10),price int)')


def menu():
    print '**** *** Operate mysql through python *** ****'
    print '1.insert data'
    print '2.delete data'
    print '3.query data'
    print '4.update data'
    print '5.exit'


def insert():
    num = int(raw_input('Please input the insert data number:'))
    n = 0
    while n < num:
        id = raw_input('Please input dress id,id should be unique:')
        name = raw_input('Please input dress name:')
        size = raw_input('Please input dress size:')
        color = raw_input('Please input dress color:')
        price = raw_input('Please input dress price:')
        cur.execute("insert into g_brand values (%s,'%s','%s','%s',%s);" % (id, name, size, color, price))
        n = n+1
        os.system('sleep 1')
    db.commit()
    print '\nInsert %s data successfully' % num


def delete():
    d_con = raw_input('Please input delete condition: ')
    cur.execute("delete from g_brand where %s" % d_con)
    db.commit()
    print '\nDelete data successfully'


def queryall():
    cur.execute("select * from g_brand")
    result = cur.fetchall()
    for i in result:
        print i


def query():
    q_con = raw_input('Please input query condition: ')
    cur.execute("select * from g_brand where %s" % q_con)
    result1 = cur.fetchall()
    for i in result1:
        print i


def update():
    context = raw_input('Please input update context: ')
    u_con = raw_input('Please input update condition: ')
    cur.execute("update g_brand set %s where %s" % (context, u_con))
    db.commit()
    print '\nUpdate data successfully'


def main():
    while True:
        os.system('clear')
        menu()
        num = raw_input('Please input your choice:')
        if num == '1':
            insert()
        elif num == '2':
            queryall()
            delete()
        elif num == '3':
            query()
        elif num == '4':
            queryall()
            update()
        elif num == '5':
            break
        else:
            break
        print
        raw_input('Please type <Enter> key to continue')
    cur.execute("drop database g_dress")
    cur.close()
    db.close()

main()
