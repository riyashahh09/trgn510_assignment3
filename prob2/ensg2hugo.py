import sys
import pandas as pd
import re
from gtfparse import read_gtf

dictionary = read_gtf('Homo_sapiens.GRCh37.75.formatted.gtf')
engs2hugo = {}
arg_len = len(sys.argv)
col = 2
if (arg_len <2):
        print("Provide file input as the first argument")
        sys.exit(1)
elif (arg_len == 2):
        file_name = sys.argv[1]
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
if (not file.endswith ('.tsv')):
        print ("File has to end with .tsv.")
        sys.exit(1)
df = pd.read_csv(file, sep='\t')
if (df.shape[1] < col or col <= 0):
        print("Number of columns should be > 0")
        sys.exit(1)

