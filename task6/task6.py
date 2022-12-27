import json

import numpy as np

def comparisons(ranks):
    table = []
    # Наполняем шаблонами
    n = len(ranks)
    m = len(ranks[0])
    for i in range(m):
        template = np.zeros((n, n))
        np.fill_diagonal(template, 0.5)
        table.append(template)

    for iTable in range(len(table)):
        for row in range(len(table[iTable])):
            rowValue = ranks[row][iTable]
            for iCell in range(len(table[iTable][row])):
                currTableValue = ranks[iCell][iTable]
                if currTableValue > rowValue:
                    table[iTable][row][iCell] = 1
                if currTableValue < rowValue:
                    table[iTable][row][iCell] = 0
                if currTableValue == rowValue:
                    table[iTable][row][iCell] = 0.5
    return table

def calc(compare):
    row_c = len(compare[0])
    cells_c = len(compare[0][0])
    exp_c = len(compare)
    res = np.zeros((row_c, cells_c))
    for i in range(0, row_c):
        for j in range(0, cells_c):
            mi = 0
            mp = 0
            mj = 0
            for t in range(0, exp_c):
                value = compare[t][i][j]
                if value == 1:
                    mi += 1
                elif value == 0.5:
                    mp += 1
                else:
                    mj += 1
            resIJ = (1 * (mi / exp_c)) + (0.5 * (mp / exp_c)) + (0 * (mj / exp_c))
            res[i][j] = resIJ
    return res

def GeneralEstimation(xTable, E):
    n = len(xTable[0])
    kPrev = np.ones(n) / n
    kNew = None
    while True:
        y = np.matmul(xTable, kPrev)
        lbd = np.matmul(np.ones(n), y)
        kNew = (1 / lbd) * y
        diff = abs(kNew - kPrev)
        max = diff.max()
        if max <= E:
            break
        else:
            kPrev = kNew
    return np.around(kNew, 3)

def parseJsonString(str):
    return json.loads(str)

def task(jsonString):
    table = np.array(parseJsonString(jsonString)).transpose()

    comparisons = comparisons(table)
    X = calc(comparisons)
    K = GeneralEstimation(X, 0.001)
    res = json.dumps(K.tolist())
    return res
