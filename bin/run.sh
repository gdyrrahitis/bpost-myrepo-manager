#!/bin/sh

ssh git@git_server -p 22
if [ $? == 0 ] || [ $? == 128 ] || [ $? == 1 ] 
then
    echo "can ssh successfully. Code $?"
    # Run app command
    now="$(date +'%d/%m/%Y-%T')"
    myrepo-manager --file "file.txt" --user "$1" --content "[$now]-exec" --diff-only
    exit 0
else
    echo "cannot connect - failing. Error code $?"
    exit 1
fi
