#!/bin/bash
export FLASK_APP=./src/main.py
flask run -h 127.0.0.1
read -p "Enter to continue"