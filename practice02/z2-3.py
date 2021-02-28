def f23(table):
    i = 0
    while i < len(table):
        j = 0
        while j < len(table[i]):
            if table[i][j] is None:
                del table[i][j]
                j -= 1
            j += 1
        if len(table[i]) == 0:
            del table[i]
            i -= 1
        i += 1

    for i in range(len(table)):
        l = table[i][0].split(".")
        table[i][0] = l[0][2::]+'-'+l[1]+'-'+l[2]

    for i in range(len(table)):
        l = table[i][1].split('|')
        table[i][1] = '{:.0%}'.format(float(l[0]))
        table[i].insert(2, l[1][3:6:]+'-'+l[1][6::])

    for i in range(len(table)):
        l = table[i][3].split(' ')
        table[i][3] = l[2] + ', ' + l[0][0]+'.'+l[1]

    tr_table = [list(i) for i in zip(*table)]

    return tr_table


# print(f23([
#     ['2002.05.23', '0.189|7257199013', 'Богдан А. Мешянц'],
#     [None, None, None],
#     ['2000.05.21', '0.771|2958901359', 'Тамерлан О. Довман'],
#     [None, None, None],
#     ['2001.04.10', '0.442|8241495761', 'Виктор Б. Косин']
# ]))
