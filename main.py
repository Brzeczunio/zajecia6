#! /usr/bin/python

import read as r

f = r.openFile("lorem.txt","r")
#r.readFileLineByLine(f)

#a = r.readFile(f)

#words =  a.find("Bash")

#r.searchWorld(f, "bash")

#a = r.countWorld(f, "bash")
#print a

#a = r.lenLine(f, 80)
#print a

#a = r.onlyNumeric(f)
#print a

import files as fi
import sys as s

path = s.argv[1]

#path = raw_input()
#fi.fileExist(path)

fi.fileExist(path)
