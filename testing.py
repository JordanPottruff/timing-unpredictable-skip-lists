import time
import math

from skip_list import SkipList
from tusl import TUSL
import matplotlib.pyplot as plt

NUMBER_OF_ITEMS = 100
NUMBER_OF_RUNS = 200000

def test_skip_list():
    skip_list = SkipList()
    items = list(range(NUMBER_OF_ITEMS))
    for item in items:
        skip_list.insert(item)

    skip_times = []
    for item in items:
        start = time.time() * 1000
        for i in range(NUMBER_OF_RUNS):
            skip_list.search(item)
        end = time.time() * 1000
        skip_times.append(end-start)
    mean_skip_time = sum(skip_times) / len(skip_times)
    std_dev_skip_time = math.sqrt(sum([(mean_skip_time - t)**2 for t in skip_times]))
    max_z_score_skip_time = (max(skip_times) - mean_skip_time) / std_dev_skip_time

    print(skip_times)
    print(mean_skip_time)
    print(std_dev_skip_time)
    print(max_z_score_skip_time)


    tusl_list = TUSL(skip_list)
    tusl_times = []
    for item in items:
        start = time.time() * 1000
        for i in range(NUMBER_OF_RUNS):
            tusl_list.search(item)
        end = time.time() * 1000
        tusl_times.append(end-start)
    mean_tusl_time = sum(tusl_times) / len(tusl_times)
    std_dev_tusl_time = math.sqrt(sum([(mean_tusl_time - t) ** 2 for t in tusl_times]))
    max_z_score_tusl_time = (max(tusl_times) - mean_tusl_time) / std_dev_tusl_time

    print(tusl_times)
    print(mean_tusl_time)
    print(std_dev_tusl_time)
    print(max_z_score_tusl_time)

    list_times = []
    for item in items:
        start = time.time() * 1000
        for i in range(NUMBER_OF_RUNS):
            items.index(item)
        end = time.time() * 1000
        list_times.append(end-start)
    mean_list_time = sum(list_times) / len(list_times)
    std_dev_list_time = math.sqrt(sum([(mean_list_time - t) ** 2 for t in list_times]))
    max_z_score_list_time = (max(list_times) - mean_list_time) / std_dev_list_time

    print(list_times)
    print(mean_list_time)
    print(std_dev_list_time)
    print(max_z_score_list_time)

    fig1 = plt.figure(1, (12, 12))
    plt.bar(items, skip_times)
    fig2 = plt.figure(2, (12, 12))
    plt.bar(items, tusl_times)
    plt.show()


test_skip_list()