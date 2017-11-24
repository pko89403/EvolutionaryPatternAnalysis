import sys
import os
import pandas as pd

baseCount_head = ['CHROM', 'TIME', 'POS', 'REF', 'A', 'C', 'G', 'T']

inputPath=sys.argv[1]
listFile=sys.argv[2]

chroms = []
chromList = open(listFile)
for chrom in chromList:
    chroms.append(chrom)

IN_PATH=inputPath
files = os.listdir(IN_PATH)

for chrom in chroms:
    print( '-',chrom,' merging...' )

    timeList= []
    for file in files:
        file = IN_PATH + '/' + file
        baseCount = pd.read_csv(file, sep='\t', header=None, names=baseCount_head )
        baseCount = baseCount[baseCount.CHROM == chrom]
        print(baseCount)
        timeList.append(baseCount)

    baseCounts = pd.concat(timeList, ignore_index=True)
    bCntSort = baseCounts.sort_values(by = ['CHROM', 'POS','TIME'])

    csvName = chrom + '.merged.csv'
    print( '-',chrom,' merging end >> ',csvName)
    bCntSort.to_csv(csvName, sep='\t', header=True, index=None)
