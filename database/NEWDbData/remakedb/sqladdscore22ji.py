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
    data = readxlsx('../2022级/1gaoyibanjixingmingxuehao.xlsx', 'Sheet1')
    classname = ""
    for tmp in data:
        breakflag = False
        if tmp == data[0]:
            continue
        #print(tmp)
        classname = tmp[0]
        stuid = tmp[1]
        stuname = tmp[2]
        text = []


        conn = sqlite3.connect("22ji.db")
        c = conn.cursor()
        sql2 = "select * from s2022" + str(stuid)
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

        if not breakflag:
            hel = opendb(dbname, stuid)
            for row in cursor:
                print(row)

                sql = "insert into CurrentScore " + """(student_id, school, stugrade, exam, class,grade,
                       Sum, SumB, SumD,
                       Yuwen, YuwenB, YuwenD,
                       Shuxue, ShuxueB, ShuxueD,
                       Waiyu, WaiyuB, WaiyuD,
                       Select1, Select1B, Select1D,
                       Select2, Select2B, Select2D,
                       Select3, Select3B, Select3D,
                       Zonghe, ZongheB, ZongheD
                       ) 
                       values(""" + str(stuid) + ",'淅川一高', '22级', '"\
                       + str(row[1]) + "'," + str(classname) + ", '高一', " +  str(row[2]) + "," + str(row[3]) + "," + str(row[4]) + ","\
                       + str(row[5]) + "," + str(row[6]) + "," + str(row[7]) + ","\
                       + str(row[8]) + "," + str(row[9]) + "," + str(row[10]) + ","\
                       + str(row[11]) + "," + str(row[12]) + "," + str(row[13]) + ","\
                       + str(row[14]) + "," + str(row[15]) + "," + str(row[16]) + ","\
                       + str(row[17]) + "," + str(row[18]) + "," + str(row[19]) + ","\
                       + str(row[20]) + "," + str(row[21]) + "," + str(row[22]) + ","\
                       + str(row[23]) + "," + str(row[24]) + "," + str(row[25]) + ")"
                print(sql)
                hel[1].execute(sql)
                hel[1].commit()

        hel[1].close()


adddb("xcyg.db")
#showalldb()







