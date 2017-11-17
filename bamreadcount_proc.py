import os

PATH = 'E:/pacbio.fabam/'
OUTPATH = './bamreadcount_proc_output/'

def alt_proc(alt_content): #base:count:avg_mapping_quality:avg_basequality:avg_se_mapping_quality:num_plus_strand:num_minus_strand:avg_pos_as_fraction:avg_num_mismatches_as_fraction:avg_sum_mismatch_qualities:num_q2_containing_reads:avg_distance_to_q2_start_in_q2_reads:avg_clipped_length:avg_distance_to_effective_3p_end
    tmp = alt_content.split(':')

    '''
    if( tmp[0] != 'A' and tmp[0] != 'C' and tmp[0] != 'G' and tmp[0] != 'T' and tmp[0] != 'N'): return
    else :
        freq = tmp[1] # base : count( = '+' strand + '-' strand )
    '''

    if(tmp[0] == '='):  return
    freq = tmp[0] + ':' + tmp[1]



    return freq

def fetchTime(file): # E:/pacbio.fabam/1-244_LTE_BYS2_D07-0.LYZE01.1.sorted.bam.txt
    name = file.split('-')
    time = name[2].split('.')[0]

    return time

files = os.listdir(PATH)

for file in files:

    fName = PATH + file
    time = fetchTime(file)

    outName = OUTPATH + 't-' + time +'.txt'
    output = open( outName, 'w' )
    output.write('NAME\tTIME\tPOS\tREF\tDEPTH\tBASE:COUNT\n')

    f = open(fName,'r')
    print(f)

    for line in f:
        offset = 0
        test = []

        for content in line.split():
            if(offset <= 3):

                test.append(content)
                if( offset == 0): test.append(time)
            else:
                alt = alt_proc(content)
                if( alt != None):
                    test.append( str(alt) )
            offset = offset+1

        offset = 0
        for tmp in test:
            output.write(tmp)
            if(offset > 4 and tmp != test[-1]): output.write(',')
            else:   output.write('\t')
            offset += 1
        output.write('\n')

    f.close()
    output.close()
