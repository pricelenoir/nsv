#!/bin/bash

PACKAGE_NAME="nba_api"

# Check if nba_api is installed
if ! pip3 show "$PACKAGE_NAME" >/dev/null 2>&1; then
    echo "Package $PACKAGE_NAME is not installed."
    exit 1
fi

if [ "$#" -ne 4 ]; then
    echo "Usage: $0 <Firstname> <Lastname> <Start season> <End season>"
    exit 1
fi

firstname="$1"
lastname="$2"
startseason="$3"
endseason="$4"

# Check if start season is less than end season
if [ "$startseason" -ge "$endseason" ]; then
    echo "Start season must be less than end season."
    exit 1
fi

# Shot tracking began in 1996
if [ "$startseason" -lt "1996" ]; then
    echo "Invalid season. Seasons must be 1996 or later."
    exit 1
fi

output_directory="shotcharts"
output_filename="${output_directory}/${firstname}_${lastname}_${startseason}-${endseason}.jpg"

# Check if the output directory exists
if [ ! -d "$output_directory" ]; then
    mkdir -p "$output_directory"
fi

# Check if the output file exists
if [ -e "$output_filename" ]; then
    echo "File already exists: $output_directory/$output_filename"
    exit 1
fi

python3 main.py "$firstname" "$lastname" "$startseason" "$endseason" | jgraph | convert -density 300 -quality 100 - "$output_filename"
