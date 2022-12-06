import datetime

h, m = input().split()

hh = list(str(h).zfill(2))
mm = list(str(m).zfill(2))

while True:
    a,b = hh[0],hh[1]
    c,d = mm[0],mm[1]

    
    if int(a+c)>= 0 and int(a+c)<=23:
        if int(b+d)>= 0 and int(b+d)<=59:
            print(int(a+b),int(c+d))
            exit()

    plus_time = datetime.timedelta(minutes=1)
    now_time = datetime.datetime.combine(datetime.date.today(),datetime.time(hour=int(a+b), minute=int(c+d)))
    next = now_time + plus_time
    #hh = [c for c in str(next.hour).zfill(2)]
    #hh = [c for c in str(next.minute).zfill(2)]
    hh = list(str(next.hour).zfill(2))
    mm = list(str(next.minute).zfill(2))



