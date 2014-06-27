#!/bin/sh
#filter /var/log/command.log
#author zlb
#date 2014/06/27
day=$(date +%F)
time="00:00:00"
cmd=""
file="/var/log/command.log"
line=100
user=""
while getopts "d:t:c:f:n:" opt;do
    case $opt in
        d) echo process $opt,print from day
           day=${OPTARG}
           ;;
        t) echo process $opt,print from time
           time=${OPTARG}
           ;;
        c) echo process $opt,print filter command
           cmd=${OPTARG}
           ;;
        u) echo process $opt,print filter user
           user=${OPTARG}
           ;;
        n) echo process $opt,print lines of output
           line=${OPTARG}
           ;;
        f) echo process $opt
           file=${OPTARG}
           ;; 
        *) echo $0 -d "`date +%F`" -t "`date +%H:%M:%S`" -c "rm" -n "10" -f /var/log/command.log
           exit 1;;
   esac
done
shift $(($OPTIND - 1))
cat $file|awk -F " " -v d=${day} -v t=${time} -v c=${cmd} -v u=${user} '{ if ($2 >= d  && $3 >= t && $5 ~ u && $9 ~ c ) print $0 }'|head -n $line
echo $day
