import pandas as pd
import os

DIR='E:/BYS_D07.3RM_masurca.vaf/snps'
CSV='E:\BYS_D07.3RM_masurca.vaf/'
CHROM_LIST= {'sscf_1_pilon':1,'sscf_2_pilon':2,'sscf_3_pilon':3,'sscf_4_pilon':4,'sscf_5_pilon':5,
             'sscf_6_pilon': 6,'sscf_7_pilon':7,'sscf_8_pilon':8,'sscf_9_pilon':9,'sscf_10_pilon':10,
             'sscf_11_pilon': 11,'sscf_12_pilon':12,'sscf_13_pilon':13,'sscf_14_pilon':14,'sscf_15_pilon':15,
             'sscf_16_pilon': 16}
#file = DIR + '/1-244_LTE_BYS2_D07-0.3RM_masurca.GATK.snps.table'
#print(file)
#data = pd.read_csv( file , sep='\t')
#print(data)


def fetch_TimePoint(name):
    timePoint_tmp = (name.split(sep='.')[0]).split(sep='-')[-1]
    return timePoint_tmp


def readRawData(dir):
    raw = pd.read_csv(dir, sep='\t')
    splitAD = raw['PA01.AD'].str.split(',').str
    raw['REF_CNT'] = splitAD.get(0)
    raw['ALT_CNT'] = splitAD.get(1)
    raw['TIME'] = timePoint
    raw['TIME'] = raw['TIME'].astype(int)
    raw['NUM'] = raw['CHROM'].str.split('_').str.get(1)
    raw['REF_CNT'] = (raw['REF_CNT'].astype(float)) / (raw['PA01.DP'].astype(float))
    raw['ALT_CNT'] = (raw['ALT_CNT'].astype(float)) / (raw['PA01.DP'].astype(float))

    raw = raw.drop(['PA01.AD', 'PA01.DP'], 1)

    raw = raw[['CHROM', 'POS', 'REF', 'ALT', 'TIME', 'REF_CNT', 'ALT_CNT', 'NUM']]
    return raw


files = os.listdir(DIR)

snps = list()
for file in files:
    timePoint = fetch_TimePoint(file)
    fileDir = DIR +'/' + file
    tmp = pd.DataFrame(readRawData(fileDir))
    print(tmp)
    snps.append(tmp)
snps = pd.concat(snps,ignore_index=True)

snps = snps.sort_values(by = ['NUM', 'POS','TIME'])
snps = snps.drop(['NUM'], 1)

outputDir = CSV + 'BYS2_D07-0.3RM_masurca.vcf.csv'
snps.to_csv(outputDir, sep=',', index=False, header=True)