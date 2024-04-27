#!/bin/bash
# Script that shows the Content-Length from HTTP request
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2
