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

def check_coordinate(i):
    if 0 <= i < columns:
        return True
    return False

def repeat_consistency_col(i ,j, num):
    if check_coordinate(j-2) and takuzu[i][j - 1] == str(num) and takuzu[i][j - 2] == str(num):
        return False
    elif check_coordinate(j+2) and takuzu[i][j + 1] == str(num) and takuzu[i][j + 2] == str(num):
        return False
    elif check_coordinate(j-1) and check_coordinate(j+1) and takuzu[i][j - 1] == str(num) and takuzu[i][j + 1] == str(num):
        return False
    else:
        return True

def repeat_consistency_row(i ,j,num):
    if check_coordinate(i-2) and takuzu[i - 1][j] == str(num) and takuzu[i - 2][j] == str(num):
        return False
    elif check_coordinate(i+2) and takuzu[i + 1][j] == str(num) and takuzu[i + 2][j] == str(num):
        return False
    elif check_coordinate(i+1) and check_coordinate(i-1) and takuzu[i + 1][j] == str(num) and takuzu[i - 1][j] == str(num):
        return False
    else:
        return True
def assignment(i , j):
    num_of_domain = 0
    domain = []
    for k in range(2):
        if not row_col_consistency(i,j,k) or not similarity_consistency_row(i,k) or not similarity_consistency_col(j,k) or not repeat_consistency_row(i,j,k) or not repeat_consistency_col(i,j,k):
            continue
        else:
            domain.append(k)
            num_of_domain += 1
    return num_of_domain, domain
def create_queue():
    queue = []
    for i in range(rows):
        for j in range(columns):
           p = [i , j]
           queue.append(p)
    return queue
def ac3(p1,p2):
    change = False
    map = np.copy(takuzu)
    number_of_domain_1, domain_1 = assignment(p1[0],p1[1])
    number_of_domain_2, domain_2 = assignment(p2[0],p2[1])
    if number_of_domain_2 != 1:
        return change
    elif number_of_domain_2 == 1:
        map[p2[0]][p2[1]] = str(domain_2[0])
        number_of_domain_1_1, domain_1_1 = assignment(p1[0],p1[1])
        change = not np.array_equal(domain_1,domain_1_1)
        return change        
def mac():
 queue1 = create_queue()
 queue2 = create_queue()
 queue = domain_queue()
 for q in queue1:
     if len(queue2) == 0 :
         break
     if ac3(q,queue2.pop()):
         queue2.append(q)
     return queue
