import csv
filename = '/home/balm/code/4D/datamining/Testingset.csv'
with open (filename) as csv_file:
    tmpdata = csv.reader(csv_file)
    data = []
    for row in tmpdata:
        for datainrow in row:
            data.append(datainrow)
            
print(data[28*28])
for dataset in range(1,451):
    for row in range(28):
        for column in range(1,29):
            print("%3d" % int(data[dataset*28*28+(28*row+column)])),
        print()