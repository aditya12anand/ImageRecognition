import sys
import urllib
import os

index = 0

with open(sys.argv[1]) as f:
	content = f.readlines()
	print 'Total: ' + str(len(content))
	for url in content:
		index = index + 1
		urllib.urlretrieve(url, str(index) + ".jpeg")
		print 'Completed: ' + str(index)

os.system('mkdir ' + sys.argv[2])
os.system('mv *.jpeg ' + sys.argv[2] + '/')