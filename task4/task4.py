#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from collections import defaultdict
from queue import SimpleQueue
import math


# In[2]:


def r1r2(a: dict, A: np.array) -> dict:
    for row in A:
        a[row[0]][0] += 1
        a[row[1]][1] += 1
        
    return a


# In[3]:


def r1r4(a: dict, A: np.array) -> dict:
    for row in A:
        main = row[0]
        sub = row[1]
        a[main][0] += 1
        a[sub][1] += 1
        for subrow in A:
            if subrow[0] == sub:
                a[main][2] += 1
                a[subrow[1]][3] += 1
                
    return a


# In[4]:


def r5(d: dict, A: np.array) -> dict:
    queue = SimpleQueue()
    queue.put(1)

    r5 = {}

    while not queue.empty():
        main = queue.get()
        a = []
        for row in A:
            if row[0] == main:
                a.append(row[1])
                queue.put(row[1])
        if len(a) > 1:
            for elem in a:
                d[elem][4] += a.__len__() - 1

    return d


# In[5]:


def check_entropy(graph: np.array) -> float:
    def set_def():
        return [0, 0, 0, 0, 0]

    a = defaultdict(set_def)

    r1r4(a, graph)
    r5(a, graph)

    a = pd.DataFrame(a)
    a = a.to_numpy().T
    print("Матрица связности графа A =\n",a)

    n = len(a)
    s = 0.0
    
    for elem in a:
        for cond in elem:
            if cond > 0:
                p = cond / (n - 1)
                logp = math.log10(p)
                s += p * logp

    return -s


# In[6]:


def pipeline(files: list):
    for i, file in enumerate(files):
        A = pd.read_csv(file).to_numpy()
        print("Задание ",i)
        entropy = check_entropy(A)
        print("Энтропия = ",entropy," \n")


# In[7]:


file = ["./graph.csv"]
pipeline(file)






