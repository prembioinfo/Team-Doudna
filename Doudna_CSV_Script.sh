#!/bin/bash

git clone "https://github.com/prembioinfo/Team-Doudna.git"
cd Team-Doudna

cat << "EOF" 

 _____                         ____                     _                _
|_   _|___   __ _  _ __ ___   |  _ \   ___   _   _   __| | _ __    __ _ | |
  | | / _ \ / _` || '_ ` _ \  | | | | / _ \ | | | | / _` || '_ \  / _` || |
  | ||  __/| (_| || | | | | | | |_| || (_) || |_| || (_| || | | || (_| ||_|
  |_| \___| \__,_||_| |_| |_| |____/  \___/  \__,_| \__,_||_| |_| \__,_|(_)

EOF

echo "Hi there this Team Doudna :-)"
echo ""
echo "Generating CSV file"
echo ""

echo "Programmers - The mythical creatures who solve all the problems of lesser mortals without having to move from their desks."
echo ""

# Our CSV header
echo "NAME, EMAIL, SLACK ID, BIOSTACK, TWITTER, HAMMING DISTANCE" > ../Team-Doudna.csv
echo ""

for file in $(ls);
do
	if [[ $file == *.py ]];
	then
		echo -n "Python running"
		python3 $file >> ../Team-Doudna.csv
		echo ""
		echo ""
	elif [[ $file == *.php ]];
	then
		echo -n "PHP running"
		php $file >> ../Team-Doudna.csv
		echo "" >> ../Team-Doudna.csv
		echo ""
		echo ""
	elif [[ $file == *.R ]];
	then
		echo -n "R running"
		Rscript $file >> ../Team-Doudna.csv
		echo "" >> ../Team-Doudna.csv
		echo ""
		echo ""
	elif [[ $file == *.pl ]];
	then
		echo -n "Perl running"
		perl $file >> ../Team-Doudna.csv
		echo ""
		echo ""
	elif [[ $file == *.rb ]];
	then
		echo -n "Ruby running"
		ruby $file >> ../Team-Doudna.csv
		echo ""
		echo ""
	elif [[ $file == *.sh ]];
	then
		echo -n "Bash is running"
		bash $file >> ../Team-Doudna.csv
		echo ""
		echo ""
	elif [[ $file == *.java ]];
        then
		echo -n "Java running"
                javac $file
		fname=`echo $file | cut -d\. -f1`
		java $fname >> ../Team-Doudna.csv
		echo ""
		echo ""
	fi
done

echo "End of execution"
echo ""

cat << "EOF" 
 ______   _______   ______   _______
| __ ) \ / / ____| | __ ) \ / / ____|
|  _ \\ V /|  _|   |  _ \\ V /|  _|
| |_) || | | |___  | |_) || | | |___
|____/ |_| |_____| |____/ |_| |_____|

EOF