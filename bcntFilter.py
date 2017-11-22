import sys

CHROM_LIST= {'LYZE01000001.1':1,'LYZE01000002.1':2,'LYZE01000003.1':3,'LYZE01000004.1':4,'LYZE01000005.1':5,
             'LYZE01000006.1': 6,'LYZE01000007.1':7,'LYZE01000008.1':8,'LYZE01000009.1':9,'LYZE01000010.1':10,
             'LYZE01000011.1': 11,'LYZE01000012.1':12,'LYZE01000013.1':13,'LYZE01000014.1':14,'LYZE01000015.1':15,
             'LYZE01000016.1': 16}

POS=sys.argv[1]
BASE=sys.argv[2]

baseFile = open(BASE)
posFile = open(POS)
posFile.readline()
baseFile.readline()

fetch_Chrom=[]
fetch_POS=[]

for line in posFile:
    line = line.strip().split('\t')
    fetch_Chrom.append(line[0].strip())
    fetch_POS.append(int(line[1].strip()))


i=0
end=len(fetch_POS)
line = baseFile.readline()
while True:

    tmp=line.strip().split('\t')
    chrom=tmp[0].strip()
    pos=int(tmp[2].strip())

    if ( CHROM_LIST[fetch_Chrom[i]] == CHROM_LIST[chrom] ):

        if ( fetch_POS[i] == pos):
            print(line)
            i += 1
            line = baseFile.readline()
            if (end <= i):
                break
        elif (fetch_POS[i] < pos):
            i += 1
            if (end <= i):
                break
        else:
            line = baseFile.readline()

    elif ( CHROM_LIST[fetch_Chrom[i]] > CHROM_LIST[chrom] ):
        line = baseFile.readline()
    else:
        i += 1

