#!/usr/bin/python
# -*- coding: utf-8 -*-
from os import listdir
from os.path import isfile, isdir, join
import os

mypath = "/home/wang/2018-13379test/fish/dat"
files = listdir(mypath)

a = []

for f in files:

  fullpath = join(mypath, f)

  if isfile(fullpath):
    print("1", f)
    a.append(f)
print(a)
for i in range(len(a)):
	os.system('strings /home/wang/2018-13379test/fish/dat/%s.dat > /home/wang/2018-13379test/fish/dat/%s.txt'%(a[i],a[i]))
