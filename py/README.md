In this directory we have an input VCF, and two small python files, which together parse the VCF,
and should produce an output of the format shown in desired-out-format.txt

If a colleague showed you this code - what might you point out?


1. Use an isolated python environment (modified install.sh)
2. Don't use "-" to separate name in files/modules (prefer "_")
    It is hard to import them, and not really a convention (https://stackoverflow.com/questions/761519/is-it-ok-to-use-dashes-in-python-files-when-trying-to-import-them/37831973)
3. input.vcf is tab-delimited, not space-delimited. cluster_vcf_records can't parse input.vcf correctly. You can replace the spaces by tabs using, e.g.
    python3 convert_spaces_into_tabs.py <input.vcf >input_with_tabs.vcf
4. Many points in the two python scripts (clean_annotated_vcf.py and clean_annotated_vcf_helper.py)


Usage:
1. go to this code repository;
2. cd py
3. bash -x install.sh
    *If you don't have python3.7, you won't be able to complete the installation successfully. Change it to any python3.6+ that you have - below than this, one of libraries break
4. source venv/bin/activate
5. python3 clean_annotated_vcf.py input_with_tabs.vcf
6. deactivate