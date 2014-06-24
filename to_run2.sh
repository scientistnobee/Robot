#!/bin/bash
sudo service motion start
sleep 30
while [ 1 ]
do

  RESULT=$(python find_img.py)
  echo "$RESULT"
 #backup as png file, later delete all jpg files
  cp $RESULT $RESULT.png
  sudo ./deepbelief $RESULT > try4.txt
  RESULT2=$(python find_max.py)
  echo "$RESULT2"
sleep 60
done
wait
#trap sudo rm *jpg EXIT

