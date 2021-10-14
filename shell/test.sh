#!/bin/bash

#set -u

featureIndexFile="/Users/chencan/Personal/Enginneering/shell/usersaa"

if [ -f "${featureIndexFile}" ]
then
    echo "[DEBUG] findex file exists"
else
    echo "[ERROR] findex file does not exist"
fi
