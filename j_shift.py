# Miles Histand

# This program will pull the nth column from a comma delimited table  (CSV) and
# save to an output file


import sys
import re
import os
import csv

def main():
    count=0
    arg = 1        # column to extract
    w = open('/Users/histand/Desktop/outfile.csv','w')

    for csvFiles in os.listdir("/Users/histand/Desktop/Data"):
        
     
        
        if csvFiles.startswith("."):
            continue
        
        reader = csv.reader(open('/Users/histand/Desktop/Data/'+csvFiles,'r'))
        for row in reader:
            
                count=count+1
                column = row[arg]                               # desired column to store   
                #column = column.strip()                       # remove any \n or stuff
                                                    #print csvFiles + column
                                                    #f = column.strip('j')
                f = column.translate(None,'j')
                print f
                z = list(f)
                z.append('j')
                z = "".join(z)
                w.write(z)                           # write out to file
                w.write('\n')
                
    print count

    w.close()                                         # close written file

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()