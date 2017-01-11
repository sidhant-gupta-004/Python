import datetime

def time_parse(t):
    #print t

    time = []
    time.append(0)

    j = 0
    for i in t:
        if i.isdigit() == True:
            time[j] = 10*time[j] + int(i)

        else:
            time[j] = time[j]-1
            time.append(0)
            j = j + 1

    s = second_calculator(time)
    return s


def second_calculator (time):
    second = 0
    for i in range(0, len(time)):
        if i == 0:
            second = second + time[i]*31536000

        if i == 1:
            second = second + time[i]*2592000

        if i == 2:
            second = second + time[i]*86164

        if i == 3:
            second = second + (time[i])*3600

        if i == 4:
            second = second + (time[i])*60

        if i == 5:
            second = second + (time[i])
    return second

def reverse_calculator(n):
    y = n/31536000
    n = n%31536000

    m = n/2592000
    n = n%2592000

    d = n/86164
    n = n%86164

    h = n/3600
    n = n%3600

    m = n/60
    n = n%60

    s = n

    print ("You need to live for " + str(y) + " years " + str(m) + " months "
            + str(d) + " days " + str(h) + " hours " + str(m) + " minutes " + str(s) + " seconds " + " more.")

t = str(datetime.datetime.now())
t = t[0:-7]
now_time = time_parse(t)

user = raw_input("Format yy/mm/dd/hour/minutes/seconds:\n")
birth_time = time_parse(user)


if now_time - birth_time >= 1000000000:
    print "You are old"

else:
    reverse_calculator(1000000000-(now_time - birth_time))
