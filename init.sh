#!/bin/sh

parent_directory="."

# Check if the parent directory exists
if [ ! -d "$parent_directory" ]; then
  echo "Error: $parent_directory does not exist."
  exit 1
fi

# Find the last directory with the pattern 'day<number>'
last_directory=$(find "$parent_directory" -type d -name 'day*' | sort -n | tail -n 1)

# Extract the last number from the directory name
last_number=$(echo "$last_directory" | grep -oE '[0-9]+$')

# Increment the last number
i=$((last_number + 1))

name="day$i"

mkdir "$name"
cd "$name"
touch "${name}_1.py" "${name}_2.py" "${name}_test.txt" "${name}.txt"