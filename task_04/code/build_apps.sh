#!/bin/bash

start_value=500
#end_value=1500
end_value=20000
step=500

len=$((((end_value-start_value)/step + 1) * 3 * 3))

count=1
count_experiment=1
for dir in experiment_?/; do
  for file in "$dir"*.c; do
    if [ -f "$file" ]; then
      ind=$(echo "$file" | awk -F/ '{print $2}' | awk -F_ '{print $2}' | awk -F. '{print $1}')
      for (( i=start_value; i<=end_value; i+=step )); do
        gcc-13 -c "$file" \
          -Werror -Wall -std=gnu99 -Wpedantic -O0 -Wextra -Wfloat-conversion -Wfloat-equal \
          -DN="$i" \
          -o app_"${count_experiment}"_"${ind}"_"${i}".o -lm

        gcc-13 -c metrics.c -Werror -Wall -std=gnu99 -Wpedantic -O0 -Wextra -Wfloat-conversion -Wfloat-equal -DN="$i"

        gcc-13 -O0 metrics.o app_"${count_experiment}"_"${ind}"_"${i}".o \
          -o "$dir"app_"${count_experiment}"_"${ind}"_"${i}".exe -lm

        rm app_"${count_experiment}"_"${ind}"_"${i}".o

        echo -n -e "$count/$len \r"
        count=$((count+1))
      done
    fi

  done
  count_experiment=$((count_experiment+1))

done

find . -type f -name "*.o" -exec rm -f {} +