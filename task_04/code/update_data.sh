#!/bin/bash

len=3
count=0
n_reps=20
IFS=$'\n'

echo -n -e "$count/$len \r"

for dir in experiment_?/; do
  for file in "$dir"*.exe; do
    if [ -f "$file" ]; then
      experiment=$(echo "$file" | awk -F/ '{print $2}' | awk -F_ '{print $2}')
      file_ind=$(echo "$file" | awk -F/ '{print $2}' | awk -F_ '{print $3}')
      out_file=data/data_"$experiment"_"$file_ind".txt

      if [ "$file_ind" == "in" ] || [ "$file_ind" == "ticks" ]; then
        ./"$file" >> "$out_file"

      else
        array=()
        rse=100
        integer_part=100
        reps=0

        while [[ "$integer_part" -ge 1 ]]; do
          reps=$((reps+n_reps))
          for (( i=1; i<="$n_reps"; i+=1 )); do
            array+=( "$(./"$file")" )
          done

          for line in "${array[@]}"; do
              echo "$line" >> temp.txt
          done

          python rse.py temp.txt > rse.txt
          rse=$(cat < "rse.txt")
          integer_part=$(echo "$rse" | bc -l | awk -F. '{print $1}')
          echo > temp.txt
        done

        for line in "${array[@]}"; do
          echo "$line" $rse $reps >> "$out_file"
        done

        rm temp.txt rse.txt
        unset rse
        unset array

      fi
    fi
  done

  count=$((count+1))
  echo -n -e "$count/$len \r"
done

