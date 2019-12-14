# responsible for pdf processing
from PIL import Image, ImageDraw
import numpy as np

number = []
for i in range(10):
    number.append(Image.open("numb/"+str(i)+".png"))


def find_element(left_shift=-11,right_shift=0, pal=None, i=0, w=0, h=0):
    '''returns detected number or None'''
    null_mask = np.zeros((18, 11))
    all_max_index = 0
    all_max_ans = 0
    print(pal[i:i + 18 , w+left_shift:w +right_shift])
    if (pal[i:i + 18 , w+left_shift:w +right_shift]==null_mask).sum() / (18 * 11) >= 0.9:
        return None
    for w_m in range(-6, 0):
        for h_m in range(-4, 2):
            max = 0
            max_ans = 0
            for j in range(10):
                numbers = np.array(number[j].convert('L')) * 1
                numbers = (numbers == 0) * 1
                try:
                    pred = (pal[i + w_m:i + 18 + w_m, w+left_shift + h_m:w + h_m+right_shift] == numbers).sum() / (18 * 11)
                    if (pred >= max):
                        max = pred
                        max_ans = j
                except:
                    continue
            if (max > all_max_ans):
                all_max_ans = max
                all_max_index = max_ans
            print(all_max_index, all_max_ans)
    if(all_max_ans==0):
        return (None)
    else:
        return(all_max_index)


def col2nums(pal, flag_3=False, flag_0=False, flag_2=False):
    '''detect all numbers in column and return them as numpy array'''

    w = pal.shape[1]-1
    h = pal.shape[0]-1

    pal = (pal == 0)*1
    i = 0
    all_count = []
    while i<(h-17):
        counter = 0
        if pal[i][w-6] == 1 and not(np.array_equal(pal[i, w-16:w],[1 for count_one in range(16)])):
            counter+=1
            find_element_numb = find_element(pal=pal, i=i, h=h, w=w)
            prenumber = find_element_numb
            if prenumber is None:
                
                i+=18
                continue
            for key in range(3):
                counter+=1
                find_element_numb = find_element(-10*counter,-10*(counter-1)+1, pal, i=i, h=h, w=w)

                if(find_element_numb!=None):
                    print(prenumber)
                    prenumber += find_element_numb*(10**(counter-1))
                else:
                    break
            temp = str(prenumber)
            if flag_3 == True:
                #  4digit numbers can only have these first numbers
                if len(temp) == 4:
                    temp = '15' + temp[2:]
                if len(temp) == 3:
                    temp = '5' + temp[1:]
                prenumber = int(temp)

            all_count.append(prenumber)
            print(prenumber)
            i+=18
#             a = input()
        else:
            i+=1
    if flag_0:
        print(all_count)
        if all_count[-1] > all_count[-2]:
            all_count[-1]= all_count[-2] // 2

        for i in range(1, len(all_count) - 1):
            if all_count[i] >= all_count[i-1] or all_count[i] <= all_count[i+1]:
                all_count[i] = (all_count[i-1] + all_count[i+1]) // 2 
    if flag_2:
        for i in range(len(all_count)):
            all_count[i] = min(all_count[i], 2)
    print(len(all_count))
    return np.array(all_count)
