#a:3で割った余りが0ならspaceとiを出力してc
#b:10で割った余りが３ならspaceとiを出力してc
#c:10で割った商が1ならb, 
#d:i++してa

n = int(input())

i = 1

while i <= n:
    if i%3 == 0:
        print(" "+str(i), end="")
    elif i%10 == 3:
        print(" "+str(i), end="")   
    elif i//10 != 0:
        if i%10 == 3:
            print(" "+str(i), end="")

    i += 1
