# Ex 17 : copy data in one file and into another
#
# 
# 
# 

from sys import argv

# *exists* function returns "true" if file exists
# or "false" if the file does not exist
from os.path import exists

# name of this file that contains the code, the file name you are pulling data from
# and the name of the file that you will put the data into from the file you pulled it from
script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
# opens file and stores it into in_file
in_file = open(from_file)

# reads file stored in in_file variable and
# then stores it to indata variable
indata = in_file.read()

# prints out the length of the data saved in the indata variable
print(f"The input file is {len(indata)} bytes long")

# checks to see if file exists
print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

# opens/creates? a file to write the data to and stores it in out_file
out_file = open(to_file, 'w')

# takes the data from the file/data stored in the indata variable
# and stores/writes it to the out_file variable that will create the to_file file
out_file.write(indata)

print("Alright, all done.")

# closes both files
#out_file.close()
#in_file.close()

