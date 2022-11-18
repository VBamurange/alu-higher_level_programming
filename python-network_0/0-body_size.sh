#!/bin/bash
#return body size of response message
url -sI "$1" | grep -i Content-Length | cut -d " " -f2
