#!/usr/bin/python3

#####
#	by Cho Woon Hyun
#	android custom log viewer
#####

import subprocess
import sys
import time

def parseArgs():
    global serial, processName, filterList, capture

    args = sys.argv
    index = 1

    while index < len(args):
        if '--' == args[index][:2]:
            option = args[index][2:]
            if option == 'serial':
                index += 1
                serial = args[index]
            elif option == 'package':
                index += 1
                processName = args[index]
            elif option == 'filter':
                index += 1
                filterList = args[index].split('\|')
            elif option == 'capture':
                index += 1
                capture = args[index].split('\|')
        index += 1

def getPID(cmd):
	tmp = []
	while len(tmp) == 0:
		proc = subprocess.Popen(list(cmd.split()), stdout=subprocess.PIPE)
		tmp = str(proc.stdout.readline().decode('utf-8')).split()

	return tmp[1]

def basicFilter(word, cut):
	if len(cut) == 0:
		return True
	for f in cut:
		if f in word:
			return True
	return False

def customFilter(pre, log, word):
	start = []
	index = 0
	while index < len(log):
		if log[index:index + len(word)] == word:
			log = log[:index] + "\33[1;43m" + log[index:index + len(word)] + "\33[0m" + pre + log[index + len(word):]
			index += (len("\33[1;43m") + len(word) + len(pre) + len("\33[0m"))
			continue
		index += 1
	
	return log

processName = "akeyboard"
fatal = False
capture = []
serial = ""
filterList = []

if len(sys.argv) >= 2:
    parseArgs()

print(serial)
cmd = "adb" + ((" -s " + serial) if serial != "" else "") + " shell ps | grep " + processName
logCommand = "adb" + ((" -s " + serial) if serial != "" else "") + " logcat"

pid = getPID(cmd)
print(pid)
print(logCommand)

proc = subprocess.Popen(list((logCommand + " -c").split()), stdout=subprocess.PIPE)
proc = subprocess.Popen(list(logCommand.split()), stdout=subprocess.PIPE)
try:
	while True:
		# if fatal is True:
		# 	pid=getPID(cmd)
		log = str(proc.stdout.readline().decode('utf-8'))[:-1]
		splitLog = log.split()
		if len(splitLog) >= 6 and (splitLog[2] == pid or (splitLog[4] == 'F' and splitLog[5] == 'DEBUG')):
			if (splitLog[4] == 'F' and splitLog[5] == 'DEBUG') or (splitLog[4] == 'E' and splitLog[5] == 'AndroidRuntime:'):
				log = "\33[38;5;196m" + log + "\33[0m"
			else:
				if len(filterList) == 0 and len(capture) != 0 and basicFilter(log, capture) is False:
					continue
				elif len(filterList) != 0 and basicFilter(splitLog[5], filterList) is False:
					continue

				if splitLog[4] == 'I':
					for i in capture:
						log = customFilter("\33[38;5;40m", log, i)
					log = "\33[38;5;40m" + log + "\33[0m"
				elif splitLog[4] == 'V':
					for i in capture:
						log = customFilter("\33[38;5;13m", log, i)
					log = "\33[38;5;13m" + log + "\33[0m"
				elif splitLog[4] == 'D':
					for i in capture:
						log = customFilter("\33[38;5;75m", log, i)
					log = "\33[38;5;75m" + log + "\33[0m"
				elif splitLog[4] == 'E':
					for i in capture:
						log = customFilter("\33[38;5;196m", log, i)
					log = "\33[38;5;196m" + log + "\33[0m"
			print(log)
except KeyboardInterrupt:
	proc.kill()
