# -*- coding: utf-8 -*-#
# filename: hello.py

from flask import Flask, request

from sqldb import readdb

import importlib,sys
importlib.reload(sys)

from draw import graphics
from myrequest import myrequest
from sqldb import myinsert
from sendmail import sendmail

import sys
import datetime
import json

from flask import render_template
from flask import send_file

from werkzeug.utils import secure_filename
from pypinyin import lazy_pinyin

import os

DBXCYG = "database/NEWDbData/remakedb/xcyg.db"
DBUSERINFO1 = "database/NEWDbData/remakedb/userinfo.db"

APPID = "wxeb5cab6c5e3e6507"
SECRET = "84fd9faf13851abea7e66f67c8ee80f4"


app = Flask(__name__)

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


WXAPP_DATA = {"schoolarray" : ['淅川一高'],
              "classarray" : [
                              [['请选择', '高一', '高二', '高三'],
                               []
                              ],

                              [['请选择', '高一', '高二', '高三'],
                               ['请选择', '2201', '2202', '2203', '2204', '2205', '2206', '2207', '2208', '2209', '2210',
                                '2211', '2212', '2213', '2214', '2215', '2216', '2217', '2218', '2219', '2220',
                                '2221', '2222', '2223', '2224', '2225', '2226', '2227', '2228', '2229', '2230',
                                '2231', '2232', '2233', '2234', '2235', '2236', '2237', '2238', '2239', '2240',
                                '2241', '2242', '2243', '2244', '2245']],

                              [['请选择', '高一', '高二', '高三'],
                               ['请选择', '2101', '2102', '2103', '2104', '2105', '2106', '2107', '2108', '2109', '2110',
                                '2111', '2112', '2113', '2114', '2115', '2116', '2117', '2118', '2119', '2120',
                                '2121', '2122', '2123', '2124', '2125', '2126', '2127', '2128', '2129', '2130',
                                '2131', '2132', '2133', '2134', '2135', '2136', '2137', '2138', '2139', '2140',
                                '2141', '2142', '2143', '2144', '2145', '2146']],

                              [['请选择', '高一', '高二', '高三'],
                               ['请选择', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010',
                                '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020',
                                '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030',
                                '2031', '2032', '2033', '2034', '2035', '2036', '2037', '2038', '2039', '2040',
                                '2041', '2042', '2043', '2044', '2045', '2046', '2047', '2048', '2049', '2050',
                               ]]
                               ],
              "examarray" : [[],
                            ['高一下期中', '月考B', '月考A'],
                            ['高二5.12月考', '高二下期中', '月考B', '联考A', '月考A', '期末A'],
                            ['二模', '联考B', '一模', '期末', '联考A']
                            ],
              "partarray" : ['全部'],
              "analysisarray" : ['整体'],
              "keystuarray" : ['本次', '历次'],
                }


def sendEMail(sendText, sendTitle, sendMail):
    sendmail.Mail().sendmail(sendText, sendTitle, sendMail)


@app.route('/aaa')
def index():
    return 'Index Page'


#成绩查询
@app.route('/scorelist')
def scorelist():
    #reload(sys)
    #sys.setdefaultencoding('utf8')
    #获取小程序发来的各种信息
    stuname = request.args.get('stuname')
    stuname = stuname.strip()
    classname = request.args.get('classname')
    examname = request.args.get('examname')
    schoolname = request.args.get('schoolname')
    userid = request.args.get('userid')
    role = '老师' if request.args.get('role') == '1' else '家长'
    #print(role)


    #记录这个接口被调用
    filetext = stuname + "---" + classname + "---" + examname + "---"
    with open('./log/scorelist.txt','at') as f:
        print(filetext,file=f)

    #县高入口
    if schoolname == '淅川一高':
        stuid = str(readdb.read_db_changeid(DBXCYG, classname, stuname))
        dbname = DBXCYG
    else:
        return "error"
    #检查变量是否等于 "error" "isnull"
    if isinstance(stuid, str) and stuid == "error":
        return "error"
    elif isinstance(stuid, str) and stuid == "isnull":
        return "isnull"

    #获取学生字典成绩
    text = readdb.read_db_json(dbname, classname, stuname, stuid, examname)
    #print(text)
    # 检查变量是否等于 "error" "isnull"
    if isinstance(text, str) and text == "error":
        return "error"
    elif isinstance(text, str) and text == "isnull":
        return "isnull"

    #成功查询记录这次行为
    if userid is not  None and  userid.strip() != "" and userid.strip() != "undefined":
        #print("记录了")
        myinsert.addrecorddb(DBUSERINFO1, userid, schoolname, classname, stuname, role)

    return text

#折线图数据返回
@app.route('/pic_data',methods = ['POST','GET'])
def get_pic_data():
    #reload(sys)
    #sys.setdefaultencoding('utf8')
    #获取小程序传来的数据
    stuname = request.args.get('stuname')
    stuname = stuname.strip()
    classname = request.args.get('classname')
    partname = request.args.get('partname')
    schoolname = request.args.get('schoolname')
    radioflag = request.args.get('radioflag')
    userid = request.args.get('userid')
    role = '老师' if request.args.get('role') == '1' else '家长'
    #print(role)


    #记录这个接口被调用
    filetext = stuname + "---" + classname
    with open('./log/pic_data.txt','at') as f:
        print(filetext,file=f)

    all_data = {"title":[],"xname":[], "yname":[], "xdata":[], "ydata":[], "datalist":[]}

    #县高入口
    if schoolname == '淅川一高':
        stuid = str(readdb.read_db_changeid(DBXCYG, classname, stuname))
        dbname = DBXCYG
    else:
        return "error"

    # 检查变量是否等于 "error" "isnull"
    if isinstance(stuid, str) and stuid == "error":
        return "error"
    elif isinstance(stuid, str) and stuid == "isnull":
        return "isnull"
        

    #任意学科折线图数据
    if partname != '全部':
        return "error"
        #title,xdata,ydata,datalist = readdb.read_db_drawpic(dbname, classname, stuname, partname)
        #if title[0] == "error":
        #    return "error"
        ##pic_name_0,pic_name_1 = graphics.picname()
        #plotname = u"" + partname
        #xname,yname = graphics.getxyname(classname, stuname)
        ##graphics.drawpic(title, xname, yname, xdata, ydata, pic_name_0, plotname, classname)
        ##pic_name_list.append(pic_name_1)
        #all_data["title"].append(title)
        #all_data["xname"].append(xname)
        #all_data["yname"].append(yname)
        #all_data["xdata"].append(xdata)
        #all_data["ydata"].append(ydata)
        #all_data["datalist"].append(datalist)
    #全部学科折线图数据
    else:
        pname = []
        selectcount = 1
        if (classname in SG3LK_2022) or (classname in SG2LK_2022):
            pname = ['总分', '语文', '数学', '外语', '物理', '化学', '生物', '理综']
        elif (classname in SG3WK_2022) or (classname in SG2WK_2022):
            pname = ['总分', '语文', '数学', '外语', '政治', '历史', '地理', '文综']
        elif classname in SG1WHS_2022:
            pname = ['总分', '语文', '数学', '外语', '物理', '化学', '生物', '综合']
        elif classname in SG1WHD_2022:
            pname = ['总分', '语文', '数学', '外语', '物理', '化学', '地理', '综合']
        elif classname in SG1WHZ_2022:
            pname = ['总分', '语文', '数学', '外语', '物理', '化学', '政治', '综合']
        elif classname in SG1SZD_2022:
            pname = ['总分', '语文', '数学', '外语', '历史', '政治', '地理', '综合']
        elif classname in SG1SZS_2022:
            pname = ['总分', '语文', '数学', '外语', '历史', '政治', '生物', '综合']
        else:
            return "error"
        for x in pname:
            if radioflag == "1":
                if schoolname == '淅川一高':
                    title,xdata,ydata,datalist = readdb.read_db_drawpic_duanci(dbname, classname, stuname, x, selectcount, stuid)
                    selectcount = selectcount + 1
                else:
                    return "error"
                if isinstance(title, str) and title == "error":
                    return "error"
                elif isinstance(title, str) and title == "isnull":
                    return "isnull"
            elif radioflag == "2":
                if schoolname == '淅川一高':
                    title,xdata,ydata,datalist = readdb.read_db_drawpic_score(dbname, classname, stuname, x, selectcount, stuid)
                    selectcount = selectcount + 1
                else:
                    return "error"
                if isinstance(title, str) and title == "error":
                    return "error"
                elif isinstance(title, str) and title == "isnull":
                    return "isnull"
            else:
                if schoolname == '淅川一高':
                    title,xdata,ydata,datalist = readdb.read_db_drawpic_duanci(dbname, classname, stuname, x, selectcount, stuid)
                    selectcount = selectcount + 1
                else:
                    return "error"
                if isinstance(title, str) and title == "error":
                    return "error"
                elif isinstance(title, str) and title == "isnull":
                    return "isnull"
            plotname = u"" + x
            xname,yname = graphics.getxyname(classname, stuname, radioflag)
            all_data["title"].append(title)
            all_data["xname"].append(xname)
            all_data["yname"].append(yname)
            all_data["xdata"].append(xdata)
            all_data["ydata"].append(ydata)
            all_data["datalist"].append(datalist)

    #成功查询记录这次行为
    if userid is not  None and  userid.strip() != "" and userid.strip() != "undefined":
        myinsert.addrecorddb(DBUSERINFO1, userid, schoolname, classname, stuname, role)
        #print(all_data)
    return all_data


#学生、班级分析
@app.route('/dataanalysis')
def dataanalysis():
    #reload(sys)
    #sys.setdefaultencoding('utf8')
    #获取小程序发来的各种信息
    stuname = request.args.get('stuname')
    classname = request.args.get('classname')
    schoolname = request.args.get('schoolname')
    gradename = request.args.get('gradename')
    partindex = request.args.get('partindex')
    role = '老师' if request.args.get('role') == '1' else '家长'
    #print(role)
    userid = request.args.get('userid')
    roleanalysis = request.args.get('roleanalysis')
    keystuflag = request.args.get('keystuflag')
    #print("keystuflag",keystuflag)


    #记录这个接口被调用
    if role == '老师':
        filetext =classname + "---" + userid + "----" + role
        #print(classname,schoolname,roleanalysis,gradename,partindex)
        if roleanalysis == "1":
            text = readdb.read_db_class_allexam_analysis(DBXCYG, classname)
            if isinstance(text, str) and text == "error":
                return "error"
            elif isinstance(text, str) and text == "isnull":
                return "isnull"
            if keystuflag == '1':
                text['KeyStu'] = readdb.read_db_class_keystu_analysis(DBXCYG, classname, keystuflag)
            else:
                if classname in (SG1WHS_2022 + SG1WHZ_2022 + SG1WHD_2022 + SG1SZD_2022 + SG1SZS_2022):
                    exam = WXAPP_DATA["examarray"][1][0]
                elif classname in (SG2WK_2022 + SG2LK_2022):
                    exam = WXAPP_DATA["examarray"][2][0]
                else:
                    exam = WXAPP_DATA["examarray"][3][0]
                text['KeyStu'] = readdb.read_db_class_keystu_analysis(DBXCYG, classname, keystuflag, exam)
            return text
        elif roleanalysis == "2":
            if int(partindex) > 6:
                partindex = str(int(partindex) - 3)
            text = readdb.read_db_class_allexam_analysis(DBXCYG, gradename, int(partindex))
            if isinstance(text, str) and text == "error":
                return "error"
            elif isinstance(text, str) and text == "isnull":
                return "isnull"
            with open('./log/scorelist.txt','at') as f:
                print(filetext,file=f)
            return text
    else:
        filetext = stuname + "---" + classname + "---" + userid + "----" + role
    with open('./log/scorelist.txt','at') as f:
        print(filetext,file=f)


    #县高入口
    if schoolname == '淅川一高':
        stuid = str(readdb.read_db_changeid(DBXCYG, classname, stuname))
    else:
        return "error"

    #检查变量是否等于 "error" "isnull"
    if isinstance(stuid, str) and stuid == "error":
        return "error"
    elif isinstance(stuid, str) and stuid == "isnull":
        return "isnull"

    #家长获取孩子总体分析
    text = readdb.read_db_studata_allanalysis(DBXCYG, classname, stuid)
    #print(text)
    # 检查变量是否等于 "error" "isnull"
    if isinstance(text, str) and text == "error":
        return "error"
    elif isinstance(text, str) and text == "isnull":
        return "isnull"
    text.append(readdb.read_db_studata_latestanalysis(DBXCYG, classname, stuid))

    #成功查询记录这次行为
    if userid is not  None and  userid.strip() != "" and userid.strip() != "undefined":
        myinsert.addrecorddb(DBUSERINFO1, userid, schoolname, classname, stuname, role)

    return text


#到对应的时间文件夹位置查找相应的图片
@app.route('/pic/<pic_name>',methods = ['POST','GET'])
def returnTimePictureExample(pic_name):
    time = datetime.datetime.now().strftime('%Y%m%d')
    dirname = 'Picture/' + time + '/'
    dirname = dirname + pic_name
    return send_file(dirname, mimetype='image/gif')

#到对应位置查找相应的图片
@app.route('/locationpic/<pic_name>',methods = ['POST','GET'])
def returnPictureExample(pic_name):
    return send_file(pic_name, mimetype='image/gif')

#绑定信息
@app.route('/bindinfo')
def bindinfo():
    #reload(sys)
    #sys.setdefaultencoding('utf8')
    #获取小程序传来的数据
    code = request.args.get('code')
    schoolname = request.args.get('schoolname')
    phone = request.args.get('phone')
    stuname = request.args.get('stuname')
    stuname = stuname.strip()
    role = '老师' if request.args.get('role') == '1' else '家长'
    #print(role)

    #通过微信服务器获取用户uid
    url = "https://api.weixin.qq.com/sns/jscode2session?appid=" + APPID + "&secret=" + SECRET + "&js_code=" + code +"&grant_type=authorization_code"
    tmpstr = myrequest.getuserid(url)
    json1=json.loads(tmpstr)
    userid =  json1["openid"]


    #记录这次接口调用
    filetext = phone + "---" + stuname + "---" + role + "---" + userid
    with open('./log/bindinfo.txt','at') as f:
        print(filetext,file=f)

    text = readdb.read_userinfo_db(DBUSERINFO1, userid)
    print(text)

    #是否读取到内容
    if not text["flag"]:
        if text["bind_state"] == '3':
            print("没绑定过")
            #之前没绑定过直接插入
            myinsert.adddb(DBUSERINFO1, userid, schoolname, phone, stuname, role)
            #插入后在读取一遍信息
            text = readdb.read_userinfo_db(DBUSERINFO1, userid)
            text.update({"insert": "success"})
        else:
            #修改绑定内容
            print("绑定过")
            myinsert.change_bindinfo(DBUSERINFO1, userid, schoolname, phone, stuname, role)

    return text

#认证信息
@app.route('/certification')
def certification():
    #reload(sys)
    #sys.setdefaultencoding('utf8')
    #获取小程序传来的数据
    code = request.args.get('code')
    phone = request.args.get('phone')
    teaname = request.args.get('teaname')
    cercode = request.args.get('cercode')
    schoolname = '淅川一高'
    role = '老师' if request.args.get('role') == '1' else '家长'
    #print(role)

    text = {"coderror" : "success"}

    if cercode != "6666":
        text["code"] = "coderror"
        return text


    #通过微信服务器获取用户uid
    url = "https://api.weixin.qq.com/sns/jscode2session?appid=" + APPID + "&secret=" + SECRET + "&js_code=" + code +"&grant_type=authorization_code"
    tmpstr = myrequest.getuserid(url)
    json1=json.loads(tmpstr)
    userid =  json1["openid"]
    text.update(readdb.read_userinfo_db(DBUSERINFO1, userid))

    #记录这次接口调用
    filetext = phone + "---" + teaname + "---" + role + "---" + userid
    with open('./log/certification.txt','at') as f:
        print(filetext,file=f)

    #是否读取到内容
    if not text["flag"]:
        if text["bind_state"] == '3':
            #之前没绑定过直接插入
            myinsert.adddb(DBUSERINFO1, userid, schoolname, phone, teaname, role)
            #插入后在读取一遍信息
            text = readdb.read_userinfo_db(DBUSERINFO1, userid)
            text.update({"insert": "success"})
        else:
            #之前绑定过修改绑定标志
            myinsert.change_bindinfo(DBUSERINFO1, userid, schoolname, phone, teaname, role)

    return text


#是否绑定
@app.route('/isbind')
def isbind():
    #reload(sys)
    #sys.setdefaultencoding('utf8')
    code = request.args.get('code')

    url = "https://api.weixin.qq.com/sns/jscode2session?appid=" + APPID + "&secret=" + SECRET + "&js_code=" + code +"&grant_type=authorization_code"

    tmpstr = myrequest.getuserid(url)
    json1=json.loads(tmpstr)

    userid =  json1["openid"]
    text = readdb.read_userinfo_db(DBUSERINFO1, userid)
    #print(text)

    #记录这次接口调用
    filetext = userid
    with open('./log/isbind.txt','at') as f:
        print(filetext,file=f)

    tmp = readdb.read_useractionrecod_db(DBUSERINFO1, userid)
    if tmp["actionrecod"]:
        if tmp["schoolarrayindex"] == "淅川一高":
            tmp["schoolarrayindex"] = 0
        if tmp["classarrayindex"] in (SG1WHS_2022 + SG1WHD_2022 + SG1WHZ_2022 + SG1SZD_2022 + SG1SZS_2022):
            tmp["classarrayindex"] = [1, int(tmp["classarrayindex"]) - 2200]
        elif tmp["classarrayindex"] in (SG2WK_2022 + SG2LK_2022):
            tmp["classarrayindex"] = [2, int(tmp["classarrayindex"]) - 2100]
        elif tmp["classarrayindex"] in (SG3WK_2022 + SG3LK_2022):
            tmp["classarrayindex"] = [3, int(tmp["classarrayindex"]) - 2000]
    else:
        tmp["schoolarrayindex"] = 0
        tmp["classarrayindex"] = [0, 0]

    text.update(tmp)


    text.update(WXAPP_DATA)
    #print(text)

    return text

#解除绑定
@app.route('/unbind')
def unbind():
    #reload(sys)
    #sys.setdefaultencoding('utf8')
    code = request.args.get('code')

    url = "https://api.weixin.qq.com/sns/jscode2session?appid=" + APPID + "&secret=" + SECRET + "&js_code=" + code +"&grant_type=authorization_code"

    tmpstr = myrequest.getuserid(url)
    json1=json.loads(tmpstr)
    userid =  json1["openid"]

    filetext = userid
    with open('./log/unbind.txt','at') as f:
        print(filetext,file=f)


    text = myinsert.change_bindstate(DBUSERINFO1, userid, '0')

    return text


#反馈信息
@app.route('/feedback')
def feedback():
    #reload(sys)
    #sys.setdefaultencoding('utf8')
    flag = request.args.get('flag')
    mesg = request.args.get('mesg')
    if flag == '1':

        phone = request.args.get('phone')
        name = request.args.get('name')
        text = "姓名:" + name + "\n联系方式:" + phone + "\n内容:" +mesg

        with open('./log/feedback.txt','at') as f:
            print(text,file=f)
        sendEMail(text,"绑定用户",["city_in_the_sky@163.com"])
    else:
        with open('./log/feedback.txt','at') as f:
            print(mesg,file=f)
        sendEMail(mesg,"未绑定用户",["city_in_the_sky@163.com"])

    return "success"

#订阅信息
@app.route('/msgpost')
def msgpost():
    #reload(sys)
    #sys.setdefaultencoding('utf8')
    flag = request.args.get('flag')
    mesg = request.args.get('mesg')

    return "success"


@app.route('/upload', methods=['GET'])
def upload_file():
    return render_template('upload/upload.html')

@app.route('/upload1', methods=['GET', 'POST'])
def upload1_file():
    if request.method == 'POST':
        f = request.files['file']
        #f.save(secure_filename(f.filename))
        #filename = secure_filename(''.join(lazy_pinyin(file.filename)))
        cmd = 'ls -l ./receivefile/'  +  ' | grep "^-" | wc -l'
        f.save(os.path.join('receivefile',graphics.getdirnum(cmd) + secure_filename(''.join(lazy_pinyin(f.filename)))))
        return 'file uploaded successfully'
    else:
        return render_template('upload/upload.html')

@app.route('/uploadpic', methods=['GET'])
def uploadpic_file():
    return render_template('uploadpic/uploadpic.html')

@app.route('/uploadpic1', methods=['GET', 'POST'])
def uploadpic1_file():
    if request.method == 'POST':
        f = request.files['file']
        #f.save(secure_filename(f.filename))
        #filename = secure_filename(''.join(lazy_pinyin(file.filename)))
        f.save("sharepic" +  os.path.splitext(f.filename)[-1])
        return 'picture uploaded successfully'
    else:
        return render_template('upload/upload.html')




if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run(host='0.0.0.0', port=int("9006"))
