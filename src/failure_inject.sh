#!/bin/bash
#getTimestamp $pointnumber $lable 
getTimestamp(){
	for i in `seq $1`
    	do
		echo $(date),$2,$(free|awk -F " " 'NR==2'|awk -F " " '{print $2}'),$(free|awk -F " " 'NR==2'|awk -F " " '{print $3}')>>t.csv
        sleep 1
    	done
}

cpu_f(){
	echo "CPU FAILURE START"
    	for rank in 1 2 3 4 5 6
    	do
        	getTimestamp 25 0
        	echo "CPU FAILURE RANK:$rank"
        	stress-ng --cpu $rank &
		getTimestamp 25 1
		pkill -9 stress
		getTimestamp 25 0   
    	done
	sleep 10
	cp t.csv /home/csy/Downloads/cpu.csv
}

vm_f(){
    	echo "VM FAILURE START"
    	getTimestamp 25 0
    	echo "VM FAILURE RANK:500M"
    	stress-ng --vm 1 --vm-bytes 500M &
    	getTimestamp 25 2
    	pkill -9 stress
    	getTimestamp 50 0

    	echo "VM FAILURE RANK:750M"
    	stress-ng --vm 1 --vm-bytes 750M &
    	getTimestamp 25 2
    	pkill -9 stress
    	getTimestamp 50 0

    	echo "VM FAILURE RANK:1G"
    	stress-ng --vm 1 --vm-bytes 1G &
    	getTimestamp 25 2
    	pkill -9 stress
    	getTimestamp 50 0

    	echo "VM FAILURE RANK:2G"
    	stress-ng --vm 2 --vm-bytes 2G &
    	getTimestamp 25 2
    	pkill -9 stress
    	getTimestamp 50 0

    	echo "VM FAILURE RANK:3G"
    	stress-ng --vm 3 --vm-bytes 3G &
    	getTimestamp 25 2
    	pkill -9 stress
    	getTimestamp 50 0

    	echo "VM FAILURE RANK:4G"
    	stress-ng --vm 4 --vm-bytes 4G &
    	getTimestamp 25 2
    	pkill -9 stress
    	getTimestamp 50 0

    	echo "VM FAILURE RANK:5G"
    	stress-ng --vm 5 --vm-bytes 5G &
    	getTimestamp 25 2
    	pkill -9 stress
    	getTimestamp 50 0

    	echo "VM FAILURE RANK:6G"
    	stress-ng --vm 6 --vm-bytes 6G &
    	getTimestamp 25 2
    	pkill -9 stress
    	getTimestamp 25 0    

	sleep 10
        cp t.csv /home/csy/Downloads/vm.csv

}


io_f(){
    	echo "IO FAILURE START"
    	getTimestamp 25 0
    	echo "IO FAILURE RANK:1"
    	stress-ng --iomix 1 --iomix-bytes 10% &
    	getTimestamp 25 3
    	pkill -9 stress 
    	getTimestamp 50 0

    	echo "IO FAILURE RANK:2"
    	stress-ng --iomix 2 --iomix-bytes 20% &
    	getTimestamp 25 3
    	pkill -9 stress 
    	getTimestamp 50 0

    	echo "IO FAILURE RANK:3"
    	stress-ng --iomix 3 --iomix-bytes 30% &
    	getTimestamp 25 3
    	pkill -9 stress 
    	getTimestamp 50 0

    	echo "IO FAILURE RANK:4"
    	stress-ng --iomix 4 --iomix-bytes 40% &
    	getTimestamp 25 3
    	pkill -9 stress 
    	getTimestamp 50 0

    	echo "IO FAILURE RANK:5"
    	stress-ng --iomix 5 --iomix-bytes 50% &
    	getTimestamp 25 3
    	pkill -9 stress 
    	getTimestamp 50 0

    	echo "IO FAILURE RANK:6"
    	stress-ng --iomix 6 --iomix-bytes 60% &
    	getTimestamp 25 3
    	pkill -9 stress 
   	getTimestamp 20 0


	sleep 10
        cp t.csv /home/csy/Downloads/io.csv

}

pl_f(){
	echo "PKT LOST START"
    	for rank in 1 2 3 4 5 6
    	do	
		getTimestamp 25 0
		if [ $rank -eq 1 ];then
			echo "PKT LOST RANK:$rank"
                	# route del 192.168.2.1 gw 192.168.1.233 dev ens160
			#./dpvs/bin/dpip route del 10.0.0.201/32 dev dpdk1
			iptables -A INPUT -i dpdk1.kni -m statistic --mode random --probability 0.1 -j DROP	
			getTimestamp 25 4
			iptables -D INPUT -i dpdk1.kni -m statistic --mode random --probability 0.1 -j DROP			
			#./dpvs/bin/dpip route add 10.0.0.201/32 dev dpdk1
			# route add 192.168.2.1 gw 192.168.1.233 dev ens160
        	elif [ $rank -eq 2 ];then
			echo "PKT LOST RANK:$rank"
                	# route del 192.168.2.1 gw 192.168.1.233 dev ens160
                	# route del 192.168.2.2 gw 192.168.1.233 dev ens160
			#./dpvs/bin/dpip route del 10.0.0.201/32 dev dpdk1
			#./dpvs/bin/dpip route del 10.0.0.202/32 dev dpdk1
			iptables -A INPUT -i dpdk1.kni -m statistic --mode random --probability 0.2 -j DROP
			getTimestamp 25 4
			iptables -D INPUT -i dpdk1.kni -m statistic --mode random --probability 0.2 -j DROP
			# route add 192.168.2.1 gw 192.168.1.233 dev ens160
                        # route add 192.168.2.2 gw 192.168.1.233 dev ens160
			#./dpvs/bin/dpip route add 10.0.0.201/32 dev dpdk1
                        #./dpvs/bin/dpip route add 10.0.0.202/32 dev dpdk1
        	elif [ $rank -eq 3 ];then
			echo "PKT LOST RANK:$rank"
                	# route del 192.168.2.1 gw 192.168.1.233 dev ens160
                	# route del 192.168.2.2 gw 192.168.1.233 dev ens160
                	# route del 192.168.2.3 gw 192.168.1.233 dev ens160
			#./dpvs/bin/dpip route del 10.0.0.201/32 dev dpdk1
                        #./dpvs/bin/dpip route del 10.0.0.202/32 dev dpdk1
			#./dpvs/bin/dpip route del 10.0.0.203/32 dev dpdk1
                        iptables -A INPUT -i dpdk1.kni -m statistic --mode random --probability 0.3 -j DROP

			getTimestamp 25 4
			iptables -D INPUT -i dpdk1.kni -m statistic --mode random --probability 0.3 -j DROP
                        # route add 192.168.2.1 gw 192.168.1.233 dev ens160
                        # route add 192.168.2.2 gw 192.168.1.233 dev ens160
                        # route add 192.168.2.3 gw 192.168.1.233 dev ens160
			#./dpvs/bin/dpip route add 10.0.0.201/32 dev dpdk1
                        #./dpvs/bin/dpip route add 10.0.0.202/32 dev dpdk1
                        #./dpvs/bin/dpip route add 10.0.0.203/32 dev dpdk1


        	elif [ $rank -eq 4 ];then
			echo "PKT LOST RANK:$rank"
                	# route del 192.168.2.1 gw 192.168.1.233 dev ens160
                	# route del 192.168.2.2 gw 192.168.1.233 dev ens160
                	# route del 192.168.2.3 gw 192.168.1.233 dev ens160
                	# route del 192.168.2.4 gw 192.168.1.233 dev ens160
			#./dpvs/bin/dpip route del 10.0.0.201/32 dev dpdk1
                        #./dpvs/bin/dpip route del 10.0.0.202/32 dev dpdk1
                        #./dpvs/bin/dpip route del 10.0.0.203/32 dev dpdk1
			#./dpvs/bin/dpip route del 10.0.0.204/32 dev dpdk1
                        iptables -A INPUT -i dpdk1.kni -m statistic --mode random --probability 0.4 -j DROP
			
			getTimestamp 25 4
			iptables -D INPUT -i dpdk1.kni -m statistic --mode random --probability 0.4 -j DROP
                        # route add 192.168.2.1 gw 192.168.1.233 dev ens160
                        # route add 192.168.2.2 gw 192.168.1.233 dev ens160
                        # route add 192.168.2.3 gw 192.168.1.233 dev ens160
                        # route add 192.168.2.4 gw 192.168.1.233 dev ens160
			#./dpvs/bin/dpip route add 10.0.0.201/32 dev dpdk1
                        #./dpvs/bin/dpip route add 10.0.0.202/32 dev dpdk1
                        #./dpvs/bin/dpip route add 10.0.0.203/32 dev dpdk1
                        #./dpvs/bin/dpip route add 10.0.0.204/32 dev dpdk1


        	elif [ $rank -eq 5 ];then
			echo "PKT LOST RANK:$rank"
                	# route del 192.168.2.1 gw 192.168.1.233 dev ens160
                	# route del 192.168.2.2 gw 192.168.1.233 dev ens160
                	# route del 192.168.2.3 gw 192.168.1.233 dev ens160
                	# route del 192.168.2.4 gw 192.168.1.233 dev ens160
                	# route del 192.168.2.5 gw 192.168.1.233 dev ens160
			#./dpvs/bin/dpip route del 10.0.0.201/32 dev dpdk1
                        #./dpvs/bin/dpip route del 10.0.0.202/32 dev dpdk1
                        #./dpvs/bin/dpip route del 10.0.0.203/32 dev dpdk1
                        #./dpvs/bin/dpip route del 10.0.0.204/32 dev dpdk1
			#./dpvs/bin/dpip route del 10.0.0.205/32 dev dpdk1
			iptables -A INPUT -i dpdk1.kni -m statistic --mode random --probability 0.5 -j DROP
			getTimestamp 25 4
			iptables -D INPUT -i dpdk1.kni -m statistic --mode random --probability 0.5 -j DROP
                        # route add 192.168.2.1 gw 192.168.1.233 dev ens160
                        # route add 192.168.2.2 gw 192.168.1.233 dev ens160
                        # route add 192.168.2.3 gw 192.168.1.233 dev ens160
                        # route add 192.168.2.4 gw 192.168.1.233 dev ens160
                        # route add 192.168.2.5 gw 192.168.1.233 dev ens160
			#./dpvs/bin/dpip route add 10.0.0.201/32 dev dpdk1
                        #./dpvs/bin/dpip route add 10.0.0.202/32 dev dpdk1
                        #./dpvs/bin/dpip route add 10.0.0.203/32 dev dpdk1
                        #./dpvs/bin/dpip route add 10.0.0.204/32 dev dpdk1
                        #./dpvs/bin/dpip route add 10.0.0.205/32 dev dpdk1
        	else
			echo "PKT LOST RANK:$rank"
                	# route del 192.168.2.1 gw 192.168.1.233 dev ens160
                	# route del 192.168.2.2 gw 192.168.1.233 dev ens160
                	# route del 192.168.2.3 gw 192.168.1.233 dev ens160
                	# route del 192.168.2.4 gw 192.168.1.233 dev ens160
                	# route del 192.168.2.5 gw 192.168.1.233 dev ens160
                	# route del 192.168.2.6 gw 192.168.1.233 dev ens160
			#./dpvs/bin/dpip route del 10.0.0.201/32 dev dpdk1
                        #./dpvs/bin/dpip route del 10.0.0.202/32 dev dpdk1
                        #./dpvs/bin/dpip route del 10.0.0.203/32 dev dpdk1
                        #./dpvs/bin/dpip route del 10.0.0.204/32 dev dpdk1
                        #./dpvs/bin/dpip route del 10.0.0.205/32 dev dpdk1
			#./dpvs/bin/dpip route del 10.0.0.206/32 dev dpdk1
			iptables -A INPUT -i dpdk1.kni -m statistic --mode random --probability 0.6 -j DROP
			
			getTimestamp 25 4
			iptables -D INPUT -i dpdk1.kni -m statistic --mode random --probability 0.6 -j DROP
                        # route add 192.168.2.1 gw 192.168.1.233 dev ens160
                        # route add 192.168.2.2 gw 192.168.1.233 dev ens160
                        # route add 192.168.2.3 gw 192.168.1.233 dev ens160
                        # route add 192.168.2.4 gw 192.168.1.233 dev ens160
                        # route add 192.168.2.5 gw 192.168.1.233 dev ens160
                        # route add 192.168.2.6 gw 192.168.1.233 dev ens160
			#./dpvs/bin/dpip route add 10.0.0.201/32 dev dpdk1
                        #./dpvs/bin/dpip route add 10.0.0.202/32 dev dpdk1
                        #./dpvs/bin/dpip route add 10.0.0.203/32 dev dpdk1
                        #./dpvs/bin/dpip route add 10.0.0.204/32 dev dpdk1
                        #./dpvs/bin/dpip route add 10.0.0.205/32 dev dpdk1
                        #./dpvs/bin/dpip route add 10.0.0.206/32 dev dpdk1
        	fi
	getTimestamp 25 0
    	done

	sleep 10
        cp t.csv /home/csy/Downloads/pl.csv
}

random_f(){
	echo "RANDOM FAULT START"
	NUM=$(($RANDOM%4+1))
	RANK=$(($RANDOM%6+1))
	getTimestamp 25 0
	if [ $NUM == 1 ];then
		echo "CPU FAULT START (RANK: $RANK)"

	elif [ $NUM == 2 ];then
		echo "VM FAULT START (RANK: $RANK)"
	else
                echo "IO FAULT START(RANK: $RANK)"
	fi
	getTimestamp 25 0

}

echo timestamp,lable,mem_total,mem_used>t.csv

if [ $1 = "cpu" ];then
        cpu_f
elif [ $1 = "vm" ];then
        vm_f
elif [ $1 = "io" ];then
	io_f
elif [ $1 = "pl" ];then
	pl_f
elif [ $1 = "hl" ];then
	hl_f
elif [ $1 = "random" ];then
	random_f
else
        echo "WRONG"
fi