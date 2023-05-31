# coding=utf-8

# filename: graphics.py
#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')

import importlib,sys
importlib.reload(sys)


import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt           #引入matplotlib库

import os
import datetime


SG1WFK_2022 = ["2201","2202","2203","2204",\
        "2205","2206","2207","2208","2209",\
        "2210","2211","2212","2213","2214",\
        "2215","2216","2217","2218","2219",\
        "2220","2221","2222","2223","2224",\
        "2225","2226","2227","2228","2229",\
        "2230","2231","2232","2233","2234",\
        "2235","2236","2237","2238","2239",\
        "2240","2241","2242","2243","2244",\
        "2245"]

SG3LK_2022 = ["2001","2002","2003","2004",\
        "2005","2006","2007","2008","2009",\
        "2010","2011","2012","2013","2014",\
        "2015","2016","2017","2018","2019",\
        "2020","2021","2022","2025","2026",\
        "2027","2028","2029","2030","2031",\
        "2032","2033","2034","2047","2048",\
        "2049","2050","2239"]

SG3WK_2022 = ["2035","2036","2037","2038",\
        "2039","2040","2041","2042","2043",\
        "2045","2046"]


SG2LK_2022 = ["2101","2102","2103","2104",\
        "2105","2106","2107","2108","2109",\
        "2110","2113","2115","2116","2117",\
        "2118","2119","2120","2121","2122",\
        "2123","2124","2127","2128","2129",\
        "2130","2131","2132","2133","2134",\
        "2135","2136","2137","2138","2143",\
        "2144","2145"]

SG2WK_2022 = ["2111","2112","2125","2126",\
        "2139","2140","2141","2142","2146"]
 
#print (matplotlib.matplotlib_fname())    # 查看字体配置路径
#print (matplotlib.get_cachedir())        # 查看缓存文件路径

plt.rcParams['font.sans-serif'] = ['SimHei']  #显示汉字
plt.rcParams['axes.unicode_minus'] = False    #用来正常显示负号


def drawpic(title, xname, yname, x_data, y_data, pic_name, plotname, classname):
#def drawpic():
    
    #x_data = ['期末考试', '拉练一', '拉练四', '拉练五']
    #y_data = [60, 84, 86, 66]               
    
    print(plotname)
    print(type(plotname))
    
    plt.style.use('ggplot')    #添加网格线
    plt.title(title)
    plt.xlabel(xname)
    plt.ylabel(yname)
    
    
    #plt.plot(x_data, y_data, label=plotname)
    plt.plot(x_data, y_data[0]["stu"])
    #plt.legend([plotname])    #设置折线名称

    if classname in SG3LK_2022:
        plt.plot(x_data, y_data[1]["yibenxian"])
        plt.legend([plotname, '一本线'])    #设置折线名称
    elif classname in SG3WK_2022:
        plt.plot(x_data, y_data[1]["yibenxian"])
        plt.legend([plotname, '一本线'])    #设置折线名称
    else:
        plt.legend([plotname])    #设置折线名称

    plt.gca().invert_yaxis()  #翻转y轴数据顺序
    
    plt.savefig(pic_name)
    plt.close()

    #plt.show()


def getdirnum(cmd):
    num = os.popen(cmd).read()
    num = num.strip()

    return num

def picname():
    time = datetime.datetime.now().strftime('%Y%m%d')

    cmd = 'ls -l ./Picture/' + time +  ' | grep "^-" | wc -l'
    dirname = './Picture/' + time
    if os.path.exists(dirname) == False:
        tcmd = 'mkdir ./Picture/' + time
        os.system(tcmd)

    num = os.popen(cmd).read()
    num = num.strip()
    #now_time = datetime.datetime.now()
    atime = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    picname_0 = './Picture/' + time + '/' + atime + '_' + num + '.png'
    picname_1 = atime + '_' + num + '.png'
    return picname_0,picname_1

def getxyname(classname, stuname, radioflag):
    xname = u""
    if radioflag == "1":
        yname = u"段次"
    if radioflag == "2":
        yname = u"成绩"
    if classname in SG2LK_2022:
        xname += u"高二上学期考试"
    elif classname in SG2WK_2022:
        xname += u"高二上学期考试"
    elif classname in SG3LK_2022:
        xname += u"高三上学期考试"
    elif classname in SG3WK_2022:
        xname += u"高三上学期考试"
    else:
        xname += u"高一上学期考试"


    xnamelist = [xname]
    ynamelist = [yname]
    return xnamelist,ynamelist



#drawpic()

#print picname()
