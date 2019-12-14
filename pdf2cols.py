from pdf2image import convert_from_path, convert_from_bytes
from PIL import Image, ImageDraw
import numpy as np
from numdetect import col2nums

def to_bin(col_2):
    col_2 = np.array(col_2.convert('L'))*1
    for i in range(col_2.shape[0]):
        for j in range(col_2.shape[1]):
            if col_2[i][j] >= 127:
                col_2[i][j] = 255
            else:
                col_2[i][j] = 0
    return col_2

def pdf2npcols(fp='data/03_март.pdf', page_num=0):
    '''cut pdf file into equal converted images(numpy arrays)'''
    images = convert_from_path(fp, fmt='png')
    img = images[page_num]

    width, height = img.size 
    left = 50
    top = 90
    right = 425
    bottom = height - 280

    all_cols = img.crop((left, top, right, bottom))
    width, height = all_cols.size
    top = 0

    size = (54, height)

    col_borders_1 = (0, top, 52, height)
    col_1 = all_cols.crop(col_borders_1)

    layer = Image.new('RGB', size, (255,255,255))
    layer.paste(col_1, (54 - 52, 0))
    col_1 = layer
    col_1 = to_bin(col_1)

    col_borders_2 = (56, top, 110, height)
    col_2 = all_cols.crop(col_borders_2)
    col_2 = to_bin(col_2)

    col_borders_3 = (112, top, 136, height)
    col_3 = all_cols.crop(col_borders_3)
    size = (54, height)
    layer = Image.new('RGB', size, (255,255,255))
    layer.paste(col_3, (54 - 136 + 120, 0))
    col_3 = to_bin(layer)

    col_borders_4 = (126, top, 180, height)  # for everything like that
    col_4 = to_bin(all_cols.crop(col_borders_4))
    
    col_borders_5 = (179, top, 170 + 54, height)
    col_5 = all_cols.crop(col_borders_5)
    layer = Image.new('RGB', size, (255,255,255))
    layer.paste(col_5, (55 - (170 + 54 - 179), 0))
    col_5 = to_bin(layer)

    col_borders_6 = (246, top, 265, height)
    col_6 = all_cols.crop(col_borders_6)
    layer = Image.new('RGB', size, (255,255,255))
    layer.paste(col_6, (34, 0))
    col_6 = to_bin(layer)

    cols = [col_1, col_2, col_3, col_4, col_5]
    return cols
