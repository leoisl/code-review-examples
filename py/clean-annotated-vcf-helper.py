import cluster_vcf_records
import os
from os import path
import pandas as pd


def load_vcf_file(filename):
    header, vcf_records = cluster_vcf_records.vcf_file_read.vcf_file_to_list(filename)

    vcf_df=pd.DataFrame([])
    cols = ["sample", "genome", "position", "ref", "alt", "gene", "gene_id", "genotype", "annotation", "annotation_impact", "cDNA", "protein"]
    anno_list=[]
    for x in vcf_records:
        file_name = os.path.basename(line.rstrip())
        sample_name = os.path.splitext(file_name)[0]
        mystr = str(x)
        vcf_anno = mystr.split("|")
        vcf_var = mystr.split("\t")
        myGT = x.FORMAT['GT']
        anno_list.append([sample_name, vcf_var[0], vcf_var[1], vcf_var[3], vcf_var[4], vcf_anno[3], vcf_anno[4], myGT, vcf_anno[1], vcf_anno[2], vcf_anno[9], vcf_anno[10]])
        vcf_df=pd.DataFrame(anno_list,columns=cols)

    return vcf_df
