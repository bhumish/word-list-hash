#!/usr/bin/env python

import sys
from hashlib import *

def hashf():
 """The hashf() function creates a new file with the md5 hash of the words (seperated by \n) contained in a given file."""
 while(1):
  path  = raw_input("Enter the path of your file:		(Press 'q' to exit) \n")
  if path == 'q':
   sys.exit(1)
  newpath = raw_input("Enter the to-be created file's name: \n>>")
  f = open(path,'r')
  newf = open(newpath,'w')
  for i in f:
   j = i[:-1]
   newf.write(j + ' : ' +md5(j).hexdigest() + '\n')
  f.close()
  newf.close
  print "Success! Operation Completed."
  print "Press any number to input more files, or any character to exit: "
  s = raw_input()
  if s.isdigit() == False:
   sys.exit(1)

def hashl():
 """The hashl() function creates a new file with the md5 hash of words provided by the user."""
 path = raw_input("Enter the file to-be created for storing the hash: \n>>")
 f = open(path,'w')
 print "Enter words or lines below seperated by the 'Enter' key, and their hash will be written in your file."
 while(1):
  s = raw_input()
  if s == 'exit':
   print "Goodbye!"
   sys.exit(1)
  f.write(s + ' : ' +md5(s).hexdigest() + '\n')   
 f.close()

def main():
 """This is the main function to let the user choose among file input and word input. It then calls the required functions accordingly."""
 i = input("1. If you want to create hash of individual passwords from a file. \n2. If you want to type individual words and have a file containing their hashes. \n  Any other key to exit(). \n>>")
 if i == 1:
  hashf()
 elif i == 2:
  hashl()
 else:
  sys.exit(1)

if __name__ == '__main__':
 main()
