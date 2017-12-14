# for the BBGP test & CMH test, transform the format
inF='E:/evolutinoarypattern/basecount.merge/LYZE01000001.1.merged.csv'
outF='chr1.tInput.csv'

def printOut(chr, pos, ref, af):
    content = chr + '\t' + str(pos) + '\t' + ref + '\t'
    for cnt in af:
        content += ('\t' + str(cnt))
    return content





iFile = open(inF,'r')
oFile = open(outF, 'w')

iHeader = iFile.readline()

oHeader='chr\tpos\tref\t0\t140\t240\t335\t415\t505\t585\t665\t745\t825\t910\t1000'
oFile.write(oHeader + '\n')

time = 0
allele = []

for line in iFile:
    time += 1
    line = line.strip().split()

    tmp = (':'.join(line[4:])) + ':0:0'
    allele.append(tmp)

    if(line[1] == "1000"):
        if( time == 12):
            out = printOut(chr = line[0], pos = line[2], ref = line[3], af=allele)
            oFile.write(out+'\n')
            allele.clear()
            time = 0
        else:
            allele.clear()
            time = 0

oFile.close()
