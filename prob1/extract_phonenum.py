import re
import sys

if len(sys.argv) == 1:
	print("Provide file input as the first argument")
	sys.exit(1)
else:
	file_name = sys.argv[1]
	print ("This is the name of the file: ", file_name)
file = open(sys.argv[1],'r')
text = file.read()

pattern = '((?:\+\d{1,2}[-\.\s]??|\d{4}[-\.\s]??)?(?:\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{2,3}[-\.\s]??\d{4}-\d{4}))'

phonenum = re.findall(pattern, text)

fin_phonenum = phonenum
for i in fin_phonenum:
	if('+' not in i):
		i = '(' + i[0:3] + ')' + i[3:] 
	print (i)

