#!/bin/bash

export DISPLAY=:0.0
nohup python3 /home/farmbot/mowbot_project/mowbot_setup/py_scripts/MowBotManage.py > /dev/null 2>&1 &
exit 0
