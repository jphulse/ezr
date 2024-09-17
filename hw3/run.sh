#!/bin/sh
cd /home/workspaces/ezr/hw3
for file in /workspaces/ezr/data/optimize/*/*; do python3 /workspaces/ezr/hw3/hw3.py $file &  done