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
        "2245","2246"]



#打开数据库
def opendb(dbname, classname):
    conn = sqlite3.connect(dbname)
    sql = "create table if not exists s2022" + str(classname) + """ (LATESTEXAM TEXT NOT NULL,
           SUMBANCIRAISE TEXT NOT NULL, SUMDUANCIRAISE TEXT NOT NULL, SUMOVERLINE TEXT NOT NULL, 
           YUWENBANCIRAISE TEXT NOT NULL, YUWENDUANCIRAISE TEXT NOT NULL, YUWENOVERLINE TEXT NOT NULL, 
           SHUXUEBANCIRAISE TEXT NOT NULL, SHUXUEDUANCIRAISE TEXT NOT NULL, SHUXUEOVERLINE TEXT NOT NULL, 
           YINGYUBANCIRAISE TEXT NOT NULL, YINGYUDUANCIRAISE TEXT NOT NULL, YINGYUOVERLINE TEXT NOT NULL, 
           SELECT1BANCIRAISE TEXT NOT NULL, SELECT1DUANCIRAISE TEXT NOT NULL, SELECT1OVERLINE TEXT NOT NULL, 
           SELECT2BANCIRAISE TEXT NOT NULL, SELECT2DUANCIRAISE TEXT NOT NULL, SELECT2OVERLINE TEXT NOT NULL, 
           SELECT3BANCIRAISE TEXT NOT NULL, SELECT3DUANCIRAISE TEXT NOT NULL, SELECT3OVERLINE TEXT NOT NULL)"""

    print(sql)
    cur = conn.execute(sql)


    return cur, conn


def read_db_exam_banciduanci(dbname, classname, stuname, graphics, stuid, dbstr):
    #reload(sys)
    #sys.setdefaultencoding('utf8')
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    sql2 = "select exam from " + dbstr + str(stuid) + " where name = '" + stuname + "' ORDER BY rowid DESC LIMIT 2"
    try:
        # 执行SQL语句
        cursor = c.execute(sql2)
    except sqlite3.Error as e:
        # 打印异常信息
        conn.close()
        if 'no such table' in str(e):
            print("跳过")
            return '1','1'
        else:
            print("error1")
            return "error","error"
    tmp = ""
    for row in cursor:
        tmp += row[0]
        tmp += " "
    x_data = tmp.split()
    if graphics == 1:
        sql = "select sumbanci, sumduanci from " + dbstr + str(stuid) + " where name = '" + stuname + "' ORDER BY rowid DESC LIMIT 2"
        sql2 = "select sumduanci from " + dbstr + str(classname) + " where name = '一本线' ORDER BY rowid DESC LIMIT 2"
    elif graphics == 2:
        sql = "select yuwenbanci, yuwenduanci from " + dbstr + str(stuid) + " where name = '" + stuname + "' ORDER BY rowid DESC LIMIT 2"
        sql2 = "select yuwenduanci from " + dbstr + str(classname) + " where name = '一本线' ORDER BY rowid DESC LIMIT 2"
    elif graphics == 3:
        sql = "select shuxuebanci, shuxueduanci from " + dbstr + str(stuid) + " where name = '" + stuname + "' ORDER BY rowid DESC LIMIT 2"
        sql2 = "select shuxueduanci from " + dbstr + str(classname) + " where name = '一本线' ORDER BY rowid DESC LIMIT 2"
    elif graphics == 4:
        sql = "select yingyubanci, yingyuduanci from " + dbstr + str(stuid) + " where name = '" + stuname + "' ORDER BY rowid DESC LIMIT 2"
        sql2 = "select yingyuduanci from " + dbstr + str(classname) + " where name = '一本线' ORDER BY rowid DESC LIMIT 2"
    elif graphics == 5:
        sql = "select select1banci, select1duanci from " + dbstr + str(stuid) + " where name = '" + stuname + "' ORDER BY rowid DESC LIMIT 2"
        sql2 = "select select1duanci from " + dbstr + str(classname) + " where name = '一本线' ORDER BY rowid DESC LIMIT 2"
    elif graphics == 6:
        sql = "select select2banci, select2duanci from " + dbstr + str(stuid) + " where name = '" + stuname + "' ORDER BY rowid DESC LIMIT 2"
        sql2 = "select select2duanci from " + dbstr + str(classname) + " where name = '一本线' ORDER BY rowid DESC LIMIT 2"
    elif graphics == 7:
        sql = "select select3banci, select3duanci from " + dbstr + str(stuid) + " where name = '" + stuname + "' ORDER BY rowid DESC LIMIT 2"
        sql2 = "select select3duanci from " + dbstr + str(classname) + " where name = '一本线' ORDER BY rowid DESC LIMIT 2"

    #print(sql)
    #print(sql2)
    try:
        # 执行SQL语句
        cursor = c.execute(sql)
    except sqlite3.Error as e:
        # 打印异常信息
        conn.close()
        if 'no such table' in str(e):
            print("跳过")
            return '1','1'
        else:
            print("error1")
            return "error","error"
    tmp_banci = ""
    tmp_duanci = ""
    results = cursor.fetchall()
    # 检查查询结果是否为空
    if not results:
        conn.close()
        print("isnull")
        return "isnull","isnull"
    else:
        # 处理查询结果
        for row in results:
            #print("results",results)
            tmp_banci += row[0]
            tmp_duanci += row[1]
            tmp_banci += " "
            tmp_duanci += " "

    str_y_data_banci = tmp_banci.split()
    str_y_data_duanci = tmp_duanci.split()
    y_data = {}
    y_data.update({"stu_banci": [int(x) for x in str_y_data_banci]})
    y_data.update({"stu_duanci": [int(x) for x in str_y_data_duanci]})

    try:
        # 执行SQL语句
        cursor = c.execute(sql2)
    except sqlite3.Error as e:
        # 打印异常信息
        conn.close()
        if 'no such table' in str(e):
            print("跳过")
            return '1','1'
        else:
            print("error1")
            return "error","error"
    tmp_yibenxian = ""
    results = cursor.fetchall()
    # 检查查询结果是否为空
    if not results:
        conn.close()
        print("isnull")
        return "isnull","isnull"
    else:
        # 处理查询结果
        for row in results:
            #print("results",results)
            tmp_yibenxian += row[0]
            tmp_yibenxian += " "
    str_y_data_yibenxian = tmp_yibenxian.split()
    y_data.update({"yibenxian_duanci": [int(x) for x in str_y_data_yibenxian]})

    return x_data,y_data



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
        print(tmp)
        classname = tmp[0]
        stuid = tmp[1]
        stuname = tmp[2]
        if classname in (SG1WHS_2022 + SG1WHD_2022 + SG1WHZ_2022 + SG1SZD_2022 + SG1SZS_2022):
            pname = ['总分', '语文', '数学', '外语', '物理', '化学', '生物']
            pname = [1,2,3,4,5,6,7]
        #print(pname)
        text = []
        xdata = []
        for x in pname:
            xdata,ydata = read_db_exam_banciduanci("22ji.db", classname, stuname, x, stuid, "s2022")
            #print("xdata",xdata)
            #print("ydata",ydata)
            #检查变量是否等于 "error" "isnull"
            if isinstance(xdata, str) and xdata == "1":
                print("没有这个表，跳过")
                breakflag = True
                break
            tmp_text = []
            if len(ydata['stu_banci']) == 2:
                tmp_text.append(ydata['stu_banci'][1] - ydata['stu_banci'][0])
                tmp_text.append(ydata['stu_duanci'][1] - ydata['stu_duanci'][0])
            else:
                tmp_text.append(0)
                tmp_text.append(0)
            if ydata['stu_duanci'][0] <= ydata['yibenxian_duanci'][0]:
                tmp_text.append(1)
            else:
                tmp_text.append(0)
            text.append(tmp_text)

        if not breakflag:
            print(not breakflag)
            text.append(xdata[0])
            print("text:",text)
            hel = opendb(dbname, stuid)
            

            sql = "DELETE FROM s2022" + str(stuid)
            print(sql)
            hel[1].execute(sql)
            hel[1].commit()
            
            sql = "insert into s2022" + str(stuid) + """(LATESTEXAM,
                   SUMBANCIRAISE, SUMDUANCIRAISE, SUMOVERLINE,
                   YUWENBANCIRAISE, YUWENDUANCIRAISE, YUWENOVERLINE,
                   SHUXUEBANCIRAISE, SHUXUEDUANCIRAISE, SHUXUEOVERLINE,
                   YINGYUBANCIRAISE, YINGYUDUANCIRAISE, YINGYUOVERLINE,
                   SELECT1BANCIRAISE, SELECT1DUANCIRAISE, SELECT1OVERLINE,
                   SELECT2BANCIRAISE, SELECT2DUANCIRAISE, SELECT2OVERLINE,
                   SELECT3BANCIRAISE, SELECT3DUANCIRAISE, SELECT3OVERLINE) 
                   values('""" + str(text[7]) + "'," + str(text[0][0]) + "," + str(text[0][1]) + "," + str(text[0][2]) + ","\
                   + str(text[1][0]) + "," + str(text[1][1]) + "," + str(text[1][2]) + ","\
                   + str(text[2][0]) + "," + str(text[2][1]) + "," + str(text[2][2]) + ","\
                   + str(text[3][0]) + "," + str(text[3][1]) + "," + str(text[3][2]) + ","\
                   + str(text[4][0]) + "," + str(text[4][1]) + "," + str(text[4][2]) + ","\
                   + str(text[5][0]) + "," + str(text[5][1]) + "," + str(text[5][2]) + ","\
                   + str(text[6][0]) + "," + str(text[6][1]) + "," + str(text[6][2]) + ")"

            print(sql)
            hel[1].execute(sql)
            hel[1].commit()
            hel[1].close()



adddb("22jilatestanalysis.db")
#showalldb()







