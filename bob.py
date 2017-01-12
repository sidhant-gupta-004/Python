import os

while 1 == 1:
    a = raw_input()
    if a != '':
        c = a[-1]
        if c == '?':
            print 'Sure.'
        elif c == '!':
            print 'Whoa, chill out!'
        else:
            print 'Whatever.'

    else:
        print 'Fine. Be that way!'
