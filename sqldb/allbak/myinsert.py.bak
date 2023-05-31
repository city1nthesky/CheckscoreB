# -*- coding: utf-8 -*-#
# filename: myinsert.py

import sqlite3


#打开数据库
def opendb(dbname, mineid):
    conn = sqlite3.connect(dbname)

    sql = "create table if not exists HXFW" + str(mineid) +"""(ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                                          SCHOOL TEXT NOT NULL,
                                                          CLASS TEXT NOT NULL,
                                                          NAME TEXT NOT NULL,
                                                          COUNT INTEGER
                                                         )"""

    cur = conn.execute(sql)


    return cur, conn

#记录家长这次行为
def addrecorddb(dbname, userid, school, classname, stuname):
    welcome = """--------------------欢迎使用添加数据功能-----------------------"""
    #print(welcome)
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    sql = "select id from wxidtomineid where wxid = '" + str(userid) + "'"

    flag = False
    cursor = c.execute(sql)
    for row in cursor:
        flag = True
        mineid = row[0]

    if flag:
        hel = opendb(dbname, mineid)
    else:
        sql = "insert into wxidtomineid (WXID) values(" + "\""+ str(userid) +"\")"
        cursor = c.execute(sql)
        conn.commit()
        sql = "select id from wxidtomineid where wxid = '" + str(userid) + "'"
        cursor = c.execute(sql)
        for row in cursor:
            mineid = row[0]
        hel = opendb(dbname, mineid)

    sql = "select count from  HXFW" + str(mineid) + " where school = '" + school + "' and class = '"  + str(classname) + "'"

    cursor = hel[1].execute(sql)
    flag = False
    count = 1
    for row in cursor:
        flag = True

    if flag:
        sql = "UPDATE  HXFW" + str(mineid) + " SET COUNT = COUNT + 1  WHERE SCHOOL = '" + school + "' AND CLASS = '" + str(classname) + "'"
        hel[1].execute(sql)
        hel[1].commit()
        hel[1].close()
    else:
        sql = "insert into HXFW" + str(mineid) + "(SCHOOL, CLASS, NAME, COUNT) values(" + \
              "\""+ school + "\", \"" + classname+ "\", \""+ stuname +"\", " + str(count)+  ")"
        hel[1].execute(sql)
        hel[1].commit()
        hel[1].close()

    hel[1].close()



#往数据库中添加内容
def adddb(dbname, userid, schoolname, phone, stuname, role, pay = '0'):
    welcome = """--------------------欢迎使用添加数据功能-----------------------"""
    #print(welcome)

    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    sql = "insert into userinfo (WXID, SCHOOLNAME, PHONE, NAME, ROLE, PAY) values(" + \
          "\""+ userid + "\", \"" + schoolname +  "\", \"" +  phone+ "\", \""+ stuname +"\", \"" + role + "\", \"" + pay + "\")"

    cursor = c.execute(sql)

    conn.commit()

    c.close()
    conn.close()


#判断是否绑定过
def isbind(dbname, userid):

    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    sql = "select * from unbindinfo where wxid = '" + userid + "'"

    cursor = c.execute(sql)
    flag = False
    for row in cursor:
        flag = True

    return flag


#往数据库添加之前绑定过的信息用来以后解绑进行限制
def addunbindinfo(dbname, userid):
    welcome = """--------------------欢迎使用解绑限制添加数据功能-----------------------"""
    #print(welcome)

    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    sql = "insert into unbindinfo (WXID, UNBINDCOUNT) values(" + \
        "\""+ userid + "\", " + "2)"


    cursor = c.execute(sql)
    conn.commit()

    c.close()
    conn.close()

#更新解除绑定次数
def updatedb(dbname, userid, unbindcount):
    welcome = """--------------------欢迎使用更新数据功能-----------------------"""
    #print(welcome)

    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    sql = " UPDATE UNBINDINFO SET UNBINDCOUNT = " + unbindcount + " WHERE WXID = '" + userid + "'"

    cursor = c.execute(sql)

    conn.commit()

    c.close()
    conn.close()


#删除数据库中内容
def deldb(dbname, userid):
    welcome = """--------------------欢迎使用删除数据功能-----------------------"""
    #print(welcome)

    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    sql = "DELETE FROM USERINFO WHERE WXID = '" + userid + "'"
          

    cursor = c.execute(sql)

    conn.commit()

    c.close()
    conn.close()

    return "success"



#deldb("userinfo.db", '1')
