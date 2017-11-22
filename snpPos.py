import os
import pandas as pd
IN_PATH='E:/evolutinoarypattern/freebayes.snp.pos'
fileList = os.listdir(IN_PATH)

timeList = []
for file in fileList:
    file = IN_PATH + '/' + file
    position = pd.read_csv(file, sep='\t', header=None, names=['CHROM', 'POS'])
    timeList.append(position)

position = pd.concat(timeList,ignore_index=True)
position = position.sort_values(by = ['CHROM', 'POS'])
position = position.drop_duplicates(keep='first')

outCSV = IN_PATH + '/' + 'BYS2_D07.snps.pos.merge'
position.to_csv(outCSV, sep='\t', index=False, header=True)