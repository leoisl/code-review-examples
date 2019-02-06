#!/usr/bin/python3 #prefer using the virtualenv, instead of the global env - maybe remove shebang?

import argparse

import clean_annotated_vcf_helper

parser = argparse.ArgumentParser(
    description = 'Clean SnpEff annotated files',
        usage='%(prog)s <filename.vcf>',
        )
parser.add_argument('filename', help='Input VCF')
options = parser.parse_args()

#call the function to load the vcf file
vcf_df = clean_annotated_vcf_helper.load_vcf_file(options.filename)

#print the dataframe tab-spaced
print("\t".join(vcf_df.columns.values))
nparray = vcf_df.values
for row in nparray:
    print("\t".join([str(x) for x in row]))