#!/bin/bash

if [ -z "$1" ]; then
  echo INFO
  echo You can pass parametrs:
  echo \"o\" - object files \"*.o\"
  echo \"exe\" - executable files \"*.exe\"
  echo \"data\" - text files in \"./data\" directory
  echo \"preproc\" - text files in \"./preproc_data\" directory
  echo \"all\" - all files above
fi

if [ "$1" == "data" ]; then
  find ./data -type f -name "*.txt" -exec rm -f {} +
fi

if [ "$1" == "preproc" ]; then
  find ./preproc_data -type f -name "*.txt" -exec rm -f {} +
fi

if [ "$1" == "o" ]; then
  find . -type f -name "*.o" -exec rm -f {} +
fi

if [ "$1" == "exe" ]; then
  find . -type f -name "*.exe" -exec rm -f {} +
fi

if [ "$1" == "all" ]; then
  find ./data -type f -name "*.txt" -exec rm -f {} +
  find ./preproc_data -type f -name "*.txt" -exec rm -f {} +
  find . -type f -name "*.o" -exec rm -f {} +
  find . -type f -name "*.exe" -exec rm -f {} +
fi
