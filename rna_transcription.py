r = raw_input()
r = r.upper()

d = ''
for i in r:
    if i == 'G':
        d = d + 'C'

    if i == 'C':
        d = d + 'G'

    if i == 'T':
        d = d + 'A'

    if i == 'A':
        d = d + 'U'

print d
