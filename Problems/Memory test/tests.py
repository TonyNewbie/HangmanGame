from test_helper import check_samples

if __name__ == '__main__':
    check_samples(samples=[["1 2 3 4 5\n5 4 1 2 1 3","True"],["999 1 1001 15 6 7\n1 6 7 1 999","False"],["3 4 5 7\n3 4 5 6 7","False"]])