#!/bin/bash
# Script that takes URL and displays all HTTP methods
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-
