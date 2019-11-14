# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import re
from sklearn.preprocessing import minmax_scale
from IPython.core.pylabtools import figsize
from matplotlib.ticker import MultipleLocator


def process_data():
    rootdir = './data/'
    list = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    for type in list:
        l = os.listdir(rootdir + type)
        if type == 'HULA':
            for dir2 in l:
                dir3 = rootdir + type + '/' + dir2
                Oint = 0
                Odata = 0
                for file_name in os.listdir(dir3):
                    df = pd.read_csv(dir3 + '/' + file_name)
                    total_overhead = float(df.iloc[0]['Average']) * float(df.iloc[0]['Rate (ms)'])
                    data_overhead = float(df.iloc[7]['Average']) * float(df.iloc[7]['Rate (ms)'])
                    int_overhead = total_overhead - data_overhead
                    if file_name[0] == '1':  # 发端
                        Oint += 2 * int_overhead
                        Odata += 2 * data_overhead
                    elif file_name[0] == '2':  # 收端
                        Oint += 6 * int_overhead
                        Odata += 6 * data_overhead
                        # print(dir2, type)
                        # print(Oint, '\t', Odata)
                        # print(Oint/Odata)
        if type == 'NEW':
            for dir2 in l:
                dir3 = rootdir + type + '/' + dir2
                Oint = 0
                Odata = 0
                for file_name in os.listdir(dir3):
                    df = pd.read_csv(dir3 + '/' + file_name)
                    int_overhead = (float(df.iloc[7]['Average']) - 1016) * float(df.iloc[7]['Rate (ms)'])
                    data_overhead = 1016 * float(df.iloc[7]['Rate (ms)'])
                    if file_name[0] == '1':  # 发端
                        Oint += 2 * int_overhead
                        Odata += 2 * data_overhead
                    elif file_name[0] == '2':  # 收端
                        Oint += 6 * int_overhead
                        Odata += 6 * data_overhead
                        # print(dir2, type)
                        # print(Oint, '\t', Odata)
                        # print(Oint/Odata)


if __name__ == '__main__':
    figsize(5, 3)
    font_legend = {'family': 'Arial',
                   'weight': 'normal',
                   'size': 15,
                   }
    font_label = {'family': 'Arial',
                  'weight': 'normal',
                  'size': 18,
                  }
    data = pd.read_excel('./data2.xlsx')

    fig, left_axis = plt.subplots()
    right_axis = left_axis.twinx()

    lns1=left_axis.plot(list(data['send']), list(data['coverage']), color='red', linewidth=2, linestyle=':', markersize=8,
                   marker='^', label='Coverage')
    lns2=right_axis.plot(list(data['send']), list(data['overhead']), color='seagreen', linewidth=2, linestyle=':', markersize=8,
                    marker='x', c='', label='Occupation')



    # plt.ylim(0, )
    # plt.xlim(0,800)
    plt.grid()
    left_axis.tick_params(labelsize=13)
    right_axis.tick_params(labelsize=13)

    lns = lns1 + lns2
    labs = [l.get_label() for l in lns]
    ax = plt.gca()
    ax.legend(lns, labs, bbox_to_anchor=(1.0, 0.8),prop=font_legend)

    labels = ax.get_xticklabels() + ax.get_yticklabels()
    [label.set_fontname('Arial') for label in labels]
    left_axis.set_xlabel('Background Traffic Rate (kbps)', font_label)
    left_axis.set_ylabel('Coverage Rate',font_label)
    right_axis.set_ylabel('Bandwidth Occupation', font_label)
    ax.xaxis.set_major_locator(MultipleLocator(50))
    left_axis.yaxis.set_major_locator(MultipleLocator(0.2))
    right_axis.yaxis.set_major_locator(MultipleLocator(0.02))
    # ax.set_position([box.x0,box.y0,box.width,box.height* 0.8])

    # legend = plt.legend(ncol=1,prop=font_legend)
    # ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
        # label.set_horizontalalignment("right")
    foo_fig = plt.gcf()  # 'get current figure'
    plt.tight_layout()
    # left_axis.legend(loc='best',   bbox_to_anchor=(1.0, 0.5), prop=font_legend)
    # right_axis.legend(loc='best',  bbox_to_anchor=(1.0, 0.7), prop=font_legend)
    foo_fig.savefig('./send.eps', format='eps', dpi=1000, bbox_inches='tight')
    plt.show()
