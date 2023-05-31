import sqlite3
import openpyxl
import copy



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
        "2245","2246"]



#打开数据库
def opendb(dbname, classname):
    conn = sqlite3.connect(dbname)
    sql = "create table if not exists s2022" + str(classname) + """ (NAME TEXT NOT NULL,
           ALLEXAM INTEGER, SUM INTEGER, YUWEN INTEGER, SHUXUE INTEGER, YINGYU INTEGER,
           SELECT1 INTEGER, SELECT2 INTEGER,SELECT3 INTEGER)"""

    print(sql)
    cur = conn.execute(sql)


    return cur, conn


def read_db_exam_duanci(dbname, classname, stuname, graphics, stuid, dbstr):
    #reload(sys)
    #sys.setdefaultencoding('utf8')
    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    conn1 = sqlite3.connect("22jilatestanalysis.db")
    c1 = conn1.cursor()

    sql = "SELECT LATESTEXAM FROM " + dbstr +str(stuid) +  " ORDER BY ROWID DESC LIMIT 1"
    print(sql)
    try:
        # 执行SQL语句
        cursor = c1.execute(sql)
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

    results = cursor.fetchall()
    # 检查查询结果是否为空
    if not results:
        conn.close()
        print("isnull")
        return "isnull","isnull","isnull"
    else:
        # 处理查询结果
        for row in results:
            print(results)
            lastexam = row[0]


    sql2 = "select exam from " + dbstr + str(stuid) + " where name = '" + stuname + "' ORDER BY ROWID DESC LIMIT 1"
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
            print("error2")
            return "error","error","error"
    for row in cursor:
        newexam = row[0]
    if lastexam == newexam:
        print("lastexam:", lastexam)
        print("newexam:", newexam)
        print("相同")
        return "same","same","same"

    if graphics == 1:
        sql = "select sumduanci from " + dbstr + str(stuid) + " where name = '" + stuname + "'"
    elif graphics == 2:
        sql = "select yuwenduanci from " + dbstr + str(stuid) + " where name = '" + stuname + "'"
    elif graphics == 3:
        sql = "select shuxueduanci from " + dbstr + str(stuid) + " where name = '" + stuname + "'"
    elif graphics == 4:
        sql = "select yingyuduanci from " + dbstr + str(stuid) + " where name = '" + stuname + "'"
    elif graphics == 5:
        sql = "select select1duanci from " + dbstr + str(stuid) + " where name = '" + stuname + "'"
    elif graphics == 6:
        sql = "select select2duanci from " + dbstr + str(stuid) + " where name = '" + stuname + "'"
    elif graphics == 7:
        sql = "select select3duanci from " + dbstr + str(stuid) + " where name = '" + stuname + "'"

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
        if graphics == 1:
            sql = "select sumduanci from " + dbstr + str(classname) + " where name = '一本线' and exam = '" + str(x) + "'"
        elif graphics == 2:
            sql = "select yuwenduanci from " + dbstr + str(classname) + " where name = '一本线' and exam = '" + str(x) + "'"
        elif graphics == 3:
            sql = "select shuxueduanci from " + dbstr + str(classname) + " where name = '一本线' and exam = '" + str(x) + "'"
        elif graphics == 4:
            sql = "select yingyuduanci from " + dbstr + str(classname) + " where name = '一本线' and exam = '" + str(x) + "'"
        elif graphics == 5:
            sql = "select select1duanci from " + dbstr + str(classname) + " where name = '一本线' and exam = '" + str(x) + "'"
        elif graphics == 6:
            sql = "select select2duanci from " + dbstr + str(classname) + " where name = '一本线' and exam = '" + str(x) + "'"
        elif graphics == 7:
            sql = "select select3duanci from " + dbstr + str(classname) + " where name = '一本线' and exam = '" + str(x) + "'"
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
    data = readxlsx('./2022级/1gaoyibanjixingmingxuehao.xlsx', 'Sheet1')
    classname = ""
    for tmp in data:
        breakflag = False
        if tmp == data[0]:
            continue
        #print(tmp)
        classname = tmp[0]
        stuid = tmp[1]
        stuname = tmp[2]
        pname = [1,2,3,4,5,6,7]
        #print(pname)
        text = []
        for x in pname:
            xdata,ydata,datalist = read_db_exam_duanci("22ji.db", classname, stuname, x, stuid, "s2022")
            #检查变量是否等于 "error" "isnull"
            if isinstance(xdata, str) and xdata == "1":
                print("没有这个表，跳过")
                breakflag = True
                break
            elif isinstance(xdata, str) and xdata == "isnull":
                print("表里数据为空，跳过")
                breakflag = True
                break
            elif isinstance(xdata, str) and xdata == "same":
                print("数据相同，跳过")
                breakflag = True
                break
            count = 0
            for y in range(len(ydata[0]['stu'])):
                if ydata[0]['stu'][y] <= ydata[1]['yibenxian'][y]:
                    count = count + 1
            text.append(count)
        #print("text:",text)
        #print("xdata:",xdata)

        if not breakflag:
            print(not breakflag)
            hel = opendb(dbname, stuid)
            sql = "select * from s2022" + str(stuid) + " where name = '" + stuname + "'  ORDER BY ROWID DESC LIMIT 1"
            cursor = hel[1].execute(sql)
            lastalldata = []
            for row in cursor:
                lastalldata.append(row[1])
                lastalldata.append(row[2])
                lastalldata.append(row[3])
                lastalldata.append(row[4])
                lastalldata.append(row[5])
                lastalldata.append(row[6])
                lastalldata.append(row[7])
                lastalldata.append(row[8])
            

            table_name = "s2022" + str(stuid)
            #c.execute(f"UPDATE {table_name} SET ALLEXAM = ?, SUM = ?, YUWEN = ?, SHUXUE = ?, YINGYU = ?, SELECT1 = ?, SELECT2 = ?, SELECT3 = ? WHERE NAME = ?",\
            #        (lastalldata[0] + 1, lastalldata[1] + text[0], lastalldata[2] + text[1], lastalldata[3] + text[2], lastalldata[4] + text[3], lastalldata[5] + text[4], lastalldata[6] + text[5],\
            #        lastalldata[7] + text[6], stuname))
            #hel[1].execute(sql)
            #hel[1].commit()
            #hel[1].close()



adddb("22jiallanalysis.db")
#showalldb()







