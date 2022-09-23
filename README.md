# trgn_assignment3
# extract_phonenum.py
## Usage
python3 extract_phonenum.py mytextfile.txt
## Description
Extracts phone numbers from a text file, and prints formatted phone numbers.
One-line per phone number formatted as [+][country code] ([AreaCode]) [local phone number]. [+][country code] optional output if number is international. Create a script called extract_phonenum.py which extracts phone numbers from text file. 
## Known Issues
There are 2 files to test the code - example1.txt and test_phonenum.txt. Program does not extract phone numbers with extension. Outputs phone numbers from a file as they were submitted by user. Area code is in brackets when there is no country code.   

# ensg2hugo.py
## Usage
python3 ensg2hugo.py [-f][0-9] [file]
## Description
Key hints. You need to read the Homo_sapiens.GRCh37.75.gtf to create a dictionary, whereby you lookup the Ensembl name and replace it with the HUGO name.
## Known Issues
Steps to download and be able to run the file:
1.curl https://raw.githubusercontent.com/comprna/SUPPA_supplementary_data/master/annotation/Homo_sapiens.GRCh37.75.formatted.gtf.gz > Homo_sapiens.GRCh37.75.formatted.gtf.gz
2.gunzip Homo_sapiens.GRCh37.75.formatted.gtf.gz 

# histogram.py
## Usage
python3 histogram.py [-f][0-9] [file]
## Description
Creates a histogram as a png from a file using the specified column in a tab delimited file.
## Known Issues
test_histogram.tsv was used to test the functionality of the script.Histogram is saved within the server under trgn510_assignment3 instead of being saved on the Desktop of the local host. Program is written in linux. An additional rsync step needs to be performed to download and view the histogram.  
