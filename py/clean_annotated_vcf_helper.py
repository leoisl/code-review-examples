import cluster_vcf_records
'''
These imports are not needed anymore
import os
from os import path
'''
import pandas as pd


def load_vcf_file(filename):
    header, vcf_records = cluster_vcf_records.vcf_file_read.vcf_file_to_list(filename)

    '''
    Declare the dataframe with the columns already - no need for anno_list
    vcf_df=pd.DataFrame([])
    cols = ["sample", "genome", "position", "ref", "alt", "gene", "gene_id", "genotype", "annotation", "annotation_impact", "cDNA", "protein"]
    anno_list=[]
    '''
    vcf_df = pd.DataFrame(columns=["sample", "genome", "position", "ref", "alt", "gene", "gene_id", "genotype", "annotation", "annotation_impact", "cDNA", "protein"])


    '''
    Prefer using meaning variable names - code as it was for the others, not for only you
    for x in vcf_records:
    '''
    for vcf_record in vcf_records:
        '''
        #Sample names are the columns in the last header line, after the FORMAT column.
        #Further, we can have several samples, not only one  
        file_name = os.path.basename(line.rstrip())
        sample_name = os.path.splitext(file_name)[0]
        '''
        splitHeader = header[-1].strip().split()
        sampleNames = splitHeader[splitHeader.index("FORMAT")+1:]

        '''
        Prefer using the interface of the class (methods and attributes you have access to) to access data in a VCF record, instead of converting it into string and reparsing
        Although the VCF record does not restrain you from modifying  its internal attributes, do it carefully (e.g. in the eventual case you need to modify the POS attribute,
        remember the 1-indexing.)
        Encapsulation of attributes in cluster_vcf_records.VcfRecord might solve possible incorrect misusages
        mystr = str(x)
        vcf_anno = mystr.split("|")
        vcf_var = mystr.split("\t")
        myGT = x.FORMAT['GT']
        '''

        #going through all samples
        for sampleName in sampleNames:
            '''
            At each iteration, here we are creating a new DataFrame with all the data seen previously.
            It is better to simply add the column to the dataframe
            anno_list.append([sample_name, vcf_var[0], vcf_var[1], vcf_var[3], vcf_var[4], vcf_anno[3], vcf_anno[4], myGT, vcf_anno[1], vcf_anno[2], vcf_anno[9], vcf_anno[10]])
            vcf_df=pd.DataFrame(anno_list,columns=cols)
            '''
            #split annotations in the INFO field into a list of list
            annotationsAsString = vcf_record.INFO['ANN']
            annotations = [annotationAsString.split("|") for annotationAsString in annotationsAsString.split(",")]

            #go through all annotations and print them
            for annotation in annotations:
                vcf_df.loc[len(vcf_df.index) + 1] = [sampleName, vcf_record.CHROM, vcf_record.POS, vcf_record.REF, annotation[0], annotation[3], annotation[4],\
                                                     vcf_record.FORMAT['GT'], annotation[1], annotation[2], annotation[9], annotation[10]]

    return vcf_df
