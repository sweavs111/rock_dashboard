#!/bin/bash

#########################################
# startup.sh
# use if connected to the pi via SSH
# this will forward the dashboard window
# to the external monitor
#########################################

set -euo pipefail

# --- Execute ---
DISPLAY=:0 python3 main.py

# --- Exit ---
echo DONE
