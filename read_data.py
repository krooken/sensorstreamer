import numpy as np
import matplotlib.pyplot as plt


def read_data(filename):
    """
    Returns:
    Dict with lists of readings, where each reading is a list
    """

    data = {
        'GYR': [],      # Gyroscope; x, y, z [rad/s]
        'ACC': [],      # Accelerometer; x, y, z [m/s^2]
        'RSSWIFI': [],  # Received Signal Strength: WiFi
        'GPS': [],      # GPS [deg North, deg East, alt m]
        'RAWGYR': [],   # Uncalibrated gyroscope; x, y, z, bx, by, bz [rad/s]
        'PRX': [],      # Proximity; [cm]
        'MAG': [],      # Magnetometer; x, y, z [uT]
        'RAWMAG': [],   # Uncalibrated magnetometer; x, y, z, bx, by, bz [uT]
        'LGT': [],      # Light [lx]
        'PRS': [],      # Pressure [hPa]
        'ORI': [],      # Orientation [normalized quaternion]
        'RSSBLE': [],   # Received Signal Strength: Bluetooth Low Energy
        'RSSCELL': []}  # Received Signal Strength: Cellular

    # Keep track of the elements that weren't parsed.
    unknown_tags = set()

    with open(filename) as datafile:
        for line in datafile:
            words = line.split("\t")
            words[-1] = words[-1].strip()
            tag = words[1]
            if tag in data:
                data[tag].append([words[0]] + words[2:])
            else:
                # The tag is currently unknown.
                unknown_tags.add(tag)
    return data, unknown_tags

def extract_timeseries(data, tag):
    timeseries = {'Tag': tag, 'Time': [], 'Data': []}

    timeseries['Data'] = np.asarray([
        [float(elem) for elem in reading[1:]
            ] for reading in data[tag]])

    timeseries['Time'] = np.asarray(
        [float(reading[0]) for reading in data[tag]])

    return timeseries

def get_data_ssid(data, ssid):
    tag = 'RSSWIFI'

    timeseries = {'Tag': tag, 'Time': [], 'Data': []}

    data_ssid = list(filter((lambda x: x[2] == ssid), data[tag]))
    timeseries['Data'] = np.asarray([int(reading[-1]) for reading in data_ssid])

    timeseries['Time'] = np.asarray([float(reading[0]) for reading in data_ssid])

    return timeseries
