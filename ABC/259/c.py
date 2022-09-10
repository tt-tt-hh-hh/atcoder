S = input()
T = input()

S = S.ljust(len(T), '0')

for i in range(len(T)):
    if S[i] == T[i]:
        continue 
    else:
        if i == 0:
            print("No")
            exit()
        if S[i-1] == T[i]:
            if S[i-1] == S[i-2]:
                if S[i-2] == T[i]:
                    continue
                else:
                    print("No")
                    exit()
            else:
                print("No")
                exit()
        else:
            print("No")
            exit()

print("Yes")


