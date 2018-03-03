#! /usr/bin/sh

ip address | grep -w 'dynamic' | awk '{print $2}' | cut -d / -f 1
