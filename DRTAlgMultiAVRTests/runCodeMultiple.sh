#!/bin/bash

for i in {1..10}
	do
		for j in {6..15}
		do 
			echo "Started run" $i" of" $j
			python3 DRTAlgo_MultiAVR.py $j
			echo "Finished run" $i" of" $j
		done
	done
