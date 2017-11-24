import sys;

input=open(sys.argv[1], 'r');

for line in input:
        if (line[0]=='#'):
                pass;
        else:
                line = line.strip().split('\t')
                chrom=line[0].strip()
                pos=line[1].strip()
                ref=line[3].strip()
                if(len(ref) > 1):
                        pass;
                else:
                        alt=line[4].strip()
                        print(chrom,'\t',pos,'\t',ref,'\t',alt)
