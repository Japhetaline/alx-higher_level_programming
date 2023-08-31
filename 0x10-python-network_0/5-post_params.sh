#!/bin/bash
# sends a POST request to the passed URl, and display the body of responce
curl -sd "email=test@gmail.com&subject=I will always be here for PLD" "$1"
