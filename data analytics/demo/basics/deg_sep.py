num = 472

while(num > 0):
    d = num % 10
    print(d)
    num = num // 10

    num = 472
    sum = 0
    while(num > 0):
        d = num % 10
        #print(d)
        sum += d
        num = num // 10
        print(sum)