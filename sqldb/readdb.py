# -*- coding: utf-8 -*-#
# filename: readdb.py

import sqlite3
#import sys
import importlib,sys
importlib.reload(sys)

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

#获取班级临界生分析 如果sql语句执行失败返回error 如果数据为空返回isnull
def read_db_class_keystu_analysis(dbname, classname, keystuflag, exam = '考试'):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    text = []
    part = ['总分','语文','数学','外语']
    if classname in (SG2LK_2022 + SG3LK_2022 + SG1WHS_2022):
        part.append('物理')
        part.append('化学')
        part.append('生物')
    elif classname in (SG2WK_2022 + SG3WK_2022):
        part.append('政治')
        part.append('历史')
        part.append('地理')
    elif classname in SG1WHD_2022:
        part.append('物理')
        part.append('化学')
        part.append('地理')
    elif classname in SG1WHZ_2022:
        part.append('物理')
        part.append('政治')
        part.append('化学')
    elif classname in SG1SZD_2022:
        part.append('历史')
        part.append('政治')
        part.append('地理')
    elif classname in SG1SZS_2022:
        part.append('历史')
        part.append('政治')
        part.append('生物')
    else:
        return "error"

    if keystuflag == '1':
        for x in part:
            sql = "select * from CurrentClassKeyStuAnalysis where Class = " + classname + " and Part = '" +str(x) + "' limit 8"
            try:
                # 执行SQL语句
                cursor = c.execute(sql)
            except sqlite3.Error as e:
                # 打印异常信息
                conn.close()
                print("error")
                return "error"

            results = cursor.fetchall()
            # 检查查询结果是否为空
            if not results:
                conn.close()
                print("isnull")
                return "isnull"
            else:
                # 处理查询结果
                data = {'name':' ', 'data':[]}
                if x == '总分':
                    data['name'] = '总分'
                elif x == '语文':
                    data['name'] = '语文'
                elif x == '数学':
                    data['name'] = '数学'
                elif x == '外语':
                    data['name'] = '外语'
                elif x == '物理':
                    data['name'] = '物理'
                elif x == '化学':
                    data['name'] = '化学'
                elif x == '生物':
                    data['name'] = '生物'
                elif x == '政治':
                    data['name'] = '政治'
                elif x == '历史':
                    data['name'] = '历史'
                elif x == '地理':
                    data['name'] = '地理'
                else:
                    return "error"
                stuname = []
                rate = []
                for row in results:
                    stuname.append(row[2])
                    rate.append(row[5])
                    if len(stuname) == 4:
                        data['data'].append(stuname)
                        data['data'].append(rate)
                        stuname = []
                        rate = []
                if len(stuname) != 0:
                    data['data'].append(stuname)
                    data['data'].append(rate)
                text.append(data)
    else:
        for x in part:
            if classname in (SG1WHS_2022 + SG1WHZ_2022 + SG1WHD_2022 + SG1SZD_2022 + SG1SZS_2022):
                grade = '高一'
            elif classname in (SG2WK_2022 + SG2LK_2022):
                grade = '高二'
            else:
                grade = '高三'
            if classname in (SG1WHS_2022 + SG1WHZ_2022 + SG1WHD_2022 + SG2LK_2022 + SG3LK_2022):
                line = '理科一本线'
            else:
                line = '文科一本线'

            data = {'name':' ', 'data':[]}
            if x == '总分':
                data['name'] = '总分'
                sql = "select SumD from SchoolLINE where line = '" + line + "' and exam = '" + exam + "' and grade = '" + grade + "'"
                sql2 = "select student_id, SumD from CurrentScore where SumD between "
            elif x == '语文':
                data['name'] = '语文'
                sql = "select YuwenD from SchoolLINE where line = '" + line + "' and exam = '" + exam + "' and grade = '" + grade + "'"
                sql2 = "select student_id, YuwenD from CurrentScore where YuwenD between "
            elif x == '数学':
                data['name'] = '数学'
                sql = "select ShuxueD from SchoolLINE where line = '" + line + "' and exam = '" + exam + "' and grade = '" + grade + "'"
                sql2 = "select student_id, ShuxueD from CurrentScore where ShuxueD between "
            elif x == '外语':
                data['name'] = '外语'
                sql = "select WaiyuD from SchoolLINE where line = '" + line + "' and exam = '" + exam + "' and grade = '" + grade + "'"
                sql2 = "select student_id, WaiyuD from CurrentScore where WaiyuD between "
            elif x == '物理':
                data['name'] = '物理'
                sql = "select Select1D from SchoolLINE where line = '" + line + "' and exam = '" + exam + "' and grade = '" + grade + "'"
                sql2 = "select student_id, Select1D from CurrentScore where Select1D between "
            elif x == '化学':
                data['name'] = '化学'
                sql = "select Select2D from SchoolLINE where line = '" + line + "' and exam = '" + exam + "' and grade = '" + grade + "'"
                sql2 = "select student_id, Select2D from CurrentScore where Select2D between "
            elif x == '生物':
                data['name'] = '生物'
                sql = "select Select3D from SchoolLINE where line = '" + line + "' and exam = '" + exam + "' and grade = '" + grade + "'"
                sql2 = "select student_id, Select3D from CurrentScore where Select3D between "
            elif x == '政治':
                data['name'] = '政治'
                if classname in (SG2WK_2022 + SG3WK_2022):
                    sql = "select Select1D from SchoolLINE where line = '" + line + "' and exam = '" + exam + "' and grade = '" + grade + "'"
                    sql2 = "select student_id, Select1D from CurrentScore where Select1D between "
                elif classname in SG1WHZ_2022:
                    sql = "select Select3D from SchoolLINE where line = '" + line + "' and exam = '" + exam + "' and grade = '" + grade + "'"
                    sql2 = "select student_id, Select3D from CurrentScore where Select3D between "
                elif classname in SG1SZD_2022:
                    sql = "select Select2D from SchoolLINE where line = '" + line + "' and exam = '" + exam + "' and grade = '" + grade + "'"
                    sql2 = "select student_id, Select2D from CurrentScore where Select2D between "
                else:
                    return "error"
            elif x == '历史':
                data['name'] = '历史'
                if classname in (SG2WK_2022 + SG3WK_2022):
                    sql = "select Select2D from SchoolLINE where line = '" + line + "' and exam = '" + exam + "' and grade = '" + grade + "'"
                    sql2 = "select student_id, Select2D from CurrentScore where Select2D between "
                elif classname in (SG1SZD_2022 + SG1SZS_2022):
                    sql = "select Select1D from SchoolLINE where line = '" + line + "' and exam = '" + exam + "' and grade = '" + grade + "'"
                    sql2 = "select student_id, Select1D from CurrentScore where Select1D between "
                else:
                    return "error"
            elif x == '地理':
                data['name'] = '地理'
                sql = "select Select3D from SchoolLINE where line = '" + line + "' and exam = '" + exam + "' and grade = '" + grade + "'"
                sql2 = "select student_id, Select3D from CurrentScore where Select3D between "
            else:
                return "error"
            #print(sql)
            try:
                # 执行SQL语句
                cursor = c.execute(sql)
            except sqlite3.Error as e:
                # 打印异常信息
                conn.close()
                print("error")
                return "error"

            results = cursor.fetchall()
            # 检查查询结果是否为空
            if not results:
                conn.close()
                print("isnull")
                return "isnull"
            else:
                # 处理查询结果
                stuname = []
                rate = []
                for row in results:
                    sql2 = sql2 + str(int(row[0]) - 150) + " and " + str(int(row[0] + 150)) +" and class = " + str(classname) + " and exam = '" + str(exam) + "' limit 8"
                    #print(sql2)
                    try:
                        # 执行SQL语句
                        cursor = c.execute(sql2)
                    except sqlite3.Error as e:
                        # 打印异常信息
                        conn.close()
                        print("error")
                        return "error"

                    results = cursor.fetchall()
                    # 检查查询结果是否为空
                    if not results:
                        conn.close()
                        print("isnull")
                        return "isnull"
                    else:
                        # 处理查询结果
                        for row in results:
                            sql3 = "select student_name from CurrentStudent where student_id = " + str(row[0])
                            #print(sql3)
                            try:
                                # 执行SQL语句
                                cursor = c.execute(sql3)
                            except sqlite3.Error as e:
                                # 打印异常信息
                                conn.close()
                                print("error")
                                return "error"

                            results3 = cursor.fetchall()
                            # 检查查询结果是否为空
                            if not results3:
                                conn.close()
                                print("isnull")
                                return "isnull"
                            else:
                                # 处理查询结果
                                for row3 in results3:
                                    stuname.append(row3)
                            rate.append(row[1])
                            if len(stuname) == 4:
                                data['data'].append(stuname)
                                data['data'].append(rate)
                                stuname = []
                                rate = []
                        if len(stuname) != 0:
                            data['data'].append(stuname)
                            data['data'].append(rate)
                        text.append(data)


    #print(text)
    return text

#获取班级分析 如果sql语句执行失败返回error 如果数据为空返回isnull
def read_db_class_allexam_analysis(dbname, classname, partindex = 0):
    #reload(sys)
    #sys.setdefaultencoding('utf8')

    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    text = {"th":[], "td":[]}
    th = []
    td = []
    mysum = []
    yuwen = []
    shuxue = []
    yingyu = []
    select1 = []
    select2 = []
    select3 = []
    gradepart = []
    count = int(partindex)

    if classname in (SG1WHS_2022 + SG1WHZ_2022 + SG1WHD_2022 + SG1SZD_2022 + SG1SZS_2022 + SG2LK_2022 + SG2WK_2022 + SG3LK_2022 + SG3WK_2022):
        th.append("学科/考试")
        mysum.append("总分")
        yuwen.append("语文")
        shuxue.append("数学")
        yingyu.append("外语")
    elif classname == "高三":
        th.append("类别/考试")
        gradepart = ['理一部','理二部','理三部','理复习','文应届','文复习']
    elif classname == "高二":
        th.append("类别/考试")
        gradepart = ['理一部','理二部','理三部','文一部','文二部','文三部']
    elif classname == "高一":
        th.append("类别/考试")
        gradepart = ['一部','二部','三部']
    else:
        return "error"


    if not gradepart:

        sql = "select * from CurrentClassGradeAnalysis where ClassGrade = " + classname + " ORDER BY id DESC"
        #print("sql",sql)

        try:
            # 执行SQL语句
            cursor = c.execute(sql)
        except sqlite3.Error as e:
            # 打印异常信息
            conn.close()
            print("error")
            return "error"


        if classname in (SG2LK_2022 + SG3LK_2022 + SG1WHS_2022):
            select1.append("物理")
            select2.append("化学")
            select3.append("生物")
        elif classname in (SG2WK_2022 + SG3WK_2022):
            select1.append("政治")
            select2.append("历史")
            select3.append("地理")
        elif classname in SG1WHD_2022:
            select1.append("物理")
            select2.append("化学")
            select3.append("地理")
        elif classname in SG1WHZ_2022:
            select1.append("物理")
            select2.append("化学")
            select3.append("政治")
        elif classname in SG1SZD_2022:
            select1.append("历史")
            select2.append("政治")
            select3.append("地理")
        elif classname in SG1SZS_2022:
            select1.append("历史")
            select2.append("政治")
            select3.append("生物")
        else:
            return "error"

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
                th.append(row[4])
                mysum.append(row[5])
                yuwen.append(row[6])
                shuxue.append(row[7])
                yingyu.append(row[8])
                select1.append(row[9])
                select2.append(row[10])
                select3.append(row[11])

        text["th"] = th
        text["td"] = [mysum,yuwen,shuxue,yingyu,select1,select2,select3]
    else:
        ffirst = True
        for x in gradepart:
            sql = "select * from CurrentClassGradeAnalysis where ClassGrade = '" + str(x) + "' and Grade = '" + str(classname) +  "' and Year = '2023s'  ORDER BY id DESC"
            #print("sql",sql)

            try:
                # 执行SQL语句
                cursor = c.execute(sql)
            except sqlite3.Error as e:
                # 打印异常信息
                conn.close()
                print("error")
                return "error"

            results = cursor.fetchall()
            # 检查查询结果是否为空
            if not results:
                conn.close()
                print("isnull")
                return "isnull"
            else:
                # 处理查询结果
                tmplist = [x]
                for row in results:
                    #print(results)
                    #print(row)
                    if ffirst:
                        th.append(row[4])
                    tmplist.append(row[5+count])
                ffirst = False
                #tmplist[0] = row[1]
                td.append(tmplist)
        
        text["th"] = th
        text["td"] = td

    #print("text",text)
    return text


#获取学生最近一次考试的分析 如果sql语句执行失败返回error 如果数据为空返回isnull
def read_db_studata_latestanalysis(dbname, classname, stuid):
    #reload(sys)
    #sys.setdefaultencoding('utf8')


    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    c2 = conn.cursor()

    sql = "select * from CurrentScore where student_id =  " + str(stuid) + " ORDER BY id DESC LIMIT 2"
    #print(sql)

    try:
        # 执行SQL语句
        cursor = c.execute(sql)
    except sqlite3.Error as e:
        # 打印异常信息
        conn.close()
        print(e)
        print("error")
        return "error"

    text = []
    tmpallsubjects = []

    if classname in (SG1WHS_2022 + SG1WHZ_2022 + SG1WHD_2022 + SG1SZD_2022 + SG1SZS_2022):
        grade = '高一'
    elif classname in (SG2WK_2022 + SG2LK_2022):
        grade = '高二'
    else:
        grade = '高三'
    if classname in (SG1WHS_2022 + SG1WHZ_2022 + SG1WHD_2022 + SG2LK_2022 + SG3LK_2022):
        line = '理科一本线'
    else:
        line = '文科一本线'

    results = cursor.fetchall()
    # 检查查询结果是否为空
    if not results:
        conn.close()
        print("isnull")
        return "isnull"
    else:
        # 处理查询结果
        if len(results) == 2:
            row = list()
            row.append(results[0][4])
            sql2 = "select * from SchoolLINE where line = '" + line + "' and exam = '" + str(results[0][4]) + "' and grade = '" + grade + "'"
            #print(sql2)

            try:
                # 执行SQL语句
                cursor2 = c2.execute(sql2)
            except sqlite3.Error as e:
                # 打印异常信息
                conn.close()
                print(e)
                print("error")
                return "error"
            results2 = cursor2.fetchall()

            #L = len(results[0])
            #for i in range((L - 6)//3):
            for i in range(8):
                row.append(results[1][8+i*3] - results[0][8+i*3])
                row.append(results[1][9+i*3] - results[0][9+i*3])
                if not (classname in (SG1WHS_2022 + SG1WHZ_2022 + SG1WHD_2022 + SG1SZD_2022 + SG1SZS_2022) and i == 7):
                    row.append(True if results[0][9+i*3] <=  results2[0][8+i*2] else False)
        elif len(results) == 1:
            row = list()
            row.append(results[0][4])
            sql2 = "select * from SchoolLINE where line = '" + line + "' and exam = '" + str(results[0][4]) + "' and grade = '" + grade + "'"
            #print(sql2)

            try:
                # 执行SQL语句
                cursor2 = c2.execute(sql2)
            except sqlite3.Error as e:
                # 打印异常信息
                conn.close()
                print(e)
                print("error")
                return "error"
            results2 = cursor2.fetchall()

            if classname in (SG2LK_2022 + SG3LK_2022 + SG2WK_2022 + SG3WK_2022):
                a = 8
            else:
                a=7
            for i in range(a):
                row.append(0)
                row.append(0)
                row.append(True if results[0][9+i*3] <=  results2[0][8+i*2] else False)
            
        #print("row", row)
        text.append({'thisExam': row[0]})
        tmpallsubjects.append({'name': '总分','riseNumB': row[1], 'riseNumD': row[2], 'passflag': row[3]})
        tmpallsubjects.append({'name': '语文','riseNumB': row[4], 'riseNumD': row[5], 'passflag': row[6]})
        tmpallsubjects.append({'name': '数学','riseNumB': row[7], 'riseNumD': row[8], 'passflag': row[9]})
        tmpallsubjects.append({'name': '外语','riseNumB': row[10], 'riseNumD': row[11], 'passflag': row[12]})
        if classname in (SG2LK_2022 + SG3LK_2022):
            tmpallsubjects.append({'name': '物理','riseNumB': row[13], 'riseNumD': row[14], 'passflag': row[15]})
            tmpallsubjects.append({'name': '化学','riseNumB': row[16], 'riseNumD': row[17], 'passflag': row[18]})
            tmpallsubjects.append({'name': '生物','riseNumB': row[19], 'riseNumD': row[20], 'passflag': row[21]})
            tmpallsubjects.append({'name': '理综','riseNumB': row[22], 'riseNumD': row[23], 'passflag': row[24]})
        elif classname in (SG2WK_2022 + SG3WK_2022):
            tmpallsubjects.append({'name': '政治','riseNumB': row[13], 'riseNumD': row[14], 'passflag': row[15]})
            tmpallsubjects.append({'name': '历史','riseNumB': row[16], 'riseNumD': row[17], 'passflag': row[18]})
            tmpallsubjects.append({'name': '地理','riseNumB': row[19], 'riseNumD': row[20], 'passflag': row[21]})
            tmpallsubjects.append({'name': '文综','riseNumB': row[22], 'riseNumD': row[23], 'passflag': row[24]})
        elif classname in SG1WHS_2022:
            tmpallsubjects.append({'name': '物理','riseNumB': row[13], 'riseNumD': row[14], 'passflag': row[15]})
            tmpallsubjects.append({'name': '化学','riseNumB': row[16], 'riseNumD': row[17], 'passflag': row[18]})
            tmpallsubjects.append({'name': '生物','riseNumB': row[19], 'riseNumD': row[20], 'passflag': row[21]})
        elif classname in SG1WHD_2022:
            tmpallsubjects.append({'name': '物理','riseNumB': row[13], 'riseNumD': row[14], 'passflag': row[15]})
            tmpallsubjects.append({'name': '化学','riseNumB': row[16], 'riseNumD': row[17], 'passflag': row[18]})
            tmpallsubjects.append({'name': '地理','riseNumB': row[19], 'riseNumD': row[20], 'passflag': row[21]})
        elif classname in SG1WHZ_2022:
            tmpallsubjects.append({'name': '物理','riseNumB': row[13], 'riseNumD': row[14], 'passflag': row[15]})
            tmpallsubjects.append({'name': '化学','riseNumB': row[16], 'riseNumD': row[17], 'passflag': row[18]})
            tmpallsubjects.append({'name': '政治','riseNumB': row[19], 'riseNumD': row[20], 'passflag': row[21]})
        elif classname in SG1SZD_2022:
            tmpallsubjects.append({'name': '历史','riseNumB': row[13], 'riseNumD': row[14], 'passflag': row[15]})
            tmpallsubjects.append({'name': '政治','riseNumB': row[16], 'riseNumD': row[17], 'passflag': row[18]})
            tmpallsubjects.append({'name': '地理','riseNumB': row[19], 'riseNumD': row[20], 'passflag': row[21]})
        elif classname in SG1SZS_2022:
            tmpallsubjects.append({'name': '历史','riseNumB': row[13], 'riseNumD': row[14], 'passflag': row[15]})
            tmpallsubjects.append({'name': '政治','riseNumB': row[16], 'riseNumD': row[17], 'passflag': row[18]})
            tmpallsubjects.append({'name': '生物','riseNumB': row[19], 'riseNumD': row[20], 'passflag': row[21]})
        text.append(tmpallsubjects)

    #print("text",text)
    return text


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

    #print("text",text)
    return text



#获取学生某科成绩 如果sql语句执行失败返回error 如果数据为空返回isnull
def read_db_drawpic_score(dbname, classname, stuname, graphics, selectcount, stuid):
    #reload(sys)
    #sys.setdefaultencoding('utf8')
    #print(dbname,classname,stuname,graphics,selectcount,stuid,dbstr)
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    title = u""
    title += (stuname + graphics + "折线图")
    #获取该学生参加的所有考试名称
    sql2 = "select exam from CurrentScore where show = 1 and student_id  = " + stuid
    #print(sql2)
    try:
        # 执行SQL语句
        cursor = c.execute(sql2)
    except sqlite3.Error as e:
        # 打印异常信息
        conn.close()
        #print("error1")
        return "error","error","error","error"
    tmp = ""
    results = cursor.fetchall()
    # 检查查询结果是否为空
    if not results:
        conn.close()
        #print("isnull1")
        return "isnull","isnull","isnull","isnull"
    else:
        # 处理查询结果
        for row in results:
            tmp += row[0]
            tmp += " "
    #获取该学生参加的所有考试某科成绩
    x_data = tmp.split()
    if selectcount == 1:
        sql = "select Sum from CurrentScore  where show = 1 and student_id  = " + stuid
    elif selectcount == 2:
        sql = "select Yuwen from CurrentScore  where show = 1 and student_id  = " + stuid
    elif selectcount == 3:
        sql = "select Shuxue from CurrentScore  where show = 1 and student_id  = " + stuid
    elif selectcount == 4:
        sql = "select Waiyu from CurrentScore  where show = 1 and student_id  = " + stuid
    elif selectcount == 5:
        sql = "select Select1 from CurrentScore  where show = 1 and student_id  = " + stuid
    elif selectcount == 6:
        sql = "select Select2 from CurrentScore  where show = 1 and student_id  = " + stuid
    elif selectcount == 7:
        sql = "select Select3 from CurrentScore  where show = 1 and student_id  = " + stuid
    elif selectcount == 8:
        sql = "select Zonghe from CurrentScore  where show = 1 and student_id  = " + stuid

    #print(sql)
    try:
        # 执行SQL语句
        cursor = c.execute(sql)
    except sqlite3.Error as e:
        # 打印异常信息
        conn.close()
        #print("error2")
        return "error","error","error","error"
    tmp = ""
    results = cursor.fetchall()
    # 检查查询结果是否为空
    if not results:
        conn.close()
        #print("isnull2")
        return "isnull","isnull","isnull","isnull"
    else:
        # 处理查询结果
        for row in results:
            tmp += str(row[0])
            tmp += " "

    #把获取的学生的所有考试的某科成绩段次添加到字典中
    str_y_data = tmp.split()
    y_data =[{"stu": [float(x) for x in str_y_data]}]
    #datalist  =[graphics + "段次"]
    datalist  =[graphics]

    tmp = ""
    if classname in (SG1WHS_2022 + SG1WHZ_2022 + SG1WHD_2022 + SG1SZD_2022 + SG1SZS_2022):
        grade = '高一'
    elif classname in (SG2WK_2022 + SG2LK_2022):
        grade = '高二'
    else:
        grade = '高三'
    if classname in (SG1WHS_2022 + SG1WHZ_2022 + SG1WHD_2022 + SG2LK_2022 + SG3LK_2022):
        line = '理科一本线'
    else:
        line = '文科一本线'

    #获取该学生参加的所有考试某科成绩段次的一本线数据
    
    for x in x_data:
        if selectcount == 1:
            sql = "select Sum from SchoolLINE where line = '" + line + "' and exam = '" + str(x) + "' and grade = '" + grade + "'"
        elif selectcount == 2:
            sql = "select Yuwen from SchoolLINE where line = '" + line + "' and exam = '" + str(x) + "' and grade = '" + grade + "'"
        elif selectcount == 3:
            sql = "select Shuxue from SchoolLINE where line = '" + line + "' and exam = '" + str(x) + "' and grade = '" + grade + "'"
        elif selectcount == 4:
            sql = "select Waiyu from SchoolLINE where line = '" + line + "' and exam = '" + str(x) + "' and grade = '" + grade + "'"
        elif selectcount == 5:
            sql = "select Select1 from SchoolLINE where line = '" + line + "' and exam = '" + str(x) + "' and grade = '" + grade + "'"
        elif selectcount == 6:
            sql = "select Select2 from SchoolLINE where line = '" + line + "' and exam = '" + str(x) + "' and grade = '" + grade + "'"
        elif selectcount == 7:
            sql = "select Select3 from SchoolLINE where line = '" + line + "' and exam = '" + str(x) + "' and grade = '" + grade + "'"
        elif selectcount == 8:
            sql = "select Zonghe from SchoolLINE where line = '" + line + "' and exam = '" + str(x) + "' and grade = '" + grade + "'"
        #print(sql)
        try:
            # 执行SQL语句
            cursor = c.execute(sql)
        except sqlite3.Error as e:
            # 打印异常信息
            conn.close()
            #print("error3")
            return "error","error","error","error"
        results = cursor.fetchall()
        # 检查查询结果是否为空
        if not results:
            #conn.close()
            #print("isnull3")
            #return "isnull","isnull","isnull","isnull"
            break
        else:
            # 处理查询结果
            for row in results:
                if selectcount == 8 and row[0] == None:
                    break;
                tmp += str(row[0])
                tmp += " "
    if selectcount == 8 and classname in (SG1WHS_2022 + SG1WHZ_2022 + SG1WHD_2022 + SG1SZD_2022 + SG1SZS_2022):
        tmp = ""
    #把获取的学生的所有考试的某科成绩段次一本线添加到字典中
    y_data.append({"yibenxian": [float(x) for x in tmp.split()]})
    if y_data[1]["yibenxian"]:
        datalist.append('一本线')

    titlelist = [title]
    c.close()
    conn.close()
    return titlelist,x_data,y_data,datalist


#获取学生某科成绩段次 如果sql语句执行失败返回error 如果数据为空返回isnull
def read_db_drawpic_duanci(dbname, classname, stuname, graphics, selectcount, stuid):
    #reload(sys)
    #sys.setdefaultencoding('utf8')
    #print(dbname,classname,stuname,graphics,selectcount,stuid,dbstr)
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    title = u""
    title += (stuname + graphics + "折线图")
    #获取该学生参加的所有考试名称
    sql2 = "select exam from CurrentScore where show = 1 and student_id  = " + stuid
    #print(sql2)
    try:
        # 执行SQL语句
        cursor = c.execute(sql2)
    except sqlite3.Error as e:
        # 打印异常信息
        conn.close()
        print("error1")
        return "error","error","error","error"
    tmp = ""
    results = cursor.fetchall()
    # 检查查询结果是否为空
    if not results:
        conn.close()
        print("isnull1")
        return "isnull","isnull","isnull","isnull"
    else:
        # 处理查询结果
        for row in results:
            tmp += row[0]
            tmp += " "
    #获取该学生参加的所有考试某科成绩段次
    x_data = tmp.split()
    if selectcount == 1:
        sql = "select SumD from CurrentScore  where show = 1 and student_id  = " + stuid
    elif selectcount == 2:
        sql = "select YuwenD from CurrentScore  where show = 1 and student_id  = " + stuid
    elif selectcount == 3:
        sql = "select ShuxueD from CurrentScore  where show = 1 and student_id  = " + stuid
    elif selectcount == 4:
        sql = "select WaiyuD from CurrentScore  where show = 1 and student_id  = " + stuid
    elif selectcount == 5:
        sql = "select Select1D from CurrentScore  where show = 1 and student_id  = " + stuid
    elif selectcount == 6:
        sql = "select Select2D from CurrentScore  where show = 1 and student_id  = " + stuid
    elif selectcount == 7:
        sql = "select Select3D from CurrentScore  where show = 1 and student_id  = " + stuid
    elif selectcount == 8:
        sql = "select ZongheD from CurrentScore  where show = 1 and student_id  = " + stuid

    #print(sql)
    try:
        # 执行SQL语句
        cursor = c.execute(sql)
    except sqlite3.Error as e:
        # 打印异常信息
        conn.close()
        print("error2")
        return "error","error","error","error"
    tmp = ""
    results = cursor.fetchall()
    # 检查查询结果是否为空
    if not results:
        conn.close()
        print("isnull2")
        return "isnull","isnull","isnull","isnull"
    else:
        # 处理查询结果
        for row in results:
            tmp += str(row[0])
            tmp += " "

    #把获取的学生的所有考试的某科成绩段次添加到字典中
    str_y_data = tmp.split()
    y_data =[{"stu": [int(x) for x in str_y_data]}]
    #datalist  =[graphics + "段次"]
    datalist  =[graphics]

    tmp = ""
    if classname in (SG1WHS_2022 + SG1WHZ_2022 + SG1WHD_2022 + SG1SZD_2022 + SG1SZS_2022):
        grade = '高一'
    elif classname in (SG2WK_2022 + SG2LK_2022):
        grade = '高二'
    else:
        grade = '高三'
    if classname in (SG1WHS_2022 + SG1WHZ_2022 + SG1WHD_2022 + SG2LK_2022 + SG3LK_2022):
        line = '理科一本线'
    else:
        line = '文科一本线'
    #获取该学生参加的所有考试某科成绩段次的一本线数据
    for x in x_data:
        if selectcount == 1:
            sql = "select SumD from SchoolLINE where line = '" + line + "' and exam = '" + str(x) + "' and grade = '" + grade + "'"
        elif selectcount == 2:
            sql = "select YuwenD from SchoolLINE where line = '" + line + "' and exam = '" + str(x) + "' and grade = '" + grade + "'"
        elif selectcount == 3:
            sql = "select ShuxueD from SchoolLINE where line = '" + line + "' and exam = '" + str(x) + "' and grade = '" + grade + "'"
        elif selectcount == 4:
            sql = "select WaiyuD from SchoolLINE where line = '" + line + "' and exam = '" + str(x) + "' and grade = '" + grade + "'"
        elif selectcount == 5:
            sql = "select Select1D from SchoolLINE where line = '" + line + "' and exam = '" + str(x) + "' and grade = '" + grade + "'"
        elif selectcount == 6:
            sql = "select Select2D from SchoolLINE where line = '" + line + "' and exam = '" + str(x) + "' and grade = '" + grade + "'"
        elif selectcount == 7:
            sql = "select Select3D from SchoolLINE where line = '" + line + "' and exam = '" + str(x) + "' and grade = '" + grade + "'"
        elif selectcount == 8:
            sql = "select ZongheD from SchoolLINE where line = '" + line + "' and exam = '" + str(x) + "' and grade = '" + grade + "'"
        #print(sql)
        try:
            # 执行SQL语句
            cursor = c.execute(sql)
        except sqlite3.Error as e:
            # 打印异常信息
            conn.close()
            print("error3")
            return "error","error","error","error"
        results = cursor.fetchall()
        # 检查查询结果是否为空
        if not results:
            #conn.close()
            #print("isnull3")
            #return "isnull","isnull","isnull","isnull"
            break
        else:
            # 处理查询结果
            for row in results:
                if selectcount == 8 and row[0] == None:
                    break;
                tmp += str(row[0])
                tmp += " "
    if selectcount == 8 and classname in (SG1WHS_2022 + SG1WHZ_2022 + SG1WHD_2022 + SG1SZD_2022 + SG1SZS_2022):
        tmp = ""
    #把获取的学生的所有考试的某科成绩段次一本线添加到字典中
    y_data.append({"yibenxian": [int(x) for x in tmp.split()]})
    if y_data[1]["yibenxian"]:
        #datalist.append('一本线段次')
        datalist.append('一本线')

    titlelist = [title]
    c.close()
    conn.close()
    return titlelist,x_data,y_data,datalist


#获得用户的相关信息 如果用户未绑定则flag标志位false
def read_userinfo_db(dbname, userid):
    #reload(sys)
    #sys.setdefaultencoding('utf8')

    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    sql = "select * from UserAccoutInfo where wxid = '" + userid + "'"
    #print(sql)

    text = {"flag": False}
    text["bind_state"] = '3'
    try:
        # 执行SQL语句
        cursor = c.execute(sql)
    except sqlite3.Error as e:
        # 打印异常信息
        conn.close()
        return text
    results = cursor.fetchall()
    # 检查查询结果是否为空
    if not results:
        conn.close()
        return text
    else:
        # 处理查询结果
        for row in results:
            text["userid"] = row[1]
            text["role"] = '1' if row[2] == '老师' else '0'
            #text["role"] = row[2]
            text["schoolname"] = row[3]
            text["phone"] = row[4]
            text["stuname"] = row[5]
            text["bind_state"] = row[6]
            text["unbindcount"] = row[7]
            if row[6] == "1":
                text["flag"] = True


    c.close()
    conn.close()

    return text



#获取用户的行为记录   如果获取失败则actionrecod标志为false
def read_useractionrecod_db(dbname, userid):
    #reload(sys)
    #sys.setdefaultencoding('utf8')

    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    sql = "SELECT * FROM AccoutRecord ORDER BY COUNT DESC  LIMIT 1"
    text = {"actionrecod": False}
    #print(sql)


    try:
        # 执行SQL语句
        cursor = c.execute(sql)
    except sqlite3.Error as e:
        # 打印异常信息
        conn.close()
        return text

    results = cursor.fetchall()
    # 检查查询结果是否为空
    if not results:
        conn.close()
        return text
    else:
        # 处理查询结果
        for row in results:
            text["actionrecod"] =  True
            text["schoolarrayindex"] = row[4]
            text["classarrayindex"] = row[6]


    conn.close()
    return text



#获取某次考试成绩列表数据 如果sql语句执行失败返回error 如果数据为空返回isnull
def read_db_json(dbname, classname, stuname, stuid, exam):
    #reload(sys)
    #sys.setdefaultencoding('utf8')



    #print(dbname)
    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    sql = "select * from CurrentScore where student_id  = " + stuid + " and exam = '" + str(exam) + "'" 
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
            print("isnull2")
            return "isnull"
        else:
            # 处理查询结果
            for row in results:
                text["td"].append(["总:"+ str(row[7]), str(row[8]), str(row[9])])
                text["td"].append(["语:"+ str(row[10]), str(row[11]), str(row[12])])
                text["td"].append(["数:"+ str(row[13]), str(row[14]), str(row[15])])
                text["td"].append(["外:"+ str(row[16]), str(row[17]), str(row[18])])
                text["td"].append(["物:"+ str(row[19]), str(row[20]), str(row[21])])
                text["td"].append(["化:"+ str(row[22]), str(row[23]), str(row[24])])
                text["td"].append(["生:"+ str(row[25]), str(row[26]), str(row[27])])
                text["td"].append(["综:"+ str(row[28]), str(row[29]), str(row[30])])
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
                text["td"].append(["总:"+ str(row[7]), str(row[8]), str(row[9])])
                text["td"].append(["语:"+ str(row[10]), str(row[11]), str(row[12])])
                text["td"].append(["数:"+ str(row[13]), str(row[14]), str(row[15])])
                text["td"].append(["外:"+ str(row[16]), str(row[17]), str(row[18])])
                text["td"].append(["政:"+ str(row[19]), str(row[20]), str(row[21])])
                text["td"].append(["历:"+ str(row[22]), str(row[23]), str(row[24])])
                text["td"].append(["地:"+ str(row[25]), str(row[26]), str(row[27])])
                text["td"].append(["综:"+ str(row[28]), str(row[29]), str(row[30])])
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
                text["td"].append(["总:"+ str(row[7]), str(row[8]), str(row[9])])
                text["td"].append(["语:"+ str(row[10]), str(row[11]), str(row[12])])
                text["td"].append(["数:"+ str(row[13]), str(row[14]), str(row[15])])
                text["td"].append(["外:"+ str(row[16]), str(row[17]), str(row[18])])
                text["td"].append(["物:"+ str(row[19]), str(row[20]), str(row[21])])
                text["td"].append(["化:"+ str(row[22]), str(row[23]), str(row[24])])
                text["td"].append(["生:"+ str(row[25]), str(row[26]), str(row[27])])
                text["td"].append(["综:"+ str(row[28]), str(row[29]), str(row[30])])
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
                text["td"].append(["总:"+ str(row[7]), str(row[8]), str(row[9])])
                text["td"].append(["语:"+ str(row[10]), str(row[11]), str(row[12])])
                text["td"].append(["数:"+ str(row[13]), str(row[14]), str(row[15])])
                text["td"].append(["外:"+ str(row[16]), str(row[17]), str(row[18])])
                text["td"].append(["物:"+ str(row[19]), str(row[20]), str(row[21])])
                text["td"].append(["化:"+ str(row[22]), str(row[23]), str(row[24])])
                text["td"].append(["地:"+ str(row[25]), str(row[26]), str(row[27])])
                text["td"].append(["综:"+ str(row[28]), str(row[29]), str(row[30])])
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
                text["td"].append(["总:"+ str(row[7]), str(row[8]), str(row[9])])
                text["td"].append(["语:"+ str(row[10]), str(row[11]), str(row[12])])
                text["td"].append(["数:"+ str(row[13]), str(row[14]), str(row[15])])
                text["td"].append(["外:"+ str(row[16]), str(row[17]), str(row[18])])
                text["td"].append(["物:"+ str(row[19]), str(row[20]), str(row[21])])
                text["td"].append(["化:"+ str(row[22]), str(row[23]), str(row[24])])
                text["td"].append(["政:"+ str(row[25]), str(row[26]), str(row[27])])
                text["td"].append(["综:"+ str(row[28]), str(row[29]), str(row[30])])
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
                text["td"].append(["总:"+ str(row[7]), str(row[8]), str(row[9])])
                text["td"].append(["语:"+ str(row[10]), str(row[11]), str(row[12])])
                text["td"].append(["数:"+ str(row[13]), str(row[14]), str(row[15])])
                text["td"].append(["外:"+ str(row[16]), str(row[17]), str(row[18])])
                text["td"].append(["历:"+ str(row[19]), str(row[20]), str(row[21])])
                text["td"].append(["政:"+ str(row[22]), str(row[23]), str(row[24])])
                text["td"].append(["地:"+ str(row[25]), str(row[26]), str(row[27])])
                text["td"].append(["综:"+ str(row[28]), str(row[29]), str(row[30])])
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
                text["td"].append(["总:"+ str(row[7]), str(row[8]), str(row[9])])
                text["td"].append(["语:"+ str(row[10]), str(row[11]), str(row[12])])
                text["td"].append(["数:"+ str(row[13]), str(row[14]), str(row[15])])
                text["td"].append(["外:"+ str(row[16]), str(row[17]), str(row[18])])
                text["td"].append(["历:"+ str(row[19]), str(row[20]), str(row[21])])
                text["td"].append(["政:"+ str(row[22]), str(row[23]), str(row[24])])
                text["td"].append(["生:"+ str(row[25]), str(row[26]), str(row[27])])
                text["td"].append(["综:"+ str(row[28]), str(row[29]), str(row[30])])
    else:
        results = cursor.fetchall()
        # 检查查询结果是否为空
        if not results:
            conn.close()
            return "isnull"
        else:
            # 处理查询结果
            for row in results:
                text["td"].append(["总:"+ str(row[2]), str(row[3]), str(row[4])])
                text["td"].append(["语:"+ str(row[5]), str(row[6]), str(row[7])])
                text["td"].append(["数:"+ str(row[8]), str(row[9]), str(row[10])])
                text["td"].append(["外:"+ str(row[11]), str(row[12]), str(row[13])])
                text["td"].append(["物:"+ str(row[14]), str(row[15]), str(row[16])])
                text["td"].append(["化:"+ str(row[17]), str(row[18]), str(row[19])])
                text["td"].append(["生:"+ str(row[20]), str(row[21]), str(row[22])])
                text["td"].append(["政:"+ str(row[23]), str(row[24]), str(row[25])])
                text["td"].append(["历:"+ str(row[26]), str(row[27]), str(row[28])])
                text["td"].append(["地:"+ str(row[29]), str(row[30]), str(row[31])])



    if classname in (SG1WHS_2022 + SG1WHZ_2022 + SG1WHD_2022 + SG1SZD_2022 + SG1SZS_2022):
        nozongheflag = 1
    else:
        nozongheflag = 0

    #找到班级各科最高分
    for i in range(len(text["td"]) - nozongheflag):
        if i == 0:
            sql = "select Sum from CurrentScore  where class  = " +str(classname)   + " and exam = '" + str(exam) + "' ORDER BY Sum DESC limit 1"
        elif i == 1:
            sql = "select Yuwen from CurrentScore  where class  = " +str(classname)   + " and exam = '" + str(exam) + "' ORDER BY Sum DESC limit 1"
        elif i == 2:
            sql = "select Shuxue from CurrentScore  where class  = " +str(classname)   + " and exam = '" + str(exam) + "' ORDER BY Sum DESC limit 1"
        elif i == 3:
            sql = "select Waiyu from CurrentScore  where class  = " +str(classname)   + " and exam = '" + str(exam) + "' ORDER BY Sum DESC limit 1"
        elif i == 4:
            sql = "select Select1 from CurrentScore  where class  = " +str(classname)   + " and exam = '" + str(exam) + "' ORDER BY Sum DESC limit 1"
        elif i == 5:
            sql = "select Select2 from CurrentScore  where class  = " +str(classname)   + " and exam = '" + str(exam) + "' ORDER BY Sum DESC limit 1"
        elif i == 6:
            sql = "select Select3 from CurrentScore  where class  = " +str(classname)   + " and exam = '" + str(exam) + "' ORDER BY Sum DESC limit 1"
        elif i == 7:
            sql = "select Zonghe from CurrentScore  where class  = " +str(classname)   + " and exam = '" + str(exam) + "' ORDER BY Sum DESC limit 1"
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
                text["td"][i].append(row[0])

    if classname in (SG1WHS_2022 + SG1WHZ_2022 + SG1WHD_2022 + SG1SZD_2022 + SG1SZS_2022):
        grade = '高一'
    elif classname in (SG2WK_2022 + SG2LK_2022):
        grade = '高二'
    else:
        grade = '高三'

    if classname in (SG1WHS_2022 + SG1WHZ_2022 + SG1WHD_2022 + SG2LK_2022 + SG3LK_2022):
        sql = "select * from SchoolLINE where line  = '理科一本线' and exam = '" + str(exam) + "' and grade = '" + grade + "'"
    else:
        sql = "select * from SchoolLINE where line  = '文科一本线' and exam = '" + str(exam) + "' and grade = '" + grade + "'"
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
                text["td"][i].append(row[i*2+7])


    c.close()
    conn.close()


    return text



#获取学生的学号 如果sql语句执行失败返回error 如果数据为空返回isnull
def read_db_changeid(dbname, classname, stuname):
    #reload(sys)
    #sys.setdefaultencoding('utf8')


    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    sql = "select student_id  from CurrentStudent where student_name = '" + stuname + "' and class = " + classname

    try:
        # 执行SQL语句
        cursor = c.execute(sql)
    except sqlite3.Error as e:
        # 打印异常信息
        conn.close()
        return "error"

    stuid = ""

    results = cursor.fetchall()
    # 检查查询结果是否为空
    if not results:
        conn.close()
        return "isnull"
    else:
        # 处理查询结果
        for row in results:
            stuid = row[0]
    
    return stuid





#read_userinfo_db("oz1Xn4opoA19fTqSCPciZXcLwWmcs")
