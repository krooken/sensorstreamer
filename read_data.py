import numpy as np
import matplotlib.pyplot as plt


def read_data(filename):
    """
    Returns:
    Dict with lists of readings, where each reading is a list
    """

    data = {
        'GYR': [],
        'ACC': [],
        'RSSWIFI': [],
        'GPS': [],
        'RAWGYR': [],
        'PRX': [],
        'MAG': [],
        'RAWMAG': [],
        'LGT': [],
        'PRS': [],
        'ORI': [],
        'RSSBLE': [],
        'RSSCELL': []}

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
