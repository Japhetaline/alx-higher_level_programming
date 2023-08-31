#!/bin/bash
#Get the request to the URL and display the body of the response
curl -sX GET -H "X-School-User-Id:98" "$1"
