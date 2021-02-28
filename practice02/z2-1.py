DecisionTree = {
    (1, 2001): {(0, 'xtend'): {(2, 2016): 0,
                               (2, 1962): 1},
                (0, 'shell'): {(2, 2016): 2,
                               (2, 1962): 3}},
    (1, 1975): {(2, 2016): 4,
                (2, 1962): {(0, 'xtend'): 5,
                            (0, 'shell'): 6}},
    (1, 2020): {(0, 'xtend'): {(3, 'ioke'): 7,
                               (3, 'ampl'): 8},
                (0, 'shell'): {(3, 'ioke'): 9,
                               (3, 'ampl'): 10}}
}
answer = 0


def frec(list, tree):
    global answer
    try:
        all_keys = tree.keys()
        for index, key in all_keys:
            if list[index] == key:
                tree = tree.get((index, key))
                answer = tree
        frec(list, tree)
    except AttributeError:
        return


def f21(input_list):
    global answer
    tree = DecisionTree.copy()
    frec(input_list, tree)
    a = answer
    answer = 0
    return a

# print(f21(['xtend', 1975, 1962, 'ampl']))
# print(f21(['xtend', 2001, 2016, 'ioke']))
# print(f21(['shell', 2020, 2016,  'ioke']))
