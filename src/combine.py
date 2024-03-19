from cmath import isnan, nan
import pandas as pd
import datetime
import math

def test(fileDelay, fileEsxtop, fileFailure, fileEsxtopAndDelay):
    data_delay = pd.read_csv(fileDelay)
    data_esxtop = pd.read_csv(fileEsxtop)
    data_failure = pd.read_csv(fileFailure)
    data_esxtopanddelay = pd.read_csv(fileEsxtopAndDelay)
    
    time_delay = str(datetime.datetime.fromtimestamp(data_delay['0'][0]) - datetime.timedelta(0, 28800, 0))[11:].replace(':','')
    time_esxtop = str(data_esxtop['(PDH-CSV 4.0) ('][0][0:19])[11:].replace(':','')
    time_failure = time_change(data_failure['timestamp'][0][18:26].replace(':',''))
    time_esxtopanddelay = data_esxtopanddelay['TimeStamp'][0][11:19].replace(':','')


    print(time_delay)
    print(time_esxtop)
    print(time_failure)
    print(time_esxtopanddelay)

#ESXi = VNF-8h69s
# ESXI = 
def time_change(time):
    hour = int(time[0:2]) 
    min = int(time[2:4])
    sec = int(time[4:6])    
    time_new = datetime.timedelta(0, hour*3600+min*60+sec-8*3600+120+15, 0)
    return ("000000" + str(time_new).replace(':',''))[-6:]

def esxtop():
    point = []
    data_esxtop = []
    data_capture = pd.read_csv('capture.csv')
    arr = [r'(PDH-CSV 4.0) (UTC)(0)',r'\\localhost\Group Cpu(2012201:FlowMonitor-csy)\% CPU Latency',r'\\localhost\Group Cpu(2012201:FlowMonitor-csy)\% Demand', \
        r'\\localhost\Group Cpu(2012201:FlowMonitor-csy)\% Idle',r'\\localhost\Group Cpu(2012201:FlowMonitor-csy)\% Overlap', \
            r'\\localhost\Group Cpu(2012201:FlowMonitor-csy)\% Ready',r'\\localhost\Group Cpu(2012201:FlowMonitor-csy)\% Run', \
            r'\\localhost\Group Cpu(2012201:FlowMonitor-csy)\% Used',r'\\localhost\Group Cpu(2012201:FlowMonitor-csy)\% VmWait', \
                r'\\localhost\Group Cpu(2012201:FlowMonitor-csy)\% Wait',r'\\localhost\Group Cpu(2012201:FlowMonitor-csy)\Migrates/sec', \
                    r'\\localhost\Group Cpu(2012201:FlowMonitor-csy)\Power Usage Watts',r'\\localhost\Group Cpu(2012201:FlowMonitor-csy)\Switches/sec', \
                    r'\\localhost\Group Cpu(2012201:FlowMonitor-csy)\Timers/sec',r'\\localhost\Group Cpu(2012201:FlowMonitor-csy)\Wakeups/sec', \
                        r'\\localhost\Network Port(sfc_switch:67109185:2378066:FlowMonitor-csy)\% Received Packets Dropped', \
                            r'\\localhost\Network Port(sfc_switch:67109185:2378066:FlowMonitor-csy)\MBits Received/sec', \
                                r'\\localhost\Network Port(sfc_switch:67109184:2378066:FlowMonitor-csy)\MBits Transmitted/sec', \
                                    r'\\localhost\Virtual Disk(FlowMonitor-csy)\Average MilliSec/Write',  \
                                        r'\\localhost\Virtual Disk(FlowMonitor-csy)\Commands/sec', \
                                            r'\\localhost\Virtual Disk(FlowMonitor-csy)\Reads/sec', \
                                                r'\\localhost\Virtual Disk(FlowMonitor-csy)\Writes/sec']

    for i in range(len(data_capture)):
        print(i)
        for j in range(len(arr)):
            point.append(data_capture[arr[j]][i])
        data_esxtop.append(point)
        point = []
    data = pd.DataFrame(data_esxtop)
    data.columns = ['TimeStamp','% CPU Latency','% Demand','% Idle','% Overlap','% Ready','% Run','% Used','% VmWait','% Wait','Migrates/sec','Power Usage Watts','Switches/sec','Timers/sec','Wakeups/sec','% IN-Received Packets Dropped','IN-MBits Received/sec','OUT-MBits Transmitted/sec','Average MilliSec/Write','Commands/sec','Reads/sec','Writes/sec']
    data.to_csv('esxtop.csv')

def extop_dpvs():
    point = []
    data_esxtop = []
    data_csv = pd.read_csv('data.csv')
    arr = [r'(PDH-CSV 4.0) (', r'\\localhost\Group Cpu(37093751:dpvs_csy)\% CPU Latency', \
            r'\\localhost\Group Cpu(37093751:dpvs_csy)\% Demand', r'\\localhost\Group Cpu(37093751:dpvs_csy)\% Idle', \
            r'\\localhost\Group Cpu(37093751:dpvs_csy)\% Overlap', r'\\localhost\Group Cpu(37093751:dpvs_csy)\% Ready', \
            r'\\localhost\Group Cpu(37093751:dpvs_csy)\% Run', r'\\localhost\Group Cpu(37093751:dpvs_csy)\% Used', \
            r'\\localhost\Group Cpu(37093751:dpvs_csy)\% Wait', r'\\localhost\Group Cpu(37093751:dpvs_csy)\Power Usage Watts', \
            r'\\localhost\Group Cpu(37093751:dpvs_csy)\Switches/sec', r'\\localhost\Group Cpu(37093751:dpvs_csy)\Timers/sec', \
            r'\\localhost\Group Cpu(37093751:dpvs_csy)\Wakeups/sec', r'\\localhost\Network Port(vnf_switch:67108883:4441444:dpvs_csy)\MBits Received/sec', \
            r'\\localhost\Network Port(vnf_switch:67108884:4441444:dpvs_csy)\MBits Transmitted/sec', r'\\localhost\Virtual Disk(dpvs_csy)\Commands/sec', \
            r'\\localhost\Virtual Disk(dpvs_csy)\Reads/sec', r'\\localhost\Virtual Disk(dpvs_csy)\Writes/sec']
        
    
    for i in range(len(data_csv)):
        print(i)
        for j in range(len(arr)):
            point.append(data_csv[arr[j]][i])
        data_esxtop.append(point)
        point = []
    data = pd.DataFrame(data_esxtop)
    data.columns = ['TimeStamp','% CPU Latency', 
                    '% Demand','% Idle', 
                    '% Overlap','% Ready',
                    '% Run','% Used',
                    '% Wait','Power Usage Watts',
                    'Switches/sec','Timers/sec',
                    'Wakeups/sec','IN-MBits Received/sec',
                    'OUT-MBits Transmitted/sec','Commands/sec',
                    'Reads/sec','Writes/sec']
    data.to_csv('esxtop.csv')

def insertDelay(fileDelay, fileEsxtop, fileName):
    n = []
    point = []
    arr = []

    data_delay = pd.read_csv(fileDelay)
    data_esxtop = pd.read_csv(fileEsxtop)

    for i in range(1,23):
        n.append(data_esxtop.columns[i])

    for i in range(len(data_esxtop)):
        time_esxtop = str(data_esxtop['TimeStamp'][i][0:19])[11:].replace(':','')
        for j in range(len(data_delay)):
            time_delay = str(datetime.datetime.fromtimestamp(data_delay['0'][j]) - datetime.timedelta(0, 28800, 0))[11:].replace(':','')
            if time_esxtop == time_delay:
                for k in range(22):
                    point.append(data_esxtop[n[k]][i])
                point.append(data_delay['2'][j])
                arr.append(point)
                point = []

    data = pd.DataFrame(arr)
    data.columns = ['TimeStamp','% CPU Latency','% Demand','% Idle','% Overlap','% Ready','% Run','% Used','% VmWait','% Wait','Migrates/sec','Power Usage Watts','Switches/sec','Timers/sec','Wakeups/sec','% IN-Received Packets Dropped','IN-MBits Received/sec','OUT-MBits Transmitted/sec','Average MilliSec/Write','Commands/sec','Reads/sec','Writes/sec','Delay/us']
    data.to_csv(fileName)

def insertFailure(fileFailure, fileEsxtopAndDelay, fileName):
    n = []
    point = []
    arr = []

    data_failure = pd.read_csv(fileFailure)
    data_esxtopanddelay = pd.read_csv(fileEsxtopAndDelay)

    for i in range(1,24):
        n.append(data_esxtopanddelay.columns[i])

    for i in range(len(data_esxtopanddelay)):
        time_esxtopanddelay = data_esxtopanddelay['TimeStamp'][i][11:19].replace(':','')
        for j in range(len(data_failure)):
            time_failure = time_change(data_failure['timestamp'][j][18:26].replace(':',''))
            if time_esxtopanddelay == time_failure:
                for k in range(23):
                    point.append(data_esxtopanddelay[n[k]][i])
                point.append(data_failure['mem_total'][j])
                point.append(data_failure['mem_used'][j])
                point.append(data_failure['lable'][j])
                arr.append(point)
                point = []

    data = pd.DataFrame(arr)
    data.columns = ['TimeStamp','%CPU Latency','% Demand','% Idle','% Overlap','% Ready','% Run','% Used','% VmWait','% Wait','Migrates/sec','Power Usage Watts','Switches/sec','Timers/sec','Wakeups/sec','% IN-Received Packets Dropped','IN-MBits Received/sec','OUT-MBits Transmitted/sec','Average MilliSec/Write','Commands/sec','Reads/sec','Writes/sec','Delay/us','mem total/KB','mem used/KB','lable']
    data.to_csv(fileName)

def insertFailure_dpvs():
    n = []
    point = []
    arr = []
    data_esxtop = pd.read_csv('esxtop.csv')
    cpu_failure = pd.read_csv('cpu.csv')
    vm_failure = pd.read_csv('vm.csv')
    io_failure = pd.read_csv('io.csv')
    pl_failure = pd.read_csv('pl.csv')

    for i in range(1,19):
        n.append(data_esxtop.columns[i])

    for i in range(len(data_esxtop)):
        time_esxtop = data_esxtop['TimeStamp'][i][11:19].replace(':','')
        for j in range(len(cpu_failure)):
            time_failure = time_change(cpu_failure['timestamp'][j][18:26].replace(':',''))
            if time_esxtop == time_failure:
                for k in range(18):
                    point.append(data_esxtop[n[k]][i])
                point.append(cpu_failure['mem_total'][j])
                point.append(cpu_failure['mem_used'][j])
                point.append(cpu_failure['lable'][j])
                arr.append(point)
                point = []
        for j in range(len(vm_failure)):
            time_failure = time_change(vm_failure['timestamp'][j][18:26].replace(':',''))
            if time_esxtop == time_failure:
                for k in range(18):
                    point.append(data_esxtop[n[k]][i])
                point.append(vm_failure['mem_total'][j])
                point.append(vm_failure['mem_used'][j])
                point.append(vm_failure['lable'][j])
                arr.append(point)
                point = []
        for j in range(len(io_failure)):
            time_failure = time_change(io_failure['timestamp'][j][18:26].replace(':',''))
            if time_esxtop == time_failure:
                for k in range(18):
                    point.append(data_esxtop[n[k]][i])
                point.append(io_failure['mem_total'][j])
                point.append(io_failure['mem_used'][j])
                point.append(io_failure['lable'][j])
                arr.append(point)
                point = []
        # for j in range(len(pl_failure)):
        #     time_failure = time_change(pl_failure['timestamp'][j][18:26].replace(':',''))
        #     if time_esxtop == time_failure:
        #         for k in range(18):
        #             point.append(data_esxtop[n[k]][i])
        #         point.append(pl_failure['mem_total'][j])
        #         point.append(pl_failure['mem_used'][j])
        #         point.append(pl_failure['lable'][j])
        #         arr.append(point)
        #         point = []

    data = pd.DataFrame(arr)
    data.columns = ['TimeStamp', '% CPU Latency', 
                    '% Demand', '% Idle', 
                    '% Overlap', '% Ready',
                    '% Run', '% Used',
                    '% Wait', 'Power Usage Watts',
                    'Switches/sec', 'Timers/sec',
                    'Wakeups/sec', 'IN-MBits Received/sec',
                    'OUT-MBits Transmitted/sec', 'Commands/sec',
                    'Reads/sec', 'Writes/sec',
                    'Mem total/KB', 'Mem used/KB',
                    'Lable']
    data.to_csv('result.csv')

def getCsv(filePath, fileName):
    point = []
    arr = []
    data_csv = pd.read_csv(filePath)
    title = ['TimeStamp','%CPU Latency','% Demand','% Idle','% Overlap','% Ready','% Run','% Used','% VmWait','% Wait','Migrates/sec','Power Usage Watts','Switches/sec','Timers/sec','Wakeups/sec','% IN-Received Packets Dropped','IN-MBits Received/sec','OUT-MBits Transmitted/sec','Average MilliSec/Write','Commands/sec','Reads/sec','Writes/sec','Delay/us','mem total/KB','mem used/KB','lable']
    for i in range(len(data_csv)):
        for j in range(1,len(title)):
            if math.isnan(data_csv[title[j]][i]):
                point.append(0)
            else:
                point.append(data_csv[title[j]][i])
        arr.append(point)
        point = []
    
    data = pd.DataFrame(arr)
    data.columns = ['%CPU Latency','% Demand','% Idle','% Overlap','% Ready','% Run','% Used','% VmWait','% Wait','Migrates/sec','Power Usage Watts','Switches/sec','Timers/sec','Wakeups/sec','% IN-Received Packets Dropped','IN-MBits Received/sec','OUT-MBits Transmitted/sec','Average MilliSec/Write','Commands/sec','Reads/sec','Writes/sec','Delay/us','mem total/KB','mem used/KB','lable']
    data.to_csv(fileName, index=False)


def main():
    # esxtop()
    # insertDelay('delay.csv', 'esxtop.csv', 'insertDelay.csv')
    # insertFailure('random.csv', 'insertDelay.csv', 'data.csv')
    # getCsv('data.csv', 'result.csv')

    extop_dpvs()
    insertFailure_dpvs()

if __name__ == '__main__':
    main()
    #test('delay.csv', 'esxtop.csv', 'cpu-4000.csv', 'insertDelay.csv')