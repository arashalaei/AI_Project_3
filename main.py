import re
import time
import numpy as np
takuzu = []

def read_map_from_file(file_name) :
    with open(file_name) as textFile:
        first_line = textFile.readline()
        rows, columns = first_line.split(" ")
        rows, columns = int(rows), int(columns)
        map = []
        for words in textFile.read().split():
            for word in words:
                map.append(word)
    ta = np.array(map)
    takuzu = ta.reshape(rows, columns)
    return takuzu,rows, columns

takuzu ,rows , columns = read_map_from_file("puzzle2.txt")
print(rows,columns)
print(takuzu)

def row_col_consistency(row, col, num):
    one_r = zero_r = 0
    k = 0
    while k < columns:
        if k != col:
          if takuzu[row][k] == '1':
                 one_r += 1
          elif takuzu[row][k] == '0':
                zero_r += 1
        k = k + 1
    one_c = zero_c = 0
    k = 0
    while k < rows:
        if k != rows:
             if takuzu[k][col] == '1':
                 one_c += 1
             elif takuzu[k][col] == '0':
                  zero_c += 1
        k = k + 1
    if num == 0:
        if zero_r > (columns - 2 )/ 2  :
            return False
        elif zero_c > (columns - 2 )/ 2 :
            return False
    elif num == 1:
        if one_r > (columns - 2 )/ 2  :
            return False
        elif one_c > (columns - 2 )/ 2 :
            return False
    return True

def similarity_consistency_col(c, num):
    col = takuzu[:, c]
    str_col = ''
    k = 0
    while k < columns:
        if k == c:
            str_col = str_col + str(num)
        else:
            str_col += col[k]
        k = k + 1
    k = 0
    while k < columns:
        str1 = creat_string(takuzu[:, k])
        if c != k :
            if "-" not in str1 and '-' not in str_col :
                if str_col == str1:
                   return False
        k = k + 1
    return True

def creat_string(arr):
    str = ''
    for i in range(len(arr)):
       str = str + arr[i]
    return str

def similarity_consistency_row(r, num):
    row = takuzu[r]
    str_row = ''
    k = 0
    while k < rows:
        if k == r:
            str_row = str_row + str(num)
        else:
            str_row = str_row + row[k]
        k = k + 1
    k = 0
    while k < rows:
        if r != k :
            if "-" not in creat_string(takuzu[k]) and '-' not in str_row :
                if str_row == creat_string(takuzu[k]):
                     return False
        k = k + 1
    return True
