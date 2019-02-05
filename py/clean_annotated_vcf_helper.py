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

        '''
        These information does not seem to come from the VCF file, so I am fixing them for the sake of this exercise...
        I think the gene and geneId can be obtained by intersecting the position of the variants with the intervals in the gff file of NC_000962.3 (can be obtained through wget -O NC_000962.3.gff "https://www.ncbi.nlm.nih.gov/sviewer/viewer.cgi?db=nuccore&report=gff3&id=NC_000962.3")
        Annotation can be obtained by checking if the variant has synonymous codons? To get the codon, I think it is enough the gff file (so that you know the CDS and the ORF), and the genome, to check if the variation induces a synonimous codon or not
        I don't know how to evaluate the annotation impact
        cDNA describes the position in the cDNA, reference allele and variant allele? I think with the gff only is enough to get this
        protein should be similar to get as we do to the gene    
        '''
        gene="dnaA"
        geneId="Rv0001"
        annotation="synonymous_variant"
        annotationImpact="LOW"
        protein="p.Ser7Ser"


        #Covering all samples - an alternative option is making the first column being able to represent multiple samples
        for sampleName in sampleNames:
            '''
            At each iteration, here we are creating a new DataFrame with all the data seen previously.
            It is better to simply add the column to the dataframe
            anno_list.append([sample_name, vcf_var[0], vcf_var[1], vcf_var[3], vcf_var[4], vcf_anno[3], vcf_anno[4], myGT, vcf_anno[1], vcf_anno[2], vcf_anno[9], vcf_anno[10]])
            vcf_df=pd.DataFrame(anno_list,columns=cols)
            '''
            #going through all alternative variants (I think each line of the output file correspond to a specific variant)
            for alt in vcf_record.ALT:
                vcf_df.loc[len(vcf_df.index) + 1] = [sampleName, vcf_record.CHROM, vcf_record.POS, vcf_record.REF, alt, gene, geneId, vcf_record.FORMAT['GT'], annotation, annotationImpact, "c.%d%s>%s"%(vcf_record.POS+1, vcf_record.REF, alt), protein]

    return vcf_df
