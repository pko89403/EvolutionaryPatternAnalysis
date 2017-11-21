import sys

File = open(sys.argv[1], 'r')


print('CHROM\tPOS\tREF\tA\tC\tG\tT')

n = 0
for line in File:
    n= n+1
    tmp=line.strip().split('\t')

    chrom=tmp[0]
    print(chrom , n)
    pos=tmp[1]
    ref=tmp[2].upper()
    bases = tmp[4].upper()
    freq = {'A': 0, 'G': 0, 'C': 0, 'T': 0, '.' : 0, ',' : 0}
    i=0

    while i < len(bases):
        base = bases[i]

        if ( base == '+' or base == '-'): # skip indels
            i += 1
            try:
                indels = int(bases[i])
            except ValueError:
                i -= 1
            else:
                i += indels

        else:
            if ( base in freq): freq[base] += 1

        i += 1
    ref_freq = ( freq['.'] + freq[','] )
    freq[ref] = ref_freq
    out = [chrom, pos, ref, freq['A'], freq['C'], freq['G'], freq['T'] ]
    print('\t'.join([str(x) for x in out ]))