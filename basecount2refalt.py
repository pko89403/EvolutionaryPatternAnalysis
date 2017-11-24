import os
from enum import Enum


def nucleo2Index(base):
    base = base.strip()
    if( base == 'A'):   return 4
    elif( base == 'C'): return 5
    elif( base == 'G'): return 6
    elif( base == 'T'): return 7
    else:   return 3


CHROM_LIST= {'LYZE01000001.1':'chrI',
             'LYZE01000002.1':'chrII',
             'LYZE01000003.1':'chrIII',
             'LYZE01000004.1':'chrIV',
             'LYZE01000005.1':'chrV',
             'LYZE01000006.1':'chrVI',
             'LYZE01000007.1':'chrVII',
             'LYZE01000008.1':'chrVIII',
             'LYZE01000009.1':'chrIX',
             'LYZE01000010.1':'chrX',
             'LYZE01000011.1':'chrXI',
             'LYZE01000012.1':'chrXII',
             'LYZE01000013.1':'chrXIII',
             'LYZE01000014.1':'chrXIV',
             'LYZE01000015.1':'chrXV',
             'LYZE01000016.1':'chrXVI'}

PATH='E:/evolutinoarypattern/basecount.merge'

nameList = os.listdir(PATH)
for name in nameList:
    fName = PATH + '/' + name
    file = open(fName)
    header = file.readline().strip().split('\t')
    for line in file:
        content = line.strip().split('\t')

        name = CHROM_LIST[ content[0].strip() ]
        time = content[1].strip()
        pos = content[2].strip()
        ref = content[3].strip()
        refIndex = nucleo2Index(ref)
        refCnt = int( content[refIndex] )




