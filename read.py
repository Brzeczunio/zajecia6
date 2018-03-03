#! /usr/bin/python

import re

def openFile(path, mode):
	file_object = open(path, mode)
	#print("Otworzylem plik")
	return file_object

def readFile(file_object):
	return file_object.read()

def readFileLineByLine(file_object):
	for line in file_object:
		print line

def searchWorld(file_object, world):
	for line in file_object:
		a = line.find(world)
		if a >= 0:
			print line

def countWorld(file_object, world):
	count = 0
	for line in file_object:
		a = line.find(world)
		if a >= 0:
			count += 1
	return count

def lenLine(file_object, count):
	c = 0
	for line in file_object:
		a = len(line)
		if a == count:
			c += 1
	return c

def onlyNumeric(file_object):
	c = 0
	for line in file_object:
		a = re.search('[0-9]+', line)
		if a:
			#print a.group()
			c += 1
	return c
