#!/bin/bash
source ./config/config.sh

jupyter lab --ip=0.0.0.0 --no-browser --port=8888 --NotebookApp.token='' --NotebookApp.password='' --allow-root &
P1=$!
code-server --auth none --disable-telemetry --bind-addr 0.0.0.0:8080 --disable-update-check --user-data-dir /app -w "Hello Brad"
P2=$!
wait $P1 $P2