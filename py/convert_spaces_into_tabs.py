import sys

for line in sys.stdin:
    line=line.strip()
    if line.startswith("#"):
        print(line)
    else:
        print("\t".join(line.split()))



'''
import sys

#some care must be taken because cluster_vcf_records bugs on empty lines
firstLine=True
for line in sys.stdin:
    line=line.strip()
    if not firstLine: print()
    if line.startswith("#"):
        print(line, end='')
    else:
        print("\t".join(line.split()), end='')
    firstLine=False
'''