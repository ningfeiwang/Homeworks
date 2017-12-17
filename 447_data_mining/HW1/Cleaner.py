
import sys, re


def clean(s):
	'''
	input: a record in original IMDB format
	output: a cleaned record with three fields separated by tab: Year of Production, Country, Title
	'''   
	# fill your code here
	q = re.compile(r'"(.*)"\t*.*\(([0-9]*)\).*\t*{.*}\t*(.*)')
	com = q.match(s)
	con = com.group(2)+'\t'+com.group(3)+'\t'+com.group(1)
	return con


  
if __name__ == '__main__':

	list_line = []
	for line in sys.stdin:
		con = clean(line.strip())
		if con not in list_line:
			list_line.append(con)
			print con


    


