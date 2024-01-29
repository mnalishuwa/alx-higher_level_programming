#!/bin/bash
# script that takes in a URL and displays HTTP methods the server will accept
curl -sI 0.0.0.0:5000/route_4 | grep 'Allow:' | awk '{print substr($0, index($0,$2))}'
