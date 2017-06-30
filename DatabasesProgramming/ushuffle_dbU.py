# -*- coding:utf-8 -*-

'''
本脚本使用mysql执行一些基本操作，在py2和py3下都可以运行。
其它组件在后面也会复用。
'''

from distutils.log import warn as printf
from random import randrange as rand
import os

if isinstance(__builtins__, dict) and 'raw_input' in __builtins__:
    scanf = input
elif hasattr(__builtins__, 'raw_input'):
    scanf = input
else:
    scanf = input

COLSIZ = 10
FIELDS = ('login', 'userid', 'projid')
RDBMSs = {'m': 'mysql',}
DBNAME = 'test'
DBUSER = 'root'
DB_EXC = None
NAMELEN = 16

tformat = lambda s: str(s).title().ljust(COLSIZ)
cformat = lambda s: s.opper().ljust(COLSIZ)

def setup():
    return RDBMSs[input('''
    Choose a database system:
    
    (M)ySQL
    
    Enter choice: ''').strip().lower()[0]]

def connect(db, DBNAME):
    global DB_EXC
    dbDir = '%s%s' % (db, DBNAME)
    if db == 'mysql':
        try:
            import pymysql
            import __mysql__exceptions as DB_EXC
            try: 
                cxn = pymysql.connect(db=DBNAME)
            except DB_EXC.OperationalError:
                try:
                    cxn = pymysql.connect(user=DBUSER)
                    cxn.query('create database %s' % DBNAME)
                    cxn.commit()
                    cxn.close()
                    cxn = pymysql.connect(db=DBNAME)
                except DB_EXC.OperationalError:
                    return None
        except ImportError:
            try:
                import mysql.connector
                import mysql.connector.error as DB_EXC
                try:
                    cxn = mysql.connector.Connect(**{
                        'database': DBNAME,
                        'user': DBUSER,
                    })
                except DB_EXC.InterfaceError:
                    return None
            except ImportError:
                return None
    else:
        return None
    return cxn

def create(cur):
    try:
        cur.execute('''
        CREATE TABLE users (
            login VARCHAR(%d),
            userid INTEGER,
            projid INTEGER)
        ''' % NAMELEN)
    except DB_EXC.OperationalError as e:
        drop(cur)
        create(cur)

drop = lambda cur: cur.execute('DROP TABLE users')

NAMES = (
    ('aaron', 8312), ('angla', 7603), ('dave', 7306),
    ('davina', 7902), ('elliot',7911), ('ernie', 7410),
    ('jess', 7912), ('jim', 7512), ('larry', 7311),
    ('leslie', 7808), ('melissa', 8602), ('pat', 7711),
    ('serena', 7003), ('stan', 7607), ('faye', 6812),
    ('amy', 7209), ('mona', 7404), ('jennifer', 7608),
)

def randName():
    pick = set(NAMES)
    while pick:
        yield pick.pop()

def insert(cur, db):
    if db == 'mysql':
        cur.execute("insert into users values(%s, %s, %s)",
                    [(who, uid, rand(1,5)) for who, uid, in randName()])

getRC = lambda cur: cur.rowcount if hasattr(cur, 'rowcount') else -1

def update(cur):
    fr = rand(1,5)
    to = rand(1,5)
    cur.execute("update users set projid=%d where projid=%d" % (to, fr))
    return fr, to, getRC(cur)

def delete(cur):
    rm = rand(1,5)
    cur.execute("delete from users where projid=%d" % rm)
    return rm, getRC(cur)

def dbDump(cur):
    cur.execute("select * from users")
    printf('\n%s' % ''.join(map(cformat, FIELDS)))
    for data in cur.fetchall():
        printf(''.join(map(tformat, data)))

def main():
    db = setup()
    printf('*** Connect to %r database' % db)
    cxn = connect(db, DBNAME)
    if not cxn:
        printf('ERROR: %r not supported or unreachable, exit' % db)
        return 
    cur = cxn.cursor()

    printf('\n*** Creating users table')
    create(cur)

    printf('\n*** Inserting names into table')
    insert(cur, db)
    dbDump(cur)

    printf('\n*** Randomly chossing group')
    rm, num = delete(cur)
    printf('\t(group #%d; %d users removed)' % (rm, num))
    dbDump(cur)

    printf('\n*** Dropping users table')
    drop(cur)
    printf('\n*** Close cxns')
    cur.close()
    cxn.commit()
    cxn.close()

if __name__ == '__main__':
    main()




        

