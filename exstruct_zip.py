import zipfile
import os


def zip2pdf(name):
    z = zipfile.ZipFile('instance/uploads/'+name)
    z.extractall('pdf_file')

    files = os.listdir('pdf_file')
    for i in range(len(files)):
        os.rename('pdf_file/'+str(files[i]),'pdf_file/'+str(i)+'.pdf')
