#!/bin/bash
#return body size of response message
curl -sI "$1" | grep -i Content-Length | cut -d " " -f2
