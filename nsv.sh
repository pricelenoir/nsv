#!/bin/bash

if [ "$#" -ne 4 ]; then
    echo "Usage: $0 <Firstname> <Lastname> <Start season> <End season>"
    exit 1
fi

firstname="$1"
lastname="$2"
startseason="$3"
endseason="$4"

# Shot tracking began in 1996
if [ "$startseason" -lt "1996" ]; then
    echo "Invalid season. Seasons must be 1996 or later."
    exit 1
fi

# Run input testing script
python input_test.py "$firstname" "$lastname" "$startseason" "$endseason"

input_test_exit_status=$?

if [ "$input_test_exit_status" -eq 1 ]; then
    exit 1
fi

python main.py "$firstname" "$lastname" "$startseason" "$endseason" | bin/main