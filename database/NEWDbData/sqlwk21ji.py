import sqlite3
import openpyxl
import copy




#打开数据库
def opendb(dbname, classname):
    conn = sqlite3.connect(dbname)
    sql = "create table if not exists s2021" + str(classname) + """ (NAME TEXT NOT NULL, EXAM TEXT,
           SUM TEXT, SUMBANCI TEXT, SUMDUANCI TEXT,
           YUWEN TEXT, YUWENBANCI TEXT, YUWENDUANCI TEXT,
           SHUXUE TEXT, SHUXUEBANCI TEXT, SHUXUEDUANCI TEXT,
           YINGYU TEXT, YINGYUBANCI TEXT, YINGYUDUANCI TEXT,
           ZHENGZHI TEXT, ZHENGZHIBANCI TEXT, ZHENGZHIDUANCI TEXT,
           LISHI TEXT, LISHIBANCI TEXT, LISHIDUANCI TEXT,
           DILI TEXT, DILIBANCI TEXT, DILIDUANCI TEXT,
           WENZONG TEXT, WENZONGBANCI TEXT, WENZONGDUANCI TEXT)"""

    print(sql)
    cur = conn.execute(sql)


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
    print("I am coming")
    # 打开文件 获取workbook
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
    data = readxlsx('./2021级/20230407/2gaoeryuekaoBwenkeyibenxian.xlsx', 'Sheet1')
    classname = ""
    for tmp in data:
        if tmp == data[0]:
            continue
        print(tmp)
        classname = tmp[0]
        hel = opendb(dbname, classname)
        
        

        sql = "insert into s2021" + str(classname) + """(NAME, EXAM, SUM, SUMBANCI, SUMDUANCI,
               YUWEN, YUWENBANCI, YUWENDUANCI, SHUXUE, SHUXUEBANCI, SHUXUEDUANCI, YINGYU, YINGYUBANCI, YINGYUDUANCI,
               ZHENGZHI, ZHENGZHIBANCI, ZHENGZHIDUANCI, LISHI, LISHIBANCI, LISHIDUANCI, DILI, DILIBANCI, DILIDUANCI,
               WENZONG, WENZONGBANCI, WENZONGDUANCI)values(""" + "\""+ str(tmp[1]) + "\", \"" + str(tmp[2])+ "\"," + str(tmp[3]) +\
               "," + str(tmp[4]) + "," + str(tmp[5]) + "," + str(tmp[6]) + "," + str(tmp[7]) + "," + str(tmp[8]) +\
               "," + str(tmp[9]) + "," + str(tmp[10]) + "," + str(tmp[11]) + "," + str(tmp[12]) + "," + str(tmp[13]) +\
               "," + str(tmp[14]) + "," + str(tmp[15]) + "," + str(tmp[16]) + "," + str(tmp[17]) + "," + str(tmp[18]) +\
               "," + str(tmp[19]) + "," + str(tmp[20]) + "," + str(tmp[21]) + "," + str(tmp[22]) + "," + str(tmp[23]) +\
               "," + str(tmp[24]) + "," + str(tmp[25]) + "," + str(tmp[26]) + ")"
        print(sql)
        hel[1].execute(sql)
        hel[1].commit()
        hel[1].close()



adddb("21ji.db")
#showalldb()







