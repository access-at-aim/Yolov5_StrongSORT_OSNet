# load libraries and set plot parameters
# import numpy as np
import matplotlib

# plt.rcParams['text.usetex'] = True

MM_TO_INCH = 1./25.4
label_size = 8
font_size = 7
legend_size = 7

def ticks_size():
    """Size of axes' ticks
    """
    return 8


def axis_lw():
    """Line width of the axes
    """
    return 0.6


def plot_lw():
    """Line width of the plotted curves
    """
    return 1.5


def figsize_mm(width, height=None, aspect=4/3):
    if height is None:
        height = width/aspect
    return width*MM_TO_INCH, height*MM_TO_INCH


figsizes = {'single': figsize_mm(90),
            '1.5': figsize_mm(140),
            'double': figsize_mm(190)}

params = {'savefig.dpi': 1000,
#               'text.usetex': True,
              'figure.dpi': 1000,
              'figure.figsize': figsizes['single'],
              'font.size': font_size,
              'axes.labelsize': label_size,
              'axes.titlesize': font_size,
              'axes.linewidth': axis_lw(),
#               'text.fontsize': font_size,
              'xtick.labelsize': ticks_size(),
              'ytick.labelsize': ticks_size(),
              'font.family': 'serif',
              'legend.fontsize': legend_size,
              'lines.markersize': 8,
         'grid.linewidth': 0.2,
         'grid.linestyle': '--',
         'legend.framealpha': 1,
         'legend.frameon': True}

matplotlib.rcParams.update(params)
