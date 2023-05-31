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
           WULI TEXT, WULIBANCI TEXT, WULIDUANCI TEXT,
           HUAXUE TEXT, HUAXUEBANCI TEXT, HUAXUEDUANCI TEXT,
           SHENGWU TEXT, SHENGWUBANCI TEXT, SHENGWUDUANCI TEXT,
           LIZONG TEXT, LIZONGBANCI TEXT, LIZONGDUANCI TEXT)"""

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
def deldb(dbname):
    welcome = """--------------------欢迎使用删除数据功能-----------------------"""
    print(welcome)
    data = readxlsx('./2021级/20230422/4gaoerxiaqizhongwenkechengji.xlsx', 'Sheet1')
    classname = ""
    for tmp in data:
        if tmp == data[0]:
            continue
        print(tmp)
        classname = tmp[0]
        hel = opendb(dbname, classname)
        
        

        sql = "delete from s2021" + str(classname) + " where EXAM = '" + str(tmp[2]) + "'"
        print(sql)
        hel[1].execute(sql)
        hel[1].commit()
        hel[1].close()



deldb("21ji.db")
#showalldb()







