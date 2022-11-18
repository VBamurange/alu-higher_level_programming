#!/bin/bash
#only status code
curl -so /dev/null --write-out "%{http_code}" "$1"
