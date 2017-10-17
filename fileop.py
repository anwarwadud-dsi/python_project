#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Program Name :  fileop.py
# Author       :  Wadud
# Date         :  October 2017
# Description  :  This program is used to separate category wise client list from large amout of input data file. and save each category
#                 based on user input name. 
#
# Pre-Req      :  Before using the run function, make sure that input file are kept into proper directory and python 3.6 sdk are installed into 
# (IMPORTANT)               computer
#
#                 
# 
# Functions    :  Functions in this set:
#                 exit()            # buid in function, used to terminate program
#                 open()            # build in function, used to open a file 
#                 len()             # build in function, used to calculate string length
#                 split()           # build in function, used to parse a string with space
#                 write()           # build in function, used to write data into file
#                 close()           # build in function, used to close a file
#                
#               
#
# 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import os
inp_file = os.path.exists("in.txt")
if inp_file is False:
    print("File does not exits")
    exit(" ")

file1 = input("Enter File name for REQ client:         ")
file2 = input("Enter File name for NEW client:         ")
file3 = input("Enter File name for PAY client:         ")
with open("in.txt") as f:
    with open(file1+".txt", "w") as f1:
        with open(file2+".txt", "w") as f2:
            with open(file3+".txt", "w") as f3:
                flag = 0
                for line in f:
                    lineLength = len(line.split())
                    if (lineLength == 1 and "REQ" in line):
                        flag = 1
                    elif (lineLength == 1 and "NEW" in line):
                        flag = 2
                    elif (lineLength == 1 and "PAY" in line):
                        flag = 3
                    if(flag == 0):
                        f1.write(line)
                        f2.write(line)
                        f3.write(line)
                    elif(flag == 1):
                        f1.write(line) 
                    elif(flag == 2):
                        f2.write(line) 
                    elif(flag == 3):
                        f3.write(line)    




f3.close()
f2.close()
f1.close()
f.close()