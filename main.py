from predictiontree import PredictionSuffixTree as PST

test_strings = ["abracadabra", "abcccdaadcdaabcad"]
L = 3
p_min = 0.1
r = 2


if __name__ == '__main__':
    for s in test_strings:
        tree = PST(s)
        print(tree)