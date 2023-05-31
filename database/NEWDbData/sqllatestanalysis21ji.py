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
    sql = "create table if not exists s2021" + str(classname) + """ (LATESTEXAM TEXT NOT NULL,
           SUMBANCIRAISE TEXT NOT NULL, SUMDUANCIRAISE TEXT NOT NULL, SUMOVERLINE TEXT NOT NULL, 
           YUWENBANCIRAISE TEXT NOT NULL, YUWENDUANCIRAISE TEXT NOT NULL, YUWENOVERLINE TEXT NOT NULL, 
           SHUXUEBANCIRAISE TEXT NOT NULL, SHUXUEDUANCIRAISE TEXT NOT NULL, SHUXUEOVERLINE TEXT NOT NULL, 
           YINGYUBANCIRAISE TEXT NOT NULL, YINGYUDUANCIRAISE TEXT NOT NULL, YINGYUOVERLINE TEXT NOT NULL, 
           WUZHENGBANCIRAISE TEXT NOT NULL, WUZHENGDUANCIRAISE TEXT NOT NULL, WUZHENGOVERLINE TEXT NOT NULL, 
           HUASHIBANCIRAISE TEXT NOT NULL, HUASHIDUANCIRAISE TEXT NOT NULL, HUASHIOVERLINE TEXT NOT NULL, 
           SHENGDIBANCIRAISE TEXT NOT NULL, SHENGDIDUANCIRAISE TEXT NOT NULL, SHENGDIOVERLINE TEXT NOT NULL, 
           LIWENBANCIRAISE TEXT NOT NULL, LIWENDUANCIRAISE TEXT NOT NULL, LIWENOVERLINE TEXT NOT NULL)"""

    print(sql)
    cur = conn.execute(sql)


    return cur, conn


def read_db_exam_banciduanci(dbname, classname, stuname, graphics, stuid, dbstr = "s2021"):
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
        print(e)
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
    if graphics == '语文':
        sql = "select yuwenbanci, yuwenduanci from " + dbstr + str(stuid) + " where name = '" + stuname + "' ORDER BY rowid DESC LIMIT 2"
        sql2 = "select yuwenduanci from " + dbstr + str(classname) + " where name = '一本线' ORDER BY rowid DESC LIMIT 2"
    elif graphics == '数学':
        sql = "select shuxuebanci, shuxueduanci from " + dbstr + str(stuid) + " where name = '" + stuname + "' ORDER BY rowid DESC LIMIT 2"
        sql2 = "select shuxueduanci from " + dbstr + str(classname) + " where name = '一本线' ORDER BY rowid DESC LIMIT 2"
    elif graphics == '外语':
        sql = "select yingyubanci, yingyuduanci from " + dbstr + str(stuid) + " where name = '" + stuname + "' ORDER BY rowid DESC LIMIT 2"
        sql2 = "select yingyuduanci from " + dbstr + str(classname) + " where name = '一本线' ORDER BY rowid DESC LIMIT 2"
    elif graphics == '政治':
        sql = "select zhengzhibanci, zhengzhiduanci from " + dbstr + str(stuid) + " where name = '" + stuname + "' ORDER BY rowid DESC LIMIT 2"
        sql2 = "select zhengzhiduanci from " + dbstr + str(classname) + " where name = '一本线' ORDER BY rowid DESC LIMIT 2"
    elif graphics == '历史':
        sql = "select lishibanci, lishiduanci from " + dbstr + str(stuid) + " where name = '" + stuname + "' ORDER BY rowid DESC LIMIT 2"
        sql2 = "select lishiduanci from " + dbstr + str(classname) + " where name = '一本线' ORDER BY rowid DESC LIMIT 2"
    elif graphics == '地理':
        sql = "select dilibanci, diliduanci from " + dbstr + str(stuid) + " where name = '" + stuname + "' ORDER BY rowid DESC LIMIT 2"
        sql2 = "select diliduanci from " + dbstr + str(classname) + " where name = '一本线' ORDER BY rowid DESC LIMIT 2"
    elif graphics == '物理':
        sql = "select wulibanci, wuliduanci from " + dbstr + str(stuid) + " where name = '" + stuname + "' ORDER BY rowid DESC LIMIT 2"
        sql2 = "select wuliduanci from " + dbstr + str(classname) + " where name = '一本线' ORDER BY rowid DESC LIMIT 2"
    elif graphics == '化学':
        sql = "select huaxuebanci, huaxueduanci from " + dbstr + str(stuid) + " where name = '" + stuname + "' ORDER BY rowid DESC LIMIT 2"
        sql2 = "select huaxueduanci from " + dbstr + str(classname) + " where name = '一本线' ORDER BY rowid DESC LIMIT 2"
    elif graphics == '生物':
        sql = "select shengwubanci, shengwuduanci from " + dbstr + str(stuid) + " where name = '" + stuname + "' ORDER BY rowid DESC LIMIT 2"
        sql2 = "select shengwuduanci from " + dbstr + str(classname) + " where name = '一本线' ORDER BY rowid DESC LIMIT 2"
    elif graphics == '总分':
        sql = "select sumbanci, sumduanci from " + dbstr + str(stuid) + " where name = '" + stuname + "' ORDER BY rowid DESC LIMIT 2"
        sql2 = "select sumduanci from " + dbstr + str(classname) + " where name = '一本线' ORDER BY rowid DESC LIMIT 2"
    elif graphics == '理综':
        sql = "select lizongbanci, lizongduanci from " + dbstr + str(stuid) + " where name = '" + stuname + "' ORDER BY rowid DESC LIMIT 2"
        sql2 = "select lizongduanci from " + dbstr + str(classname) + " where name = '一本线' ORDER BY rowid DESC LIMIT 2"
    elif graphics == '文综':
        sql = "select wenzongbanci, wenzongduanci from " + dbstr + str(stuid) + " where name = '" + stuname + "' ORDER BY rowid DESC LIMIT 2"
        sql2 = "select wenzongduanci from " + dbstr + str(classname) + " where name = '一本线' ORDER BY rowid DESC LIMIT 2"
    else:
        sql = "select yuwenbanci, yuwenduanci from " + dbstr + str(stuid) + " where name = '" + stuname + "' ORDER BY rowid DESC LIMIT 2"
        sql2 = "select yuwenduanci from " + dbstr + str(classname) + " where name = '一本线' ORDER BY rowid DESC LIMIT 2"

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
        return "isnull",'isnull'
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
        return "isnull",'isnull'
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
    data = readxlsx('./2021级/1gaoerbanjixingmingxuehaoquan2.xlsx', 'Sheet1')
    classname = ""
    for tmp in data:
        breakflag = False
        if tmp == data[0]:
            continue
        print(tmp)
        classname = tmp[0]
        stuid = tmp[1]
        stuname = tmp[2]
        if (classname in SG3LK_2022) or (classname in SG2LK_2022):
            pname = ['总分', '语文', '数学', '外语', '物理', '化学', '生物', '理综']
        else:
            pname = ['总分', '语文', '数学', '外语', '政治', '历史', '地理', '文综']
        #print(pname)
        text = []
        xdata = []
        for x in pname:
            xdata,ydata = read_db_exam_banciduanci("21ji.db", classname, stuname, x, stuid, "s2021")
            #检查变量是否等于 "error" "isnull"
            if isinstance(xdata, str) and xdata == "1":
                print("没有这个表，跳过")
                breakflag = True
                break
            #print("xdata",xdata)
            #print("ydata",ydata)
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

            sql = "DELETE FROM s2021" + str(stuid)
            print(sql)
            hel[1].execute(sql)
            hel[1].commit()
            
            
            sql = "insert into s2021" + str(stuid) + """(LATESTEXAM,
                   SUMBANCIRAISE, SUMDUANCIRAISE, SUMOVERLINE,
                   YUWENBANCIRAISE, YUWENDUANCIRAISE, YUWENOVERLINE,
                   SHUXUEBANCIRAISE, SHUXUEDUANCIRAISE, SHUXUEOVERLINE,
                   YINGYUBANCIRAISE, YINGYUDUANCIRAISE, YINGYUOVERLINE,
                   WUZHENGBANCIRAISE, WUZHENGDUANCIRAISE, WUZHENGOVERLINE,
                   HUASHIBANCIRAISE, HUASHIDUANCIRAISE, HUASHIOVERLINE,
                   SHENGDIBANCIRAISE, SHENGDIDUANCIRAISE, SHENGDIOVERLINE,
                   LIWENBANCIRAISE, LIWENDUANCIRAISE, LIWENOVERLINE) 
                   values('""" + str(text[8]) + "'," + str(text[0][0]) + "," + str(text[0][1]) + "," + str(text[0][2]) + ","\
                   + str(text[1][0]) + "," + str(text[1][1]) + "," + str(text[1][2]) + ","\
                   + str(text[2][0]) + "," + str(text[2][1]) + "," + str(text[2][2]) + ","\
                   + str(text[3][0]) + "," + str(text[3][1]) + "," + str(text[3][2]) + ","\
                   + str(text[4][0]) + "," + str(text[4][1]) + "," + str(text[4][2]) + ","\
                   + str(text[5][0]) + "," + str(text[5][1]) + "," + str(text[5][2]) + ","\
                   + str(text[6][0]) + "," + str(text[6][1]) + "," + str(text[6][2]) + ","\
                   + str(text[7][0]) + "," + str(text[7][1]) + "," + str(text[7][2]) + ")"

            print(sql)
            hel[1].execute(sql)
            hel[1].commit()
            hel[1].close()



adddb("21jilatestanalysis.db")
#showalldb()







