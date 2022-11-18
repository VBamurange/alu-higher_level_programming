#!/bin/bash
#sends a post request to the passed URL
curl -s -X POST -d "email=test@gmail.com.com&subject=I will always be here for PLD" "$1"
