import numpy as np
import matplotlib.pyplot as plt


def read_data(filename):
    """
    Returns:
    Dict with lists of readings, where each reading is a list
    """
    data = {'GYR': [], 'ACC': [], 'RSSWIFI': [], 'GPS': []}
    for line in open(filename):
        words = line.split("\t")
        words[-1] = words[-1].strip()
        tag = words[1]
        data[tag].append([words[0]] + words[2:])
        return data
