import sys

for line in sys.stdin:
    line=line.strip()
    if line.startswith("#"):
        print(line)
    else:
        print("\t".join(line.split()))
