import csv
with open ("employeedetails.csv",'r')as file1:
    reader=csv.reader(file1)
    for row in reader:
        print(row)
