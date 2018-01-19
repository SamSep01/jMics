#!/bin/bash

#
# Fix this fucking error when using ssh or scp
# Unable to negotiate with 1.2.3.4 port 22: no matching cipher found. Their offer: aes128-cbc,3des-cbc,blowfish-cbc,cast128-cbc,arcfour,aes192-cbc,aes256-cbc
#

hist=/Users/j3ssie/.zsh_history
cmd=$( tail $hist | grep @ | tail -n 10 | grep -v 'tail' | tail -n 1 )

# host=$(echo $cmd | awk {print $2})

command=$( echo $cmd | cut -d ';' -f 2)
echo "[+] Fix this shit --> " $command
first=$( echo $command | cut -d ' ' -f 1)

rest=$( echo $command | awk '{$1 = ""; print $0;}' )

# echo $first
# echo $rest

if [[ "$first" == "scp" ]]; then
	scp -c aes128-cbc $rest
else
	ssh -c aes128-cbc $rest
fi

