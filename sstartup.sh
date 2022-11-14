#!/bin/bash
source ./config/config.sh

jupyter lab --ip=0.0.0.0 --no-browser --port=8888 --NotebookApp.token='' --NotebookApp.password='' --allow-root

code-server