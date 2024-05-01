#!/bin/bash
# Script that displays body of response after POST request sent
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
