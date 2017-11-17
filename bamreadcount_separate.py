import os
import pandas as pd

PATH = 'E:/python_workspace/EvolutionaryPatternAnalysis/bamreadcount_proc_output'
OUT = 'E:/python_workspace/EvolutionaryPatternAnalysis/bamreadcount_sep/'
CHROM_LIST= {'LYZE01000001.1':1,'LYZE01000002.1':2,'LYZE01000003.1':3,'LYZE01000004.1':4,'LYZE01000005.1':5,
             'LYZE01000006.1': 6,'LYZE01000007.1':7,'LYZE01000008.1':8,'LYZE01000009.1':9,'LYZE01000010.1':10,
             'LYZE01000011.1': 11,'LYZE01000012.1':12,'LYZE01000013.1':13,'LYZE01000014.1':14,'LYZE01000015.1':15,
             'LYZE01000016.1': 16}

'''
files = os.listdir(PATH)

for file in files:
    fileDir = PATH +'/' + file
    tmp = pd.read_csv(fileDir, sep = '\t')

'''
def sep_brc(fileDir, time):
    file = open(fileDir, 'r')
    file.readline()
    chroms_idx = 0
    sep_out = open(OUT + time + '.' + chroms[chroms_idx] + '.txt', 'w')
    for line in file:
        name = line.split('\t')[0]
        if (chroms[chroms_idx] == name):
            sep_out.write(line + '\n')
        else:
            sep_out.close()
            chroms_idx = chroms_idx + 1
            sep_out = open(OUT + time + '.' + chroms[chroms_idx] + '.txt', 'w')
            sep_out.write(line + '\n')

chroms =list()
for i in CHROM_LIST.keys():
    chroms.append(i)

files = os.listdir(PATH)
for file in files:
    fileDir = PATH +'/' + file
    name = file.split()[0]
    sep_brc(fileDir, name)



