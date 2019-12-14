from pdf2image import convert_from_path, convert_from_bytes
import numpy as np
import matplotlib.pyplot as plt

def pdf_to_cols(pdffile='/home/daniil/programming/rjd/data/01_январь.pdf'):

    images = convert_from_path(pdffile, fmt='png')

    img = images[0]

    width, height = img.size 
    left = 50
    top = 90
    right = 425
    bottom = height - 280

    all_cols = img.crop((left, top, right, bottom))

    all_cols.save('cols/all_cols.png')

    width, height = all_cols.size
    top = 0
    col_borders_1 = (10, top, 60, height)

    col_1 = all_cols.crop(col_borders_1)

    width, height = all_cols.size
    top = 0
    col_borders_2 = (60, top, 117, height)

    col_2 = all_cols.crop(col_borders_2)

    width, height = all_cols.size
    top = 0
    col_borders_3 = (112, top, 130, height)

    col_3 = all_cols.crop(col_borders_3)

    width, height = all_cols.size
    top = 0
    col_borders_4 = (126, top, 180, height)

    col_4 = all_cols.crop(col_borders_4)

    width, height = all_cols.size
    top = 0
    col_borders_5 = (179, top, 250, height)

    col_5 = all_cols.crop(col_borders_5)

    width, height = all_cols.size
    top = 0
    col_borders_6 = (250, top, 300, height)

    col_6 = all_cols.crop(col_borders_6)
    cols = [col_1, col_2, col_3, col_4, col_5, col_6]

    for i in range(len(cols)):
        cols[i].save(f'cols/col{i}.png')
    return cols
    
pdf_to_cols()