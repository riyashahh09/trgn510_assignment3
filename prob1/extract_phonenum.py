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
pattern = r"\d{3}-\d{3}-\d{4}"
pattern2 = r"\+\d{12}"
phonenum = re.findall(pattern, text)
phonenum2 = re.findall(pattern2, text)
fin_phonenum = phonenum + phonenum2
for i in fin_phonenum:
	print (i)

