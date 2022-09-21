# trgn_assignment3
# extract_phonenum.py
## Usage
python3 extract_phonenum.py mytextfile.txt
## Description
Extracts phone numbers from a text file, and prints formatted phone numbers.
One-line per phone number formatted as [+][country code] ([AreaCode]) [local phone number]. [+][country code] optional output if number is international. Create a script called extract_phonenum.py which extracts phone numbers from text file. 
## Known Issues
This was the last script that I worked on which is why it is very premature. test_phonenum.txt was used to test the functionality of the script. Currently, only extracts phone numbers of the order xxx-xxx-xxxx and +yyxxxxxxxxxx. Does not extract phone numbers with spaces in it. Does not differenciate between country code, area code, and phone number. 

# ensg2hugo.py
## Usage
python3 ensg2hugo.py [-f][0-9] [file]
## Description
Key hints. You need to read the Homo_sapiens.GRCh37.75.gtf to create a dictionary, whereby you lookup the Ensembl name and replace it with the HUGO name.
## Known Issues
Execute the following command to download the Homo_sapiens.GRCh37.75.gtf file:
curl https://raw.githubusercontent.com/comprna/SUPPA_supplementary_data/master/annotation/Homo_sapiens.GRCh37.75.formatted.gtf.gz > Homo_sapiens.GRCh37.75.formatted.gtf.gz 
I have loaded the .gtf file and the following steps would be to lookup the Ensembl name and replace it with the HUGO name.

# histogram.py
## Usage
python3 histogram.py [-f][0-9] [file]
## Description
Creates a histogram as a png from a file using the specified column in a tab delimited file.
## Known Issues
test_histogram.tsv was used to test the functionality of the script. Non numerical data is not formatted correctly. Histogram is saved within the server under trgn510_assignment3 instead of being saved on the Desktop of the local host. An additional scp step needs to be performed to view the histogram.  
