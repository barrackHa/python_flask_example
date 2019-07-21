#/bin/bash

jq=$(which jq)
curl=$(which curl)


#make sure we get back the json {'hello':'world'}

json=$($curl -s http://0.0.0.0:3000/ | jq -r '.hello')

if [ "$json" != "world" ]; then
	echo "failed"
	exit 1
else
	echo "passed"
fi    
