import os
import pandas as pd

IN_PATH='E:/evolutinoarypattern/basecount.filt'
OUT_PATH='E:/evolutinoarypattern/basecount.filt.merge'
files = os.listdir(IN_PATH)


timeList= []
for file in files:
    file = IN_PATH + '/' + file
    baseCount = pd.read_csv(file, sep='\t')
    timeList.append(baseCount)


baseCounts = pd.concat(timeList)
bCntSort = baseCounts.sort_values(by = ['CHROM', 'POS','TIME'])

outCSV = OUT_PATH + '/' + 'BYS2_D07.snps.merge.txt'
bCntSort.to_csv(outCSV, sep='\t', index=False, header=True)
