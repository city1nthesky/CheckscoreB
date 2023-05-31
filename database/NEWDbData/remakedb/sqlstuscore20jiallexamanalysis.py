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
    classname = ""
    #data = [123,[2218,1235223014,2131]]
    #data = [123,[2220, 1235223010, '杨晓晴']]
    data = [123, [2213, 1235223013, '马继东']]
    data = [123, [2214, 1235223011, '王少峰']]
    for tmp in data:
        breakflag = False
        if tmp == data[0]:
            continue
        #print(tmp)
        classname = str(tmp[0])
        stuid = tmp[1]
        stuname = tmp[2]
        text = []


        conn = sqlite3.connect("xcyg.db")
        c = conn.cursor()
        c2 = conn.cursor()

        print("classname", classname)
        print("typeclass", type(classname))
        if classname in (SG1WHS_2022 + SG1WHZ_2022 + SG1WHD_2022 + SG2LK_2022 + SG3LK_2022):
            print("that")
            line = '理科一本线'
        else:
            print("this")
            line = '文科一本线'

        if classname in (SG2LK_2022 + SG2WK_2022 + SG3LK_2022 + SG3WK_2022):
            print(classname)
            fg1 = False
        else:
            fg1 = True

        sql2 = "select * from CurrentScore where student_id = " + str(stuid)
        print(sql2)
        try:
            # 执行SQL语句
            cursor = c.execute(sql2)
        except sqlite3.Error as e:
            # 打印异常信息
            conn.close()
            print(e)

        allexamcount = 0
        sumcount = 0
        yuwencount = 0
        shuxuecount = 0
        waiyucount = 0
        select1count  = 0
        select2count = 0
        select3count = 0
        zonghecount = 0
        i = 0
        for row in cursor:
            print(cursor)
            print(row)
            i = i+1
            print("i", i)
            allexamcount = allexamcount + 1
            sql = "select * from SchoolLINE where exam  = '" + str(row[4]) + "' and grade = '" + str(row[6]) + "' and line = '" + str(line) + "'"

            print(sql)
            try:
                # 执行SQL语句
                cursor2 = c2.execute(sql)
            except sqlite3.Error as e:
                # 打印异常信息
                conn.close()
                print(e)
                print("error1")
            for row2 in cursor2:
                print(row2)

                if row[9] <= row2[8]:
                    sumcount = sumcount + 1
                if row[12] <= row2[10]:
                    yuwencount = yuwencount + 1
                if row[15] <= row2[12]:
                    shuxuecount = shuxuecount + 1
                if row[18] <= row2[14]:
                    waiyucount = waiyucount + 1
                if row[21] <= row2[16]:
                    select1count = select1count + 1
                if row[24] <= row2[18]:
                    select2count = select2count + 1
                if row[27] <= row2[20]:
                    select3count = select3count + 1
                if not fg1:
                    print(fg1)
                    if row[30] <= row2[22]:
                        zonghecount = zonghecount + 1

        print(allexamcount,sumcount,yuwencount,shuxuecount,waiyucount,select1count,select2count,select3count,zonghecount)
        if not fg1:
            sql = "insert into CurrentStuAllScoreAnalysis " + """(student_id, AllExam,
                   Sum, Yuwen, Shuxue,Waiyu,
                   Select1,Select2,Select3,
                   Zonghe
                   ) 
                   values(""" + str(stuid) + "," + str(allexamcount) + ","\
                   + str(sumcount) + "," + str(yuwencount) + "," +  str(shuxuecount) + "," + str(waiyucount) + ","\
                   + str(select1count) + "," + str(select2count) + "," + str(select3count) + ","\
                   + str(zonghecount) + ")"
        else:
            sql = "insert into CurrentStuAllScoreAnalysis " + """(student_id, AllExam,
                   Sum, Yuwen, Shuxue,Waiyu,
                   Select1,Select2,Select3
                   ) 
                   values(""" + str(stuid) + "," + str(allexamcount) + ","\
                   + str(sumcount) + "," + str(yuwencount) + "," +  str(shuxuecount) + "," + str(waiyucount) + ","\
                   + str(select1count) + "," + str(select2count) + "," + str(select3count) + ")"
        print(sql)

        hel = opendb(dbname, stuid)
        try:
            # 执行SQL语句
            hel[1].execute(sql)
        except sqlite3.Error as e:
            # 打印异常信息
            conn.close()
            print(e)
            print("error1")
        #hel[1].execute(sql)
        hel[1].commit()
        hel[1].close()



adddb("xcyg.db")
#showalldb()







