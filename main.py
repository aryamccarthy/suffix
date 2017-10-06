from predictiontree import PredictionSuffixTree as PST

test_strings = ["abracadabra", "abcccdaadcdaabcad"]
L = 3
p_min = 0.1
r = 2


if __name__ == '__main__':
    tree = PST('there would have been a time for such a word')
    print(tree.has_substring("nope"))
    print(tree.has_substring("would have been"))
    print(tree.has_suffix("such a word"))

    # tree.search(test_strings[0], L)
    # print("Tree structure before elimination:")
    # tree.list()
    # tree.eliminate_empirical(test_strings[0], p_min)