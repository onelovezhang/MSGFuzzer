import matplotlib.pyplot as plt
from math import *
from matplotlib.pyplot import MultipleLocator
import numpy as np

def data_crash_hour(crash_time_list, crash_num_list, is_print = False):
    total_time = sum(crash_time_list)/3600
    total_crash = sum(crash_num_list)
    if is_print:
        print(f"total_time: {total_time}\ntotal_crash: {total_crash}")
    crash_time_hour = [0]
    crash_num_hour = [0]
    count_num = 0
    for hours_i in range(24):
        count_time = 0
        for i in range(len(crash_time_list)):
            count_time += crash_time_list[i]
            if (count_time > hours_i * 3600) and (count_time <= (hours_i + 1) * 3600):
                count_num += crash_num_list[i]
        crash_time_hour.append(hours_i + 1)
        crash_num_hour .append(count_num)

    return crash_time_hour, crash_num_hour


fig, ax = plt.subplots(1,2, figsize=(10,5))
ax[0].spines['right'].set_visible(False)
ax[0].spines['left'].set_linewidth(2)
ax[0].spines['top'].set_visible(False)
ax[0].spines['bottom'].set_linewidth(2)

plt.subplot(1,2,1)
plt.xlim(-0.5, 25)
plt.ylim(-0.5, 33)
plt.grid(False)
plt.xlabel("Time(Hour)")
plt.ylabel("Crash Number")
plt.title("Crash Detection")\

plt.subplot(1,2,2)
ax[1].spines['right'].set_visible(False)
ax[1].spines['left'].set_linewidth(2)
ax[1].spines['top'].set_visible(False)
ax[1].spines['bottom'].set_linewidth(2)
plt.xlim(-0.5, 25)
plt.ylim(-0.5, 14)
plt.grid(False)
plt.xlabel("Time(Hour)")
plt.ylabel("Unique Crash Number")
plt.title("Unique Crash Detection")

x_major_locator=MultipleLocator(2)

y_major_locator=MultipleLocator(5)


ax[0].xaxis.set_major_locator(x_major_locator)

ax[0].yaxis.set_major_locator(y_major_locator)
x_major_locator=MultipleLocator(2)

y_major_locator=MultipleLocator(5)

ax[1].xaxis.set_major_locator(x_major_locator)

ax[1].yaxis.set_major_locator(y_major_locator)

# MSGFuzzer

crash_time_num = [[0, 0], [398, 3], [2617, 3], [3521, 5], [3087, 0], [2876, 3], [1623, 2], [7281, 2], [6787, 0], [2918, 2], [4498, 0], [5603, 3], [5425, 0], [2913, 3], [4961, 2], [7653, 2], [15115, 1], [8265, 0]]
unique_crash_time_num = [[0, 0], [398, 2], [2617, 1], [3521, 2], [3087, 0], [2876, 1], [1623, 0], [7281, 2], [6787, 0], [2918, 1], [4498, 1], [5603, 0], [5425, 1], [2913, 0], [4961, 0], [7653, 0], [15115, 1], [8265, 0]]
crash_time_num = np.array(crash_time_num)
unique_crash_time_num = np.array(unique_crash_time_num)
crash_time_hour, crash_num_hour = data_crash_hour(crash_time_num[:,0], crash_time_num[:, 1], is_print=True)
crash_time_hour, unique_crash_num_hour = data_crash_hour(unique_crash_time_num[:,0], unique_crash_time_num[:, 1], is_print=True)
print(crash_time_hour)
print(crash_num_hour)
print(unique_crash_num_hour)
# plt.subplot(1, 2, 1)
plt.subplot(1,2,1)
plt.plot(crash_time_hour, crash_num_hour, c = 'r', linestyle='--', linewidth = 2, label = "MSGFuzzer")
plt.subplot(1,2,2)
plt.plot(crash_time_hour, unique_crash_num_hour, c = 'r', linestyle='--', linewidth = 2, label = "MSGFuzzer")

# KittyFuzzer
print("============KittyFuzzer============")

crash_time_num = [[0, 0], [837, 2], [3345, 3],  [1287, 1], [7190, 1], [7625, 1], [7726, 1], [2817, 1], [4312, 0], [7918, 1], [4107, 0], [8012, 0], [10928, 0], [6516, 0], [4345 + 7635, 0]]
unique_crash_time_num = [[0, 0], [837, 1], [3345, 0],  [1287, 1], [7190, 1], [7625, 1], [7726, 0], [2817, 0], [4312, 0], [7918, 0], [4107, 0], [8012, 0], [10928, 0], [6516, 0], [4345 + 7635, 0]]
crash_time_num = np.array(crash_time_num)
unique_crash_time_num = np.array(unique_crash_time_num)
crash_time_hour, crash_num_hour = data_crash_hour(crash_time_num[:,0], crash_time_num[:, 1], is_print=True)
crash_time_hour, unique_crash_num_hour = data_crash_hour(unique_crash_time_num[:,0], unique_crash_time_num[:, 1], is_print=True)
print(crash_time_hour)
print(crash_num_hour)
print(unique_crash_num_hour)
# plt.subplot(2, 2, 2)
plt.subplot(1,2,1)
plt.plot(crash_time_hour, crash_num_hour, c = 'b', linestyle='--', linewidth = 2, label = "KittyFuzzer")
plt.subplot(1,2,2)
plt.plot(crash_time_hour, unique_crash_num_hour, c = 'b', linestyle='--', linewidth = 2, label = "KittyFuzzer")


# Boofuzz 
print("============Boofuzz============")

crash_time_num = [[0, 0], [1126, 3], [3322, 2], [2019, 2], [6415, 2], [7918, 1], [5618, 1], [9287, 1], [6012, 0], [7112, 0], [16827, 0], [4345 + 5627, 0], [8826, 0]]
unique_crash_time_num = [[0, 0], [1126, 1], [3322, 1], [2019, 1], [6415, 1], [7918, 1], [5618, 0], [9287, 0], [6012, 0], [7112, 0], [16827, 0], [4345 + 5627, 0], [8826, 0]]
crash_time_num = np.array(crash_time_num)
unique_crash_time_num = np.array(unique_crash_time_num)
crash_time_hour, crash_num_hour = data_crash_hour(crash_time_num[:,0], crash_time_num[:, 1], is_print=True)
crash_time_hour, unique_crash_num_hour = data_crash_hour(unique_crash_time_num[:,0], unique_crash_time_num[:, 1], is_print=True)
print(crash_time_hour)
print(crash_num_hour)
print(unique_crash_num_hour)
# plt.subplot(2, 2, 3)
plt.subplot(1,2,1)
plt.plot(crash_time_hour, crash_num_hour, c = 'g', linestyle='--', linewidth = 2, label = "Boofuzz")
plt.subplot(1,2,2)
plt.plot(crash_time_hour, unique_crash_num_hour, c = 'g', linestyle='--', linewidth = 2, label = "Boofuzz")

# Normal-MSGFuzzer
print("============Normal-MSGFuzzer============")

crash_time_num = [[0, 0], [1126, 2], [7817, 2], [1978, 0], [5516, 1], [6714, 0], [9618, 0], [9716, 2], [7012, 0], [8917, 1], [7717, 1], [2871 + 6001, 1], [9981, 1]]
unique_crash_time_num = [[0, 0], [1126, 1], [7817, 1], [1978, 0], [5516, 0], [6714, 0], [9618, 0], [9716, 1], [7012, 0], [8917, 0], [7717, 1], [2871 + 6001, 1], [9981, 0]]
crash_time_num = np.array(crash_time_num)
unique_crash_time_num = np.array(unique_crash_time_num)
crash_time_hour, crash_num_hour = data_crash_hour(crash_time_num[:,0], crash_time_num[:, 1], is_print=True)
crash_time_hour, unique_crash_num_hour = data_crash_hour(unique_crash_time_num[:,0], unique_crash_time_num[:, 1], is_print=True)
print(crash_time_hour)
print(crash_num_hour)
print(unique_crash_num_hour)
# plt.subplot(2, 2, 3)
plt.subplot(1,2,1)
plt.plot(crash_time_hour, crash_num_hour, c = 'y', linestyle='--', linewidth = 2, label = "Normal-MSGFuzzer")
plt.subplot(1,2,2)
plt.plot(crash_time_hour, unique_crash_num_hour, c = 'y', linestyle='--', linewidth = 2, label = "Normal-MSGFuzzer")
# plt.suptitle("Normal-MSGFuzzer")

# PCFuzzer
print("============PCFuzzer============")

crash_time_num = [[0, 0], [717, 2], [2918, 1],  [1627, 3], [4918, 1], [8911, 2], [1918, 1], [7815, 1], [3819, 2], [8819, 1], [6716, 1], [4012, 2], [5512, 0], [9817, 1], [5816, 2], [12287, 0]]
unique_crash_time_num = [[0, 0], [717, 2], [2918, 0],  [1627, 1], [4918, 0], [8911, 1], [1918, 0], [7815, 1], [3819, 0], [8819, 0], [6716, 1], [4012, 0], [5512, 0], [9817, 0], [5816, 1], [12287, 0]]
crash_time_num = np.array(crash_time_num)
unique_crash_time_num = np.array(unique_crash_time_num)
crash_time_hour, crash_num_hour = data_crash_hour(crash_time_num[:,0], crash_time_num[:, 1], is_print=True)
crash_time_hour, unique_crash_num_hour = data_crash_hour(unique_crash_time_num[:,0], unique_crash_time_num[:, 1], is_print=True)
print(crash_time_hour)
print(crash_num_hour)
print(unique_crash_num_hour)
# plt.subplot(2, 2, 4)
plt.subplot(1,2,1)
plt.plot(crash_time_hour, crash_num_hour, c = 'm', linestyle='--', linewidth = 2, label = "PCFuzzer")
plt.subplot(1,2,2)
plt.plot(crash_time_hour, unique_crash_num_hour, c = 'm', linestyle='--', linewidth = 2, label = "PCFuzzer")

plt.subplot(1,2,1)
# plt.legend(loc = "upper left", fontsize=7)
plt.savefig("crash_detected.pdf")
plt.savefig("crash_detected.png")






