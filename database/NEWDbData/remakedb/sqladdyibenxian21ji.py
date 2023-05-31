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
        "2045","2046"]



#打开数据库
def opendb(dbname, classname):
    conn = sqlite3.connect(dbname)
    cur = "222"


    return cur, conn

#获取某次考试成绩列表数据 如果sql语句执行失败返回error 如果数据为空返回isnull
def read_db_json(dbname, classname, stuname, stuid, exam, dbstr):
    #reload(sys)
    #sys.setdefaultencoding('utf8')



    #print(dbname)
    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    sql = "select * from " + dbstr + stuid + " where name = '" + stuname + "' and exam = '" + str(exam) + "'" 
    #print(sql)

    try:
        # 执行SQL语句
        cursor = c.execute(sql)
    except sqlite3.Error as e:
        # 打印异常信息
        #print("error")
        conn.close()
        return "error"

    text = {"th": ["成绩", "班次", "段次", "班级最高分", "一本线"], "td": []}

    if (classname in SG2LK_2022) or (classname in SG3LK_2022):
        results = cursor.fetchall()
        # 检查查询结果是否为空
        if not results:
            conn.close()
            #print("isnull")
            return "isnull"
        else:
            # 处理查询结果
            for row in results:
                text["td"].append(["总分:"+ row[2], row[3], row[4]])
                text["td"].append(["语文:"+ row[5], row[6], row[7]])
                text["td"].append(["数学:"+ row[8], row[9], row[10]])
                text["td"].append(["外语:"+ row[11], row[12], row[13]])
                text["td"].append(["物理:"+ row[14], row[15], row[16]])
                text["td"].append(["化学:"+ row[17], row[18], row[19]])
                text["td"].append(["生物:"+ row[20], row[21], row[22]])
                text["td"].append(["理综:"+ row[23], row[24], row[25]])
    elif (classname in SG2WK_2022) or (classname in SG3WK_2022):
        results = cursor.fetchall()
        # 检查查询结果是否为空
        if not results:
            conn.close()
            #print("isnull")
            return "isnull"
        else:
            # 处理查询结果
            for row in results:
                text["td"].append(["总分:"+ row[2], row[3], row[4]])
                text["td"].append(["语文:"+ row[5], row[6], row[7]])
                text["td"].append(["数学:"+ row[8], row[9], row[10]])
                text["td"].append(["外语:"+ row[11], row[12], row[13]])
                text["td"].append(["政治:"+ row[14], row[15], row[16]])
                text["td"].append(["历史:"+ row[17], row[18], row[19]])
                text["td"].append(["地理:"+ row[20], row[21], row[22]])
                text["td"].append(["文综:"+ row[23], row[24], row[25]])
    elif classname in SG1WHS_2022:
        results = cursor.fetchall()
        # 检查查询结果是否为空
        if not results:
            conn.close()
            #print("isnull")
            return "isnull"
        else:
            # 处理查询结果
            for row in results:
                text["td"].append(["总分:"+ row[2], row[3], row[4]])
                text["td"].append(["语文:"+ row[5], row[6], row[7]])
                text["td"].append(["数学:"+ row[8], row[9], row[10]])
                text["td"].append(["外语:"+ row[11], row[12], row[13]])
                text["td"].append(["物理:"+ row[14], row[15], row[16]])
                text["td"].append(["化学:"+ row[17], row[18], row[19]])
                text["td"].append(["生物:"+ row[20], row[21], row[22]])
                text["td"].append(["综合:"+ row[23], row[24], row[25]])
    elif classname in SG1WHD_2022:
        results = cursor.fetchall()
        # 检查查询结果是否为空
        if not results:
            conn.close()
            #print("isnull")
            return "isnull"
        else:
            # 处理查询结果
            for row in results:
                text["td"].append(["总分:"+ row[2], row[3], row[4]])
                text["td"].append(["语文:"+ row[5], row[6], row[7]])
                text["td"].append(["数学:"+ row[8], row[9], row[10]])
                text["td"].append(["外语:"+ row[11], row[12], row[13]])
                text["td"].append(["物理:"+ row[14], row[15], row[16]])
                text["td"].append(["化学:"+ row[17], row[18], row[19]])
                text["td"].append(["地理:"+ row[20], row[21], row[22]])
                text["td"].append(["综合:"+ row[23], row[24], row[25]])
    elif classname in SG1WHZ_2022:
        results = cursor.fetchall()
        # 检查查询结果是否为空
        if not results:
            conn.close()
            #print("isnull")
            return "isnull"
        else:
            # 处理查询结果
            for row in results:
                text["td"].append(["总分:"+ row[2], row[3], row[4]])
                text["td"].append(["语文:"+ row[5], row[6], row[7]])
                text["td"].append(["数学:"+ row[8], row[9], row[10]])
                text["td"].append(["外语:"+ row[11], row[12], row[13]])
                text["td"].append(["物理:"+ row[14], row[15], row[16]])
                text["td"].append(["化学:"+ row[17], row[18], row[19]])
                text["td"].append(["政治:"+ row[20], row[21], row[22]])
                text["td"].append(["综合:"+ row[23], row[24], row[25]])
    elif classname in SG1SZD_2022:
        results = cursor.fetchall()
        # 检查查询结果是否为空
        if not results:
            conn.close()
            #print("isnull")
            return "isnull"
        else:
            # 处理查询结果
            for row in results:
                text["td"].append(["总分:"+ row[2], row[3], row[4]])
                text["td"].append(["语文:"+ row[5], row[6], row[7]])
                text["td"].append(["数学:"+ row[8], row[9], row[10]])
                text["td"].append(["外语:"+ row[11], row[12], row[13]])
                text["td"].append(["历史:"+ row[14], row[15], row[16]])
                text["td"].append(["政治:"+ row[17], row[18], row[19]])
                text["td"].append(["地理:"+ row[20], row[21], row[22]])
                text["td"].append(["综合:"+ row[23], row[24], row[25]])
    elif classname in SG1SZS_2022:
        results = cursor.fetchall()
        # 检查查询结果是否为空
        if not results:
            conn.close()
            #print("isnull")
            return "isnull"
        else:
            # 处理查询结果
            for row in results:
                text["td"].append(["总分:"+ row[2], row[3], row[4]])
                text["td"].append(["语文:"+ row[5], row[6], row[7]])
                text["td"].append(["数学:"+ row[8], row[9], row[10]])
                text["td"].append(["外语:"+ row[11], row[12], row[13]])
                text["td"].append(["历史:"+ row[14], row[15], row[16]])
                text["td"].append(["政治:"+ row[17], row[18], row[19]])
                text["td"].append(["生物:"+ row[20], row[21], row[22]])
                text["td"].append(["综合:"+ row[23], row[24], row[25]])
    else:
        results = cursor.fetchall()
        # 检查查询结果是否为空
        if not results:
            conn.close()
            return "isnull"
        else:
            # 处理查询结果
            for row in results:
                text["td"].append(["总分:"+ row[2], row[3], row[4]])
                text["td"].append(["语文:"+ row[5], row[6], row[7]])
                text["td"].append(["数学:"+ row[8], row[9], row[10]])
                text["td"].append(["外语:"+ row[11], row[12], row[13]])
                text["td"].append(["物理:"+ row[14], row[15], row[16]])
                text["td"].append(["化学:"+ row[17], row[18], row[19]])
                text["td"].append(["生物:"+ row[20], row[21], row[22]])
                text["td"].append(["政治:"+ row[23], row[24], row[25]])
                text["td"].append(["历史:"+ row[26], row[27], row[28]])
                text["td"].append(["地理:"+ row[29], row[30], row[31]])


    sql = "select * from " + dbstr + classname + " where name = '班级最高分' and exam = '" + str(exam) + "'"
    #print(sql)
    try:
        # 执行SQL语句
        cursor = c.execute(sql)
    except sqlite3.Error as e:
        # 打印异常信息
        #print("error")
        conn.close()
        return "error"
    results = cursor.fetchall()
    # 检查查询结果是否为空
    if not results:
        conn.close()
        #print("isnull")
        return text
    else:
        # 处理查询结果
        for row in results:
            if classname in (SG1WHS_2022 + SG1WHZ_2022 + SG1WHD_2022 + SG1SZD_2022 + SG1SZS_2022):
                nozongheflag = 1
            else:
                nozongheflag = 0
            for i in range(len(text["td"]) - nozongheflag):
                text["td"][i].append(row[i*3+2])

    sql = "select * from " + dbstr + classname + " where name = '一本线' and exam = '" + str(exam) + "'"
    #print(sql)
    try:
        # 执行SQL语句
        cursor = c.execute(sql)
    except sqlite3.Error as e:
        # 打印异常信息
        conn.close()
        #print("error")
        return "error"
    results = cursor.fetchall()
    # 检查查询结果是否为空
    if not results:
        conn.close()
        #print("isnull")
        return text
    else:
        # 处理查询结果
        for row in results:
            if classname in (SG1WHS_2022 + SG1WHZ_2022 + SG1WHD_2022 + SG1SZD_2022 + SG1SZS_2022):
                nozongheflag = 1
            else:
                nozongheflag = 0
            for i in range(len(text["td"]) - nozongheflag):
                text["td"][i].append(row[i*3+2])


    c.close()
    conn.close()


    #print("text")
    return text


def read_db_exam_duanci(dbname, classname, stuname, graphics, stuid, dbstr = "s2021"):
    #reload(sys)
    #sys.setdefaultencoding('utf8')
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    sql2 = "select exam from " + dbstr + str(stuid) + " where name = '" + stuname + "'"
    try:
        # 执行SQL语句
        cursor = c.execute(sql2)
    except sqlite3.Error as e:
        # 打印异常信息
        conn.close()
        print(e)
        if 'no such table' in str(e):
            print("跳过")
            return '1','1','1'
        else:
            print("error1")
            return "error","error","error"
    tmp = ""
    for row in cursor:
        tmp += row[0]
        tmp += " "
    x_data = tmp.split()
    if graphics == '语文':
        sql = "select yuwenduanci from " + dbstr + str(stuid) + " where name = '" + stuname + "'"
    elif graphics == '数学':
        sql = "select shuxueduanci from " + dbstr + str(stuid) + " where name = '" + stuname + "'"
    elif graphics == '外语':
        sql = "select yingyuduanci from " + dbstr + str(stuid) + " where name = '" + stuname + "'"
    elif graphics == '政治':
        sql = "select zhengzhiduanci from " + dbstr + str(stuid) + " where name = '" + stuname + "'"
    elif graphics == '历史':
        sql = "select lishiduanci from " + dbstr + str(stuid) + " where name = '" + stuname + "'"
    elif graphics == '地理':
        sql = "select diliduanci from " + dbstr + str(stuid) + " where name = '" + stuname + "'"
    elif graphics == '物理':
        sql = "select wuliduanci from " + dbstr + str(stuid) + " where name = '" + stuname + "'"
    elif graphics == '化学':
        sql = "select huaxueduanci from " + dbstr + str(stuid) + " where name = '" + stuname + "'"
    elif graphics == '生物':
        sql = "select shengwuduanci from " + dbstr + str(stuid) + " where name = '" + stuname + "'"
    elif graphics == '总分':
        sql = "select sumduanci from " + dbstr + str(stuid) + " where name = '" + stuname + "'"
    elif graphics == '理综':
        sql = "select lizongduanci from " + dbstr + str(stuid) + " where name = '" + stuname + "'"
    elif graphics == '文综':
        sql = "select wenzongduanci from " + dbstr + str(stuid) + " where name = '" + stuname + "'"
    else:
        sql = "select yuwenduanci from " + dbstr + str(stuid) + " where name = '" + stuname + "'"

    cursor = c.execute(sql)
    tmp = ""
    for row in cursor:
        tmp += row[0]
        tmp += " "

    str_y_data = tmp.split()
    y_data =[{"stu": [float(x) for x in str_y_data]}]
    datalist  =[graphics]

    tmp = ""
    for x in x_data:
        if graphics == '语文':
            sql = "select yuwenduanci from " + dbstr + str(classname) + " where name = '一本线' and exam = '" + str(x) + "'"
        elif graphics == '数学':
            sql = "select shuxueduanci from " + dbstr + str(classname) + " where name = '一本线' and exam = '" + str(x) + "'"
        elif graphics == '外语':
            sql = "select yingyuduanci from " + dbstr + str(classname) + " where name = '一本线' and exam = '" + str(x) + "'"
        elif graphics == '政治':
            sql = "select zhengzhiduanci from " + dbstr + str(classname) + " where name = '一本线' and exam = '" + str(x) + "'"
        elif graphics == '历史':
            sql = "select lishiduanci from " + dbstr + str(classname) + " where name = '一本线' and exam = '" + str(x) + "'"
        elif graphics == '地理':
            sql = "select diliduanci from " + dbstr + str(classname) + " where name = '一本线' and exam = '" + str(x) + "'"
        elif graphics == '物理':
            sql = "select wuliduanci from " + dbstr + str(classname) + " where name = '一本线' and exam = '" + str(x) + "'"
        elif graphics == '化学':
            sql = "select huaxueduanci from " + dbstr + str(classname) + " where name = '一本线' and exam = '" + str(x) + "'"
        elif graphics == '生物':
            sql = "select shengwuduanci from " + dbstr + str(classname) + " where name = '一本线' and exam = '" + str(x) + "'"
        elif graphics == '总分':
            sql = "select sumduanci from " + dbstr + str(classname) + " where name = '一本线' and exam = '" + str(x) + "'"
        elif graphics == '理综':
            sql = "select lizongduanci from " + dbstr + str(classname) + " where name = '一本线' and exam = '" + str(x) + "'"
        elif graphics == '文综':
            sql = "select wenzongduanci from " + dbstr + str(classname) + " where name = '一本线' and exam = '" + str(x) + "'"
        else:
            sql = "select yuwenduanci from " + dbstr + str(classname) + " where name = '一本线' and exam = '" + str(x) + "'"
        cursor = c.execute(sql)
        for row in cursor:
            tmp += row[0]
            tmp += " "
    y_data.append({"yibenxian": [float(x) for x in tmp.split()]})
    if y_data[1]["yibenxian"]:
        datalist.append('一本线')

    return x_data,y_data,datalist



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
    data = SG3LK_2022 + SG3WK_2022

    classname = "2111"

    conn = sqlite3.connect("21ji.db")
    c = conn.cursor()
    sql2 = "select * from s2021" + str(classname)
    print(sql2)
    try:
        # 执行SQL语句
        cursor = c.execute(sql2)
    except sqlite3.Error as e:
        # 打印异常信息
        conn.close()
        print(e)
        if 'no such table' in str(e):
            print("跳过")
            breakflag = True
        else:
            print("error1")
    hel = opendb(dbname, classname)
    for row in cursor:
        if row[0] == "一本线":
            sql = "insert into SchoolLINE " + """(school, exam, line,year, grade,
                Sum, SumD,
                Yuwen, YuwenD,
                Shuxue, ShuxueD,
                Waiyu, WaiyuD,
                Select1, Select1D,
                Select2, Select2D,
                Select3, Select3D,
                Zonghe, ZongheD)
                values(""" + "'淅川一高', '" + str(row[1]) + "', '文科" + str(row[0]) + "', 2023, '高二', "\
                + str(row[2]) + "," + str(row[4]) + ","\
                + str(row[5]) + "," + str(row[7]) + ","\
                + str(row[8]) + "," + str(row[10]) + ","\
                + str(row[11]) + "," + str(row[13]) + ","\
                + str(row[14]) + "," + str(row[16]) + ","\
                + str(row[17]) + "," + str(row[19]) + ","\
                + str(row[20]) + "," + str(row[22]) + ","\
                + str(row[23]) + "," + str(row[25]) + ")"
            print(sql)
            hel[1].execute(sql)
            hel[1].commit()
    hel[1].close()
    conn.close()

adddb("xcyg.db")
#showalldb()







