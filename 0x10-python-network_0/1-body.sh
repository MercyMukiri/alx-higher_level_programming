#!/bin/bash
# script that takes in a URL, sends a GET request to the URL, and displays the body of the response if status code is 200
curl -sL "$1" -X GET
