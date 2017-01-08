a = raw_input()
b = raw_input()

j = 0
c = 0
for i in a:
    if i != b[j]:
        c = c + 1
    j = j + 1

print 'Hamming Distance: ' + str(c)
