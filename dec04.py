low = 254032
high = 789860

cnt1 = 0
cnt2 = 0
for i1 in range(2,8):
    for i2 in range(i1,10):
        for i3 in range(i2, 10):
            for i4 in range(i3, 10):
                for i5 in range(i4, 10):
                    for i6 in range(i5,10):

                        i = i1*100000+i2*10000+i3*1000+i4*100+i5*10+i6
                        i_str = str(i)
                        if low <= i <= high:
                            for n in range(0, 10):
                                n_str = str(n)
                                if 2 * n_str in i_str:  # part one
                                    cnt1 += 1
                                    break

                            for n in range(0, 10):
                                n_str = str(n)
                                if (2*n_str in i_str) and (3*n_str not in i_str):  #part two
                                    cnt2 += 1
                                    break


print(cnt1)  # part one
print(cnt2)  # part two

