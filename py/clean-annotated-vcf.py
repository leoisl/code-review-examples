#!/usr/bin/env python3

import argparse

import clean_annotated_vcf_helper

parser = argparse.ArgumentParser(
    description = 'Clean SnpEff annotated files',
        usage='%(prog)s <filename.vcf>',
        )
parser.add_argument('filename', help='Input VCF')
options = parser.parse_args()
        
