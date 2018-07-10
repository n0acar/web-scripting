import os
import glob
word="/Users/nev/Desktop/iddaa.docx"
array = glob.glob("/Users/nev/Desktop/IUI Yaz Çalışması/sporx/*.txt")
for item in array:
    file = item
    f=open(file, 'r')
    if not f.readlines()
        os.remove(file)
    f.close()

