from PIL import Image
import os
import csv
width = 28
height = 28



def imgtograyscale(filename, Class):
    # filename = PATH+filename
    im = Image.open(filename).convert('LA')
    pixels = list(im.getdata())
    data = []
    for index in pixels:
        data.append(index[0])
    data.append(Class)
    for row in range(height):
        for column in range(width):
            print("%3d" % data[(width*row)+column]),
        print()
    print()
    return data

# define column and create csv file
def insertColumn():
    columnname = []
    for row in range(height):
        for column in range(width):
            tmpOfColumnName = 'Pixel_R'+str(row)+'C'+str(column)
            columnname.append(tmpOfColumnName)                    

    columnname.append('Class')
    with open(FILENAME, 'w') as writefile:
        writer = csv.writer(writefile)
        writer.writerow(columnname)
    writefile.close()

# insert data
def insertData(filename, Path, Class):
    inputfile = os.listdir(Path)
    for ele in inputfile:
        if ele.endswith(imgtype):
            imgFilename = Path + ele
            data = imgtograyscale(imgFilename, Class)
            
            with open(filename, 'a') as writefile:
                writer = csv.writer(writefile)
                writer.writerow(data)
            writefile.close()

imgtype = '.jpg'
FILENAME = 'dataset.csv'
PATH = '/home/balm/code/4D/datamining/data/'
Class = ""
insertColumn()
for i in range(10):
    filePath = PATH+str(i)+'/'
    Class = str(i)
    print(filePath, Class)
    insertData(FILENAME, filePath, Class)
