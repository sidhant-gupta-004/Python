a = raw_input()

word = ''
string = []

j = 0
for i in a:
    if i.isalpha() == True:
        word = word + i

    elif word.isalpha():
        string.append(word)
        word = ''

string.append(word)

count = []

k = 0
for i in string:
    count.append(0)
    for j in string:
        if i == j:
            count[k] = count[k] + 1
            if count[k] > 1:
                string.remove(string[k])
    k = k + 1
k = 0
for i in string:
    print i + " : " + str(count[k])
    k = k + 1
