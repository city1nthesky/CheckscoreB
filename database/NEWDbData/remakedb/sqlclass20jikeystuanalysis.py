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


#获取学生整体的分析 如果sql语句执行失败返回error 如果数据为空返回isnull
def read_db_studata_allanalysis(dbname, classname, stuid):
    #reload(sys)
    #sys.setdefaultencoding('utf8')


    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    sql = "select * from CurrentStuAllScoreAnalysis where student_id = " + str(stuid)
    #print("sql",sql)

    try:
        # 执行SQL语句
        cursor = c.execute(sql)
    except sqlite3.Error as e:
        # 打印异常信息
        conn.close()
        print("error")
        return "error"

    text = []
    tmpallsubjects = []

    results = cursor.fetchall()
    # 检查查询结果是否为空
    if not results:
        conn.close()
        print("isnull")
        return "isnull"
    else:
        # 处理查询结果
        for row in results:
            #print(results)
            text.append({'totalNum': row[1]})
            if row[1] != 0:
                tmpallsubjects.append({'name': '总分','passNum' : row[2], 'passRate': round(row[2] / row[1] *100, 1)})
                tmpallsubjects.append({'name': '语文','passNum' : row[3], 'passRate': round(row[3] / row[1] *100, 1)})
                tmpallsubjects.append({'name': '数学','passNum' : row[4], 'passRate': round(row[4] / row[1] *100, 1)})
                tmpallsubjects.append({'name': '外语','passNum' : row[5], 'passRate': round(row[5] / row[1] *100, 1)})
            else:
                tmpallsubjects.append({'name': '总分','passNum' : 0, 'passRate': 0})
                tmpallsubjects.append({'name': '语文','passNum' : 0, 'passRate': 0})
                tmpallsubjects.append({'name': '数学','passNum' : 0, 'passRate': 0})
                tmpallsubjects.append({'name': '外语','passNum' : 0, 'passRate': 0})
            if classname in (SG2LK_2022 + SG3LK_2022):
                if row[1] != 0:
                    tmpallsubjects.append({'name': '物理','passNum' : row[6], 'passRate': round(row[6] / row[1] *100, 1)})
                    tmpallsubjects.append({'name': '化学','passNum' : row[7], 'passRate': round(row[7] / row[1] *100, 1)})
                    tmpallsubjects.append({'name': '生物','passNum' : row[8], 'passRate': round(row[8] / row[1] *100, 1)})
                    tmpallsubjects.append({'name': '理综','passNum' : row[9], 'passRate': round(row[9] / row[1] *100, 1)})
                else:
                    tmpallsubjects.append({'name': '物理','passNum' : 0, 'passRate': 0})
                    tmpallsubjects.append({'name': '化学','passNum' : 0, 'passRate': 0})
                    tmpallsubjects.append({'name': '生物','passNum' : 0, 'passRate': 0})
                    tmpallsubjects.append({'name': '理综','passNum' : 0, 'passRate': 0})
            elif classname in (SG2WK_2022 + SG3WK_2022):
                if row[1] != 0:
                    tmpallsubjects.append({'name': '政治','passNum' : row[6], 'passRate': round(row[6] / row[1] *100, 1)})
                    tmpallsubjects.append({'name': '历史','passNum' : row[7], 'passRate': round(row[7] / row[1] *100, 1)})
                    tmpallsubjects.append({'name': '地理','passNum' : row[8], 'passRate': round(row[8] / row[1] *100, 1)})
                    tmpallsubjects.append({'name': '文综','passNum' : row[9], 'passRate': round(row[9] / row[1] *100, 1)})
                else:
                    tmpallsubjects.append({'name': '政治','passNum' : 0, 'passRate': 0})
                    tmpallsubjects.append({'name': '历史','passNum' : 0, 'passRate': 0})
                    tmpallsubjects.append({'name': '地理','passNum' : 0, 'passRate': 0})
                    tmpallsubjects.append({'name': '文综','passNum' : 0, 'passRate': 0})
            elif classname in SG1WHS_2022:
                if row[1] != 0:
                    tmpallsubjects.append({'name': '物理','passNum' : row[6], 'passRate': round(row[6] / row[1] *100, 1)})
                    tmpallsubjects.append({'name': '化学','passNum' : row[7], 'passRate': round(row[7] / row[1] *100, 1)})
                    tmpallsubjects.append({'name': '生物','passNum' : row[8], 'passRate': round(row[8] / row[1] *100, 1)})
                else:
                    tmpallsubjects.append({'name': '物理','passNum' : 0, 'passRate': 0})
                    tmpallsubjects.append({'name': '化学','passNum' : 0, 'passRate': 0})
                    tmpallsubjects.append({'name': '生物','passNum' : 0, 'passRate': 0})
            elif classname in SG1WHD_2022:
                if row[1] != 0:
                    tmpallsubjects.append({'name': '物理','passNum' : row[6], 'passRate': round(row[6] / row[1] *100, 1)})
                    tmpallsubjects.append({'name': '化学','passNum' : row[7], 'passRate': round(row[7] / row[1] *100, 1)})
                    tmpallsubjects.append({'name': '地理','passNum' : row[8], 'passRate': round(row[8] / row[1] *100, 1)})
                else:
                    tmpallsubjects.append({'name': '物理','passNum' : 0, 'passRate': 0})
                    tmpallsubjects.append({'name': '化学','passNum' : 0, 'passRate': 0})
                    tmpallsubjects.append({'name': '地理','passNum' : 0, 'passRate': 0})
            elif classname in SG1WHZ_2022:
                if row[1] != 0:
                    tmpallsubjects.append({'name': '物理','passNum' : row[6], 'passRate': round(row[6] / row[1] *100, 1)})
                    tmpallsubjects.append({'name': '化学','passNum' : row[7], 'passRate': round(row[7] / row[1] *100, 1)})
                    tmpallsubjects.append({'name': '政治','passNum' : row[6], 'passRate': round(row[6] / row[1] *100, 1)})
                else:
                    tmpallsubjects.append({'name': '物理','passNum' : 0, 'passRate': 0})
                    tmpallsubjects.append({'name': '化学','passNum' : 0, 'passRate': 0})
                    tmpallsubjects.append({'name': '政治','passNum' : 0, 'passRate': 0})
            elif classname in SG1SZD_2022:
                if row[1] != 0:
                    tmpallsubjects.append({'name': '政治','passNum' : row[6], 'passRate': round(row[6] / row[1] *100, 1)})
                    tmpallsubjects.append({'name': '历史','passNum' : row[7], 'passRate': round(row[7] / row[1] *100, 1)})
                    tmpallsubjects.append({'name': '地理','passNum' : row[8], 'passRate': round(row[8] / row[1] *100, 1)})
                else:
                    tmpallsubjects.append({'name': '政治','passNum' : 0, 'passRate': 0})
                    tmpallsubjects.append({'name': '历史','passNum' : 0, 'passRate': 0})
                    tmpallsubjects.append({'name': '地理','passNum' : 0, 'passRate': 0})
            elif classname in SG1SZS_2022:
                if row[1] != 0:
                    tmpallsubjects.append({'name': '政治','passNum' : row[6], 'passRate': round(row[6] / row[1] *100, 1)})
                    tmpallsubjects.append({'name': '历史','passNum' : row[7], 'passRate': round(row[7] / row[1] *100, 1)})
                    tmpallsubjects.append({'name': '生物','passNum' : row[8], 'passRate': round(row[8] / row[1] *100, 1)})
                else:
                    tmpallsubjects.append({'name': '政治','passNum' : 0, 'passRate': 0})
                    tmpallsubjects.append({'name': '历史','passNum' : 0, 'passRate': 0})
                    tmpallsubjects.append({'name': '生物','passNum' : 0, 'passRate': 0})
            text.append(tmpallsubjects)

    print("text",text)
    return text



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
    data = readxlsx('../2022级/1gaoyibanjixingmingxuehao.xlsx', 'Sheet1')
    classname = ""
    for tmp in data:
        print(tmp)
        if tmp == data[0]:
            continue
        #print(tmp)
        classname = str(tmp[0])
        stuid = str(tmp[1])
        stuname = tmp[2]

        text = read_db_studata_allanalysis(dbname, classname, stuid)
        print(text)
        for i in range(7):
            print(text[1][i])
            partname = text[1][i]["name"]
            rate = text[1][i]["passRate"]
            if 60<= rate <70:
                sql = "insert into CurrentClassKeyStuAnalysis" + """(student_id, student_name, Class,
                       Part, Rate
                       ) 
                       values(""" + str(stuid) + ", '" + str(stuname) + "', "\
                       + str(classname) + ",'" + str(partname) + "', " +  str(rate) + ")"
                print(sql)
                hel = opendb(dbname, "222")
                try:
                    # 执行SQL语句
                    hel[1].execute(sql)
                except sqlite3.Error as e:
                    # 打印异常信息
                    print(e)
                    print("error1")
                    return
                hel[1].commit()
                hel[1].close()



adddb("xcyg.db")
#showalldb()







