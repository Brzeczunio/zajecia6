#! /usr/bin/python

import os

#! /usr/bin/bsh

f = os.popen("id")
x = f.read()
print x
