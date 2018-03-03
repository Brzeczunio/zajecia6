#! /usr/bin/python

import os.path as o

def fileExist(path):
	if o.isfile(path):
		print 'plik {0} istnieje'.format(path)
	else:
		print 'plik {0} nie istnieje'.format(path)
