#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
jxpjpath="$DIR/jxpj.py"

# put old cron to file
crontab -l > tmpcron.txt

s=`crontab -l | grep "$jxpjpath"`
# echo "$s"x
if [[ -z "$s" ]]; then
    # 10:00 every day
    echo "00 10 * * * $jxpjpath" >> tmpcron.txt 
fi

#install new cron file
crontab tmpcron.txt
rm -f tmpcron.txt

python "$jxpjpath"
