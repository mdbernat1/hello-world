#!/usr/bin/python

def encode( input ):
  onestr = ""
  for item in input:
      if item.isalnum() == False:
        print "%s is not a valid input" % item
        exit();
      onestr = onestr + item + "*"
  return onestr[:-1];
  
def decode( onestring ):
  return onestring.split("*");
  
input = ["dwe","qwdw","cwewre"];
print "input: ", input
onestring = encode(input);
print "after encode: ", onestring
output = decode(onestring);
print "output: ", output
print "another change!!!!"
