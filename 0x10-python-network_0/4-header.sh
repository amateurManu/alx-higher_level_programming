#!/bin/bash
# Script that takes URL as argument, displays body of response
curl -s "$1" -H "X-School-User-Id: 98"
