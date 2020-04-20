#!/usr/bin/python3

import os
import datetime

currentDT = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
path = str(currentDT).replace(" ", "").replace("-", "").replace(":", "_")
smokePath = "C:\\Users\\" + path
os.makedirs(smokePath)
