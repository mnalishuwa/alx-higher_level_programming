#!/bin/bash
# script that takes in a URL and displays HTTP methods the server will accept
curl -sX OPTIONS "$1"
