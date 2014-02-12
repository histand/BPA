# Miles Histand

# This program will search for the username of a specific site entered by user


import sys
import re

def main():
    x = open('/Users/histand/Desktop/Data.txt','r')
    y = x.readline()
    # z= list(y)
    print y
    f=y.strip('j')
    print f
    z=list(f)
    z.append('j')
    z = "".join(z)
    print z
    
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
