import sys,re

regex = sys.argv[1]

for line in sys.stdin:
    if re.search(re.compile(regex),line):
        sys.stdout.write(line)

'''
usage is type sample.txt | python egrep.py "[0-9]" | python  line_count.py 
'''