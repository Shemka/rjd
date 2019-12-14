# responsible for pdf processing
from PIL import Image, ImageDraw
import numpy as np

letter = [];
letter=[
    Image.open(r"/letter/P.png"),
    Image.open(r"/letter/PRL.png"),
    Image.open(r"/letter/PRP.png"),
    Image.open(r"/letter/R.png"),
    Image.open(r"/letter/U.png"),
    Image.open(r"/letter/USH.png")
]
dictionary = {
    0:'П',
    1:'Пр.л',
    2:'Пр.п',
    3:'Р',
    4:'У',
    5:'Уш'
}

def find_element(left_shift=-11,right_shift=0, pal=None, i=0, w=0, h=0):
    '''returns detected number or None'''
    all_max_index = 0
    all_max_ans = 0
    #print(pal[i:i + 18 , w+left_shift:w +right_shift])
    for w_m in range(-6, 0):
        max = 0
        max_ans = 0
        for j in range(6):
            letters = np.array(letter[j].convert('L')) * 1
            letters = (letters == 0) * 1
            pred = (pal[i + w_m:i + 18 + w_m, 0:w+1] == letters).sum() / (18 * w)
                if (pred >= max):
                    max = pred
                    max_ans = j
        if (max > all_max_ans):
            all_max_ans = max
            all_max_index = max_ans
            #print(all_max_index, all_max_ans)

    if(all_max_ans==0):
        return (None)
    else:
        return(all_max_index)


def col2lets(pal):
    '''detect all numbers in column and return them as numpy array'''

    w = pal.shape[1]-1
    h = pal.shape[0]-1

    pal = (pal == 0)*1
    i = 0
    all_count = []
    while i<(h-17):
        if pal[i][8] == 1 and not(np.array_equal(pal[i],[i for count_one in range(54)])):
            find_element_letter = find_element(pal=pal, i=i, h=h, w=w)
            all_count.append(dictionary[find_element_letter])
            i+=18
#             a = input()
        else:
            i+=1
    print(all_count)
    return np.array(all_count)
