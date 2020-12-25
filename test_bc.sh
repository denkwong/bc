#!/usr/local/bin/bash

declare -A tests=(
  ["-g"]="0 cats found"
  ["-h"]="Battle Cats, search for cats by attributes."
  ["-a strengthen"]="a\[Strengthen\]"
  ["-b killer"]="b\[Zombie Killer\]"
  ["-c 150"]="c\[150\]"
  ["--cost <150"]="c\[148\]"
  ["-c <=75"]="c\[75\]"
  ["-c >6000"]="c\[6150\]"
  ["-c >=7500"]="c\[7500\]"
  ["-d Baseball"]="Hijiri Rokudo CC"
  ["-eResistant"]="e\[Resistant\]"
  ["-f true"]="f\[True\]"
  ["-l"]="Cat (n);.11"
  ["-n Keiji"]="Immortal Keiji (Maeda Keiji, Wargod Keiji)"
  ["-r uber"]="Uber"
  ["-s"]="  Area Attack: "
  ["-t red"]="t\[Red\]"
  ["--target traitless"]="Gothic Mitama"
  ["-n wall -a.*"]="Wall Cat.*a\[Area Attack\]"
  ["-n keiji -a.* -b.* -c>10 -d.* -e.* -f.* -r.* -t.*"]="Immortal Keiji (Maeda Keiji, Wargod Keiji), Uber, .*, c\[3585\], f\[True\], a\[Strengthen, Immune to Waves, Area Attack\], t\[Black\], e\[Resistant\], b\[Strengthen, Immune to Waves, Area Attack, Resistant\], d\[As the cherries blossom, so does Keiji's battle fury. Resistant to Black, immune to Wave attacks. Area attacks grow stronger as he takes damage.\]"
  ["-n anubis -bcurse"]="0 cats found"
  ["-n balrog -awave"]="Balrog Cat (Lesser Demon Cat, Greater Demon Cat), Uber, .*, a\[Resist Wave\]"
)

declare -a failed_tests=()
errors=0
SECONDS=0
for key in "${!tests[@]}"; do
  echo "./bc" $key | grep "${tests[$key]}"
  ./bc $key | grep "${tests[$key]}"
  if [ "$?" -ne 0 ]
  then
    let "errors++"
    failed_tests=("${failed_tests[@]}" "$key")
  fi
done
duration=$SECONDS

echo ""
echo "System tests"
echo "Ran" ${#tests[@]} "tests in" $(($duration / 60)) "minutes and" $(($duration % 60)) "seconds with" $errors "failure(s)"
if [ "$errors" -gt 0 ]
then
  for failure in "${failed_tests[@]}"; do
    echo "  ./bc "$failure
    echo "    expected: "${tests[$failure]}
  done
fi

echo ""
echo "Unit tests"
python -m unittest
