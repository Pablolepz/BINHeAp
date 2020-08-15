# Python Example Appendix
# Optional extras:

# === Config Section [DO NOT CHANGE]===
import csv
# === End Config Section ===


# ///////////////////////////////////
# Example_1: ==Open CSV (READ ONLY // LINE-BY-LINE)==
# Description:  To get information from a CSV 
#               line by line (i.e. read csv line-by-line)   
#               you need to specify the path, and create a file object
#               with the open mode "r" which means "read-only"
#
#               You then pass that file object into the csv module
#               via csv.reader(file_object) .
#
#               Once instantiated, you can iterate line by line via a loop.
#               When we're done, we'll close the loop to make sure other
#               programs/users can access it.

print("==Example_1==")
print("\n*(1a)*\n")
file_path="assets/tempCsv.csv"

#open file
file_object=open(file_path,"r")

#instantiate as reader object
reader = csv.reader(file_object)

#For each line in the csv
for line in reader:
    #Do processing...
    print(line)
    

#close file
file_object.close()

# ///////////////////////////////////