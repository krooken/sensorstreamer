import matplotlib.pyplot as plt

def plot_timeseries(ts, labels=['x', 'y', 'z', 'bx', 'by', 'bz'],  ylabel=''):
    plt.figure()
    plt.ion()

    time_ms = ts['Time']
    time = [float(t)/1000.0 for t in time_ms]

    for column, legend in zip(ts['Data'].T, labels):
        plt.plot(time, column, label=legend)

    plt.ylabel(ylabel)
    plt.xlabel('Time [s]')
    plt.title(ts['Tag'])

    plt.legend()
    plt.show()
    plt.ioff()
