#!/bin/sh -

# add VIP to WAN interface
./dpvs/bin/dpip addr add 10.0.0.100/32 dev dpdk1

# route for WAN/LAN access
# add routes for other network or default route if needed.
./dpvs/bin/dpip route add 10.0.0.0/16 dev dpdk1
./dpvs/bin/dpip route add 192.168.100.0/24 dev dpdk0

# add service <VIP:vport> to forwarding, scheduling mode is RR.
# use ipvsadm --help for more info.
./dpvs/bin/ipvsadm -A -t 10.0.0.100:80 -s rr

# add two RS for service, forwarding mode is FNAT (-b)
./dpvs/bin/ipvsadm -a -t 10.0.0.100:80 -r 192.168.100.2:80 -b

# add at least one Local-IP (LIP) for FNAT on LAN interface
./dpvs/bin/ipvsadm --add-laddr -z 192.168.100.200 -t 10.0.0.100:80 -F dpdk0
