#!/bin/bash
# menu for guidemejacket proofofconcept
reset

PS3='Enter choice: '
options=("Run GuideMe" "Kill GuideMe" "Kill and exit this program")
select opt in "${options[@]}"
do
	case $opt in
		"Run GuideMe")
			echo "Running GuideMe..."
			python execFL.py & python execFR.py & python execR.py &
			;;
		"Kill GuideMe")
			echo "Killing GuideMe..."
			killall python
			python stopPulsing.py
			;;
		"Kill and exit this program")
			echo "quitting..."
			killall python
			python stopPulsing.py
			break
			;;
		*) echo "invalid option $REPLY";;
	esac
done
