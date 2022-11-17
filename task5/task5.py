#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import json
from io import StringIO


# In[2]:


SEQ_LEN = 10


# In[53]:


def crow(visited: set, cur: int) -> np.array:
    row = []
    for i in range(SEQ_LEN):
        row.append(1 if i+1 in visited else 0)
        
    return np.array(row)


# In[54]:


def cmatrix(data: list) -> np.array:
    visited = set()
    matrix = list()

    for elem in data:
        if type(elem) == str:
            visited.add(int(elem))
            row = crow(visited=visited, cur=int(elem))
            matrix.append({'num': int(elem), 'row': row})
        else:
            for subelem in elem:
                visited.add(int(subelem))
            for subelem in elem:
                row = crow(visited=visited, cur=int(subelem))
                matrix.append({'num': int(subelem), 'row': row})

    matrix.sort(key=(lambda x: x['num']))
    raw = [elem['row'] for elem in matrix]

    return np.array(raw)


# In[57]:


def task(json_path: str) -> list:
    data = json.loads(open(json_path).read())

    matrix1 = cmatrix(data['input1'])
    matrix2 = cmatrix(data['input2'])

    matrix12 = matrix1 * matrix2
    matrix12T = matrix1.T * matrix2.T

    criterion = np.logical_or(matrix12, matrix12T)

    answer = []
    for i in range(criterion.shape[0]):
        for j in range(i):
            if not criterion[i][j]:
                answer.append([j+1, i+1])
    
    return print(answer)


# In[58]:


task("example.json")
