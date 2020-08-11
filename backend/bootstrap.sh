#!/bin/bash
export FLASK_APP=./src/app.py
flask run -h 127.0.0.1
read -p "Press Enter to end..."
