while True:
    num = int(input())
    if num == -1:
        break

    divisor = []
    for i in range(num-1):
        if num%(i+1) == 0:
            divisor.append(i+1)

    if sum(divisor) == num:
        strdiv = ' + '.join(str(s) for s in divisor)
        print(num, '=', strdiv)
    else:
        print(num, 'is NOT perfect.')
