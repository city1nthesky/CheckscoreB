# coding=utf-8

# filename: twographics.py
#import pandas as pd
import random
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator


def draw1(lx, dy, title):
    """画双轴折线图
    :param lx x轴数据集合
    :param dy y轴数据字典
    """
    # 设置图片可以显示中文和特殊字符
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    #df = pd.DataFrame(dy, index=lx)
    fyt = list(dy.keys())[0]
    syt = list(dy.keys())[1]
    ax = df.plot(secondary_y=[syt], x_compat=True, grid=True, linewidth=0.8)
    ax.set_title(title)
    ax.set_ylabel(fyt)
    ax.grid(linestyle="--", alpha=0.3)
    ax.right_ax.set_ylabel(syt)
    plt.show()


def draw2(lx, dy, title):
    """画双轴折线图
    :param lx x轴数据集合
    :param dy y轴数据字典
    """
    # 设置图片可以显示中文和特殊字符
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    fyt = list(dy.keys())[0]
    syt = list(dy.keys())[1]
    plt.figure(figsize=(8, 5), dpi=120)
    plt.plot(lx, dy.get(fyt), label=fyt, linewidth=0.8, color='b')
    plt.grid(linestyle="--", alpha=0.3)
    plt.title(title, fontsize=12)
    plt.xticks(rotation=30)
    plt.ylabel(fyt, fontsize=9)
    # plt.ylim(-10, 30)
    plt.legend(loc='upper left')
    # 调用twinx后可绘制次坐标轴
    plt.twinx()
    plt.plot(lx, dy.get(syt), label=syt, linewidth=0.8, color='y')
    plt.ylabel(syt, fontsize=9)
    # plt.ylim(-60, 50)
    plt.legend(loc='upper right')
    # 设置x轴刻度
    ax = plt.gca()
    ax.xaxis.set_major_locator(MultipleLocator(2))
    plt.show()
    plt.savefig("1.png")


def main():
    """主函数"""
    lx = [1,2,3,4,5,6,7,8,9,10,11,12]
    #lx = pd.period_range(start='2022-01', periods=12, freq="M")
    y1 = [round(random.random(), 3) for i in range(12)]
    y2 = [random.randint(1, 40) for i in range(12)]
    dy = {'应力(MPa)': y1, '温度(℃)': y2}
    title = '应力随温度变化情况'
    # draw1(lx, dy, title)
    lxx = [str(i) for i in list(lx)]
    draw2(lxx, dy, title)


if __name__ == '__main__':
    main()
