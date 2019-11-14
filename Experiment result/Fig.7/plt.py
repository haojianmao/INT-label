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
    font_legend = {'family': 'Arial',
                   'weight': 'normal',
                   'size': 15,
                   }
    font_label = {'family': 'Arial',
                  'weight': 'normal',
                  'size': 18,
                  }
    data = pd.read_excel('./data.xlsx')
    data['HULA'] = data['HULA-int'] / data['HULA-data']
    data['NEW'] = data['NEW-int'] / data['NEW-data']
    figsize(5, 3)
    plt.figure()
    plt.plot(np.array(data.index)*1000, list(data['HULA']), color='red', linewidth=2, linestyle=':', markersize=8,
                   marker='^', label='HULA')
    plt.plot(np.array(data.index)*1000, list(data['NEW']), color='seagreen', linewidth=2, linestyle=':', markersize=8,
                    marker='x', c='', label='INT-label')
    plt.ylim(-0.02, 1)
    plt.xlim(8, 102)
    plt.grid()
    plt.tick_params(labelsize=13)
    ax = plt.gca()
    ax.xaxis.set_major_locator(MultipleLocator(10))
    ax.yaxis.set_major_locator(MultipleLocator(0.2))
    labels = ax.get_xticklabels() + ax.get_yticklabels()
    [label.set_fontname('Arial') for label in labels]
    plt.xlabel('Probe/Label Interval (ms)', font_label)
    plt.ylabel('Bandwidth Occupation', font_label)
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
    ax.legend( ncol=1, prop=font_legend)
    foo_fig = plt.gcf()  # 'get current figure'
    plt.tight_layout()
    foo_fig.savefig('./overhead.eps', format='eps', dpi=1000,bbox_inches='tight')
    plt.show()