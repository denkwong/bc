#!/bin/bash

declare -a tests=(
  "-h"
  "-a strengthen"
  "-b killer"

  "-c 150"
  "-c <150"
  "-c <=75"
  "-c >6000"
  "-c >=6500"

  "-d Baseball"
  "-eResistant"
  "-f true"
  "-l"
  "-n Keiji"
  "-r uber"
  "-t red"
  "-n wall -a.*"
  "-n keiji -a.* -b.* -c>10 -d.* -e.* -f.* -r.* -t.*"
  "-n anubis -bcurse"
  "-n balrog -awave"
)

errors=0
for val in "${tests[@]}"; do
  echo "./bc" $val
  ./bc $val
  if [ "$?" -ne 0 ]
  then
    let "errors++"
  fi
done

echo "Error count = " $errors
if [ "$errors" -gt 0 ]
then
  exit 1
fi
