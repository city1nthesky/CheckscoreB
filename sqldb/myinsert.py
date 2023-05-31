# -*- coding: utf-8 -*-#
# filename: myinsert.py

import sqlite3

SG1WHS_2022 = ["2201","2202","2203","2204",\
        "2205","2206","2207","2208","2209",\
        "2215","2216","2217","2218","2219",\
        "2220","2221","2222","2223",\
        "2241","2242","2245"]

SG1WHD_2022 = ["2229","2230","2231","2232","2233"]

SG1WHZ_2022 = ["2210","2211","2212","2213","2214",\
        "2224","2225","2226","2227","2228","2243"]

SG1SZD_2022 = ["2234","2235","2236","2237","2244"]

SG1SZS_2022 = ["2238","2239","2240"]


SG2LK_2022 = ["2101","2102","2103","2104",\
        "2105","2106","2107","2108","2109",\
        "2110","2113","2114","2115","2116",\
        "2117","2118","2119","2120","2121",\
        "2122","2123","2124","2127","2128",\
        "2129","2130","2131","2132","2133",\
        "2134","2135","2136","2137","2138",\
        "2143","2144","2145"]

SG2WK_2022 = ["2111","2112","2125","2126",\
        "2139","2140","2141","2142","2146"]

SG3LK_2022 = ["2001","2002","2003","2004",\
        "2005","2006","2007","2008","2009",\
        "2010","2011","2012","2013","2014",\
        "2015","2016","2017","2018","2019",\
        "2020","2021","2022","2023","2024",\
        "2025","2026","2027","2028","2029",\
        "2030","2031","2032","2033","2034",\
        "2047","2048","2049","2050"]

SG3WK_2022 = ["2035","2036","2037","2038",\
        "2039","2040","2041","2042","2043",\
        "2044","2045","2046"]




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

#记录用户这次行为
def addrecorddb(dbname, userid, school, classname, stuname, role):
    welcome = """--------------------欢迎使用添加数据功能-----------------------"""
    #print(welcome)
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    sql = "select count from AccoutRecord where wxid = '" + str(userid) + "' and school = '" + school + "' and class = " + classname
    #print(sql)

    flag = False
    cursor = c.execute(sql)
    for row in cursor:
        flag = True


    if classname in (SG1WHS_2022 + SG1WHZ_2022 + SG1WHD_2022 + SG1SZD_2022 + SG1SZS_2022):
        grade = '高一'
    elif classname in (SG2WK_2022 + SG2LK_2022):
        grade = '高二'
    else:
        grade = '高三'


    if flag:
        sql = "UPDATE  AccoutRecord SET count = count + 1, time = datetime('now','localtime')   WHERE wxid = '" + str(userid) + "' AND school = '" + school + "' AND class = " + classname
        #print(sql)
        cursor = c.execute(sql)
        conn.commit()
    else:
        sql = "insert into AccoutRecord (wxid, role, name, school, grade, class) values(" + \
              "'"+ userid + "', '" + role+ "', '"+ stuname +"', '" + school +  "', '" + grade+ "', "+ classname + ")"
        #print(sql)
        cursor = c.execute(sql)
        conn.commit()

    c.close()
    conn.close()



#往数据库中添加内容
def adddb(dbname, userid, schoolname, phone, stuname, role):
    welcome = """--------------------欢迎使用添加数据功能-----------------------"""
    #print(welcome)

    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    sql = "insert into UserAccoutInfo (wxid, role, school, phone, name,  bind_state) values(" + \
          "'"+ userid + "', '" + role +  "', '" +  schoolname+ "', '"+ phone + "', '" + stuname + "', 1)"
    #print(sql)

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

#更改绑定内容
def change_bindinfo(dbname, userid, schoolname, phone, stuname, role):
    welcome = """--------------------欢迎使用删除数据功能-----------------------"""
    #print(welcome)

    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    sql = "UPDATE UserAccoutInfo SET bind_state  = '1', school = '" + schoolname + "', phone = '" + "', name = '" + stuname +  "', role = '" + role + "', time = datetime('now','localtime')  WHERE WXID = '" + userid + "'"
    #print(sql)


    cursor = c.execute(sql)

    conn.commit()

    c.close()
    conn.close()

    return "success"

#更改绑定状态
def change_bindstate(dbname, userid, bindstate):
    welcome = """--------------------欢迎使用删除数据功能-----------------------"""
    #print(welcome)

    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    if bindstate == '0':
        count = '1'
    else:
        count = '0'

    sql = "UPDATE UserAccoutInfo SET bind_state  = '" + bindstate + "', time = datetime('now','localtime'), count = count -" + count + " WHERE WXID = '" + userid + "'"
    #print(sql)


    cursor = c.execute(sql)

    conn.commit()

    c.close()
    conn.close()

    return "success"
