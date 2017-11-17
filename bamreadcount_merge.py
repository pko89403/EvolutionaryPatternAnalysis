import pandas as pd
import os

DIR='E:/python_workspace/EvolutionaryPatternAnalysis/bamreadcount_sep/'

CHROM_LIST= {'LYZE01000001.1':1,'LYZE01000002.1':2,'LYZE01000003.1':3,'LYZE01000004.1':4,'LYZE01000005.1':5,
             'LYZE01000006.1': 6,'LYZE01000007.1':7,'LYZE01000008.1':8,'LYZE01000009.1':9,'LYZE01000010.1':10,
             'LYZE01000011.1': 11,'LYZE01000012.1':12,'LYZE01000013.1':13,'LYZE01000014.1':14,'LYZE01000015.1':15,
             'LYZE01000016.1': 16}

HEADER = ['NAME', 'TIME', 'POS', 'REF', 'DEPTH', 'BASE:COUNT', 'DUMMY']

files = os.listdir(DIR)


def fetch_keys():
    keyList = list()
    for i in CHROM_LIST.keys():
        i = i + '.txt'
        keyList.append(i)
    return keyList

def make_mergeList(chromName):
    target = list()
    for file in files:
        if file.endswith(chromName):
            target.append(file)
    return target

def merging(tList, outName):
    snps = list()
    for target in tList:
        file = DIR + target
        print(file)
        tmp = pd.read_csv(file, sep='\t', header=None)
        snps.append(tmp)
    snps = pd.concat(snps, ignore_index=True)
    outputDir = './' + outName + '.csv'
    snps.to_csv(outputDir, sep=',', index=False, header=True)

chroms = fetch_keys()
for chrom in chroms:
    tList = make_mergeList( chrom)
    merging(tList, chrom)