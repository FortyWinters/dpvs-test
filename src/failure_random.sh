#!/bin/bash
#getTimestam $pointnumber $lable 
getTimestamp(){
	for i in `seq $1`
    	do
		echo $(date),$2,$(free|awk -F " " 'NR==2'|awk -F " " '{print $2}'),$(free|awk -F " " 'NR==2'|awk -F " " '{print $3}')>>t.csv
        sleep 1
    	done
}

random_f(){
	for NUM in 1 2 3
	do
		RANK=$(($RANDOM%6+1))
		echo $NUM,$RANK>>f.csv 
		getTimestamp 25 0
		if [ $NUM == 1 ];then
			echo "CPU FAULT START (RANK: $RANK)"
			cpu_f $RANK
		elif [ $NUM == 2 ];then
			echo "VM FAULT START (RANK: $RANK)"
			vm_f $RANK
		else
	                echo "IO FAULT START (RANK: $RANK)"
			io_f $RANK
		fi
		getTimestamp 25 0
	done
}

cpu_f(){
	if [ $1 == 1 ];then
		stress-ng --cpu 1 &
		getTimestamp 25 1
		pkill -9 stress
	elif [ $1 == 2 ];then
		stress-ng --cpu 2 &
		getTimestamp 25 1
		pkill -9 stress
	elif [ $1 == 3 ];then
		stress-ng --cpu 3 &
		getTimestamp 25 1
		pkill -9 stress
	elif [ $1 == 4 ];then
		stress-ng --cpu 4 &
		getTimestamp 25 1
		pkill -9 stress
	elif [ $1 == 5 ];then
		stress-ng --cpu 5 &
		getTimestamp 25 1
		pkill -9 stress
	else
		stress-ng --cpu 6 &
		getTimestamp 25 1
		pkill -9 stress
	fi
}

vm_f(){
	if [ $1 == 1 ];then
        stress-ng --vm 1 --vm-bytes 1G &
        getTimestamp 25 2
        pkill -9 stress
	elif [ $1 == 2 ];then
        stress-ng --vm 2 --vm-bytes 2G &
        getTimestamp 25 2
        pkill -9 stress
	elif [ $1 == 3 ];then
        stress-ng --vm 3 --vm-bytes 3G &
        getTimestamp 25 2
        pkill -9 stress
	elif [ $1 == 4 ];then
        stress-ng --vm 4 --vm-bytes 4G &
        getTimestamp 25 2
        pkill -9 stress
	elif [ $1 == 5 ];then
        stress-ng --vm 5 --vm-bytes 5G &
        getTimestamp 25 2
        pkill -9 stress
	else
        stress-ng --vm 6 --vm-bytes 6G &
        getTimestamp 25 2
        pkill -9 stress
	fi
}

io_f(){
        if [ $1 == 1 ];then
            stress-ng --iomix 1 --iomix-bytes 10% &
            getTimestamp 25 3
            pkill -9 stress
        elif [ $1 == 2 ];then
            stress-ng --iomix 2 --iomix-bytes 20% &
            getTimestamp 25 3
            pkill -9 stress
        elif [ $1 == 3 ];then
            stress-ng --iomix 3 --iomix-bytes 30% &
            getTimestamp 25 3
            pkill -9 stress
        elif [ $1 == 4 ];then
            stress-ng --iomix 4 --iomix-bytes 40% &
            getTimestamp 25 3
            pkill -9 stress
        elif [ $1 == 5 ];then
            stress-ng --iomix 5 --iomix-bytes 50% &
            getTimestamp 25 3
            pkill -9 stress
        else
            stress-ng --iomix 6 --iomix-bytes 60% &
            getTimestamp 25 3
            pkill -9 stress
        fi
}

main(){
	echo lable,rank>f.csv
	echo timestamp,lable,mem_total,mem_used>t.csv
	for i in `seq 6`
	do
		echo "FAILURE NUMBER: $i"
		random_f
	done
	cp t.csv /home/csy/Downloads/random.csv
	cp f.csv /home/csy/Downloads/fault.csv
	echo "FINISHED!!!"
}

main