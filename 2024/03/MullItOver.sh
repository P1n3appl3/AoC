#!/usr/bin/env bash

function solve() {
  # rg 'mul\((\d+),(\d+)\)' -or '$1*$2+' | tr -d '\n' | cat - <(echo 0) | bc
  # rg 'mul\((\d+),(\d+)\)' -or '$1*$2' | paste -s -d+ | bc
  rg 'mul\((\d+),(\d+)\)' -or '$1*$2' | bc | datamash sum 1
}

echo -n "part 1: "
<"$1" solve
echo -n "part 2: "
# remove dont -> do and dont -> EOF
<"$1" tr -d '\n' |
  sd "don't\(\).*?do\(\)" '' |
  sd "don't\(\).*" '' |
  solve
