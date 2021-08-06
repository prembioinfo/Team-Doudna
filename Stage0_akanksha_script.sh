#!/bin/bash
name="Akanksha Kulkarni"
email="gmsbin15.akanksha.kulkarni@gnkhalsa.edu.in"
slackid="@Akanksha"
biostack="Drug Development"
twitter="@Avynksha"
main() {
	

        
        
        distance=0

    
        for (( i=0; i<${#slackid}; i++ )); do
            if [ ${slackid:$i:1} != ${twitter:$i:1} ]; then
                let "distance++"
            fi
        done

        


}

main "$@"

echo "$name , $email , $slackid , $biostack , $twitter , $distance"