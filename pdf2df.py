import PyPDF2 
from pdf2image import convert_from_path, convert_from_bytes
import pytesseract
from PIL import Image
import pandas as pd
import os

def pdf_to_df(fp='processed/01_январь.pdf', pn=0):
    images = convert_from_path(fp)
    image = images[pn]
    im = image.crop((0, 70, 400, 2050))
    text = pytesseract.image_to_string(im, lang='rus')
    data = [i.split() for i in text.split('\n')]
    df = pd.DataFrame(data, columns='м Отст Ст Откл Дл Кол'.split())
    return df

if os 

dfs = [pdf_to_df(df) for df in os.listdir('processed')]
