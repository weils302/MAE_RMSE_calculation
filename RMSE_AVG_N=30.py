import csv
import os
from random import sample
import numpy as np
from sklearn.metrics import mean_squared_error

RMSE = []
rootDir = ''
os.chdir(rootDir)

obs = []
list_dirs = os.walk(rootDir)

for root, dirs, files in list_dirs:
    for d in dirs:
        # read obs data
        os.chdir(rootDir + d)
        csvFile = open('testy_h.csv', 'r')
        obs_reader = csv.reader(csvFile)
        obs.clear()
        for item in obs_reader:
            obs.append(float(item[4]))
        csvFile.close()

        # read sim data, calculate RMSE
        RMSE = []
        for times in range(40):  # 40 times of pick up
            randomNo = sample(range(500), 30)
            randomNo.sort()
            sim_Data_seq = []  # 多次训练结果的列表
            for n in randomNo:
                sim_Data = []  # sim_data：一次训练的8736个预测值
                # n_seq_no = randomNo.index(n)    #n在列表中的序号
                csvFile = open('test_%s.csv' % n, 'r')
                sim_reader = csv.reader(csvFile)
                for item in sim_reader:
                    sim_Data.append(item[4])
                sim_Data_seq.append(sim_Data)
                csvFile.close()
            sim_array = np.array(sim_Data_seq, float)  # 列表放进数组
            sim_array_avg = np.mean(sim_array, axis=0)  # 算平均
            sim_list_avg = sim_array_avg.tolist()  # 转换为list
            RMSE.append(np.sqrt(mean_squared_error(sim_list_avg, obs)))
            print(d + str(times))

        os.chdir(os.path.abspath(r".."))
        csvFile = open('RMSE_elu.csv', 'a', newline='')
        writer = csv.writer(csvFile)
        writer.writerow([d] + RMSE)
        csvFile.close()
