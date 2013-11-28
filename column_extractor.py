# Miles Histand

# This program will pull the nth column from a comma delimited table  (CSV) and
# save to an output file


import sys
import re
import os

def column_extractor(arg):

    w = open('/Users/histand/Desktop/outfile.txt','w')    # JORDAN: change this path

    for csvFiles in os.listdir("/Users/histand/Desktop/CSV"): # JORDAN: change this path
    
        
        argument = 0                    # set to 0 to remove header during first iteration
        if csvFiles.startswith("."):
            continue
        for y in open('/Users/histand/Desktop/CSV/'+csvFiles,'r'): # JORDAN: change this path
            
            z = re.split(',',y )                          # re function to split line
            column = z[arg]                               # desired column to store   
            column = column.strip()                       # remove any \n or stuff
            if argument > 1:
                print csvFiles + column
                w.write(column)                           # write out to file
                w.write('\n')
            argument = argument + 1    


   

    w.close()                                         # close written file
    
def main():
    arg = input('Please enter column number to extract (column 0 is first column):')
    
    column_extractor(arg)

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
