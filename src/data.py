import pandas as pd
import math

def getArr(fileName):
    data = pd.read_csv(fileName)  
    arr = []
    for i in range(21):
        arr.append(data.columns[i])
    return arr

def getData(data, arr, data_all):
    point = []
    for i in range(len(data)):
        for j in range(2, len(arr)):
            if math.isnan(int(data[arr[j]][i])):
                point.append(0)
            else:
                point.append(data[arr[j]][i])
            
        pkt_lost = data['OUT-MBits Transmitted/sec'][i]/data['IN-MBits Received/sec'][i]
        point.append(pkt_lost)
        point.append(data['Lable'][i])
        data_all.append(point)
        point = []
        pkt_lost = 0  
    return data_all

def main():
    data_all = []
    data_1 = pd.read_csv('1.csv')
    data_2 = pd.read_csv('2.csv')
    data_3 = pd.read_csv('3.csv')
    data_4 = pd.read_csv('4.csv')
    data_5 = pd.read_csv('5.csv')
    data_6 = pd.read_csv('6.csv')
    data_7 = pd.read_csv('7.csv')
    data_8 = pd.read_csv('8.csv')
    data_9 = pd.read_csv('9.csv')
    data_10 = pd.read_csv('10.csv')
    data_11 = pd.read_csv('11.csv')
    # data_12 = pd.read_csv('12.csv')
    # data_13 = pd.read_csv('13.csv')
    # data_14 = pd.read_csv('14.csv')
    # data_15 = pd.read_csv('15.csv')
    # data_16 = pd.read_csv('16.csv')
    # data_17 = pd.read_csv('17.csv')
    # data_18 = pd.read_csv('18.csv')
    # data_19 = pd.read_csv('19.csv')
    # data_20 = pd.read_csv('20.csv')



    arr = getArr('1.csv')
    data1 = getData(data_1, arr, data_all)
    data2 = getData(data_2, arr, data_all)
    data3 = getData(data_3, arr, data_all)
    data4 = getData(data_4, arr, data_all)
    data5 = getData(data_5, arr, data_all)
    data6 = getData(data_6, arr, data_all)
    data7 = getData(data_7, arr, data_all)
    data8 = getData(data_8, arr, data_all)
    data9 = getData(data_9, arr, data_all)
    data10 = getData(data_10, arr, data_all)
    data11 = getData(data_11, arr, data_all)
    # data12 = getData(data_12, arr, data_all)
    # data13 = getData(data_13, arr, data_all)
    # data14 = getData(data_14, arr, data_all)
    # data15 = getData(data_15, arr, data_all)
    # data16 = getData(data_16, arr, data_all)
    # data17 = getData(data_17, arr, data_all)
    # data18 = getData(data_18, arr, data_all)
    # data19 = getData(data_19, arr, data_all)
    # data20 = getData(data_20, arr, data_all)

    data_csv = pd.DataFrame(data11)
    data_csv.columns = [
                        '% CPU Latency', '% Demand', 
                        '% Idle', '% Overlap', 
                        '% Ready', '% Run', 
                        '% Used', '% Wait', 
                        'Power Usage Watts', 'Switches/sec', 
                        'Timers/sec', 'Wakeups/sec', 
                        'IN-MBits Received/sec', 'OUT-MBits Transmitted/sec', 
                        'Commands/sec', 'Reads/sec', 
                        'Writes/sec', 'Mem total/KB', 
                        'Mem used/KB', 'OUT/IN',
                        'Lable']
    data_csv.to_csv('data.csv',index=False)
       
if __name__ == '__main__':
    main()