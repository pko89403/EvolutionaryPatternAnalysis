import pandas as pd

INPUT='E:/evolutinoarypattern/inputData/chr1.tinput.csv'
# ACGT
OUTPUT = 'E:/evolutinoarypattern/betaDistribution1229/chr1.beta.csv'
def binomial(ref, af):
    depths = af.strip().split(':')
    depths = list(map(int, depths))
    total = sum(depths)

    if(ref == 'A'):
        idx = 0
    elif(ref == 'C'):
        idx = 1
    elif(ref == 'G'):
        idx = 2
    elif(ref == 'T'):
        idx = 3

    return ( depths[idx] / total )

iFile = open(INPUT, 'r')
head = iFile.readline()

oFile = open(OUTPUT, 'w')
head = 'NAME\tPOS\tREF\t0\t140\t240\t335\t415\t505\t585\t665\t745\t825\t910\t1000\n'
oFile.write(head+'\t')
for line in iFile:
    tmp = line.strip().split('\t')
    ref = tmp[2]
    alleles = tmp[4:]

    dummy = False
    time = []
    for allele in alleles:
        val = binomial(ref, allele)
        time.append( val )
        if(val == 1.0):
            dummy = True

    if(dummy == True):
        continue
    else:
        res = tmp[0] + '\t' + tmp[1] + '\t' + ref + '\t' + '\t'.join(str(p) for p in time)
        oFile.write(res + '\n')

oFile.close()
