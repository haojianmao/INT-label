# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import re
from sklearn.preprocessing import minmax_scale
from IPython.core.pylabtools import figsize
from matplotlib.ticker import MultipleLocator

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
    figsize(5, 3)
    plt.figure()
    plt.plot(np.array(data['loss']), list(data['base']), color='red', linewidth=2, linestyle=':', markersize=8,
             marker='^',
             label='Base')
    # plt.plot(df['step'], df['accuracy youku'], color='black', linewidth=3, linestyle=':', markersize=10, marker='.',
    #          label='Youku:LSTM')
    # plt.plot(df['step'], df['accuracy amazon'], color='darkgreen', linewidth=3, linestyle=':', markersize=10,
    #          marker='+', label='Amazon:LSTM')
    plt.plot(np.array(data['loss']), list(data['pro']), color='seagreen', linewidth=2, linestyle=':', markersize=8,
             marker='x', label='Pro')
    # plt.plot(str_process(df[50][0]), color='springgreen', linewidth=3, linestyle=':', markersize=7,
    #          marker='|', label='50')
    # plt.plot(df['step'], df['accuracy youku reverse'], color='springgreen', linewidth=3, linestyle=':', markersize=10,
    #          marker='|', label='Youku:R-LSTM')
    # plt.plot(df['step'], df['accuracy amazon reverse'], color='purple', linewidth=3, linestyle=':', markersize=10,
    #          marker='^', label='Amazon:R-LSTM')
    # plt.ylim(0.4, 1.05)
    plt.xlim(-0.01, 0.6)
    plt.grid()
    plt.tick_params(labelsize=13)
    ax = plt.gca()
    ax.xaxis.set_major_locator(MultipleLocator(0.1))
    ax.yaxis.set_major_locator(MultipleLocator(0.05))
    labels = ax.get_xticklabels() + ax.get_yticklabels()
    [label.set_fontname('Arial') for label in labels]
    plt.xlabel('Packet Loss Rate', font_label)
    plt.ylabel('Coverage Rate', font_label)
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
    ax.legend(ncol=1, prop=font_legend)
    foo_fig = plt.gcf()  # 'get current figure'
    plt.tight_layout()
    foo_fig.savefig('./loss-cover.eps', format='eps', dpi=1000, bbox_inches='tight')
    plt.show()
