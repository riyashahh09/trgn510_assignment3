import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

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
	print ("Too many arguments to run.")
if (not file.endswith ('.tsv')):
	print ("File has to end with .tsv.")
	sys.exit(1)
df = pd.read_csv(file, sep='\t')
if (df.shape[1] < col or col <= 0):
	print("Number of columns should be > 0")
	sys.exit(1)
name_col = df.columns[col-1]
plt.hist(df[name_col].astype(str), rwidth=0.8)
plt.ylabel("Count")
plt.xlabel(name_col)
plt.show()
plt.savefig('histogram.png')
