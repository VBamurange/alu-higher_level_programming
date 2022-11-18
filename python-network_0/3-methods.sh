#!bin/bash
#display all HTTP methods acccepted by server
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
