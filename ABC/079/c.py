A, B, C, D = list(map(int, list(input())))

op = [-1, 1]

for i in range(2):
    for j in range(2):
        for k in range(2):
           ans = A + op[i]*B + op[j]*C + op[k]*D
           if ans == 7:
                if i == 0:
                    op1 = "-"
                else:
                    op1 = "+"
                if j == 0:
                    op2 = "-"
                else:
                    op2 = "+"
                if k == 0:
                    op3 = "-"
                else:
                    op3 = "+"
                print("{}{}{}{}{}{}{}=7".format(A,op1,B,op2,C,op3,D))
                exit()