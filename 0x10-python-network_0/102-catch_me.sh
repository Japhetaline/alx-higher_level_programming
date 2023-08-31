#!/bin/bash
# Get request to the URL and display the body of the response

response=$(curl -s -X PUT -d "user_id=98" "0.0.0.0:5000/catch_me")

response_body=$(grep -oP '(?<=<body>).*(?=</body>)' <<< "$response")

printf "%s\n" "$response_body"
