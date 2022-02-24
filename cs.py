import csv
with open('D:\priya\iris.data','rb') as csvfile:
 lines=csv.reader(csvfile)
 for row in lines:
   print (','.join(row))