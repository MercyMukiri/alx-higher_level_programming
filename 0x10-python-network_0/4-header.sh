#!/bin/bash
# script that takes in a URL as an argument, sends a GET request with a header variable X-School-User-Id whose value is 98 to the URL, and displays the body of the response
curl -sX GET -H "X-School-User-Id: 98" "$1"
