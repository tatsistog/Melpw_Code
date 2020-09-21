#!/bin/bash

k=(4 5 6)

for i in "${k[@]}"; do
  python matrix.py "$i" &
done
