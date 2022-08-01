#!/bin/bash
# Script to retrieve compute engine details.
# Author - Rajathithan Rajasekar - 03/03/2020
# Updated - Chad Pritchett - 07/20/2022

echo "PROJECT NAME, INSTANCE NAME , ZONE , MACHINE-TYPE , OPERATING SYSTEM , CPU , MEMORY , DISK SIZE, CREATION TIME, LAST START, LAST STOP, STATUS, STATUS MESSAGE, LABELS " > compute-engine-details.csv
prjs=( $(gcloud projects list | tail -n +2 | awk {'print $1'}) )
for i in "${prjs[@]}"
    do
        echo "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@" >> list.txt
        echo "Setting Project: $i" >> list.txt
        echo $(gcloud config set project $i)
        echo $(gcloud compute instances list | awk '{print $1,$2}' | tail -n +2| while read line; do echo "$i $line"; done |xargs -n3 sh -c 'python3  retrieve-compute-engine-details.py $1 $2 $3 >> compute-engine-details.csv' sh)
    done
