#!/usr/bin/python3
# -*-coding:utf-8 -*
import sys 
  
for line in sys.stdin:
    line = line.lower()
    line = line.strip() 
    words = line.split() 
    for word in words:
        print('%s\t%s' % (word, 1))
