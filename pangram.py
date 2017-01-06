c = 0
a = raw_input()
for i in a:
    if (ord(i) > 96 and ord(i) < 123) or (ord(i) > 64 and ord(i) < 91):
        c = c+1

if c > 25:
    print "Pangram"

else:
    print "Not Pangram"
