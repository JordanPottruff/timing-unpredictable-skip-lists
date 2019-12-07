# testing.py
# Tests the skip list and TUSL according to our experimental design, where we query the items in each data structure
# and graph the time taken to query each index.
import time
import math

from skip_list import SkipList
from tusl import TUSL
import matplotlib.pyplot as plt

# The integers to add, from 0 to NUMBER_OF_ITEMS
NUMBER_OF_ITEMS = 100
# The number of times to run queries on a single item to eliminate noise.
NUMBER_OF_RUNS = 1000


# For both data structures
def test():
    skip_list = SkipList()
    items = list(range(NUMBER_OF_ITEMS))
    for item in items:
        skip_list.insert(item)

    # Runs the experiment on the original skip list.
    skip_times = [0 for i in items]
    for i in range(NUMBER_OF_RUNS):
        for item in items:
            start = time.time() * 1000
            skip_list.search(item)
            end = time.time() * 1000
            skip_times[item] += (end - start) / NUMBER_OF_RUNS
    mean_skip_time = sum(skip_times) / len(skip_times)
    std_dev_skip_time = math.sqrt(sum([(mean_skip_time - t)**2 for t in skip_times]))
    max_z_score_skip_time = (max(skip_times) - mean_skip_time) / std_dev_skip_time

    print("Skip List Data: ")
    print(skip_times)
    print(mean_skip_time)
    print(std_dev_skip_time)
    print(max_z_score_skip_time)

    # Runs the experiment on the TUSL.
    tusl_list = TUSL(skip_list)
    tusl_times = [0 for i in items]
    for i in range(NUMBER_OF_RUNS):
        for item in items:
            start = time.time() * 1000
            tusl_list.search(item)
            end = time.time() * 1000
            tusl_times[item] += (end-start) / NUMBER_OF_RUNS
    mean_tusl_time = sum(tusl_times) / len(tusl_times)
    std_dev_tusl_time = math.sqrt(sum([(mean_tusl_time - t) ** 2 for t in tusl_times]))
    max_z_score_tusl_time = (max(tusl_times) - mean_tusl_time) / std_dev_tusl_time

    print("TUSL Data: ")
    print(tusl_times)
    print(mean_tusl_time)
    print(std_dev_tusl_time)
    print(max_z_score_tusl_time)

    # Creates charts showing the query times for each index.
    fig1 = plt.figure(1, (12, 12))
    plt.bar(items, skip_times)
    fig2 = plt.figure(2, (12, 12))
    plt.bar(items, tusl_times)
    plt.show()


test()