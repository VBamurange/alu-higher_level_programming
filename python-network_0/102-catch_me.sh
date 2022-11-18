#!/bin/bash
#make a request that causes the server to respond
curl -sL 0.0.0.0:5000/catch_me -X PUT -H "Origin: You got me!" -d "user_id=98"
