import sqlite3
import openpyxl
import copy

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
def opendb(dbname, classname):
    conn = sqlite3.connect(dbname)
    cur = "222"


    return cur, conn

#查询全部信息
def showalldb():
    print("--------------处理后的数据------------")
    hel=opendb("yigaoDB.db", '2101')

    cur=hel[1].cursor()
    classname = "2101"
    sql = "select * from s2022" + classname

    cur.execute(sql)

    res = cur.fetchall()

    for line in res:
        for h in line:
            print(h),
        print()
    cur.close()
    hel[1].close()



#读取excel中的数据
def readxlsx(xlsxname, sheetname):
    print("I am coming") # 打开文件 获取workbook
    data = openpyxl.load_workbook(xlsxname)
    # 获取sheet页
    table = data.get_sheet_by_name(sheetname)
    nrows = table.rows
    ncols = table.columns

    data = list()

    for row in nrows:
        line = [col.value for col in row]
        #print(type(line))
        data.append(copy.deepcopy(line))
        #print(data)
        #print(line)

    print("I am outing")
    #print(data)
    print("I am outing")
    return data
    


#往数据库中添加内容
def adddb(dbname):
    welcome = """--------------------欢迎使用添加数据功能-----------------------"""
    print(welcome)
    #data = readxlsx('../2020级/1gaosanbanjixingmingxuehaoquan.xlsx', 'Sheet1')
    #data = readxlsx('../2021级/1gaoerbanjixingmingxuehaoquan2.xlsx', 'Sheet1')
    #data = readxlsx('../2022级/1gaoyibanjixingmingxuehao.xlsx', 'Sheet1')
    data = ['B1', 'B2', 'B3']
    classname = ""
    for tmp in data:
        print(tmp)

        #conn = sqlite3.connect("xcyg.db")
        conn = sqlite3.connect("22jiclassgrade.db")
        c = conn.cursor()


        sql2 = "select * from s2022" + str(tmp)
        print(sql2)
        try:
            # 执行SQL语句
            cursor = c.execute(sql2)
        except sqlite3.Error as e:
            # 打印异常信息
            conn.close()
            print(e)

        i = 0
        for row in cursor:
            print(row)
            i = i+1
            print("i", i)

            sql = "insert into CurrentClassGradeAnalysis" + """(ClassGrade , Grade, Year, Exam,
                   Sum, Yuwen, Shuxue,Waiyu
                   ) 
                   values('""" + str(row[0]) + "', '高一', '2023s', '" + str(row[1]) + "',"\
                   + str(row[2]) + "," + str(row[3]) + "," +  str(row[4]) + "," + str(row[5]) + ")"
            print(sql)
            hel = opendb(dbname, "222")
            try:
                # 执行SQL语句
                hel[1].execute(sql)
            except sqlite3.Error as e:
                # 打印异常信息
                conn.close()
                print(e)
                print("error1")
            hel[1].commit()
            hel[1].close()

        #hel[1].close()
        #print(allexamcount,sumcount,yuwencount,shuxuecount,waiyucount,select1count,select2count,select3count,zonghecount)


adddb("xcyg.db")
#showalldb()







