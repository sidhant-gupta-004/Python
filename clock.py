from datetime import datetime
import sys
import time

print "Press 1 to increase 1 min"
print "Press 2 to decrease 1 min"
print "Press 3 to exit."

while 1 == 1:
	a = str(datetime.now())[11:19]
	# a = str(a)
	# a = a[11:19]

	'''
	i = sys.stdin.readline()

	if i == 1:
		c = a[14:16]
		c = str(int(c+1))
		a[14:16] = c

	if i == 2:
		c = a[14:16]
		c = str(int(c-1))
		a[14:16] = c

	if i == 3:
		exit()
	'''

	sys.stdout.write("\r" + a)
	sys.stdout.flush()
	time.sleep(1)
