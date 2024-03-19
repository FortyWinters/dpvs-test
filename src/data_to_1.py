import pandas as pd

def main():
    point = []
    arr = []
    data = pd.read_csv('data.csv')
    for i in range(len(data)):
        point.append(data['% CPU Latency'][i]/100)
        point.append(data['% Demand'][i]/1000)
        point.append(data['% Idle'][i]/1000)
        point.append(data['% Overlap'][i]/10)
        point.append(data['% Ready'][i]/100)
        point.append(data['% Run'][i]/1000)
        point.append(data['% Used'][i]/1000)
        point.append(data['% Wait'][i]/10000)
        point.append(data['Power Usage Watts'][i]/1000)
        point.append(data['Switches/sec'][i]/10000)
        point.append(data['Timers/sec'][i]/1000)
        point.append(data['Wakeups/sec'][i]/100000)
        point.append(data['IN-MBits Received/sec'][i]/1000)
        point.append(data['OUT-MBits Transmitted/sec'][i]/1000)
        point.append(data['Commands/sec'][i]/10000)
        point.append(data['Reads/sec'][i]/1000)
        point.append(data['Writes/sec'][i]/10000)
        point.append(data['Mem total/KB'][i]/10000000)
        point.append(data['Mem used/KB'][i]/10000000)
        point.append(data['OUT/IN'][i])
        point.append(data['Lable'][i])


        arr.append(point)
        point = [] 


    data = pd.DataFrame(arr)
    data.columns = ['% CPU Latency','% Demand','% Idle','% Overlap','% Ready','% Run','% Used','% Wait','Power Usage Watts','Switches/sec','Timers/sec','Wakeups/sec','IN-MBits Received/sec','OUT-MBits Transmitted/sec','Commands/sec','Reads/sec','Writes/sec','Mem total/KB','Mem used/KB','OUT/IN','Lable']
    data.to_csv('train_dpvs.csv',index=False)
       
if __name__ == '__main__':
    main()