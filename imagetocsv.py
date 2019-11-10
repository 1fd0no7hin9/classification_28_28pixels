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
    return data

# define column and create csv file
def insertColumn():
    column = []
    for j in range(width):
        for i in range(height):
            columnname = 'Pixel_R'+str(i)+'C'+str(j)
            column.append(columnname)                    

    column.append('Class')
    with open(FILENAME, 'w') as writefile:
        writer = csv.writer(writefile)
        writer.writerow(column)
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