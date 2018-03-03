#! /usr/bin/python

import os

#! /usr/bin/bsh

f = os.popen("id")
x = f.read()
print x

f = os.popen("cat /proc/cpuinfo | grep fpu")
x = f.read()
x = x.split("\n")
d = len(x)-1
print d
