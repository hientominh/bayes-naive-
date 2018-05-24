def solve():
    with open('label_test.txt', 'rt') as f:
        label_real = f.readlines()
    with open('label_after_test.txt', 'rt') as f:
        label_after_test = f.readlines()
    num_case = len(label_real)
    count = 0
    for i in range(num_case):
        if label_real[i] == label_after_test[i]:
            count += 1
    result = count/num_case * 100
    print("Match: {0:.2f}%".format(result))


def main():
    solve()


if __name__ == '__main__':
    main()
