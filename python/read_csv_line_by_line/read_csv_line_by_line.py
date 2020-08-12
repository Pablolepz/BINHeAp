# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 16:36:35 2020

@author: Omar
"""


'''
Method 1 

Using the CSV module
'''
import csv


file_path="test.csv"

#open file
fileobj=open(file_path,"r",encoding="utf8")


#instantiate as reader object
reader = csv.reader(fileobj)

#For each line in the csv
for line in reader:
    #Do processing...
    print(line)
    

#close file
fileobj.close()