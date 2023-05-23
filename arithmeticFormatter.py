def arithmetic_arranger(l, condition=False):
    # situation of an error
    lnum1 = []
    lnum2 = list()
    lopr = []
    length = []
    op_line1 = str()
    op_line2 = str()
    op_line3 = str()
    op_line4 = str()
    if len(l) > 5:
        return 'Error: Too many problems'
    for i in range(len(l)):
        qty = l[i].split()
        num1 = qty[0]
        lnum1.append(num1)
        num2 = qty[2]
        lnum2.append(num2)
        operator = qty[1]
        lopr.append(operator)

        if operator not in ['+','-']:
            return "Error: Operator must be '+' or '-'."
        for item in num1:
            if item not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                return 'Error: Numbers must only contain digits'
        for item in num2:
            if item not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                return 'Error: Numbers must only contain digits'
        l1 = len(num1)
        l2 = len(num2)
        if l1 > 4 or l2 > 4:
            return 'Error: Numbers cannot be more than four digits'
    # if all the pass value is according to the specs

    for i in range(len(lopr)):
        a = len(lnum1[i])
        b = len(lnum2[i])
        lmax = max(a, b)
        length.append(lmax)
        op_line1 += (lmax - a + 1) * ' ' + lnum1[i] + 4 * ' '
    print(f'{op_line1}\n')
    for i in range(len(lopr)):
        b = len(lnum2[i])
        lmax = length[i]
        op_line2 += lopr[i] + (lmax - b) * ' ' + lnum2[i] + 4 * ' '
    print(f'{op_line2}\n')
    for i in range(len(lopr)):
        lmax = length[i]
        op_line3 += (lmax + 1) * '-' + 4 * ' '
    print(f'{op_line3}\n')
    if condition is True:
        for i in range(len(lopr)):
            lmax = length[i]
            lmax += 1
            num1 = int(lnum1[i])
            num2 = int(lnum2[i])

            if lopr[i]=='+':
                sigma = num1 + num2
            else:
                sigma = num1 - num2
            snum = str(sigma)
            lth = len(snum)

            op_line4 += (lmax - lth) * ' ' + snum + 4 * ' '

    print(f'{op_line4}')
