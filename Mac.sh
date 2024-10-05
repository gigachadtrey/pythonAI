#!/bin/bash

cd "$(dirname "$0")"  # Change to the script's directory
pip install -r requirements.txt &> /dev/null
exec python code.py