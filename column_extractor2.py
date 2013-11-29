# Miles Histand

# This program will pull the nth column from a comma delimited table  (CSV) and
# save to an output file


import sys
import re
import os
import csv

def main():
    arg = 11        # column to extract
    w = open('/Users/histand/Desktop/outfile.txt','w')

    for csvFiles in os.listdir("/Users/histand/Desktop/Test_Data"):
        
        argument = 0                    # set to 0 to remove header during first iteration
        
        if csvFiles.startswith("."):
            continue
        
        reader = csv.reader(open('/Users/histand/Desktop/Test_Data/'+csvFiles,'r'))
        for row in reader:
            if argument > 1:
                column = row[arg]                               # desired column to store   
                column = column.strip()                       # remove any \n or stuff
                print csvFiles + column
                w.write(column)                           # write out to file
                w.write('\n')
            argument = argument + 1    
   

    w.close()                                         # close written file

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
