# Tutorial

## 虚拟机设置
| VM | ens34 | ens35 | OS |
| - | - | - | - |
| client | vnf_test_0/E1000 | // | Ubuntu20.04 |
| dpvs | vnf_test_0/E1000 | vnf_test_1/E1000 | Ubuntu20.04 |
| server | vnf_test_1/E1000 | // | Ubuntu20.04 |

## 部署
### DPVS
#### 依赖安装
```shell
$ apt udpate
$ apt install -y libnuma-dev libpopt-dev build-essential meson ninja-build libssl-dev autoconf automake libtool
```
#### pkg-config更新
```shell
$ wget https://launchpad.net/ubuntu/+archive/primary/+sourcefiles/pkg-config/0.29.2-1ubuntu3/pkg-config_0.29.2.orig.tar.gz
$ tar -xvzf pkg-config_0.29.2.orig.tar.gz
$ cd pkg-config-0.29.2
$ ./configure --with-internal-glib
$ make
$ make install
```
#### igb_uio安装
```shell
$ git clone https://github.com/RealEffect/dpdk-kmods.git
$ cd dpdk-kmods
$ make
$ modprobe uio
$ insmod igb_uio.ko
```
#### dpdk部署
```shell
$ git clone https://github.com/iqiyi/dpvs.git
$ cd dpvs
$ ./scripts/dpdk-build.sh
$ cd dpdk/dpdk-stable-20.11.1
$ insmod dpdkbuild/kernel/linux/kni/rte_kni.ko carrier=on
$ ifconfig ens34 down
$ ifconfig ens35 down
$ ./usertools/dpdk-devbind.py --status
$ ./usertools/dpdk-devbind.py -b igb_uio 0000:02:02.0
$ ./usertools/dpdk-devbind.py -b igb_uio 0000:02:03.0
$ echo 4096 > /sys/devices/system/node/node0/hugepages/hugepages-2048kB/nr_hugepages
$ mkdir /mnt/huge
$ mount -t hugetlbfs nodev /mnt/huge
$ cat /proc/meminfo | grep Huge
```
#### dpvs部署
```shell
$ export PKG_CONFIG_PATH=/root/dpvs/dpdk/dpdklib/lib/x86_64-linux-gnu/pkgconfig
$ cd dpvs
$ make
$ make install
```
### client
#### TRex部署
```shell
$ apt update
$ apt install python3-distutils
$ git clone https://github.com/FortyWinters/dpvs-test.git
$ wget --no-cache --no-check-certificate https://trex-tgn.cisco.com/trex/release/latest
$ tar -xzvf latest
$ cp dpvs-test/src/trex_cfg.yaml
$ cd v3.04
$ ./dpdk_setup_ports.py
$ ./dpdk_setup_ports.py -s  # 查看网卡绑定状态
$ ./dpdk_setup_ports.py -L  # 网卡解绑
```

### server
```shell
$ apt update
$ apt install nginx
```
## 测试
### dpvs启动
```shell
$ git clone https://github.com/FortyWinters/dpvs-test.git
$ cp dpvs-test/src/dpvs.conf /etc/dpvs.conf
$ . dpvs-test/src/route.sh 
$ ./dpvs/bin/dpvs &
$ ./dpvs/bin/dpip route show
```
### client打流
```shell
$ cd v3.04
$ ./t-rex-64 -f cap2/http_simple.yaml -d 10000
```
### ESXi
```shell
$ esxtop -b -d 2 -n 1200 -a > data.csv
```
### dpvs故障注入
```shell
$ . dpvs-test/src/run.sh             # 按序注入
$ . dpvs-test/src/failure_random.sh  # 随机注入
```
## 数据处理
ESXi获得data.csv，dpvs获得cpu.csv、vm.csv、io.csv，按照流量阶梯共十组
```shell
$ python3 dpvs-test/src/combine.py      # 得到阶梯数据
$ python3 dpvs-test/src/data.py         # 阶梯数据合并
$ python3 dpvs-test/src/data_to_1.py    # 数据归一化

```