import sys
import pandas as pd
import re
from gtfparse import read_gtf

ensg2hugo = {}

dictionary = read_gtf('Homo_sapiens.GRCh37.75.formatted.gtf')
for i, row in dictionary.iterrows():
	ensg2hugo[row["gene_id"]] = row["gene_name"]

arg_len = len(sys.argv)
col = 2
if (arg_len <2):
        print("Provide file input as the first argument")
        sys.exit(1)
elif (arg_len == 2):
        file = sys.argv[1]
#-f has not been used
elif (arg_len == 3):
        arg_col = sys.argv[1]
        if (not arg_col.startswith ('-f')):
                print ("Invalid argument. Enter \'-f'\ to specify column.")
                sys.exit(1)
        col = arg_col [2:]
        if (not col.isdigit ()):
                print ("Argument for -f should be a number.")
                sys.exit(1)
        col = int(col)
        file = sys.argv[2]
elif (arg_len >3):
	print("ensg2.hugo.py takes only 2 arguments: -f and file name.")
elif (arg_len <3):
        print ("Not enough arguments to run.")

if (not file.endswith ('.tsv') and not file.endswith ('.csv')):
        print ("File has to end with .tsv or .csv")
        sys.exit(1)

df = pd.read_csv(file, sep='\t', dtype=str)
if(file.endswith('.csv')):
	df = pd.read_csv(file, sep= ',', dtype=str)

if(df.shape[1] < col or col <= 0):
    print("Number of columns in argument must be <= number of columns in file and should be > 0")
    sys.exit()
col_name = df.columns[col-1]

hugo_name = []
for i, row in df.iterrows(): #iterate data frame
	en_name = row[col_name] #find the Ensembl name with or without the '.'
	if ('.' in en_name): #if there is a dot in the Ensembl name
		en_name = re.match("(.*?)\.",row[col_name]).group(1) #get part before '.'
	if(en_name in ensg2hugo.keys()): #if the Ensembl name exists in the dictionary
		hugo_name.append(ensg2hugo[en_name]) #find Hugo name from dictionary
	else:
		hugo_name.append('') #if no Hugo name found becuase Ensembl name is not in dict
df[col_name] = hugo_name #set gene_name to Hugo name instead of Ensembl
df.to_csv(sys.stdout, sep='\t') #print tsv to terminal
