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

#print the vcf on the desire output format
print(vcf_df.to_string(index=False, justify="left"))