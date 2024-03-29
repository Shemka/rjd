import numpy as np
from numpy import array
from tensor2dfs import tensor2dfs
from analysis import *

a = [[array([991, 816, 804, 769, 709, 680, 640, 457, 444, 431, 354, 251, 250,
       225, 137, 111, 110, 102,  44,  19,  18,   9]), array(['Уш', 'Р', 'П', 'Р', 'П', 'П', 'У', 'П', 'Уш', 'Р', 'Уш', 'Уш',
       'Пр.п', 'П', 'П', 'Уш', 'Р', 'У', 'У', 'Уш', 'Уш', 'П', 'Уш'],
      dtype='<U4'), array([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]), array([1529,   55,   13,   29,   14,   15, 1525, 1534, 1500,   14,   15,
         10, 1529,   27,   12,   12, 1537, 1537,   13, 1536]), array([ 5, 25, 13, 24, 12,  5, 15,  6, 15,  2,  5,  4,  5,  6,  1, 23,  9,
        3,  5,  8, 15,  2])], [array([969, 917, 884, 864, 846, 836, 820, 802, 799, 779, 769, 767, 726,
       721, 709, 702, 692, 681, 663, 642, 622, 528, 466, 444, 434, 429,
       357, 186, 157, 129, 110,  84,  47,  11,   5]), array(['Уш', 'Уш', 'Уш', 'Уш', 'Уш', 'Уш', 'П', 'Уш', 'Р', 'Уш', 'Уш',
       'Р', 'Уш', 'Уш', 'Уш', 'Уш', 'Уш', 'Уш', 'Уш', 'Р', 'П', 'Уш',
       'Пр.п', 'Уш', 'Уш', 'Уш', 'П', 'П', 'Уш', 'Уш', 'Уш', 'Уш', 'Р',
       'Уш', 'Р', 'Уш', 'Р'], dtype='<U4'), array([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]), array([1529, 1520, 1522, 1534, 1522, 1532,   19, 1537,   29, 1531, 1529,
         26, 1525, 1534, 1529, 1533, 1529, 1529, 1532, 1533,   14, 1534,
       1535, 1534, 1529, 1529, 1529, 1529,   16, 1539,   26, 1540,   24]), array([ 7, 17, 11, 25,  5, 11,  4, 12, 31, 12,  2, 25, 11, 13,  1, 14,  4,
        2,  4, 15, 19,  5, 14,  4,  3, 15,  2,  7,  4,  2, 20, 14, 24, 10,
       49])], [array([980, 977, 975, 955, 941, 931, 926, 918, 873, 848, 838, 825, 812,
       807, 802, 778, 769, 714, 682, 668, 655, 640, 650, 615, 580, 555,
       509, 505, 503, 460, 458, 456, 436, 434, 430, 420, 412, 405, 492,
       523, 371, 295, 300, 302, 403, 341, 280, 260, 255, 250, 230, 226,
       215, 204, 191, 179, 154, 145, 285, 197, 110, 107, 104,  82,  79,
        54,  42,  40,  29,  19,  15,   4]), array(['Пр.л', 'Пр.п', 'Уш', 'Пр.п', 'Уш', 'Пр.л', 'П', 'Уш', 'Уш', 'Уш',
       'Уш', 'П', 'П', 'Уш', 'Р', 'Уш', 'Р', 'Уш', 'Уш', 'Пр.п', 'Уш',
       'Р', 'Уш', 'Пр.п', 'Пр.п', 'Пр.п', 'Уш', 'Пр.п', 'Уш', 'Пр.п',
       'Пр.п', 'Уш', 'Уш', 'Р', 'Пр.п', 'Пр.п', 'Пр.п', 'Пр.л', 'Пр.л',
       'Пр.п', 'Пр.п', 'Пр.п', 'Пр.п', 'Пр.п', 'Пр.л', 'Уш', 'Пр.п',
       'Пр.п', 'Пр.п', 'Уш', 'Пр.п', 'П', 'Пр.п', 'Пр.п', 'Пр.п', 'Уш',
       'Пр.п', 'Пр.п', 'Уш', 'Р', 'У', 'Пр.л', 'Пр.п', 'Пр.п', 'Пр.п',
       'Пр.п', 'Уш', 'Р', 'Пр.п', 'П', 'Уш', 'Пр.п'], dtype='<U4'), array([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
       2, 2, 2, 2]), array([  13,   14, 1502,   13, 1529,   13,   15, 1530, 1539, 1502, 1532,
         14,   14, 1537,   32, 1505,   28, 1526, 1522,   15, 1532, 1533,
         44,   15,   15, 1535,   20, 1534,   14,   14, 1559, 1536,   17,
         14,   14,   16,   13,   14,   14,   44,   14,   14,   13, 1529,
         13,   15,   15, 1529,   15,   16,   17,   44,   14, 1529,   13,
         15, 1529,   27,   12,   14,   13,   15,   15,   15, 1528,   26,
         17,   17, 1539,   44]), array([ 3,  3,  5,  3,  4,  3,  9, 16, 39,  4, 11,  5,  4, 17, 27, 21, 25,
       54,  7,  5,  4, 15, 20,  2,  2,  5,  3,  5,  1,  2,  2, 20, 14, 15,
        5,  2,  2,  5,  3,  5,  5,  2,  2,  5,  3,  2,  5,  2,  2,  1,  3,
        6,  5,  2,  2,  2,  3,  5,  2, 22,  2,  5,  3,  5,  5,  2, 12, 25,
        3, 15, 14,  2])], [array([991, 906, 895, 816, 770, 708, 682, 640, 587, 458, 444, 431, 420,
       407, 364, 446, 684, 494, 304, 265, 246, 232, 226, 205, 186, 141,
       130, 118, 116, 114,  54,  62,  34,   7]), array(['Уш', 'Пр.л', 'П', 'Р', 'Р', 'П', 'П', 'У', 'П', 'Уш', 'Уш', 'П',
       'П', 'П', 'Пр.л', 'Уш', 'Уш', 'Уш', 'Уш', 'Уш', 'Уш', 'Уш', 'Уш',
       'Уш', 'П', 'Уш', 'Уш', 'Уш', 'Уш', 'Уш', 'Р', 'У', 'Уш', 'Уш',
       'Уш', 'Уш'], dtype='<U4'), array([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2]), array([1534,   14,   15,   24,   26,   13,   14, 1538, 1529,   16,   19,
       1534, 1529, 1570, 1529, 1531, 1504, 1552, 1529, 1530,   10, 1520,
       1530, 1531, 1529, 1530,   26,   12, 1536, 1537, 1538, 1536]), array([ 6,  5, 19, 25, 24, 15,  7, 15, 18, 54, 15, 15,  9,  5,  4,  9,  5,
        9,  7, 19,  1, 11,  7,  6, 19, 10,  2, 11, 24,  2,  3,  6, 16,  1])], [array([991, 987, 978, 972, 928, 915, 896, 859, 822, 817, 852, 824, 796,
       775, 767, 733, 699, 680, 653, 626, 621, 605, 596, 569, 597, 555,
       514, 505, 485, 466, 447, 437, 432, 428, 423, 494, 425, 356, 455,
       403, 462, 381, 301, 289, 283, 277, 264, 248, 247, 237, 224, 214,
       198, 192, 328, 253, 179, 150, 122, 118, 101,  96,  72,  44,  39,
        26,  24,  13]), array(['Р', 'Уш', 'Пр.п', 'Уш', 'Пр.л', 'Уш', 'Уш', 'Уш', 'Уш', 'Уш', 'П',
       'Уш', 'Р', 'Уш', 'Р', 'Уш', 'Уш', 'Уш', 'Уш', 'Р', 'П', 'П',
       'Пр.л', 'Р', 'Р', 'Р', 'Пр.п', 'Р', 'Пр.п', 'Уш', 'Уш', 'Уш', 'Р',
       'П', 'Пр.л', 'Уш', 'Уш', 'Р', 'Р', 'Уш', 'Пр.л', 'Пр.п', 'Уш',
       'Уш', 'Уш', 'Пр.п', 'Пр.л', 'Р', 'Пр.п', 'Уш', 'Р', 'П', 'Р', 'Уш',
       'Уш', 'Уш', 'Уш', 'Уш', 'Уш', 'Р', 'Уш', 'Пр.п', 'Р', 'Р', 'Уш',
       'Уш', 'Пр.п', 'Р', 'Уш'], dtype='<U4'), array([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
       2]), array([  28, 1536,   14, 1533,   14, 1550, 1529, 1536, 1580, 1529,   10,
       1540,   22, 1535,   26, 1559, 1537, 1505, 1532, 1534,   15,   29,
         27,   28,   44,   31,   14, 1538, 1536, 1540,   20,   20, 1536,
       1534,   16,   16, 1522,   14,   13, 1500, 1532, 1529,   14,   18,
         16,   15, 1534,   29,   14,   18, 1530, 1529, 1529, 1529, 1529,
       1550,   29, 1529,   15,   34,   26, 1536, 1536,   15,   32, 1526]), array([21, 14,  2,  4,  3, 25,  2, 57,  4,  2,  6, 19, 35, 25, 24, 41, 24,
        9,  6, 15, 21,  5, 40, 55, 37,  2, 24,  5,  9, 19, 21,  4, 15,  5,
        4,  2, 18,  4, 16,  5,  3,  6,  7,  2,  2,  5, 20,  5, 55, 22,  7,
       17,  3,  1,  1,  6,  1,  5, 33,  2,  5, 34, 40,  2,  4,  5, 25,  6])], [array([994, 924, 890, 871, 856, 842, 826, 816, 808, 805, 786, 772, 734,
       714, 686, 658, 640, 629, 585, 514, 508, 483, 461, 433, 432, 431,
       476, 379, 282, 254, 241, 229, 218, 207, 182,  81,  56,  31,  27,
        24,  14]), array(['Уш', 'П', 'Уш', 'Уш', 'Уш', 'Уш', 'П', 'П', 'Уш', 'Р', 'Уш', 'Р',
       'Уш', 'Уш', 'Уш', 'Уш', 'П', 'П', 'Уш', 'Пр.п', 'Р', 'Пр.п',
       'Пр.п', 'Уш', 'Пр.п', 'Пр.п', 'П', 'П', 'Пр.п', 'Пр.п', 'Пр.л',
       'Пр.п', 'Пр.п', 'П', 'Пр.п', 'Пр.л', 'Пр.п', 'Пр.п', 'Пр.п',
       'Пр.п', 'Уш', 'П', 'Уш'], dtype='<U4'), array([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]), array([1534,   14, 1531, 1535, 1529, 1529,   42,   13, 1529,   28, 1520,
         31, 1534, 1534, 1529, 1500, 1531,   14,   17,   18,   13, 1535,
         15,   15,   14,   15,   15,   15,   42,   15,   15,   14,   15,
         14,   15,   15, 1536,   15, 1536]), array([ 5, 19, 11, 24,  2,  6,  5,  4,  8, 26, 11, 24, 29, 12,  3,  5, 15,
       16,  5, 42,  3,  3,  6,  3,  5, 15,  2,  5,  5,  4,  2,  6,  5,  5,
        2,  2,  5,  3,  5, 16,  5])], [array([978, 971, 961, 888, 886, 796, 790, 782, 748, 714, 688, 662, 625,
       562, 525, 490, 484, 445, 427, 416, 414, 412, 408, 479, 412, 346,
       335, 304, 285, 246, 223, 208, 177, 174, 169, 126, 121, 105, 102,
        96,  94,  53,  36,  27,   4]), array(['П', 'Уш', 'П', 'П', 'Пр.п', 'Р', 'Пр.п', 'П', 'П', 'Пр.п', 'П',
       'П', 'Р', 'Пр.п', 'Уш', 'Уш', 'Уш', 'Уш', 'Уш', 'П', 'П', 'Пр.л',
       'Пр.п', 'Пр.п', 'Уш', 'Уш', 'Уш', 'Уш', 'Уш', 'Уш', 'Уш', 'Уш',
       'П', 'Уш', 'Уш', 'Уш', 'Уш', 'Уш', 'Пр.п', 'Пр.п', 'Уш', 'Уш', 'Р',
       'Уш', 'Уш', 'Уш', 'Уш'], dtype='<U4'), array([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
       2]), array([  15, 1536,   14,   18,   15,   32,   44,   14,   17,   16,   13,
         17,   13, 1550, 1535, 1537, 1538, 1529,   15,   13,   41,    7,
       1534, 1520, 1529, 1529, 1532, 1522, 1531, 1531,   14, 1529, 1529,
       1529, 1530, 1529,   41,    1, 1529, 1529,   29, 1536, 1537, 1538,
       1526]), array([  14,    9,   10,    7,    3,   25,    5,   14,    8,    5,   16,
          6,   15,    3,    5,    4,   11,   22,   22,   15,   15,    3,
       7794,    7,    2,    4,    1,    9,   14,   19,   17,    7,    2,
          1,    6,    4,    3, 7444,    2,    5,    2,   23,    3,    5,
          8,    6])], [array([992, 986, 980, 962, 944, 905, 904, 890, 869, 854, 853, 804, 800,
       768, 748, 729, 679, 629, 628, 541, 507, 497, 479, 476, 474, 429,
       391, 369, 347, 320, 302, 262, 239, 224, 198, 320, 228, 136, 126,
       117, 111,  52,  42,  25,  20,  10]), array(['Р', 'Уш', 'Пр.п', 'Уш', 'Уш', 'Пр.л', 'У', 'П', 'Р', 'Пр.п', 'Р',
       'Пр.п', 'Р', 'Р', 'П', 'Пр.п', 'П', 'У', 'П', 'П', 'Уш', 'Уш',
       'Уш', 'Пр.п', 'Уш', 'Уш', 'П', 'П', 'Уш', 'Уш', 'Уш', 'Уш', 'Уш',
       'Уш', 'Уш', 'П', 'Уш', 'Уш', 'Уш', 'Уш', 'Р', 'Уш', 'Уш', 'Уш',
       'Уш', 'Р', 'Уш', 'Уш'], dtype='<U4'), array([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]), array([  24, 1536,   13, 1531, 1529,   15,   12,   13,   31,   14,   28,
         15,   50,   28,   15,   14,   14,   13, 1531, 1534, 1535,   14,
       1589, 1538, 1534, 1520, 1529, 1532, 1532, 1522, 1531,   15, 1529,
       1580, 1520, 1529,   18, 1530, 1529, 1537, 1537,   26, 1537, 1536]), array([17,  9,  5,  1,  2,  5,  2, 14, 24,  5, 26,  2, 26, 26,  9,  3,  7,
       15,  9, 12,  5,  9,  9, 21, 21, 15,  1,  9,  3,  9, 15, 20, 18,  6,
        2, 17,  5,  5, 19,  6,  9,  2,  4, 25,  6,  2])], [array([988, 972, 938, 922, 916, 904, 887, 871, 846, 836, 830, 814, 850,
       824, 799, 777, 767, 739, 724, 701, 692, 681, 654, 653, 637, 622,
       602, 528, 504, 445, 429, 428, 491, 384, 278, 250, 203, 187, 134,
       127, 111, 102,  37,  26,  13,   6]), array(['Уш', 'Уш', 'Уш', 'П', 'Уш', 'Пр.п', 'П', 'Уш', 'Уш', 'Уш', 'П',
       'П', 'П', 'Уш', 'Р', 'Уш', 'Р', 'Уш', 'Уш', 'Уш', 'Уш', 'Уш',
       'Пр.п', 'Уш', 'Р', 'Уш', 'Пр.п', 'Пр.п', 'Пр.п', 'Уш', 'Р', 'Пр.л',
       'Пр.л', 'Пр.п', 'Пр.п', 'Пр.п', 'Пр.п', 'Уш', 'Уш', 'Р', 'Р',
       'Пр.л', 'Уш', 'П', 'Уш', 'П'], dtype='<U4'), array([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]), array([1536, 1522, 1529,   13, 1530,   10,   13, 1535, 1532, 1532,   13,
         10,   13, 1526,   32, 1522,   26, 1535, 1534, 1533, 1529, 1529,
         13, 1531, 1533,   14,   15,   15, 1534,   15,   13,   14,   15,
         14,   13, 1529, 1530,   16,   27,   14, 1536,   15, 1538,   44]), array([13,  4,  5, 12, 20,  5, 17, 40,  6, 11,  4,  4,  3, 15, 32, 49, 25,
       12, 15, 12,  2,  2,  3,  4, 15, 20,  2,  5,  5,  9, 15,  3,  3,  5,
        5,  4,  3,  5,  4, 20, 22,  3,  3,  5,  9, 49])], [array([774, 117, 548, 741, 833, 832, 831, 866, 833, 801, 768, 609, 579,
       554, 506, 504, 502, 494, 479, 470, 446, 437, 433, 429, 416, 404,
       466, 346, 325, 415, 347, 279, 278, 253, 226, 225, 205, 203, 195,
       335, 256, 177, 155, 135, 125, 103,  90,  78,  48,  28,  27,  17,
        13]), array(['У', 'Уш', 'Пр.п', 'Пр.п', 'П', 'Уш', 'П', 'П', 'П', 'Р', 'Р', 'Р',
       'Пр.п', 'Пр.п', 'Уш', 'Пр.п', 'Уш', 'П', 'Пр.п', 'Уш', 'Уш', 'Р',
       'Пр.л', 'Пр.п', 'Пр.п', 'Пр.п', 'Пр.п', 'Пр.п', 'Пр.п', 'Пр.п',
       'Пр.л', 'Пр.п', 'Пр.п', 'Пр.п', 'Пр.п', 'П', 'Пр.п', 'Пр.л', 'Уш',
       'Уш', 'Пр.п', 'Уш', 'Пр.л', 'Уш', 'Р', 'Пр.п', 'Пр.п', 'Пр.п',
       'Уш', 'У', 'Пр.п', 'П', 'Уш'], dtype='<U4'), array([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
       2, 2, 2, 2, 2, 2]), array([  47, 1535,   14,   14,   10, 1529,   14,   44,   42,   28,   31,
         14,   12, 1535,   20, 1534,   12,   15, 1534, 1576,   15,   14,
         14,   15,   15,   13,   14,   14,   15,   13,   15,   16,   15,
         16,   17,   13, 1529, 1529,   14, 1529,   15, 1529,   27,   13,
         44,   15, 1558,   11,   16,   14, 1526]), array([ 7,  8,  2,  5, 12,  5,  5,  5,  2, 26, 25, 15,  5,  9,  9,  2,  2,
       19,  5,  9, 35, 15,  3,  5,  5,  9,  5,  5,  2,  2,  5,  3,  5,  5,
        2,  6,  5,  3,  1,  5,  2,  2,  5,  3, 27,  5,  2,  2, 15,  2,  5,
       16, 14])], [array([994, 988, 982, 942, 927, 924, 887, 868, 849, 841, 834, 814, 805,
       803, 781, 770, 722, 707, 662, 656, 644, 624, 602, 581, 510, 506,
       504, 496, 481, 464, 458, 452, 443, 434, 431, 705, 530, 355, 330,
       305, 280, 255, 229, 226, 215, 204, 194, 186, 179, 161, 143, 136,
       127, 104,  79,  54,  41,  28,  18,  14]), array(['П', 'П', 'Пр.л', 'Пр.п', 'Уш', 'П', 'Уш', 'Уш', 'Уш', 'Уш', 'Уш',
       'П', 'П', 'Уш', 'Р', 'Уш', 'Р', 'Уш', 'Уш', 'Уш', 'Уш', 'П', 'П',
       'Уш', 'Пр.п', 'Пр.п', 'Уш', 'Пр.п', 'Уш', 'П', 'Пр.п', 'Уш', 'Уш',
       'Уш', 'П', 'П', 'Пр.л', 'Пр.п', 'Пр.л', 'Пр.п', 'Пр.п', 'Пр.п',
       'Пр.п', 'Пр.п', 'Пр.п', 'Пр.п', 'П', 'Пр.п', 'Пр.п', 'Уш', 'Уш',
       'Пр.п', 'Пр.л', 'Уш', 'Уш', 'Р', 'Пр.п', 'Пр.п', 'Пр.п', 'Пр.п',
       'П', 'Уш', 'Уш'], dtype='<U4'), array([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]), array([1526,   14,   14, 1529,   14, 1500, 1555, 1537, 1534, 1520,   14,
         15, 1534,   83, 1530,   31, 1535, 1532, 1520, 1531, 1529,   15,
         19, 1535,   19, 1535,   14,   14, 1538, 1534, 1535,   16,   14,
         14,   14,   12,   14,   13,   14,   15,   14,   15,   16,   15,
       1529, 1529,   14,   15, 1529, 1500,   32,   14,   15,   15,   17,
         15, 1537, 1537]), array([ 8,  5,  3,  3,  9, 18, 12, 25,  3,  8,  5,  5, 10, 26,  6, 25, 28,
       10,  5,  4, 15, 19,  8,  2,  2,  5,  2, 18,  5,  8,  2,  5, 15,  5,
        5,  2,  9,  9,  3,  3,  5,  2,  2,  6,  3,  5,  2,  6,  2,  5,  1,
        5, 22,  2,  2,  5,  3,  5,  4,  6])]]
    
dfss = tensor2dfs(a)
dfs = [df.transpose() for df in dfss]

dfs = [df2batch2df(process_df(df)) for df in dfs]
print(problems_to_excel(dfs))