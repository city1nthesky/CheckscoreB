import sqlite3
import openpyxl
import copy




#打开数据库
def opendb(dbname, classname):
    conn = sqlite3.connect(dbname)
    sql = "create table if not exists s2022" + str(classname) + """ (EXAM TEXT NOT NULL,
           SUM TEXT NOT NULL,YUWEN TEXT NOT NULL,SHUXUE TEXT NOT NULL,YINGYU TEXT NOT NULL,
           SELECT1 TEXT NOT NULL,SELECT2 TEXT NOT NULL,SELECT3 TEXT NOT NULL)"""
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
def adddb(dbname):
    welcome = """--------------------欢迎使用添加数据功能-----------------------"""
    print(welcome)
    data = readxlsx('./2022级/analysis/20230411/3gaoyibanjifenxi.xlsx', 'Sheet1')
    classname = ""
    for tmp in data:
        if tmp == data[0]:
            continue
        print(tmp)
        classname = tmp[0]
        hel = opendb(dbname, classname)
        
        

        sql = "insert into s2022" + str(classname) + """(EXAM, SUM,
               YUWEN, SHUXUE, YINGYU, SELECT1, SELECT2, SELECT3) 
               values(""" + "\""+ str(tmp[1]) + "\", \"" + str(tmp[2])+ "\"," + str(tmp[3]) +\
               "," + str(tmp[4]) + "," + str(tmp[5]) + "," + str(tmp[6]) + "," + str(tmp[7]) + "," + str(tmp[8]) + ")"
        print(sql)
        hel[1].execute(sql)
        hel[1].commit()
        hel[1].close()



adddb("22jiclassgrade.db")
#showalldb()







