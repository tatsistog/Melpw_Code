#!/bin/bash

for k in {4..80}; do
  python matrix.py "$k" &
done
