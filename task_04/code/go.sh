#!/bin/bash

cyan="\033[36m"
reset_color="\033[0m"

./clean.sh all

echo -e "$cyan"BUILD_APPS.SH"$reset_color"
./build_apps.sh

echo -e "$cyan"UPDATE_DATA.SH"$reset_color"
./update_data.sh

echo -e "$cyan"MAKE_PREPROC.PY"$reset_color"
python make_preproc.py

echo Draw graph? [yes/no]
read ans
if [ $ans == "yes" ]; then
  echo Enter flag to draw graphs:
  echo 1 - ordinary graph of function
  echo 2 - graph of function with max values and min values
  echo 3 - graph of function with boxplots

  echo IND:
  read graph_ind
  echo -e "$cyan"MAKE_POSTPROC.PY"$reset_color"
  python make_postproc.py $graph_ind
fi
