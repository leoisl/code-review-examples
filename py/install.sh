SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )" #get the dir of this script
cd $SCRIPT_DIR #got to it

#install the virtual env
python3.7 -m venv venv
source venv/bin/activate
pip install wheel cluster_vcf_records pandas
chmod +x py/cleanAnnotatedVcf.py
deactivate