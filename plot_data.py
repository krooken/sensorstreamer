import matplotlib.pyplot as plt
import numpy as np
import calc_stats
import math

def plot_timeseries(ts, labels=['x', 'y', 'z', 'bx', 'by', 'bz'],
        ylabel='', start_time=-1, end_time=-1):
    plt.figure()
    plt.ion()

    time = time_offset_base(ts['Time'])

    start_index, end_index = index_helper(start_time, end_time, time)

    for column, legend in zip(ts['Data'].T, labels):
        plt.plot(time[start_index:end_index], column[start_index:end_index], label=legend)

    plt.ylabel(ylabel)
    plt.xlabel('Time [s]')
    plt.title(ts['Tag'])

    plt.legend()
    plt.show()
    plt.ioff()

def hist_timeseries(ts, labels=['x', 'y', 'z', 'bx', 'by', 'bz'],
        xlabel='', start_time=-1, end_time=-1, plot_dist=False):

    time = time_offset_base(ts['Time'])

    start_index, end_index = index_helper(start_time, end_time, time)

    colors = ['dodgerblue','darkorange','g','r','c','m','y','k','w']

    for column, legend, color in \
            zip(ts['Data'].T, labels, colors):
        plt.figure()
        plt.ion()

        data = column[start_index:end_index]
        nr_bins = math.sqrt(data.size)
        n,bins,_ = plt.hist(data,
            label=legend,
            color=color,
            bins='auto')

        if plot_dist:
            sum = 0.0
            for i in range(0,len(n)):
                sum += n[i]*(bins[i+1] - bins[i])
            x, c = calc_stats.bell_curve(data)
            plt.plot(x, np.multiply(c, sum), color='k')

        plt.ylabel('#')
        plt.xlabel(xlabel)
        plt.title(ts['Tag'])

        plt.legend()
        plt.show()
        plt.ioff()

def index_helper(start_time, end_time, time):

    if start_time < 0:
        start_index = 0
    else:
        start_index = np.where(time >= start_time)[0][0]

    if end_time < 0:
        end_index = time.size - 1
    else:
        end_index = np.where(time <= end_time)[0][-1]

    return start_index, end_index

def time_offset_base(time_ms):
    first_time = time_ms[0]
    time_s = np.asarray([float(t - first_time)/1000.0 for t in time_ms])
    return time_s
